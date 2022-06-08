# emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil; coding: utf-8 -*-
# ex: set sts=4 ts=4 sw=4 et:
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the datalad package for the
#   copyright and license terms.
#
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##

import base64
import platform
import sys
import os
import random
import logging

try:
    # optional direct dependency we might want to kick out
    import bs4
except ImportError:  # pragma: no cover
    bs4 = None

from glob import glob
from os.path import exists, join as opj, basename

from urllib.request import (
    urlopen,
    Request,
)
from urllib.parse import quote as url_quote

from unittest.mock import patch
from datalad.utils import (
    chpwd,
    getpwd,
    Path,
)
from datalad.tests.utils import (
    assert_cwd_unchanged,
    assert_dict_equal,
    assert_false,
    assert_in,
    assert_not_in,
    assert_raises,
    assert_re_in,
    assert_str_equal,
    assert_true,
    eq_,
    get_most_obscure_supported_name,
    ignore_nose_capturing_stdout,
    known_failure_githubci_win,
    known_failure_windows,
    local_testrepo_flavors,
    nok_startswith,
    OBSCURE_FILENAMES,
    OBSCURE_PREFIX,
    ok_,
    ok_broken_symlink,
    ok_file_has_content,
    ok_file_under_git,
    ok_generator,
    ok_good_symlink,
    ok_startswith,
    ok_symlink,
    on_windows,
    patch_config,
    probe_known_failure,
    rmtemp,
    run_under_dir,
    serve_path_via_http,
    skip_if,
    skip_if_no_module,
    skip_if_no_network,
    skip_if_on_windows,
    skip_ssh,
    SkipTest,
    skip_wo_symlink_capability,
    swallow_logs,
    with_tempfile,
    with_testrepos, with_tree,
    with_testsui,
    without_http_proxy,
)

from datalad.support.gitrepo import GitRepo
from datalad.support import path as op
from datalad import cfg as dl_cfg
#
# Test with_tempfile, especially nested invocations
#

@with_tempfile
def _with_tempfile_decorated_dummy(path):
    return path


def test_with_tempfile_dir_via_env_variable():
    target = os.path.join(os.path.expanduser("~"), "dataladtesttmpdir")
    assert_false(os.path.exists(target), "directory %s already exists." % target)

    with patch_config({'datalad.tests.temp.dir': target}):
        filename = _with_tempfile_decorated_dummy()
        ok_startswith(filename, target)

@with_tempfile
@with_tempfile
def test_nested_with_tempfile_basic(f1, f2):
    ok_(f1 != f2)
    ok_(not os.path.exists(f1))
    ok_(not os.path.exists(f2))


# And the most obscure case to test.  Generator for the test is
# used as well to verify that every one of those functions adds new argument
# to the end of incoming arguments.
@with_tempfile(prefix="TEST", suffix='big')
@with_tree((('f1.txt', 'load'),))
@with_tempfile(suffix='.cfg')
@with_tempfile(suffix='.cfg.old')
@with_testrepos(flavors=local_testrepo_flavors, count=1)
def check_nested_with_tempfile_parametrized_surrounded(
        param, f0, tree, f1, f2, repo):
    eq_(param, "param1")
    ok_(f0.endswith('big'), msg="got %s" % f0)
    ok_(os.path.basename(f0).startswith('TEST'), msg="got %s" % f0)
    ok_(os.path.exists(os.path.join(tree, 'f1.txt')))
    ok_(f1 != f2)
    ok_(f1.endswith('.cfg'), msg="got %s" % f1)
    ok_(f2.endswith('.cfg.old'), msg="got %s" % f2)
    ok_(repo)  # got some repo -- local or url


def test_nested_with_tempfile_parametrized_surrounded():
    yield check_nested_with_tempfile_parametrized_surrounded, "param1"


@with_tempfile(content="testtest")
def test_with_tempfile_content(f):
    ok_file_has_content(f, "testtest")
    ok_file_has_content(f, "test*", re_=True)


