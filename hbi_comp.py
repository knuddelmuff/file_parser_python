# -*- coding: utf-8  -*-

import click
import pandas as pd
from tqdm import tqdm
from helper import *
import datetime


@click.command()
@click.option("--file", help="CSV file")
@click.option("--nc", help="Needs the converter from 'on' to 1")
@click.argument("new_column")
@click.argument("column_list")
# @click.argument("EIMArth")
# @click.argument("EIMIrit")
# @click.argument("EIMEryt")
# @click.argument("EIMPyod")
# @click.argument("EIMOrAp")
# @click.argument("EIMAnaF")
# @click.argument("EIMPerA")
# @click.argument("EIMAOthF")
#def hbi(file, nc,new_column, eimarth, eimirit, eimeryt, eimpyod, eimorap, eimanaf, eimpera, eimaothf):
def hbi(file, nc, new_column, column_list):
    df = pd.read_csv(file, "r", encoding="iso-8859-1",
                     delimiter=";", keep_default_na=False, dtype='unicode')

    # Info Print
    print("[Info] Calculate Harvey-Bradshaw-Index (HBI) for file ({}) and store into the new column V0_HBI".format(file))

    newDf = df[column_list]

    if nc:
        for column in newDf:
            newDf[column] = newDf[column].replace("on", 1)
            newDf[column] = newDf[column].replace("", 0)

    counts = newDf.sum(axis=1)

    df.insert(1, new_column, counts)

    # Progress Bar:
    for _ in tqdm(range(10000000)):
        pass

    df.to_csv("edit_{}".format(file), sep=";", encoding="iso-8859-1")

    openFolder()


if __name__ == "__main__":
    hbi()
