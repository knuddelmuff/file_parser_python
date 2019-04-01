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

    for column in newDf:
        # TODO: Change values from CSV to numbers -> (0) keine => 0 ...
        newDf[column] = newDf[column].replace("(0) sehr gut", 0)
        newDf[column] = newDf[column].replace("(1) sehr gut", 1)
        newDf[column] = newDf[column].replace("(2) sehr gut", 2)
        newDf[column] = newDf[column].replace("(3) sehr gut", 3)
        newDf[column] = newDf[column].replace("(4) sehr gut", 4)
        newDf[column] = newDf[column].replace("(0) gut", 0)
        newDf[column] = newDf[column].replace("(1) gut", 1)
        newDf[column] = newDf[column].replace("(2) gut", 2)
        newDf[column] = newDf[column].replace("(3) gut", 3)
        newDf[column] = newDf[column].replace("(4) gut", 4)
        newDf[column] = newDf[column].replace("(0) beeinträchtigt", 0)
        newDf[column] = newDf[column].replace("(1) beeinträchtigt", 1)
        newDf[column] = newDf[column].replace("(2) beeinträchtigt", 2)
        newDf[column] = newDf[column].replace("(3) beeinträchtigt", 3)
        newDf[column] = newDf[column].replace("(4) beeinträchtigt", 4)
        newDf[column] = newDf[column].replace("(0) unerträglich", 0)
        newDf[column] = newDf[column].replace("(1) unerträglich", 1)
        newDf[column] = newDf[column].replace("(2) unerträglich", 2)
        newDf[column] = newDf[column].replace("(3) unerträglich", 3)
        newDf[column] = newDf[column].replace("(4) unerträglich", 4)
        newDf[column] = newDf[column].replace("(0) schlecht", 0)
        newDf[column] = newDf[column].replace("(1) schlecht", 1)
        newDf[column] = newDf[column].replace("(2) schlecht", 2)
        newDf[column] = newDf[column].replace("(3) schlecht", 3)
        newDf[column] = newDf[column].replace("(4) schlecht", 4)
        newDf[column] = newDf[column].replace("(0) sehr schlecht", 0)
        newDf[column] = newDf[column].replace("(1) sehr schlecht", 1)
        newDf[column] = newDf[column].replace("(2) sehr schlecht", 2)
        newDf[column] = newDf[column].replace("(3) sehr schlecht", 3)
        newDf[column] = newDf[column].replace("(4) sehr schlecht", 4)
        newDf[column] = newDf[column].replace("(0) sehr Schlecht", 0)
        newDf[column] = newDf[column].replace("(1) sehr Schlecht", 1)
        newDf[column] = newDf[column].replace("(2) sehr Schlecht", 2)
        newDf[column] = newDf[column].replace("(3) sehr Schlecht", 3)
        newDf[column] = newDf[column].replace("(4) sehr Schlecht", 4)
        newDf[column] = newDf[column].replace("(0) keine", 0)
        newDf[column] = newDf[column].replace("(1) leichte", 1)
        newDf[column] = newDf[column].replace("(2) mäßige", 2)
        newDf[column] = newDf[column].replace("(3) starke", 3)
        newDf[column] = newDf[column].replace("(0) nein", 0)
        newDf[column] = newDf[column].replace("(1) zweifelhaft", 1)
        newDf[column] = newDf[column].replace("(1) fraglich", 1)
        newDf[column] = newDf[column].replace("(2) sicher", 2)
        newDf[column] = newDf[column].replace("(3) schmerzhaft und sicher", 3)






    counts = newDf.sum(axis=1)

    df.insert(1, "V0_HBISum", counts)

    # Progress Bar:
    for _ in tqdm(range(10000000)):
        pass

    df.to_csv("edit_{}".format(file), sep=";", encoding="iso-8859-1")

    openFolder()

if __name__ == "__main__":
    hbi()