def test_with_tempfile_content_raises_on_mkdir():

    @with_tempfile(content="test", mkdir=True)
    def t():  # pragma: no cover
        raise AssertionError("must not be run")

    with assert_raises(ValueError):
        # after this commit, it will check when invoking, not when decorating
        t()


def test_with_testrepos():
    repos = []

    @with_testrepos
    def check_with_testrepos(repo):
        repos.append(repo)

    check_with_testrepos()

    eq_(len(repos),
        2 if on_windows  # TODO -- would fail now in DATALAD_TESTS_NONETWORK mode
          else (15 if dl_cfg.get('datalad.tests.nonetwork') else 16))  # local, local-url, clone, network

    for repo in repos:
        if not (repo.startswith('git://') or repo.startswith('http')):
            # either it is a "local" or a removed clone
            ok_(exists(opj(repo, '.git'))
                or
                not exists(opj(repo, '.git', 'remove-me')))


def test_get_resolved_values():
    from datalad.tests.utils import _get_resolved_flavors
    flavors = ['networkish', 'local']
    eq_(([] if dl_cfg.get('datalad.tests.nonetwork') else ['networkish'])
        + ['local'],
        _get_resolved_flavors(flavors))

    with patch_config({'datalad.tests.nonetwork': '1'}):
        eq_(_get_resolved_flavors(flavors), ['local'])

        # and one more to see the exception being raised if nothing to teston
        @with_testrepos(flavors=['network'])
        def magical():
            raise AssertionError("Must not be ran")
        assert_raises(SkipTest, magical)

def test_with_tempfile_mkdir():
    dnames = []  # just to store the name within the decorated function

    @with_tempfile(mkdir=True)
    def check_mkdir(d1):
        ok_(os.path.exists(d1))
        ok_(os.path.isdir(d1))
        dnames.append(d1)
        eq_(glob(os.path.join(d1, '*')), [])
        # Create a file to assure we can remove later the temporary load
        with open(os.path.join(d1, "test.dat"), "w") as f:
            f.write("TEST LOAD")

    check_mkdir()
    if not dl_cfg.get('datalad.tests.temp.keep'):
        ok_(not os.path.exists(dnames[0]))  # got removed


@with_tempfile()
def test_with_tempfile_default_prefix(d1):
    d = basename(d1)
    short = 'datalad_temp_'
    full = short + \
           'test_with_tempfile_default_prefix'
    if on_windows:
        ok_startswith(d, short)
        nok_startswith(d, full)
    else:
        ok_startswith(d, full)


@with_tempfile(prefix="nodatalad_")
def test_with_tempfile_specified_prefix(d1):
    ok_startswith(basename(d1), 'nodatalad_')
    ok_('test_with_tempfile_specified_prefix' not in d1)


def test_get_most_obscure_supported_name():
    n = get_most_obscure_supported_name()
    ok_startswith(n, OBSCURE_PREFIX)
    ok_(len(OBSCURE_FILENAMES) > 1)
    # from more complex to simpler ones
    ok_(len(OBSCURE_FILENAMES[0]) > len(OBSCURE_FILENAMES[-1]))
    print(repr(n))


def test_keeptemp_via_env_variable():

    if dl_cfg.get('datalad.tests.temp.keep'):  # pragma: no cover
        raise SkipTest("We have env variable set to preserve tempfiles")

    files = []

    @with_tempfile()
    def check(f):
        open(f, 'w').write("LOAD")
        files.append(f)

    with patch.dict('os.environ', {}):
        check()

    with patch.dict('os.environ', {'DATALAD_TESTS_TEMP_KEEP': '1'}):
        check()

    eq_(len(files), 2)
    ok_(not exists(files[0]), msg="File %s still exists" % files[0])
    ok_(    exists(files[1]), msg="File %s not exists" % files[1])

    rmtemp(files[-1])


