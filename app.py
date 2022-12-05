from flask import Flask, request, jsonify, render_template
from service import ToDoService
from models import Schema
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from sqlalchemy.orm import relationship

import json

app = Flask(__name__)

bootstrap = Bootstrap(app)

db_name = 'C:\\Users\\seled\\Desktop\\SQL_PROJEKT\\projekt\\app\\system_zarzadzania_aptekami.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)



class OSOBA(db.Model):
    __tablename__ = 'OSOBA'
    id = db.Column(db.Integer, primary_key=True)
    nazwisko = db.Column(db.String, nullable = False)
    imie = db.Column(db.String, nullable = False)
    data_urodzenia = db.Column(db.String, nullable = False)
    telefon = db.Column(db.Integer, nullable = False)
    email = db.Column(db.String, nullable = True)
    adres = db.Column(db.String,nullable = False)

class ADMINISTRATOR(db.Model):
    __tablename__ = 'ADMINISTRATOR'
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.Integer, nullable = False)
    id_osoba = db.Column(db.Integer, db.ForeignKey('OSOBA.id'), nullable = False)

class KLIENT(db.Model):
    __tablename__ = 'KLIENT'
    id = db.Column(db.Integer, primary_key=True)
    poprzedni_zakup = db.Column(db.Integer, nullable = False)
    id_osoba = db.Column(db.Integer, db.ForeignKey('OSOBA.id'), nullable = False)

class ZAMOWIENIE(db.Model):
    __tablename__ = 'ZAMOWIENIE'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, nullable=False)
    data_zamowienia = db.Column(db.Date, nullable=False)

class FARMACEUTA(db.Model):
    __tablename__ = 'FARMACEUTA'
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.Integer, nullable=False)
    wyksztalcenie = db.Column(db.String, nullable=False)
    id_osoba = db.Column(db.Integer, db.ForeignKey('OSOBA.id'), nullable=False)

class APTEKA(db.Model):
    __tablename__ = 'APTEKA'
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String, nullable=False)
    godz_od = db.Column(db.Integer, nullable=False)
    godz_do = db.Column(db.Integer, nullable=False)
    adres = db.Column(db.String, nullable=False)
    telefon = db.Column(db.Integer, nullable=False)

class DYZUR(db.Model):
    __tablename__ = 'DYZUR'
    dzien = db.Column(db.String)
    godz_od = db.Column(db.Integer, nullable=False)
    godz_do = db.Column(db.Integer, nullable=False)
    ID_FARMACEUTA = db.Column(db.Integer, primary_key=True, nullable=False)
    ID_APTEKA = db.Column(db.Integer,primary_key=True, nullable=False)
    db.ForeignKeyConstraint(
        ['ID_FARMACEUTA', 'ID_APTEKA'],['FARMACEUTA.id','APTEKA.id']
    )


class MIASTO(db.Model):
    __tablename__ = 'MIASTO'
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String, nullable=False)
    kod = db.Column(db.Integer, nullable=False)

class MAGAZYN(db.Model):
    __tablename__ = 'MAGAZYN'
    id = db.Column(db.Integer, primary_key=True)
    adres = db.Column(db.String, nullable=False)
    pojemnosc = db.Column(db.Integer, nullable=False)


class LEKI(db.Model):
    __tablename__ = 'LEKI'
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String, nullable=False)
    recepta = db.Column(db.String, nullable=False)

class LEKARSTWA(db.Model):
    __tablename__ = 'LEKARSTWA'
    ilosc = db.Column(db.Integer,  nullable=False)
    ID_ZAMOWIENIE = db.Column(db.Integer, primary_key=True,  nullable=False)
    ID_LEKARSTWO = db.Column(db.Integer, primary_key=True, nullable=False)
    db.ForeignKeyConstraint(
        ['ID_ZAMOWIENIE','ID_LEKARSTWO'],['ZAMOWIENIE.id','LEKI.id']
    )




@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response


@app.route("/")
def index():
    classes = ["OSOBA","ADMINISTRATOR", "KLIENT", "ZAMOWIENIE", "FARMACEUTA", "LEKI","APTEKA" , "MIASTO", "MAGAZYN", "DYZUR", "LEKARSTWA"]

    return render_template('index(1).html', lista=classes)

