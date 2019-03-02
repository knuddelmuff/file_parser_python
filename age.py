import click
import os
import pandas as pd

@click.command()
@click.option("--file", help="CSV file", envvar="file")
@click.argument("bdate_column")
@click.argument("date_column")





def age(file,bdate_column, date_column):
    """Calculates the age."""

    df = pd.read_csv(file, "r", encoding="iso-8859-1", delimiter=";", keep_default_na=False, dtype='unicode'))

    # Info Print
    print("[Info] File ({}) is searched and get age".format(file))

    date = date_column
    bdate = bdate_colum

    pd.to_datetime(date).year - pd.to_datetime(bdate).year

if __name__ == "__main__":
    age()