@skip_wo_symlink_capability
@with_tempfile
def test_ok_symlink_helpers(tmpfile):

    assert_raises(AssertionError, ok_symlink, tmpfile)
    assert_raises(AssertionError, ok_good_symlink, tmpfile)
    assert_raises(AssertionError, ok_broken_symlink, tmpfile)

    tmpfile_symlink = tmpfile + '_symlink'
    Path(tmpfile_symlink).symlink_to(Path(tmpfile))

    # broken symlink
    ok_symlink(tmpfile_symlink)
    ok_broken_symlink(tmpfile_symlink)
    assert_raises(AssertionError, ok_good_symlink, tmpfile_symlink)

    with open(tmpfile, 'w') as tf:
        tf.write('test text')
    
    # tmpfile is still not a symlink here
    assert_raises(AssertionError, ok_symlink, tmpfile)
    assert_raises(AssertionError, ok_good_symlink, tmpfile)
    assert_raises(AssertionError, ok_broken_symlink, tmpfile)

    ok_symlink(tmpfile_symlink)
    ok_good_symlink(tmpfile_symlink)
    assert_raises(AssertionError, ok_broken_symlink, tmpfile_symlink)


def test_ok_startswith():
    ok_startswith('abc', 'abc')
    ok_startswith('abc', 'a')
    ok_startswith('abc', '')
    ok_startswith(' abc', ' ')
    ok_startswith('abc\r\n', 'a')  # no effect from \r\n etc
    assert_raises(AssertionError, ok_startswith, 'abc', 'b')
    assert_raises(AssertionError, ok_startswith, 'abc', 'abcd')


def test_nok_startswith():
    nok_startswith('abc', 'bc')
    nok_startswith('abc', 'c')
    assert_raises(AssertionError, nok_startswith, 'abc', 'a')
    assert_raises(AssertionError, nok_startswith, 'abc', 'abc')

def test_ok_generator():
    def func(a, b=1):
        return a+b
    def gen(a, b=1):  # pragma: no cover
        yield a+b
    # not sure how to determine if xrange is a generator
    assert_raises(AssertionError, ok_generator, range(2))
    assert_raises(AssertionError, ok_generator, gen)
    ok_generator(gen(1))
    assert_raises(AssertionError, ok_generator, func)
    assert_raises(AssertionError, ok_generator, func(1))


def _test_assert_Xwd_unchanged(func):
    orig_cwd = os.getcwd()
    orig_pwd = getpwd()

    @assert_cwd_unchanged
    def do_chdir():
        func(os.pardir)

    with assert_raises(AssertionError) as cm:
        do_chdir()

    eq_(orig_cwd, os.getcwd(),
        "assert_cwd_unchanged didn't return us back to cwd %s" % orig_cwd)
    eq_(orig_pwd, getpwd(),
        "assert_cwd_unchanged didn't return us back to pwd %s" % orig_pwd)

def test_assert_Xwd_unchanged():
    yield _test_assert_Xwd_unchanged, os.chdir
    yield _test_assert_Xwd_unchanged, chpwd


def _test_assert_Xwd_unchanged_ok_chdir(func):
    # Test that we are not masking out other "more important" exceptions

    orig_cwd = os.getcwd()
    orig_pwd = getpwd()

    @assert_cwd_unchanged(ok_to_chdir=True)
    def do_chdir_value_error():
        func(os.pardir)
        return "a value"

    with swallow_logs() as cml:
        eq_(do_chdir_value_error(), "a value")
        eq_(orig_cwd, os.getcwd(),
            "assert_cwd_unchanged didn't return us back to cwd %s" % orig_cwd)
        eq_(orig_pwd, getpwd(),
            "assert_cwd_unchanged didn't return us back to cwd %s" % orig_pwd)
        assert_not_in("Mitigating and changing back", cml.out)


def test_assert_Xwd_unchanged_ok_chdir():
    yield _test_assert_Xwd_unchanged_ok_chdir, os.chdir
    yield _test_assert_Xwd_unchanged_ok_chdir, chpwd


