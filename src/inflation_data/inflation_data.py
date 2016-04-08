import urllib.request
#url = "https://www.ons.gov.uk/file?uri=/economy/inflationandpriceindices/datasets/consumerpriceindices/current/mm23.csv"


import os
import logging
import csv
import pandas as pd

if __name__=="__main__" :
    path = os.path.realpath(__name__)
    data_path = os.path.join(path, "../mm23.xlsx")
    df = pd.read_excel(data_path, sheetname=None)['data']
    df_cleaned = df.filter(regex=())





