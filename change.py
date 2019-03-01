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
        # TODO: include regex (regular expression) for male string
        df[spalte] = df[spalte].replace("m nnlich", 1)
        df[spalte] = df[spalte].replace("unbekannt", 100)
        df[spalte] = df[spalte].replace("Rektum", 1)
        df[spalte] = df[spalte].replace("Rektum", 1)
        df[spalte] = df[spalte].replace("Kolon", 2)
        df[spalte] = df[spalte].replace("Duendarm, ohne term. Ileum", 3)
        df[spalte] = df[spalte].replace("term. Ileum", 4)
        df[spalte] = df[spalte].replace("Duodenum", 5)
        df[spalte] = df[spalte].replace("Magen", 6)
        df[spalte] = df[spalte].replace("Oesophagus", 7)
        df[spalte] = df[spalte].replace("unklare Zuordnung", 0)
        df[spalte] = df[spalte].replace("akuter Schub", 1)
        df[spalte] = df[spalte].replace("chronisch aktiv", 2)
        df[spalte] = df[spalte].replace("Remission", 3)
        df[spalte] = df[spalte].replace("Azathiopin", 0)
        df[spalte] = df[spalte].replace("6-Mercaptopurin", 1)
        df[spalte] = df[spalte].replace("MTX", 2)
        df[spalte] = df[spalte].replace("anderes Immunsuppressivum", 3)
        df[spalte] = df[spalte].replace("Azathioprin", 0)
        df[spalte] = df[spalte].replace("5-ASA", 1)
        df[spalte] = df[spalte].replace("6-Mercaptopurin", 2)
        df[spalte] = df[spalte].replace("TNF-alpha AK", 3)
        df[spalte] = df[spalte].replace("Vedolizumab", 4)
        df[spalte] = df[spalte].replace("Usterkinumab", 5)
        df[spalte] = df[spalte].replace("andere Unvertraeglichkeiten", 6)





    df.to_csv("edit_{}".format(file), sep=";", encoding="iso-8859-1")

    # Check what operating system (OS) the user is using
    if platform.system() == "Darwin": #Mac OSX
        os.system("open .")
    elif platform.system() == "Windows":
        os.system("start .")

if __name__ == "__main__":
    change()