def test_assert_cwd_unchanged_not_masking_exceptions():
    # Test that we are not masking out other "more important" exceptions

    orig_cwd = os.getcwd()

    @assert_cwd_unchanged
    def do_chdir_value_error():
        os.chdir(os.pardir)
        raise ValueError("error exception")

    with swallow_logs(new_level=logging.WARN) as cml:
        with assert_raises(ValueError) as cm:
            do_chdir_value_error()
        # retrospect exception
        eq_(orig_cwd, os.getcwd(),
            "assert_cwd_unchanged didn't return us back to %s" % orig_cwd)
        assert_in("Mitigating and changing back", cml.out)

    # and again but allowing to chdir
    @assert_cwd_unchanged(ok_to_chdir=True)
    def do_chdir_value_error():
        os.chdir(os.pardir)
        raise ValueError("error exception")

    with swallow_logs(new_level=logging.WARN) as cml:
        assert_raises(ValueError, do_chdir_value_error)
        eq_(orig_cwd, os.getcwd(),
            "assert_cwd_unchanged didn't return us back to %s" % orig_cwd)
        assert_not_in("Mitigating and changing back", cml.out)


@with_tempfile(mkdir=True)
def _test_serve_path_via_http(test_fpath, use_ssl, auth, tmp_dir):  # pragma: no cover
    tmp_dir = Path(tmp_dir)
    test_fpath = Path(test_fpath)
    # First verify that filesystem layer can encode this filename
    # verify first that we could encode file name in this environment
    try:
        filesysencoding = sys.getfilesystemencoding()
        test_fpath_encoded = str(test_fpath.as_posix()).encode(filesysencoding)
    except UnicodeEncodeError:  # pragma: no cover
        raise SkipTest("Environment doesn't support unicode filenames")
    if test_fpath_encoded.decode(filesysencoding) != test_fpath.as_posix():  # pragma: no cover
        raise SkipTest("Can't convert back/forth using %s encoding"
                       % filesysencoding)

    test_fpath_full = tmp_dir / test_fpath
    test_fpath_full.parent.mkdir(parents=True, exist_ok=True)
    test_fpath_full.write_text(
        f'some txt and a randint {random.randint(1, 10)}')

    @serve_path_via_http(tmp_dir, use_ssl=use_ssl, auth=auth)
    def test_path_and_url(path, url):
        def _urlopen(url, auth=None):
            req = Request(url)
            if auth:
                req.add_header(
                    "Authorization",
                    b"Basic " + base64.standard_b64encode(
                        '{0}:{1}'.format(*auth).encode('utf-8')))
            return urlopen(req)

        # @serve_ should remove http_proxy from the os.environ if was present
        if not on_windows:
            assert_false('http_proxy' in os.environ)
        # get the "dir-view"
        dirurl = url + test_fpath.parent.as_posix()
        u = _urlopen(dirurl, auth)
        assert_true(u.getcode() == 200)
        html = u.read()
        # get the actual content
        file_html = _urlopen(
            url + url_quote(test_fpath.as_posix()), auth).read().decode()
        # verify we got the right one
        eq_(file_html, test_fpath_full.read_text())

        if bs4 is None:
            return

        # MIH is not sure what this part below is supposed to do
        # possibly some kind of internal consistency test
        soup = bs4.BeautifulSoup(html, "html.parser")
        href_links = [txt.get('href') for txt in soup.find_all('a')]
        assert_true(len(href_links) == 1)
        parsed_url = f"{dirurl}/{href_links[0]}"
        u = _urlopen(parsed_url, auth)
        html = u.read().decode()
        eq_(html, file_html)

    test_path_and_url()


def test_serve_path_via_http():
    for test_fpath in ['test1.txt',
                       Path('test_dir', 'test2.txt'),
                       Path('test_dir', 'd2', 'd3', 'test3.txt'),
                       'file with space test4',
                       u'Джэйсон',
                       get_most_obscure_supported_name(),
                      ]:
        yield _test_serve_path_via_http, test_fpath, False, None
        yield _test_serve_path_via_http, test_fpath, True, None
        yield _test_serve_path_via_http, test_fpath, False, ('ernie', 'bert')

    # just with the last one check that we did remove proxy setting
    with patch.dict('os.environ', {'http_proxy': 'http://127.0.0.1:9/'}):
        yield _test_serve_path_via_http, test_fpath, False, None


