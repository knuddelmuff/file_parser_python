# -*- coding: utf-8  -*-

import click
import pandas as pd
from tqdm import tqdm
from helper import *


@click.command()
@click.option("--file", help="CSV file")
@click.argument("V0_HBIGen")
@click.argument("V0_HBIAbdo")
@click.argument("V0_HBIStool")
@click.argument("V0_HBIRes")
@click.argument("V0_EIMSum")
def hbi(file, V0_HBIGen, V0_HBIAbdo, V0_HBIStool, V0_HBIRes, V0_EIMSum):
    df = pd.read_csv(file, "r", encoding="iso-8859-1",
                     delimiter=";", keep_default_na=False, dtype='unicode')

    # Info Print
    print("[Info] Calculate Harvey-Bradshaw-Index (HBI) for file ({}) and store into the new column V0_HBI".format(file))

    newDf = df[[V0_HBIGen, V0_HBIAbdo, V0_HBIStool, V0_HBIRes, V0_EIMSum]]

    for column in newDf
        # TODO: Change values from CSV to numbers -> (0) keine => 0 ... 
        newDf[column] = newDf[column].replace("on", 1)
        newDf[column] = newDf[column].replace("", 0)

    counts = newDf.sum(axis=1)

    df.insert(1, "V0_HBISum", counts)

    # Progress Bar:
    for _ in tqdm(range(10000000)):
        pass

    df.to_csv("edit_{}".format(file), sep=";", encoding="iso-8859-1")

    openFolder()

if __name__ == "__main__":
    hbi()
