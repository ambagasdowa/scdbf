#!/usr/bin/env python3
# coding: utf-8
from __future__ import print_function

#from rich import print
#from rich.console import Console
#from rich.table import Table
#
#from rich.syntax import Syntax
#from rich.theme import Theme

import sys
import csv
from dbfread import DBF


def show(*words):
    print('  ' + ' '.join(str(word) for word in words))


def show_field(field):
    print('    {} ({} {})'.format(field.name, field.type, field.length))


def info():
    for filename_info in sys.argv[1:]:

        print(filename_info + ':')
        table_info = DBF(filename_info, ignore_missing_memofile=True)
        show('Name:', table_info.name)
        show('Memo File:', table_info.memofilename or '')
        show('DB Version:', table_info.dbversion)
        show('Records:', len(table_info))
        show('Deleted Records:', len(table_info.deleted))
        show('Last Updated:', table_info.date)
        show('Character Encoding:', table_info.encoding)
        show('Fields:')
        for field in table_info.fields:
            show_field(field)


def code():
    for file in sys.argv[1:]:
        tbl = DBF(file, ignore_missing_memofile=True)
        if(tbl.encoding == 'ascii'):
            return 'cp850'
        else:
            return tbl.encoding


def main():


    for filename in sys.argv[1:]:

        table = DBF(filename, ignore_missing_memofile=True, encoding=code())
        writer = csv.writer(sys.stdout)
        writer.writerow(table.field_names)

        for record in table:
            writer.writerow(list(record.values()))


if __name__ == "__main__":
    main()
