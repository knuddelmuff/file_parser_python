# -*- coding: utf-8  -*-

import click
import pandas as pd
from tqdm import tqdm
from helper import *
import datetime


@click.command()
@click.option("--file", help="CSV file")
@click.argument("Date_Column")
@click.argument("Birthday_Column")
def age(file, date_column, birthday_column):
    df = pd.read_csv(file, "r", encoding="iso-8859-1", delimiter=";", keep_default_na=False, dtype='unicode')

    #Info Print
    print("[Info] Calculate ages for file ({})and store into the new column V0_Age".format(file))

    yearNow = datetime.datetime.now().year

    bdates = [int(bdate[3:]) if len(bdate) > 0 else yearNow for bdate in df[birthday_column]]
    dates = [int(date[-2:]) + 2000  if len(date) > 0 else yearNow for date in df[date_column]]

    ages = []

    for index, bdate in enumerate(bdates):
        ages.append(dates[index] - bdate)

    print(ages)
    df["V0_Ages"] = ages

    #Progress Bar:
    for _ in tqdm(range(10000000)):
        pass

    df.to_csv("edit_{}".format(file), sep=";", encoding="iso-8859-1")

    openFolder()

if __name__ == "__main__":
    age()
