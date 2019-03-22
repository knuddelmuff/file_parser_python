# -*- coding: utf-8  -*-

import click
import pandas as pd
from tqdm import tqdm
from helper import *


@click.command()
@click.option("--file", help="CSV file")
@click.argument("Weight_Column")
@click.argument("Size_Column")
def bmi(file, weight_column, size_column):
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    df = pd.read_csv(file, "r", encoding="iso-8859-1", delimiter=";", keep_default_na=False, dtype='unicode')

    #Info Print
    print("[Info] Calculate Body-Mass-Index (BMI) for file ({}) and store into the new column V0_BMI".format(file))

    # TODO: Better else value
    sizes = [float((int(size) / 100) ** 2) if len(size) > 0 and int(size) > 0 else 100000 for size in df[size_column]]
    weights = [int(weight) if len(weight) > 0 and int(weight) > 0 else 100000 for weight in df[weight_column]]

    bmis = [weights[index] / size for index, size in enumerate(sizes)]

    df.insert(9, "V0_BMI", bmis)

    #Progress Bar:
    for _ in tqdm(range(10000000)):
        pass

    df.to_csv("edit_{}".format(file), sep=";", encoding="utf-8") # encoding="iso-8859-1"

    openFolder()

if __name__ == "__main__":
    bmi()
