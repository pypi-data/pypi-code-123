"""
This module contains the command line interface to molcas_suite
"""

import os
import sys
import argparse
import xyz_py as xyzp
from textwrap import dedent

import hpc_suite as hpc
from hpc_suite.action import OrderAction
from angmom_suite import QuaxAction, cfp_parser

from . import generate_input
from . import generate_job
from . import extractor
from . import barrier
from . import orbs
from . import cfp


def generate_input_func(args):
    """
    Wrapper function for command line interface call to generate_input

    Parameters
    ----------
    args : argparser object
        command line arguments

    Returns
    -------
    None

    """
    labels, coords = xyzp.load_xyz(args.xyz_input)
    labels = xyzp.add_label_indices(labels)

    # set output to stem of xyz_input if not supplied
    path = args.xyz_input
    abs_stem = os.path.splitext(path)[0]

    output = args.output if args.output else abs_stem + '.input'

    if args.xfield_input and not args.xfield_external:
        with open(args.xfield_input, 'r') as f:
            xfield = [
                [int(num) for num in line.split()]
                for line in f if line.strip() != ""
                     ]
    else:
        xfield = []

    xyz_output = args.xyz_output if args.xyz_output else args.xyz_external

    generate_input.generate_input(
        labels,
        coords,
        args.central_atom,
        args.charge,
        args.n_active_elec,
        args.n_active_orb,
        args.n_coord_atoms,
        output,
        xfield=xfield,
        xfield_ext=args.xfield_external,
        xyz_ext=args.xyz_external,
        xyz_out=xyz_output,
        seward_decomp=args.seward_decomp,
        seward_extra=args.seward_extra,
        basis_set_central=args.basis_set_central,
        basis_set_coord=args.basis_set_coord,
        basis_set_remaining=args.basis_set_remaining,
        casscf_extra=args.rasscf_extra,
        high_S_only=args.high_S_only,
        initial_orb=args.initial_orb,
        max_orb=args.max_orb,
        caspt2=args.caspt2,
        rassi=args.rassi,
        rassi_extra=args.rassi_extra,
        single_aniso=args.single_aniso,
        single_aniso_extra=args.single_aniso_extra,
        quax=args.quax,
        skip_magneto=args.skip_magneto,
        ang_central=args.ang_central
    )


def generate_job_func(args, unknown_args):
    """
    Wrapper function for command line interface call to gen_submission

    Parameters
    ----------
    args : argparser object
        command line arguments
    unknown_args : list
        unknown command line flags to be passed on to a secondary parser

    Returns
    -------
    None

    """
    path = args.input_name
    base = os.path.basename(path)
    rel_stem = os.path.splitext(base)[0]
    abs_stem = os.path.splitext(path)[0]

    project_name = args.project_name if args.project_name else rel_stem
    output_name = args.output_name if args.output_name else abs_stem + '.out'
    err_name = args.err_name if args.err_name else abs_stem + '.err'

    if args.Help:
        unknown_args.append('--help')

    generate_job.gen_submission(
        project_name=project_name,
        input_name=args.input_name, output_name=output_name, err_name=err_name,
        molcas_module=args.molcas_module, molcas_path=args.molcas_path,
        memory=args.memory, disk=args.disk, scratch=args.scratch,
        in_scratch=args.in_scratch, hpc_args=unknown_args)


def extractor_func(args, unknown_args):
    """
    Wrapper function for command line interface call to extractor

    Parameters
    ----------
    args : argparser object
        command line arguments
    unknown_args : list
        unknown command line flags to be passed on to a secondary parser

    Returns
    -------
    None

    """

    selected = args.order

    if not selected:
        sys.exit("No section selected for extraction!")

    # default filter selection {source: destination}
    default_filter = {
        "quax": {1: ()},  # by default select first occurrence
        "cfp": {1: ()},  # by default select first occurrence
        "timing": hpc.store.keep_all("occurrence")  # by default keep all
    }

    store_args = hpc.read_args(['store'] + unknown_args)

    # set up default filter
    store_args.filter = store_args.filter or \
        [default_filter.get(item, None) for item, _ in selected]

    hpc.store_func(store_args, extractor.make_extractor, selected)


