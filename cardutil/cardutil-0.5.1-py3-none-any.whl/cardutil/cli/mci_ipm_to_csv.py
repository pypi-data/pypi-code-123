import argparse
import collections
import csv

from cardutil.cli import add_version, get_config
from cardutil.mciipm import IpmReader


def cli_entry():
    cli_run(**vars(cli_parser().parse_args()))


def cli_run(**kwargs):

    config = get_config('cardutil.json', cli_filename=kwargs.get('config_file'))

    if not kwargs.get('out_filename'):
        kwargs['out_filename'] = kwargs['in_filename'] + '.csv'

    with open(kwargs['in_filename'], 'rb') as in_ipm:
        with open(kwargs['out_filename'], 'w', encoding=kwargs.get('out_encoding')) as out_csv:
            mci_ipm_to_csv(in_ipm=in_ipm, out_csv=out_csv, config=config, **kwargs)


def dicts_to_csv(data_list, output_file, field_list=None):
    """
    Writes dict data to CSV file

    :param data_list: list of dictionaries that contain the data to be loaded
    :param output_file: output CSV file
    :param field_list: (optional) list of fields to output to CSV file
    :return: None
    """

    if not field_list:
        # get the fields present in the dicts
        field_summary = collections.Counter()
        data_list = list(data_list)
        for item in data_list:
            field_summary.update(item.keys())
        field_list = [field_key for field_key in field_summary]

    writer = csv.DictWriter(
        output_file,
        fieldnames=field_list,
        extrasaction="ignore",
        lineterminator="\n")

    writer.writeheader()
    for data_item in data_list:
        writer.writerow({item: data_item[item] for item in data_item if item in field_list})


def cli_parser():
    parser = argparse.ArgumentParser(prog='mci_ipm_to_csv', description='Mastercard IPM to CSV')
    parser.add_argument('in_filename')
    parser.add_argument('-o', '--out-filename')
    parser.add_argument('--in-encoding')
    parser.add_argument('--out-encoding')
    parser.add_argument('--no1014blocking', action='store_true')
    parser.add_argument('--config-file', help='File containing cardutil configuration - JSON format')
    add_version(parser)

    return parser


def mci_ipm_to_csv(in_ipm, out_csv, config, in_encoding=None, no1014blocking=False, **_):
    """
    Create a csv file given an input Mastercard IPM file

    :param in_ipm: binary input IPM file object
    :param out_csv: output csv file object
    :param config: dict containing cardutil config
    :param in_encoding: input file encoding string
    :param no1014blocking: set True if no 1014 blocking used
    :return: None
    """
    blocked = not no1014blocking
    dicts_to_csv(
        IpmReader(in_ipm, encoding=in_encoding, blocked=blocked, iso_config=config.get('bit_config')),
        out_csv, field_list=config.get('output_data_elements'))
