# -*- coding: utf-8  -*-

import click
import pandas as pd
from tqdm import tqdm
from helper import *
import datetime


@click.command()
@click.option("--file", help="CSV file")
@click.argument("new_file")
def statistics(file, date_column, birthday_column):
    df = pd.read_csv(file, "r", encoding="iso-8859-1", delimiter=";", keep_default_na=False, dtype='unicode')

    #Info Print
    print("[Info] Calculate Statistics for file ({}) and store into the new file statistics_{}".format(file,file))




    #Progress Bar:
    for _ in tqdm(range(10000000)):
        pass

    df.to_csv("statistics_{}".format(file), sep=";", encoding="iso-8859-1")

    openFolder()

if __name__ == "__main__":
    statistics()
