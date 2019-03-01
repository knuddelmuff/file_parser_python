# -*- coding: utf-8  -*-

import click
import pandas as pd
from tqdm import tqdm
import os
import platform


@click.command()
@click.option("--file", help="CSV file")
def change(file):
    df = pd.read_csv(file, "r", encoding="iso-8859-1", delimiter=";", keep_default_na=False, dtype='unicode')

    #Info Print
    print("[Info] File ({}) is searched and changed".format(file))

    for spalte in tqdm(df):
        df[spalte] = df[spalte].replace("ja", 1)
        df[spalte] = df[spalte].replace("nein", 0)
        df[spalte] = df[spalte].replace("Raucher", 0)
        df[spalte] = df[spalte].replace("Nicht-Raucher", 1)
        df[spalte] = df[spalte].replace("Ex-Raucher", 2)
        df[spalte] = df[spalte].replace("weiblich", 0)
        df[spalte] = df[spalte].replace("m nnlich", 1)
        df[spalte] = df[spalte].replace("unbekannt", 100)

        # df.loc[df[spalte] == "ja", spalte] = "1"

        # df.loc[df[spalte] == "nein", spalte] = 0
        #
        # df.loc[df[spalte] == "unbekannt", spalte] = 100
        #
        # df.loc[df[spalte] == "Raucher", spalte] = 0
        # df.loc[df[spalte] == "Nicht-Raucher", spalte] = 1
        # df.loc[df[spalte] == "Ex-Raucher", spalte] = 2
        # df.loc[df[spalte] == "weiblich", spalte] = 0
        # df.loc[df[spalte] == "mnnlich", spalte] = 1
        # df.loc[df[spalte] == "Rektum", spalte] = 1
        # df.loc[df[spalte] == "Kolon", spalte] = 2
        # df.loc[df[spalte] == "Duendarm, ohne term. Ileum", spalte] = 3
        # df.loc[df[spalte] == "term. Ileum", spalte] = 4
        # df.loc[df[spalte] == "Duodenum", spalte] = 5
        # df.loc[df[spalte] == "Magen", spalte] = 6
        # df.loc[df[spalte] == "Oesophagus", spalte] = 7
        # df.loc[df[spalte] == "unklare Zuordnung", spalte] = 0
        # df.loc[df[spalte] == "akuter Schub", spalte] = 1
        # df.loc[df[spalte] == "chronisch aktiv", spalte] = 2
        # df.loc[df[spalte] == "Remission", spalte] = 3
        # df.loc[df[spalte] == "Azathiopin", spalte] = 0
        # df.loc[df[spalte] == "5-ASA", spalte] = 1
        # df.loc[df[spalte] == "6-Mercaptopurin", spalte] = 3
        # df.loc[df[spalte] == "TNF-alpha AK", spalte] = 3
        # df.loc[df[spalte] == "Vedolizumab", spalte] = 4
        # df.loc[df[spalte] == "Usterkinumab", spalte] = 5
        # df.loc[df[spalte] == "andere Unvertraeglichkeiten", spalte] = 6
        # # df.loc[df[spalte] == "ja", spalte] = 1
        # # df.loc[df[spalte] == "ja", spalte] = 1
        # # df.loc[df[spalte] == "ja", spalte] = 1
        # # df.loc[df[spalte] == "ja", spalte] = 1
        # # df.loc[df[spalte] == "ja", spalte] = 1
        # # df.loc[df[spalte] == "ja", spalte] = 1
        # # df.loc[df[spalte] == "ja", spalte] = 1
        # # df.loc[df[spalte] == "ja", spalte] = 1

    df.to_csv("edit_{}".format(file), sep=";", encoding="iso-8859-1")

    if platform.system() == "Darwin": #Mac OSX
        os.system("open .")
    elif platform.system() == "Windows":
        os.system("start .")

if __name__ == "__main__":
    change()
