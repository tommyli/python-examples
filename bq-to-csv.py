"""Take SQL file input, query BigQuery and write results as CSV

"""

import argparse as ap
import pandas_gbq as pdbq

options = ap.ArgumentParser(
    description='Run BigQuery from SQL file and output to CSV')
options.add_argument('sql_file', metavar='SQLFILE', type=str, nargs='+',
                     help='input SQL file')
options.add_argument('--csv', metavar='CSVFILE', type=str, nargs='?', default='bq_out.csv',
                     help='output CSV file path')
args = options.parse_args()

with open(args.sql_file[0]) as file:
    df = pdbq.read_gbq(file.read())
    df.to_csv(args.csv)