def barrier_func(args):
    """
    Wrapper function for command line interface call to barrier

    Parameters
    ----------
    args : argparser object
        command line arguments

    Returns
    -------
    None

    """

    barrier.barrier(
        args.molcas_output,
        args.k_max,
        args.bz,
        *args.jls,
        trans_colour=args.trans_colour,
        state_colour=args.state_colour,
        show=args.show,
        save=args.save,
        save_name=args.save_name,
        xlabel=args.x_label,
        ylabel=args.y_label,
        yax2=args.yax2,
        yax2_label=args.yax2_label,
        yax2_conv=args.yax2_conv,
        print_datafile=not args.no_datafile,
        verbose=not args.quiet
    )

    return


def orbs_func(args):
    """
    Wrapper function for command line interface call to orbs

    Parameters
    ----------
    args : argparser object
        command line arguments

    Returns
    -------
    None

    """
    orbs.orbital_analysis(
        args.h5file,
        orbname=args.orbfile,
        pattern=args.sep,
        thr=args.thr,
        wfmode=args.wf,
        outfile=args.out,
        alpha=args.alpha,
        beta=args.beta
    )

    return


def rotate_func(args):
    """
    Wrapper function for command line interface call to rotate

    Parameters
    ----------
    args : argparser object
        command line arguments

    Returns
    -------
    None

    """

    # Parse swap string
    swap_orb = []
    swap_space = []
    # Reparse if user has included quotation marks
    if len(args.swap_string) == 1 and args.swap_string[0].count(" ") > 0:
        args.swap_string = args.swap_string[0].split(" ")

    for pair in args.swap_string:
        [index, space] = pair.split("-")
        swap_orb.append(int(index))
        swap_space.append(space)

    orbs.rotate_spaces(
        orbname=args.orbfile,
        swap_orb=swap_orb,
        swap_space=swap_space,
        outfile=args.out
    )

    return


def reorder_func(args):
    """
    Wrapper function for command line interface call to reorder

    Parameters
    ----------
    args : argparser object
        command line arguments

    Returns
    -------
    None

    """

    # Parse swap string
    swap_list = []
    # Reparse if user has included quotation marks
    if len(args.swap_string) == 1 and args.swap_string[0].count(" ") > 0:
        args.swap_string = args.swap_string[0].split(" ")

    for pair in args.swap_string:
        sep = pair.split("-")
        initial = int(sep[0]) - 1
        final = int(sep[1]) - 1
        swap_list.append([initial, final])

    orbs.reorder_orbitals(
        orbname=args.orbfile,
        swap_list=swap_list,
        outfile=args.out
    )

    return


def cfp_func(args, unknown_args):
    """
    Wrapper function for command line interface call to cfp.

    Parameters
    ----------
    args : argparser object
        command line arguments
    unknown_args : list
        unknown command line flags to be passed on to a secondary parser

    Returns
    -------
    None
    """

    store_args = hpc.read_args(['store'] + unknown_args)

    options = {
        'basis': args.basis,
        'symbol': args.symbol,
        'space': args.space,
        'ion': args.ion,
        'k_max': args.k_max,
        'theta': args.theta,
        'quax': args.quax,
        'ground': args.ground,
        'verbose': args.verbose,
        'comp_thresh': args.comp_thresh,
        'ener_thresh': args.ener_thresh,
        'field': args.field
    }

    hpc.store_func(store_args, cfp.make_evaluator, (options,))


