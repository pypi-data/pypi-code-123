"""
Nose test running.

This module implements ``test()`` and ``bench()`` functions for NumPy modules.

"""
from __future__ import division, absolute_import, print_function

import os
import sys
import warnings
#from numpy.compat import basestring


__all__ = ['get_package_name', 'run_module_suite', 'NoseTester',
           'get_package_name']


def get_package_name(filepath):
    """
    Given a path where a package is installed, determine its name.

    Parameters
    ----------
    filepath : str
        Path to a file. If the determination fails, "numpy" is returned.

    """

    fullpath = filepath[:]
    pkg_name = []
    while 'site-packages' in filepath or 'dist-packages' in filepath:
        filepath, p2 = os.path.split(filepath)
        if p2 in ('site-packages', 'dist-packages'):
            break
        pkg_name.append(p2)

    # if package name determination failed, just default to numpy/scipy
    if not pkg_name:
        if 'scipy' in fullpath:
            return 'scipy'
        else:
            return 'numpy'

    # otherwise, reverse to get correct order and return
    pkg_name.reverse()

    # don't include the outer egg directory
    if pkg_name[0].endswith('.egg'):
        pkg_name.pop(0)

    return '.'.join(pkg_name)


def run_module_suite(file_to_run=None, argv=None):
    """
    Run a test module.

    Equivalent to calling ``$ nosetests <argv> <file_to_run>`` from
    the command line

    Parameters
    ----------
    file_to_run : str, optional
        Path to test module, or None.
        By default, run the module from which this function is called.
    argv : list of strings
        Arguments to be passed to the nose test runner. ``argv[0]`` is
        ignored. All command line arguments accepted by ``nosetests``
        will work. If it is the default value None, sys.argv is used.

        .. versionadded:: 1.9.0

    Examples
    --------
    Adding the following::

        if __name__ == "__main__" :
            run_module_suite(argv=sys.argv)

    at the end of a test module will run the tests when that module is
    called in the python interpreter.

    """
    if file_to_run is None:
        f = sys._getframe(1)
        file_to_run = f.f_locals.get('__file__', None)
        if file_to_run is None:
            raise AssertionError

    if argv is None:
        argv = sys.argv + [file_to_run]
    else:
        argv = argv + [file_to_run]

    import nose
    nose.run(argv=argv, addplugins=[])


