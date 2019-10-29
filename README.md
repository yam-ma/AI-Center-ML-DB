# AI-Center-ML-DB
Some examples/templates for handling the AI-Center ML DB

## How to access the AI-Center ML DB (read-only)

$ mysql -u ai-center -p -h floria.wni.co.jp

If your computer does not recognize mysql, install it. 
mysqlを認識しない場合は、適宜インストールしてください。

## How to read grib files on the web (in the AI-Center ML DB)

Some databases have columns for URLs for grib data.
You can access and read them as in MSM_DB_read.py. 
(You need to install sqlalchemy)
データベースの中には、web上のgribファイルのURLが格納してあるものがあります。
こういったweb上のファイルにアクセスするには、サンプルファイル(MSM_DB_read.py)を参考にしてください。
(sqlalchemyのインストールが必要です)