@known_failure_githubci_win
def test_without_http_proxy():

    @without_http_proxy
    def check(a, kw=False):
        assert_false('http_proxy' in os.environ)
        assert_false('https_proxy' in os.environ)
        assert_in(kw, [False, 'custom'])

    check(1)

    with patch.dict('os.environ', {'http_proxy': 'http://127.0.0.1:9/'}):
        check(1)
        check(1, "custom")
        with assert_raises(AssertionError):
            check(1, "wrong")

    with patch.dict('os.environ', {'https_proxy': 'http://127.0.0.1:9/'}):
        check(1)
    with patch.dict('os.environ', {'http_proxy': 'http://127.0.0.1:9/',
                                   'https_proxy': 'http://127.0.0.1:9/'}):
        check(1)


def test_assert_re_in():
    assert_re_in(".*", "")
    assert_re_in(".*", ["any"])

    # should do match not search
    assert_re_in("ab", "abc")
    assert_raises(AssertionError, assert_re_in, "ab", "cab")
    assert_raises(AssertionError, assert_re_in, "ab$", "abc")

    # Sufficient to have one entry matching
    assert_re_in("ab", ["", "abc", "laskdjf"])
    assert_raises(AssertionError, assert_re_in, "ab$", ["ddd", ""])

    # Tuples should be ok too
    assert_re_in("ab", ("", "abc", "laskdjf"))
    assert_raises(AssertionError, assert_re_in, "ab$", ("ddd", ""))

    # shouldn't "match" the empty list
    assert_raises(AssertionError, assert_re_in, "", [])


def test_skip_if_no_network():
    cleaned_env = os.environ.copy()
    cleaned_env.pop('DATALAD_TESTS_NONETWORK', None)
    # we need to run under cleaned env to make sure we actually test in both conditions
    with patch('os.environ', cleaned_env):
        @skip_if_no_network
        def somefunc(a1):
            return a1
        ok_(hasattr(somefunc, "network"))
        with patch_config({'datalad.tests.nonetwork': '1'}):
            assert_raises(SkipTest, somefunc, 1)
        with patch.dict('os.environ', {}):
            eq_(somefunc(1), 1)
        # and now if used as a function, not a decorator
        with patch_config({'datalad.tests.nonetwork': '1'}):
            assert_raises(SkipTest, skip_if_no_network)
        with patch.dict('os.environ', {}):
            eq_(skip_if_no_network(), None)


def test_skip_if_no_module():

    def testish():
        skip_if_no_module("nonexistingforsuremodule")
        raise ValueError
    assert_raises(SkipTest, testish)

    def testish2():
        skip_if_no_module("datalad")
        return "magic"
    eq_(testish2(), "magic")


def test_skip_if():

    with assert_raises(SkipTest):
        @skip_if(True)
        def f():  # pragma: no cover
            raise AssertionError("must have not been ran")
        f()

    @skip_if(False)
    def f():
        return "magical"
    eq_(f(), 'magical')


@assert_cwd_unchanged
@with_tempfile(mkdir=True)
def test_run_under_dir(d):
    orig_pwd = getpwd()
    orig_cwd = os.getcwd()

    @run_under_dir(d)
    def f(arg, kwarg=None):
        eq_(arg, 1)
        eq_(kwarg, 2)
        eq_(getpwd(), d)

    f(1, 2)
    eq_(getpwd(), orig_pwd)
    eq_(os.getcwd(), orig_cwd)

    # and if fails
    assert_raises(AssertionError, f, 1, 3)
    eq_(getpwd(), orig_pwd)
    eq_(os.getcwd(), orig_cwd)


