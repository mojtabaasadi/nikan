
from flask import Flask,request,redirect
import sqlite3
from .utils import dict_factory,db_action



app = Flask(__name__)

@app.route("/")
def main():
    sql = """
    SELECT * from clips c WHERE  first_correction is NULL  order by prediction_score ASC , id DESC  LIMIT  1;
    """
    (crrc,closer) = db_action(sql)
    closer()
    return """
<html dir="rtl">
<head>
    <meta charset="UTF-8" />
    <title>اصلاحات OCR</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="https://cdn.tailwindcss.com"></script>
    </head>
<body class="h-screen flex flex-col justify-center">
<div class="border border-orange-300 rounded-lg items-center flex flex-col justidy-center p-4 w-screen-sm mx-auto">
    <p >ID: {1}</p>
<form action="/correct" method="post">
    <img  src="{0}" alt="{1}" class="min-h-20 my-4" />
    <input class="border active:border-blue-300 rounded-md w-full px-3 py-1" type="text" value="{2}" name="correction" />
    <input type="hidden" value="{1}" name="id" />
    <div>
    <button class="bg-green-600 border-green-800 mt-3 py-1 px-3 rounded-md " type="submit">
        ذخیره
    </button>
    <div>
</form>
<div>
</body> </html>""".format(crrc['image'],crrc['id'],crrc['predicted'])


@app.route("/correct",methods=['POST'])
def correction():
    sql = "UPDATE  clips  SET  first_correction = '{0}' WHERE  id = {1};".format(
        request.form['correction'],
        request.form['id'],
    )
    (res,closer) = db_action(sql)
    print(res)
    closer(True)
    return redirect('/')