def read_args(arg_list=None):
    """
    Parser for command line arguments. Uses subparsers for individual programs

    Parameters
    ----------
    args : argparser object
        command line arguments

    Returns
    -------
    None

    """

    description = dedent(
        '''
        A package for dealing with OpenMOLCAS input and output files.

        Available programs:
            molcas_suite generate_input ...
            molcas_suite generate_job ...
            molcas_suite extractor ...
            molcas_suite barrier ...
            molcas_suite orbs ...
            molcas_suite rotate ...
            molcas_suite cfp ...
        '''
    )

    epilog = dedent(
        """To display options for a specific program, use molcas_suite PROGRAMNAME -h""" # noqa
    )

    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=argparse.RawTextHelpFormatter
    )

    subparsers = parser.add_subparsers(dest='prog')

    # Generate Input files

    gen_inp = subparsers.add_parser(
        'generate_input',
        formatter_class=argparse.RawTextHelpFormatter
    )
    gen_inp.set_defaults(func=generate_input_func)

    gen_inp.add_argument(
        'xyz_input',
        type=str,
        help='Input file containing the xyz-coordinates.'
    )

    gen_inp.add_argument(
        'central_atom',
        type=str,
        help='Indexed atomic label of central ion of complex, e.g. "Dy1".'
    )

    gen_inp.add_argument(
        'n_active_elec',
        type=int,
        help='Number of electrons in active space.'
    )

    gen_inp.add_argument(
        'n_active_orb',
        type=int,
        help='Number of orbitals in active space.'
    )

    gen_inp.add_argument(
        'n_coord_atoms',
        type=int,
        help='Number of atoms coordinated to central atom.'
    )

    gen_inp.add_argument(
        'charge',
        type=int,
        default=0,
        help='Molecular charge.'
    )

    gen_inp.add_argument(
        '--output',
        type=str,
        default=None,
        help='Name of resulting OpenMolcas input file.'
    )

    gen_inp.add_argument(
        '--xfield_input',
        type=str,
        default=[],
        help=dedent(
            """\
            Name of the file containing input charges and dipoles in raw format
            Each line contains < x y z q dipx dipy dipz >.
            """
        )
    )

    gen_inp.add_argument(
        '--xfield_external',
        type=str,
        help='Name of the external file containing charges '
             + 'and multipoles in MOLCAS format.'
    )

    gen_inp.add_argument(
        '--seward_decomp',
        type=str,
        default="High Cholesky",
        choices=["High Cholesky", "RICD_acCD"],
        help='Option for Cholesky decomposition in MOLCAS.'
    )

    gen_inp.add_argument(
        '--seward_extra',
        type=str,
        action='append',
        default=[],
        help='Additional options for seward section.'
    )

    gen_inp.add_argument(
        '--basis_set_central',
        type=str,
        default="ANO-RCC-VTZP",
        help='Basis set of the central ion metal ion.'
    )

    gen_inp.add_argument(
        '--basis_set_coord',
        type=str,
        default="ANO-RCC-VDZP",
        help='Basis set of the coordinating atoms.'
    )

    gen_inp.add_argument(
        '--basis_set_remaining',
        type=str,
        default="ANO-RCC-VDZ",
        help='Basis set of the remaining atoms.'
    )

    gen_inp.add_argument(
        '--rasscf_extra',
        type=str,
        action='append',
        default=[],
        help='Additional options for RASSCF section.'
    )

    gen_inp.add_argument(
        '--high_S_only',
        default=False,
        action='store_true',
        help='If specified, only consider the highest spin state.'
    )

    gen_inp.add_argument(
        '--initial_orb',
        type=str,
        default="",
        help='Path to a custom input guess orbital file used in the initial '
             + 'RASSCF call.'
    )

    gen_inp.add_argument(
        '--max_orb',
        type=int,
        default=None,
        help=dedent(
            """\
            Maximum number of RasOrb files to produce one for each root up to
            the specified maximum. Default = number of roots per spin state.
            """
        )
    )

    gen_inp.add_argument(
        '--caspt2',
        type=bool,
        default=False,
        metavar='True/False',
        help='Include (True) a CASPT2 section.'
    )

    gen_inp.add_argument(
        '--rassi',
        type=bool,
        default=True,
        metavar='True/False',
        help='Include (Default, True) a RASSI section.'
    )

    gen_inp.add_argument(
        '--rassi_extra',
        type=str,
        action='append',
        default=[],
        help='Additional options for RASSI section.'
    )

    gen_inp.add_argument(
        '--xyz_external',
        type=str,
        default="",
        help='Name of the external xyz-file containing coordinates and'
             + 'basis set labels in extended MOLCAS format.'
    )

    gen_inp.add_argument(
        '--xyz_output',
        type=str,
        default="",
        help='Output file containing the xyz-coordinates'
             + ' including basis set labels.'
    )

    gen_inp.add_argument(
        '--single_aniso',
        type=bool,
        default=True,
        metavar='True/False',
        help='Include (True) a SINGLE_ANISO section.'
    )

    gen_inp.add_argument(
        '--single_aniso_extra',
        type=str,
        action='append',
        default=[],
        help='Additional options for SINGLE_ANISO section.'
    )

    gen_inp.add_argument(
        '--basis',
        default='j',
        help='Basis of the quax info read from Molcas output.'
    )

    gen_inp.add_argument(
        '--quax',
        action=QuaxAction,
        help=('Molcas output or HDF5 database containing the rotation matrix '
              'for the CFP reference frame. Use together with --basis.')
    )

    gen_inp.add_argument(
        '--skip_magneto',
        default=False,
        action='store_true',
        help='If True, skip calculation of magnetic data.'
    )

    gen_inp.add_argument(
        '--ang_central',
        default=False,
        action='store_true',
        help='if True, Angular momentum will match the'
             + ' central metal coordinates which will not be shifted.'
    )

    # Generate Jobscript

    job = subparsers.add_parser(
        'generate_job',
        description="""
        Creates shell script for running molcas calculation
        """,
    )

    job.set_defaults(func=generate_job_func)

    job.add_argument(
        '-H', '--Help', const='generate_job',
        action=hpc.SecondaryHelp,
        help='show help message for additional arguments and exit'
    )

    molcas_job = job.add_argument_group('molcas specific arguments')

    molcas_job.add_argument(
        'input_name',
        type=str,
        help='Name of molcas input file.'
    )

    molcas_job.add_argument(
        '--output_name',
        type=str,
        help='Name of molcas output file, default = stem of input + .out'
    )

    molcas_job.add_argument(
        '--err_name',
        type=str,
        help='Name of molcas error file, default = stem of input + .err'
    )

    molcas_job.add_argument(
        '--project_name',
        type=str,
        help='Job name, default = stem of input file name'
    )

    molcas_job.add_argument(
        '--molcas_module',
        type=str,
        help='Path to molcas module.'
    )

    molcas_job.add_argument(
        '--molcas_path',
        type=str,
        help='Path to the molcas executables, e.g. the $MOLCAS env variable'
    )

    molcas_job.add_argument(
        '--scratch',
        type=str,
        help='Path to the molcas scratch directory'
    )

    molcas_job.add_argument(
        '--in_scratch',
        default=None,
        action='store_true',  # todo: change to BooleanOptionalAction
        help='Run Molcas job entirely in scratch'
    )

    molcas_job.add_argument(
        '--memory',
        type=int,
        help='Amount of memory given to molcas in megabytes'
    )

    molcas_job.add_argument(
        '--disk',
        type=int,
        help='Amount of disk given to molcas in megabytes'
    )

    # Extractor

    extract = subparsers.add_parser(
        'extractor',
        description="""Program which facilitates extraction of data from the
        human-readable text output and *.hdf5 output files from an (Open)Molcas
        calculation.""",
        epilog="""Example: molcas_suite extractor -i dy.out -o CFPs_dy.hdf5
        --cfp j""")

    extract.set_defaults(func=extractor_func)

    extract.add_argument(
        '-H', '--Help', const='store',
        action=hpc.SecondaryHelp,
        help='show help message for additional arguments and exit'
    )

    extract.add_argument(
        '--cfp',
        nargs=1,
        action=OrderAction,
        choices=["l", "j", "zeeman"],
        help='extract CFPs (by order)'
    )

    extract.add_argument(
        '--quax',
        nargs=1,
        action=OrderAction,
        choices=["l", "j", "zeeman"],
        help='extract quax (by order)'
    )

    extract.add_argument(
        '--rassi',
        nargs='+',
        action=OrderAction,
        choices=["SOS_energies", "SOS_coefficients", "SOS_angmom",
                 "HSO_matrix", "SFS_energies", "SFS_angmom", "SFS_AMFIint",
                 "spin_mult", "center_coordinates", "SFS_edipmom",
                 "SOS_edipmom"],
        help='followed by list of items to read from the rassi.h5 file'
    )

    extract.add_argument(
        '--rasscf',
        nargs='+',
        action=OrderAction,
        choices=['energies'],
        help=('followed by list of items to read from the rasscf.h5 file or '
              'molcas output file (by multiplicity)')
    )

    extract.add_argument(
        '--gradients',
        action=OrderAction,
        help='extract gradients (by multiplicity/root)'
    )

    extract.add_argument(
        '--nacs',
        nargs='+',
        action=OrderAction,
        choices=["total", "CSF", "CI"],
        help=('extract non-adiabatic/derivative coupling vectors '
              '(by multiplicity/root_i/root_j)')
    )

    extract.add_argument(
        '--wf_spec',
        nargs='+',
        action=OrderAction,
        choices=extractor.MOLCAS_WF_PRGS,
        help=('extract wave function specification (by multiplicity)')
    )

    extract.add_argument(
        '--timing',
        nargs='+',
        action=OrderAction,
        choices=extractor.MOLCAS_PRGS,
        help=('extract timings of specified modules (by order)')
    )

    extract.add_argument(
        '--timestamp',
        nargs='+',
        action=OrderAction,
        choices=extractor.MOLCAS_PRGS,
        help=('extract timestamp of specified modules (by order)')
    )

    # Barrier figure

    barrier = subparsers.add_parser(
        'barrier',
        description="""
        Creates barrier figure of lowest lying J multiplet.
        Transition probabilities are given by magnetic moment operator.
        Note a small quantisation field is applied along the z axis to give
        correct <Jz> values
        """
    )

    barrier.set_defaults(func=barrier_func)

    barrier.add_argument(
        "molcas_output",
        type=str,
        help='Molcas output file name'
    )

    barrier.add_argument(
        "--k_max",
        type=int,
        default=False,
        metavar="value",
        help="Maximum value of k to use in Crystal Field Hamiltonian\n\
              default = 2J"
    )

    barrier.add_argument(
        "--bz",
        type=float,
        default=25E-6,
        metavar="value",
        help="Magnetic field strength in z direction in Tesla\n\
              (x and y are zero), default=25 uT"
    )

    barrier.add_argument(
        "--jls",
        type=float,
        nargs=3,
        default=[None, None, None],
        metavar="J, L, S",
        help="J, L, and S quantum numbers (all are needed), default is to\n\
              guess from number of active orbitals/electrons in output file"
    )

    barrier.add_argument(
        "--trans_colour",
        type=str,
        default="#ff0000",
        metavar="value",
        help="Colour for transition arrows as hex or name (default red)"
    )

    barrier.add_argument(
        "--state_colour",
        type=str,
        default="black",
        metavar="value",
        help="Colour for states as hex or name"
    )

    barrier.add_argument(
        "--show",
        action="store_true",
        default=False,
        help="If true, show barrier figure on screen"
    )

    barrier.add_argument(
        "--save",
        action="store_true",
        default=False,
        help="If true, save barrier figure to current directory"
    )

    barrier.add_argument(
        "--save_name",
        type=str,
        default="barrier.svg",
        help="File to save barrier figure to"
    )

    barrier.add_argument(
        "--x_label",
        type=str,
        default=r"$\langle \ \hat{J}_{z} \ \rangle$",
        help="Label for x axis"
    )

    barrier.add_argument(
        "--y_label",
        type=str,
        default=r"Energy (cm$^{-1}$)",
        help="Label for primary (left) y axis"
    )

    barrier.add_argument(
        "--yax2",
        action="store_true",
        default=False,
        help="If true, include secondary (left) y axis"
    )

    barrier.add_argument(
        "--yax2_label",
        type=str,
        default=r"Energy (K)",
        help="Label for secondary (right) y axis"
    )

    barrier.add_argument(
        "--yax2_conv",
        type=float,
        default=1.4,
        help="Conversion factor between left --> right y axes"
             + "(default is cm-1 --> K)"
    )

    barrier.add_argument(
        "--no_datafile",
        action="store_true",
        default=False,
        help="Disable printing of datafile to execution directory"
    )

    barrier.add_argument(
        "--quiet",
        action="store_true",
        default=False,
        help="Prevent output of file names to screen"
    )

    # Orbital analysis
    orbitals = subparsers.add_parser('orbs')
    orbitals.set_defaults(func=orbs_func)

    orbitals.add_argument(
        'h5file',
        type=str,
        help='OpenMolcas HDF5 file name'
    )

    orbitals.add_argument(
        'orbfile',
        type=str,
        nargs='?',
        default=None,
        help='OpenMolcas ASCII file name (optional)'
             + '- overrides MO information from HDF5 file'
    )

    orbitals.add_argument(
        '--sep',
        type=str,
        default='cnl',
        choices=['c', 'cn', 'cl', 'cnl', 'clm', 'cnlm'],
        help='Pattern used to separate AO contributions;'
             + 'string is a subset of c (atom index),'
             + ' n (shell number), l (angular momentum)'
             + 'and m (angular momentum projection). Default: cnl'
    )

    orbitals.add_argument(
        '--thr',
        type=float,
        default=1.0,
        help='Percentage threshold for printing contributions'
    )
    orbitals.add_argument(
        '--wf',
        action='store_true',
        default=False,
        help='Enables wf mode. Equivalent to --sep cnlm'
    )
    orbitals.add_argument(
        '--out',
        type=str,
        default=None,
        help='Path to output file for the orbital analysis'
    )

    orbitals.add_argument(
        '--alpha',
        action='store_true',
        default=False,
        help='Print alpha orbitals instead of default'
             + 'natural orbitals (UHF only)'
    )

    orbitals.add_argument(
        '--beta',
        action='store_true',
        default=False,
        help='Print beta orbitals instead of default'
             + 'natural orbitals (UHF only)'
    )

    # Rotation of spaces
    rotate = subparsers.add_parser('rotate')
    rotate.set_defaults(func=rotate_func)

    rotate.add_argument(
        'orbfile',
        type=str,
        help='OpenMolcas ASCII orbital file name'
    )

    # Green start and end ascii
    sc = '\033[0;32m'
    ec = '\033[0m'

    rotate.add_argument(
        'swap_string',
        type=str,
        nargs='+',
        help='String specifying rotations to perform \
              format is "' + sc + 'x-c y-c z-c ...' + ec +
             '" where orbital space is c = f,i,1,2,3,s,d \
              and orbital number(s) are x, y, z.\
              N.B. quotations should not be included'
    )

    rotate.add_argument(
        '--out',
        type=str,
        default='ModOrb',
        help='Path to output file for rotated orbital file. \
              Default is ModOrb'
    )

    # Rotation of spaces
    reorder = subparsers.add_parser('reorder')
    reorder.set_defaults(func=reorder_func)

    reorder.add_argument(
        'orbfile',
        type=str,
        help='OpenMolcas ASCII orbital file name'
    )

    reorder.add_argument(
        'swap_string',
        type=str,
        nargs='+',
        help='String specifying which orbitals to swap \
              format is "' + sc + 'i-f i-f i-f ...' + ec +
             '" where i is initial and f is final orbital number \
              N.B. quotations should not be included'
    )

    reorder.add_argument(
        '--out',
        type=str,
        default='ModOrb',
        help='Path to output file for reordered orbital file. \
              Default is ModOrb'
    )

    cfp = subparsers.add_parser(
        'cfp',
        description="""Program to perform crystal field projection based on the
        *.rassi.h5 output containing the [ SOS | SFS ]_angmom operators of a
        spin-orbit molcas calculation. Use --ground and --basis zeeman to
        reproduce the results of single_aniso. If the input space is not
        specified, a default "small" CASSCF calculation is assumed. If no
        symbol is specified, the Hund's ground term/level is assumed.""",
        epilog="""Example: molcas_suite cfp -i dy.rassi.h5 --basis "j"
        --ion "Dy3+" --quax dy.out --symbol 6H15/2""",
        parents=[cfp_parser])

    cfp.set_defaults(func=cfp_func)

    cfp.add_argument(
        '-H', '--Help', const='store',
        action=hpc.SecondaryHelp,
        help='show help message for additional arguments and exit'
    )

    # read sub-parser
    parser.set_defaults(func=lambda args: parser.print_help())
    args, unknown_args = parser.parse_known_args(arg_list)

    # select parsing option based on sub-parser
    if args.prog in ['generate_job', 'extractor', 'cfp']:
        args.func(args, unknown_args)
    else:
        args = parser.parse_args(arg_list)
        args.func(args)


def main():
    read_args()