class NoseTester(object):
    """
    Nose test runner.

    This class is made available as numpy.testing.Tester, and a test function
    is typically added to a package's __init__.py like so::

      from numpy.testing import Tester
      test = Tester().test

    Calling this test function finds and runs all tests associated with the
    package and all its sub-packages.

    Attributes
    ----------
    package_path : str
        Full path to the package to test.
    package_name : str
        Name of the package to test.

    Parameters
    ----------
    package : module, str or None, optional
        The package to test. If a string, this should be the full path to
        the package. If None (default), `package` is set to the module from
        which `NoseTester` is initialized.
    raise_warnings : None, str or sequence of warnings, optional
        This specifies which warnings to configure as 'raise' instead
        of being shown once during the test execution.  Valid strings are:

          - "develop" : equals ``(Warning,)``
          - "release" : equals ``()``, don't raise on any warnings.

        Default is "release".
    depth : int, optional
        If `package` is None, then this can be used to initialize from the
        module of the caller of (the caller of (...)) the code that
        initializes `NoseTester`. Default of 0 means the module of the
        immediate caller; higher values are useful for utility routines that
        want to initialize `NoseTester` objects on behalf of other code.

    """
    def __init__(self, package=None, raise_warnings="release", depth=0):
        # Back-compat: 'None' used to mean either "release" or "develop"
        # depending on whether this was a release or develop version of
        # numpy. Those semantics were fine for testing numpy, but not so
        # helpful for downstream projects like scipy that use
        # numpy.testing. (They want to set this based on whether *they* are a
        # release or develop version, not whether numpy is.) So we continue to
        # accept 'None' for back-compat, but it's now just an alias for the
        # default "release".
        if raise_warnings is None:
            raise_warnings = "release"

        package_name = None
        if package is None:
            f = sys._getframe(1 + depth)
            package_path = f.f_locals.get('__file__', None)
            if package_path is None:
                raise AssertionError
            package_path = os.path.dirname(package_path)
            package_name = f.f_locals.get('__name__', None)
        elif isinstance(package, type(os)):
            package_path = os.path.dirname(package.__file__)
            package_name = getattr(package, '__name__', None)
        else:
            package_path = str(package)

        self.package_path = package_path

        # Find the package name under test; this name is used to limit coverage
        # reporting (if enabled).
        if package_name is None:
            package_name = get_package_name(package_path)
        self.package_name = package_name

        # Set to "release" in constructor in maintenance branches.
        self.raise_warnings = raise_warnings

    def _test_argv(self, label, verbose, extra_argv):
        ''' Generate argv for nosetest command

        Parameters
        ----------
        label : {'fast', 'full', '', attribute identifier}, optional
            see ``test`` docstring
        verbose : int, optional
            Verbosity value for test outputs, in the range 1-10. Default is 1.
        extra_argv : list, optional
            List with any extra arguments to pass to nosetests.

        Returns
        -------
        argv : list
            command line arguments that will be passed to nose
        '''
        argv = [__file__, self.package_path, '-s']
        if label and label != 'full':
            if not isinstance(label, str):
                raise TypeError('Selection label should be a string')
            if label == 'fast':
                label = 'not slow'
            argv += ['-A', label]
        argv += ['--verbosity', str(verbose)]

        # When installing with setuptools, and also in some other cases, the
        # test_*.py files end up marked +x executable. Nose, by default, does
        # not run files marked with +x as they might be scripts. However, in
        # our case nose only looks for test_*.py files under the package
        # directory, which should be safe.
        argv += ['--exe']

        if extra_argv:
            argv += extra_argv
        return argv

    def _show_system_info(self):
        import nose
        pyversion = sys.version.replace('\n', '')
        print("Python version %s" % pyversion)
        print("nose version %d.%d.%d" % nose.__versioninfo__)

    def _get_custom_doctester(self):
        """ Return instantiated plugin for doctests

        Allows subclassing of this class to override doctester

        A return value of None means use the nose builtin doctest plugin
        """
        from .noseclasses import NumpyDoctest
        return NumpyDoctest()

    def prepare_test_args(self, label='fast', verbose=1, extra_argv=None,
                          doctests=False, coverage=False, timer=False):
        """
        Run tests for module using nose.

        This method does the heavy lifting for the `test` method. It takes all
        the same arguments, for details see `test`.

        See Also
        --------
        test

        """
        # fail with nice error message if nose is not present
        import nose
        # compile argv
        argv = self._test_argv(label, verbose, extra_argv)
        # our way of doing coverage
        if coverage:
            argv += ['--cover-package=%s' % self.package_name, '--with-coverage',
                   '--cover-tests', '--cover-erase']

        if timer:
            if timer is True:
                argv += ['--with-timer']
            elif isinstance(timer, int):
                argv += ['--with-timer', '--timer-top-n', str(timer)]

        # construct list of plugins
        import nose.plugins.builtin
        from nose.plugins import EntryPointPluginManager
        from .noseclasses import Unplugger
        plugins = []# KnownFailurePlugin()]
        plugins += [p() for p in nose.plugins.builtin.plugins]
        try:
            # External plugins (like nose-timer)
            entrypoint_manager = EntryPointPluginManager()
            entrypoint_manager.loadPlugins()
            plugins += [p for p in entrypoint_manager.plugins]
        except ImportError:
            # Relies on pkg_resources, not a hard dependency
            pass

        # add doctesting if required
        doctest_argv = '--with-doctest' in argv
        if doctests == False and doctest_argv:
            doctests = True
        plug = self._get_custom_doctester()
        if plug is None:
            # use standard doctesting
            if doctests and not doctest_argv:
                argv += ['--with-doctest']
        else:  # custom doctesting
            if doctest_argv:  # in fact the unplugger would take care of this
                argv.remove('--with-doctest')
            plugins += [Unplugger('doctest'), plug]
            if doctests:
                argv += ['--with-' + plug.name]
        return argv, plugins

    def test(self, label='fast', verbose=1, extra_argv=None,
             doctests=False, coverage=False, raise_warnings=None,
             timer=False):
        """
        Run tests for module using nose.

        Parameters
        ----------
        label : {'fast', 'full', '', attribute identifier}, optional
            Identifies the tests to run. This can be a string to pass to
            the nosetests executable with the '-A' option, or one of several
            special values.  Special values are:
            * 'fast' - the default - which corresponds to the ``nosetests -A``
              option of 'not slow'.
            * 'full' - fast (as above) and slow tests as in the
              'no -A' option to nosetests - this is the same as ''.
            * None or '' - run all tests.
            attribute_identifier - string passed directly to nosetests as '-A'.
        verbose : int, optional
            Verbosity value for test outputs, in the range 1-10. Default is 1.
        extra_argv : list, optional
            List with any extra arguments to pass to nosetests.
        doctests : bool, optional
            If True, run doctests in module. Default is False.
        coverage : bool, optional
            If True, report coverage of NumPy code. Default is False.
            (This requires the `coverage module:
             <http://nedbatchelder.com/code/modules/coverage.html>`_).
        raise_warnings : None, str or sequence of warnings, optional
            This specifies which warnings to configure as 'raise' instead
            of being shown once during the test execution.  Valid strings are:

              - "develop" : equals ``(Warning,)``
              - "release" : equals ``()``, don't raise on any warnings.

            The default is to use the class initialization value.
        timer : bool or int, optional
            Timing of individual tests with ``nose-timer`` (which needs to be
            installed).  If True, time tests and report on all of them.
            If an integer (say ``N``), report timing results for ``N`` slowest
            tests.

        Returns
        -------
        result : object
            Returns the result of running the tests as a
            ``nose.result.TextTestResult`` object.

        Notes
        -----
        Each NumPy module exposes `test` in its namespace to run all tests for it.
        For example, to run all tests for numpy.lib:

        >>> result.errors #doctest: +SKIP
        []
        >>> result.knownfail #doctest: +SKIP
        []
        """

        # cap verbosity at 3 because nose becomes *very* verbose beyond that
        verbose = min(verbose, 3)

        argv, plugins = self.prepare_test_args(
                label, verbose, extra_argv, doctests, coverage, timer)

        if doctests:
            print("Running unit tests and doctests for %s" % self.package_name)
        else:
            print("Running unit tests for %s" % self.package_name)

        self._show_system_info()

        # reset doctest state on every run
        import doctest
        doctest.master = None

        if raise_warnings is None:
            raise_warnings = self.raise_warnings

        _warn_opts = dict(develop=(Warning,),
                          release=())
        if isinstance(raise_warnings, str):
            raise_warnings = _warn_opts[raise_warnings]

        # Filter out some deprecation warnings inside nose 1.3.7 when run
        # on python 3.5b2. See
        #     https://github.com/nose-devs/nose/issues/929
        # Note: it is hard to filter based on module for sup (lineno could
        #       be implemented).
        warnings.filterwarnings("ignore", message=".*getargspec.*",
                                category=DeprecationWarning,
                                module=r"nose\.")

        from .noseclasses import NumpyTestProgram

        t = NumpyTestProgram(argv=argv, exit=False, plugins=plugins)

        return t.result

    def bench(self, label='fast', verbose=1, extra_argv=None):
        """
        Run benchmarks for module using nose.

        Parameters
        ----------
        label : {'fast', 'full', '', attribute identifier}, optional
            Identifies the benchmarks to run. This can be a string to pass to
            the nosetests executable with the '-A' option, or one of several
            special values.  Special values are:
            * 'fast' - the default - which corresponds to the ``nosetests -A``
              option of 'not slow'.
            * 'full' - fast (as above) and slow benchmarks as in the
              'no -A' option to nosetests - this is the same as ''.
            * None or '' - run all tests.
            attribute_identifier - string passed directly to nosetests as '-A'.
        verbose : int, optional
            Verbosity value for benchmark outputs, in the range 1-10. Default is 1.
        extra_argv : list, optional
            List with any extra arguments to pass to nosetests.

        Returns
        -------
        success : bool
            Returns True if running the benchmarks works, False if an error
            occurred.

        Notes
        -----
        Benchmarks are like tests, but have names starting with "bench" instead
        of "test", and can be found under the "benchmarks" sub-directory of the
        module.

        Each NumPy module exposes `bench` in its namespace to run all benchmarks
        for it.

        Examples
        --------
        """

        print("Running benchmarks for %s" % self.package_name)
        self._show_system_info()

        argv = self._test_argv(label, verbose, extra_argv)
        argv += ['--match', r'(?:^|[\\b_\\.%s-])[Bb]ench' % os.sep]

        # import nose or make informative error
        import nose

        # get plugin to disable doctests
        from .noseclasses import Unplugger
        add_plugins = [Unplugger('doctest')]

        return nose.run(argv=argv, addplugins=add_plugins)