@app.route('/inventory/<style>')
def inventory(style):
    try:
       if style == "OSOBA":
           osoby = OSOBA.query.all()
           return render_template('osoba.html', lista=osoby)
       elif style == "ADMINISTRATOR":
           records = ADMINISTRATOR.query.all()
           return render_template('administrator.html', lista=records)
       elif style == "KLIENT":
           records = KLIENT.query.all()
           return render_template('klient.html', lista=records)
       elif style == "ZAMOWIENIE":
           records = ZAMOWIENIE.query.all()
           return render_template('zamowienie.html', lista=records)
       elif style == "FARMACEUTA":
           records = FARMACEUTA.query.all()
           return render_template('farmaceuta.html', lista=records)
       elif style == "LEKI":
           records = LEKI.query.all()
           return render_template('leki.html', lista=records)
       elif style == "APTEKA":
           records = APTEKA.query.all()
           return render_template('apteka.html', lista=records)
       elif style == "MIASTO":
           records = MIASTO.query.all()
           return render_template('miasto.html', lista=records)
       elif style == "MAGAZYN":
           records = MAGAZYN.query.all()
           return render_template('magazyn.html', lista=records)
       elif style == "DYZUR":
           records = DYZUR.query.all()
           return render_template('dyzur.html', lista=records)
       elif style == "LEKARSTWA":
           records = LEKARSTWA.query.all()
           return render_template('lekarstwa.html', lista=records)

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


'''@app.route("/OSOBA")
def OSOBA():
    #styles = OSOBA.query.with_entities(OSOBA.imie).distinct()
    #osoby = OSOBA.query.all()
    #classes = [LEKI,OSOBA]
    #classes = OSOBA.query.with_entities(OSOBA.nazwisko).distinct()
    try:
        osoby = OSOBA.query.all()
        return render_template('osoba.html', lista=osoby)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.route("/ADMINISTRATOR")
def ADMINISTRATOR():
    try:
        records = ADMINISTRATOR.query.all()
        return render_template('administrator.html', lista=records)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.route("/KLIENT")
def KLIENT():
    try:
        records = KLIENT.query.all()
        return render_template('klient.html', lista=records)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.route("/ZAMOWIENIE")
def ZAMOWIENIE():
    try:
        records = ZAMOWIENIE.query.all()
        return render_template('zamowienie.html', lista=records)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.route("/FARMACEUTA")
def FARMACEUTA():
    try:
        records = FARMACEUTA.query.all()
        return render_template('farmaceuta.html', lista=records)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


@app.route("/LEKI")
def LEKI():
    try:
        records = LEKI.query.all()
        return render_template('leki.html', lista=records)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


@app.route("/APTEKA")
def APTEKA():
    try:
        records = APTEKA.query.all()
        return render_template('apteka.html', lista=records)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.route("/MIASTO")
def MIASTO():
    try:
        records = MIASTO.query.all()
        return render_template('miasto.html', lista=records)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.route("/MAGAZYN")
def MAGAZYN():
    try:
        records = MAGAZYN.query.all()
        return render_template('magazyn.html', lista=records)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text'''

'''@app.route("/DYZUR")
def dyzur():
    try:
        records = DYZUR.query.all()
        return render_template('dyzur.html', lista=records)
    except Exception as e:
         
         error_text = "<p>The error:<br>" + str(e) + "</p>"
         hed = '<h1>Something is broken.</h1>'
         return hed + error_text

@app.route("/LEKARSTWA")
def lekarstwa():
    try:
        records = LEKARSTWA.query.all()
        return render_template('lekarstwa.html', lista=records)
    except Exception as e:
    
    error_text = "<p>The error:<br>" + str(e) + "</p>"
    hed = '<h1>Something is broken.</h1>'
    return hed + error_text

def inventory():
    try:
        osoby = OSOBA.query.all()
        return render_template('list.html', osoby=osoby)
    except Exception as e:
        
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


def index():
    try:
        osoby = OSOBA.query.all()
        osoba_text = '<ul>'
        for osoba in osoby:
            osoba_text += '<li>' + osoba.imie +  osoba.nazwisko + '</li>'
        osoba_text += '</ul>'
        return osoba_text
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text'''

'''@app.route("/<name>")
def hello_name(name):
    return "Hello " + name


@app.route("/todo", methods=["GET"])
def list_todo():
    return jsonify(ToDoService().list())


@app.route("/todo", methods=["POST"])
def create_todo():
    return jsonify(ToDoService().create(request.get_json()))


@app.route("/todo/<item_id>", methods=["PUT"])
def update_item(item_id):
    return jsonify(ToDoService().update(item_id, request.get_json()))

@app.route("/todo/<item_id>", methods=["GET"])
def get_item(item_id):
    return jsonify(ToDoService().get_by_id(item_id))

@app.route("/todo/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    return jsonify(ToDoService().delete(item_id))'''


if __name__ == "__main__":
    Schema()
    app.run(debug=True, host='127.0.0.1', port=8888)