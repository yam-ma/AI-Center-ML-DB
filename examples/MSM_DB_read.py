##
## MSM_DB_read.py: MSM DBからgribファイルを読み込むテスト
##                 Oct. 24. 2019, M. Yamada
##

import os
import urllib.error
import urllib.request

import tempfile

import pygrib

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, func
from sqlalchemy.sql import select, literal_column

#===========================
# URLからデータを読み込む
#===========================
def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)


#============
# Main
#============
if __name__ == "__main__":

    #
    # データベースからデータフレームを取得
    #
    engine = create_engine('mysql://yam-ma:KJ99FivY@floria.wni.co.jp/MSM', echo = True)
    df = pd.read_sql('MSM', con = engine)

    print(df)

    #
    # URLを取得＆データ取得
    #
    url = df['URL'][0]
    print(url)
    with urllib.request.urlopen(url) as web_file:
        data = web_file.read()
   
    #
    # 一時ファイル
    #
    fp = tempfile.NamedTemporaryFile()
    print(fp.name)
    fp.write(data)

    gribs = pygrib.open(fp.name)

    #
    # gribファイル読み出し
    #
    for grb in gribs:
        param = grb.parameterName
        print("parameter=", param, df['parameter'][0])

    fp.close()
    gribs.close()
            
