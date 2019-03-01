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
        df[spalte] = df[spalte].replace("Sonstige", 200)
        df[spalte] = df[spalte].replace("sonstige", 200)
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
        df[spalte] = df[spalte].replace("Humira", 0)
        df[spalte] = df[spalte].replace("Amgevita", 1)
        df[spalte] = df[spalte].replace("Hyrimoz", 2)
        df[spalte] = df[spalte].replace("Imraldi", 3)
        df[spalte] = df[spalte].replace("sehr gut", 1)
        df[spalte] = df[spalte].replace("gut", 2)
        df[spalte] = df[spalte].replace("befriedigend", 3)
        df[spalte] = df[spalte].replace("ausreichend", 4)
        df[spalte] = df[spalte].replace("mangelhaft", 5)
        df[spalte] = df[spalte].replace("ungenügend", 6)
        df[spalte] = df[spalte].replace("unbekannt", 1)
        df[spalte] = df[spalte].replace("unbekannt", 1)
        df[spalte] = df[spalte].replace("Remicade®", 0)
        df[spalte] = df[spalte].replace("Flixabi®", 1)
        df[spalte] = df[spalte].replace("Inflectra®", 2)
        df[spalte] = df[spalte].replace("Remsima®", 3)
        df[spalte] = df[spalte].replace("laufend", 0)
        df[spalte] = df[spalte].replace("vereinzelt", 1)
        df[spalte] = df[spalte].replace("fruehere Therapie", 2)
        df[spalte] = df[spalte].replace("Homeopathie", 0)
        df[spalte] = df[spalte].replace("Weihrauch", 1)
        df[spalte] = df[spalte].replace("Yoga", 2)
        df[spalte] = df[spalte].replace("Akkupunktur", 3)
        df[spalte] = df[spalte].replace("Nahrungsergaenzungen", 4)
        df[spalte] = df[spalte].replace("keine", 0)
        df[spalte] = df[spalte].replace("leicht", 1)
        df[spalte] = df[spalte].replace("mittel", 2)
        df[spalte] = df[spalte].replace("stark", 3)
        df[spalte] = df[spalte].replace("fraglich", 1)
        df[spalte] = df[spalte].replace("sicher", 2)
        df[spalte] = df[spalte].replace("sicher und schmerzhaft", 3)
        df[spalte] = df[spalte].replace("Arthralgie/Arthritis", 1)
        df[spalte] = df[spalte].replace("Uveitis/Iritis", 2)
        df[spalte] = df[spalte].replace("Erythema nodosum", 3)
        df[spalte] = df[spalte].replace("orale Aphten", 4)
        df[spalte] = df[spalte].replace("Pyoderma gangraenosum", 5)
        df[spalte] = df[spalte].replace("Analfissur", 6)
        df[spalte] = df[spalte].replace("neue Fistel", 7)
        df[spalte] = df[spalte].replace("Abszess", 8)
        df[spalte] = df[spalte].replace("Ich habe keine Probleme herumzugehe", 0)
        df[spalte] = df[spalte].replace("Ich habe einige Probleme herumzugehen", 1)
        df[spalte] = df[spalte].replace("Ich bin ans Bett gebunden", 2)
        df[spalte] = df[spalte].replace("Ich habe keine Probleme fuer mich selber zu sorgen", 0)
        df[spalte] = df[spalte].replace("Ich habe einige Probleme mich selbst zu waschen oder anzuziehen", 1)
        df[spalte] = df[spalte].replace("Ich bin nicht in der Lage mich selbst zu waschen oder anzuziehen", 2)
        df[spalte] = df[spalte].replace("Ich habe keine Probleme meinen alltäglichen Taetigkeiten nachzugehen", 0)
        df[spalte] = df[spalte].replace("Ich habe einige Probleme meinen alltaeglichen Taetigkeiten nachzugehen", 1)
        df[spalte] = df[spalte].replace("Ich bin nicht in der Lage meinen alltaeglichen Taetigkeiten nachzugehen", 2)
        df[spalte] = df[spalte].replace("Ich habe keine Schmerzen oder Beschwerden", 0)
        df[spalte] = df[spalte].replace("Ich habe maessige Schmerzen oder Beschwerden", 1)
        df[spalte] = df[spalte].replace("Ich habe extreme Schmerzen oder Beschwerden", 2)
        df[spalte] = df[spalte].replace("Ich bin nicht aengstlich", 0)
        df[spalte] = df[spalte].replace("Ich bin maessig aengstlich", 1)
        df[spalte] = df[spalte].replace("Ich bin extrem aengstlich oder deprimiert", 2)
        df[spalte] = df[spalte].replace("A1 < 16 Jahre", 0)
        df[spalte] = df[spalte].replace("A2 ≥ 17, ≤ 40 Jahre", 1)
        df[spalte] = df[spalte].replace("A3 > 40 Jahr", 2)
        df[spalte] = df[spalte].replace("L1 Ileum", 0)
        df[spalte] = df[spalte].replace("l2 Kolon", 1)
        df[spalte] = df[spalte].replace("L3 Ileum und Kolon", 2)
        df[spalte] = df[spalte].replace("B1 Entzuendlicher, nicht penetr./stenos. Phaenotyp", 0)
        df[spalte] = df[spalte].replace("B2 Stenos. Phaenotyp", 1)
        df[spalte] = df[spalte].replace("B3 Penetr./fist. Phaenotyp", 2)


    df.to_csv("edit_{}".format(file), sep=";", encoding="iso-8859-1")

    # Check what operating system (OS) the user is using
    if platform.system() == "Darwin": #Mac OSX
        os.system("open .")
    elif platform.system() == "Windows":
        os.system("start .")

if __name__ == "__main__":
    change()
