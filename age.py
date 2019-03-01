# -*- coding: utf-8  -*-

import click
import pandas as pd
from tqdm import tqdm
import os
import platform


@click.command()
@click.option("--file", help="CSV file")
@click.argument("Date_Column")
@click.argument("Birthday_Column")
def age(file, date_column, birthday_column):
    df = pd.read_csv(file, "r", encoding="iso-8859-1", delimiter=";", keep_default_na=False, dtype='unicode')

    #Info Print
    print("[Info] Calculate ages for file ({})and store into the new column V0_Age".format(file))

    bdates = [bdate.replace(".","")[:2] for bdate in df[birthday_column]]
    dates = [date.replace(".","")[:2] for date in df[date_column]]



if __name__ == "__main__":
    age()
