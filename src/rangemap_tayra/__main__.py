# SPDX-FileCopyrightText: 2026-present Tayra Sakurai <tayra_sakurai@icloud.com>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
"""The runnable code."""
from ._mapping import *
import argparse

def main():
    """The main thred."""
    parser = argparse.ArgumentParser(
        description='Loads the data and maps the data to a HTML file.'
    )
    parser.add_argument(
        'range',
        type=float,
        help='The range to be mapped.'
    )
    parser.add_argument(
        'file',
        help='File saving place.'
    )
    placer = parser.add_mutually_exclusive_group(
        required=True
    )
    placer.add_argument(
        '-l',
        '--coord',
        nargs=2,
        type=float,
        help='The coordinate of the place.'
    )
    placer.add_argument(
        '-n',
        '--name',
        help='The name of the place'
    )
    args = parser.parse_args()
    data: DataMap
    if 'coord' in args and args.coord is not None:
        data = load_data(args.coord, args.range)
    else:
        data = load_data(args.name, args.range)
    m = map_circle(data)
    save_map(args.file, m)


if __name__ == '__main__':
    main()
