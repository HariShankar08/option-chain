#!/usr/bin/python

import argparse
from nsepython import nse_optionchain_scrapper, fnolist
import pandas as pd


def main(args):
    if args.eq.upper() in fnolist():
        d = nse_optionchain_scrapper(args.eq.upper())

        d = d['records']
        expiry_date = args.exp
        if expiry_date not in d['expiryDates']:
            if expiry_date == "First":
                expiry_date = d['expiryDates'][0]
            else:
                print(f'Error: Use Expiry dates {" or ".join(d["expiryDates"])}')
                parser.print_help()
                return
        pe_data = [thing['PE'] for thing in d['data'] if thing['expiryDate'] == expiry_date]

        pe = pd.DataFrame(pe_data)
        pe = rename_columns(pe)
        pe.to_csv(f'{args.eq}_PE.csv')

        ce_data = [thing['CE'] for thing in d['data'] if thing['expiryDate'] == expiry_date]
        ce = pd.DataFrame(ce_data)
        ce = rename_columns(ce)
        ce.to_csv(f'{args.eq}_CE.csv')

        print()
        print(f"Option Chain Data for {args.eq} saved.")
    else:
        print("Error: not a valid FNO Stock")
        

def rename_columns(df):
    header_full = ["openInterest", "changeinOpenInterest", "totalTradedVolume",
    "impliedVolatility", "lastPrice", "change", "bidQty", "bidprice", "askPrice",
    "askQty", "strikePrice"]
    headers = ["OI", "CHNG IN OI", "VOLUME", "IV", "LTP", "CHNG", "BID QTY",
               "BID PRICE", "ASK PRICE", "ASK QTY", "STRIKE PRICE"]
    cols_to_change = zip(headers, header_full)
    for thing in cols_to_change:
        df[thing[0]] = df[thing[1]]
        # print(thing[0], thing[1])
    df = df.loc[:, headers]
    return df
    
    
parser = argparse.ArgumentParser(description="Gets Put and Call Data from NSE into CSV files.")
parser.add_argument("-eq", "--equity", dest="eq", default="TCS",
		help="The Equity whose Option Chain is needed. (default: TCS)")
parser.add_argument("-exp", "--expiry", dest="exp", default="First",
		help="The Expiry Date; Format DD-MMM-YYYY, ex; 25-Mar-2021. Defaults to first (closest) expiry date.")
args = parser.parse_args()
main(args)



