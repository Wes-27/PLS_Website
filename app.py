import os
import sys
from flask import Flask, render_template
import getpass
import oracledb

un = "ADMIN"
cs = "(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.us-phoenix-1.oraclecloud.com))(connect_data=(service_name=g4a560c102d9091_tipjfxu4a4ibrwrv_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))"
pw = getpass.getpass(f'Enter password for {un}@{cs}: ')

with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
  with connection.cursor() as cursor:
      sql = """select sysdate from dual"""
      for r in cursor.execute(sql):
          print(r)


app = Flask(__name__)



@app.route("/")
def hello():
  return render_template("home.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
