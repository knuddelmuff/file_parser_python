# -*- coding: utf-8  -*-

import click
import pandas as pd
from tqdm import tqdm
from helper import *


@click.command()
@click.option("--file", help="CSV file")
def vedo(file):
    df = pd.read_csv(file, "r", encoding="iso-8859-1",
                     delimiter=";", keep_default_na=False, dtype='unicode')

    df = df[df.V0_Gruppe == "Gruppe 1"]

    # TODO: einteilen in 13 Vs und es in jedem V durchlaufen lassen

    # Progress Bar:
    for _ in tqdm(range(10000000)):
        pass

    df.to_csv("vedo_{}".format(file), sep=";", encoding="iso-8859-1")

    openFolder()


if __name__ == "__main__":
    vedo()