def test_assert_dict_equal():
    assert_dict_equal({}, {})
    assert_dict_equal({"a": 3}, {"a": 3})
    assert_raises(AssertionError, assert_dict_equal, {1: 3}, {1: 4})
    assert_raises(AssertionError, assert_dict_equal, {1: 3}, {2: 4})
    assert_raises(AssertionError, assert_dict_equal, {1: 3}, {2: 4, 1: 3})
    assert_raises(AssertionError, assert_dict_equal, {1: 3}, {2: 4, 1: 'a'})
    try:
        import numpy as np
    except:  # pragma: no cover
        raise SkipTest("need numpy for this tiny one")
    # one is scalar another one array
    assert_raises(AssertionError, assert_dict_equal, {1: 0}, {1: np.arange(1)})
    assert_raises(AssertionError, assert_dict_equal, {1: 0}, {1: np.arange(3)})


def test_assert_str_equal():
    assert_str_equal("a", "a")
    assert_str_equal("a\n", "a\n")
    assert_str_equal("a\nb", "a\nb")
    assert_raises(AssertionError, assert_str_equal, "a", "a\n")
    assert_raises(AssertionError, assert_str_equal, "a", "b")
    assert_raises(AssertionError, assert_str_equal, "ab", "b")


def test_testsui():
    # just one for now to test conflicting arguments
    with assert_raises(ValueError):
        @with_testsui(responses='some', interactive=False)
        def some_func():   # pragma: no cover
            pass

    from datalad.ui import ui

    @with_testsui(responses=['yes', "maybe so"])
    def func2(x):
        assert x == 1
        eq_(ui.yesno("title"), True)
        eq_(ui.question("title2"), "maybe so")
        assert_raises(AssertionError, ui.question, "asking more than we know")
        return x*2
    eq_(func2(1), 2)

    @with_testsui(interactive=False)
    def func3(x):
        assert_false(ui.is_interactive)
        return x*3
    eq_(func3(2), 6)


def test_setup():
    # just verify that we monkey patched consts correctly
    from datalad.consts import DATASETS_TOPURL
    eq_(DATASETS_TOPURL, 'https://datasets-tests.datalad.org/')
    from datalad.tests.utils import get_datasets_topdir
    eq_(get_datasets_topdir(), 'datasets-tests.datalad.org')


def test_skip_ssh():
    with patch_config({'datalad.tests.ssh': False}):
        with assert_raises(SkipTest):
            skip_ssh(lambda: False)()


def test_probe_known_failure():
    # should raise assert error if function no longer fails
    with patch_config({'datalad.tests.knownfailures.probe': True}):
        with assert_raises(AssertionError):
            probe_known_failure(lambda: True)()

    with patch_config({'datalad.tests.knownfailures.probe': False}):
        ok_(probe_known_failure(lambda: True))


def test_ignore_nose_capturing_stdout():
    # Just test the logic, not really a situation under overwritten stdout
    def raise_exc():
        raise AttributeError('nose causes a message which includes words '
                             'StringIO and fileno')
    with assert_raises(AttributeError):
        ignore_nose_capturing_stdout(raise_exc)()


@skip_wo_symlink_capability
@with_tree(tree={'ingit': '', 'staged': 'staged', 'notingit': ''})
def test_ok_file_under_git_symlinks(path):
    # Test that works correctly under symlinked path
    orepo = GitRepo(path)
    orepo.add('ingit')
    orepo.commit('msg')
    orepo.add('staged')
    lpath = path + "-symlink"  # will also be removed AFAIK by our tempfile handling
    Path(lpath).symlink_to(Path(path))
    ok_symlink(lpath)
    ok_file_under_git(op.join(path, 'ingit'))
    ok_file_under_git(op.join(lpath, 'ingit'))
    ok_file_under_git(op.join(lpath, 'staged'))
    with assert_raises(AssertionError):
        ok_file_under_git(op.join(lpath, 'notingit'))
    with assert_raises(AssertionError):
        ok_file_under_git(op.join(lpath, 'nonexisting'))
