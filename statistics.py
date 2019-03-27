# -*- coding: utf-8  -*-

import click
import pandas as pd
from tqdm import tqdm
from helper import *


@click.command()
@click.option("--file", help="CSV file")
@click.argument("column")
def statistics(file, column):

    df = pd.read_csv(file, "r", encoding="iso-8859-1", delimiter=";", keep_default_na=False, dtype='unicode')
    df = df[column]

    #Info Print
    print("Statistics for file ({})".format(file))

    summe = 0
    for x in df: 
        if len(x) != 0:
            summe += int(x)

    shape = df.shape[0]
    average = summe / shape

    newFile = open("Statistics_{}_{}".format(column, file), "w") 
    newFile.write("Average of {} from file {}: {}".format(column, file, str(average)))
    # TODO
    #newFile.write("Sum ... irgendwas ...  of {} from file {}: {}".format(column, file, str(average)))
    newFile.close()

    #Progress Bar:
    for _ in tqdm(range(10000000)):
        pass

    openFolder()

if __name__ == "__main__":
    statistics()
