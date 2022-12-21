from flask import Flask, request, jsonify, render_template
# from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
# from sqlalchemy.orm import relationship
import mysql.connector

app = Flask(__name__)

bootstrap = Bootstrap(app)

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bazaDanych"
)

mycursor=mydb.cursor();
mycursor.execute("select * from LEK");

data=mycursor.fetchall();
#for data in records:
    #print(data)

headings = ("ID", "NAZWA", "RECEPTA")

@app.route("/home")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/watch")
def watch():
    return render_template('watch_database_administrator.html', headings=headings, data=data)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8888)

