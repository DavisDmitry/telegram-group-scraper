import argparse


def add_parsing_arguments(parser: argparse.ArgumentParser):
    parser.add_argument(
        '--api-id',
        dest='api_id', type=int, required=True
    )
    parser.add_argument(
        '--api-hash',
        dest='api_hash', type=str, required=True
    )
    parser.add_argument(
        '--group-name',
        dest='group_name', type=str, required=False
    )
    parser.add_argument(
        '--group-id',
        dest='group_id', type=int, required=False
    )
