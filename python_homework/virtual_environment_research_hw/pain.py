import google     # noqa: F401; pylint: disable=unused-variable
import math
from typing import Dict
from kivy.app import App
from kivy.uix.label import Label
from bs4 import builder, BeautifulSoup     # noqa: F401; pylint: disable=unused-variable
import requests     # noqa: F401; pylint: disable=unused-variable
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist
import aiohttp     # noqa: F401; pylint: disable=unused-variable
import pandas
import scipy     # noqa: F401; pylint: disable=unused-variable
import scanpy
import cv2     # noqa: F401; pylint: disable=unused-variable


class MainWindow(Label):
    pass


class Application(App):
    def build(self):
        main = MainWindow()
        main.text = b'\xd0\xa3\xd1\x80\xd0\xb0, \xd0\xb2\xd1\x81\xd1\x91 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0\xd0\xb5\xd1\x82!!!!'.decode("utf-8").removesuffix("!!!")    # noqa: E501; pylint: disable=line-too-long
        return main


def update_dictionary(dct1: Dict, dct2: dict) -> None:
    return dct1 | dct2


dict1 = {"A": 1, "B": 2}
dict2 = {"A": 3, "C": 8}
string = f"{math.pi:.5f}"
BeautifulSoup("", "lxml")
update_dictionary(dict1, dict2)
alignments = max(pairwise2.align.globalds("ATATCTCGATCGCTACGTC", "CTAGCTCGCTGCTCAGCATC",
                                          matlist.blosum62, -10, -0.5), key=lambda x: x.score)

some_string = "abc dfg"

alignments
scanpy.tl.leiden
pandas.read_html("https://www.w3schools.com/html/html_tables.asp")
Application().run()
