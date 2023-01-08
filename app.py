from flask import Flask, request, jsonify, render_template, redirect
# from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
# from sqlalchemy.orm import relationship
import mysql.connector
from update import Update
from insert import Insert

app = Flask(__name__)

bootstrap = Bootstrap(app)

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bazaDanych"
)

mycursor=mydb.cursor()
update = Update(mycursor)
insert = Insert(mycursor)
#for data in records:
    #print(data)

headings_apteka = ("ID", "NAZWA", "GODZ_OD", "GODZ_DO", "ADRES", "TELEFON")
headings_dyzury = ("DZIEN", "GODZ_OD", "GODZ_DO", "ID_FARMACEUTA", "ID_APTEKA")
headings_farmaceuci = ("ID", "PLACA", "WYKSZTALCENIE")
headings_klienci = ("ID", "POPRZEDNI_ZAKUP")
headings_zamowienia = ("ID", "STATUS", "DATA_ZAMOWIENIA")
headings_lek = ("ID", "NAZWA", "RECEPTA")
headings_magazyny = ("POJEMNOSC", "ADRES", "ID_APTEKA", "ID_LEKARSTWO")
headings_administratorzy = ("ID", "PLACA")

@app.route("/home")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/watch_administrator")
def watch_adm():
    return render_template('watch_database_administrator.html')


@app.route("/watch_farmaceuta")
def watch_farmaceuta():
    return render_template('watch_database_farmaceuta.html')

@app.route("/modify", methods=['GET', 'POST'])
def modify_lek():
    if request.method == "POST":
        id = [request.form['id_apteka']]
        nazwa = [request.form['nazwa_apteka']]
        recepta = [request.form['recepta_apteka']]


        update.lek(id,nazwa,recepta)

        mycursor.session.commit()
        #return render_template('index.html')
    else:
       return render_template('modyfikacja_listy_lekow.html')



@app.route("/apteki", methods=['GET', 'POST'])
def show_table_apteka_to_adm():
    if request.method == "POST":
        nazwa = [request.form['Apteka']]
        mycursor.execute("SELECT * FROM APTEKA WHERE NAZWA = %s", nazwa)
        data_apteka = mycursor.fetchall()
        return render_template('watch_database_administrator_apteka.html', headings=headings_apteka, data=data_apteka)
    else:
        mycursor.execute("select * from APTEKA")
        data_apteka = mycursor.fetchall()
        return render_template('watch_database_administrator_apteka.html', headings=headings_apteka, data=data_apteka)

@app.route("/dyzury", methods=['GET', 'POST'])
def show_table_dyzury_to_adm():
    if request.method == "POST":
        Day = [request.form['Dyzur']]
        mycursor.execute("SELECT * FROM DYZUR WHERE DZIEN = %s", Day)
        data_dyzury = mycursor.fetchall()
        return render_template('watch_database_administrator_dyzury.html', headings=headings_dyzury, data=data_dyzury)
    else:
        mycursor.execute("select * from DYZUR")
        data_dyzury = mycursor.fetchall()
        return render_template('watch_database_administrator_dyzury.html', headings=headings_dyzury, data=data_dyzury)

@app.route("/farmaceuci", methods=['GET', 'POST'])
def show_table_farmaceuta_to_adm():
    if request.method == "POST":
        id = [request.form['Farmaceuta']]
        mycursor.execute("SELECT * FROM FARMACEUTA WHERE ID = %s", id)
        data_farmaceuci = mycursor.fetchall()
        return render_template('watch_database_administrator_farmaceuci.html', headings=headings_farmaceuci, data=data_farmaceuci)
    else:
        mycursor.execute("select * from FARMACEUTA")
        data_farmaceuci = mycursor.fetchall()
        return render_template('watch_database_administrator_farmaceuci.html', headings=headings_farmaceuci, data=data_farmaceuci)

@app.route("/klienci_administrator", methods=['GET', 'POST'])
def show_table_klient_to_adm():
    if request.method == "POST":
        id = [request.form['Klient']]
        mycursor.execute("SELECT * FROM KLIENT WHERE ID = %s", id)
        data_klienci = mycursor.fetchall()
        return render_template('watch_database_administrator_klienci.html', headings=headings_klienci, data=data_klienci)
    else:
        mycursor.execute("select * from KLIENT")
        data_klienci = mycursor.fetchall()
        return render_template('watch_database_administrator_klienci.html', headings=headings_klienci, data=data_klienci)

@app.route("/klienci_farmaceuta", methods=['GET', 'POST'])
def show_table_klient_to_fmc():
    if request.method == "POST":
        id = [request.form['Klient_farmaceuta']]
        mycursor.execute("SELECT * FROM KLIENT WHERE ID = %s", id)
        data_klienci = mycursor.fetchall()
        return render_template('watch_database_farmaceuta_klienci.html', headings=headings_klienci, data=data_klienci)
    else:
        mycursor.execute("select * from KLIENT")
        data_klienci = mycursor.fetchall()
        return render_template('watch_database_farmaceuta_klienci.html', headings=headings_klienci, data=data_klienci)


@app.route("/zamowienia_administrator", methods=['GET', 'POST'])
def show_table_zamowienia_to_adm():
    if request.method == "POST":
        id = [request.form['Zamowienie']]
        mycursor.execute("SELECT * FROM ZAMOWIENIE WHERE ID = %s", id)
        data_zamowienia = mycursor.fetchall()
        return render_template('watch_database_administrator_zamowienia.html', headings=headings_zamowienia, data=data_zamowienia)
    else:
        mycursor.execute("select * from ZAMOWIENIE")
        data_zamowienia = mycursor.fetchall()
        return render_template('watch_database_administrator_zamowienia.html', headings=headings_zamowienia, data=data_zamowienia)

@app.route("/zamowienia_farmaceuta", methods=['GET', 'POST'])
def show_table_zamowienia_to_fmc():
    if request.method == "POST":
        id = [request.form['Zamowienie_farmaceuta']]
        mycursor.execute("SELECT * FROM ZAMOWIENIE WHERE ID = %s", id)
        data_zamowienia = mycursor.fetchall()
        return render_template('watch_database_farmaceuta_zamowienia.html', headings=headings_zamowienia, data=data_zamowienia)
    else:
        mycursor.execute("select * from ZAMOWIENIE")
        data_zamowienia = mycursor.fetchall()
        return render_template('watch_database_farmaceuta_zamowienia.html', headings=headings_zamowienia, data=data_zamowienia)

@app.route("/leki_administrator", methods=['GET', 'POST'])
def show_table_lek_to_adm():
    if request.method == "POST":
        nazwa = [request.form['LEK']]
        mycursor.execute("SELECT ID,NAZWA,RECEPTA FROM LEK WHERE NAZWA = %s", nazwa)
        data_lek = mycursor.fetchall()
        return render_template('watch_database_administrator_lek.html', headings=headings_lek, data=data_lek)
    else:
        mycursor.execute("select * from LEK")
        data_lek = mycursor.fetchall()
        return render_template('watch_database_administrator_lek.html', headings=headings_lek, data=data_lek)

@app.route("/leki_farmaceuta", methods=['GET', 'POST'])
def show_table_lek_to_fmc():
    if request.method == "POST":
        nazwa = [request.form['LEK_farmaceuta']]
        mycursor.execute("SELECT ID,NAZWA,RECEPTA FROM LEK WHERE NAZWA = %s", nazwa)
        data_lek = mycursor.fetchall()
        return render_template('watch_database_farmaceuta_leki.html', headings=headings_lek, data=data_lek)
    else:
        mycursor.execute("select * from LEK")
        data_lek = mycursor.fetchall()
        return render_template('watch_database_farmaceuta_leki.html', headings=headings_lek, data=data_lek)

@app.route("/magazyny", methods=['GET', 'POST'])
def show_table_magazyn_to_adm():
    if request.method == "POST":
        adres = [request.form['Magazyn']]
        mycursor.execute("SELECT * FROM MAGAZYN WHERE ADRES = %s", adres)
        data_magazyny = mycursor.fetchall()
        return render_template('watch_database_administrator_magazyny.html', headings=headings_magazyny, data=data_magazyny)
    else:
        mycursor.execute("select * from MAGAZYN")
        data_magazyny = mycursor.fetchall()
        return render_template('watch_database_administrator_magazyny.html', headings=headings_magazyny, data=data_magazyny)

@app.route("/administratorzy", methods=['GET', 'POST'])
def show_table_administrator_to_adm():
    if request.method == "POST":
        id = [request.form['Administrator']]
        mycursor.execute("SELECT ID,PLACA FROM ADMINISTRATOR WHERE ID = %s", id)
        data_administratorzy = mycursor.fetchall()
        return render_template('watch_database_administrator_administratorzy.html', headings=headings_administratorzy, data=data_administratorzy)
    else:
        mycursor.execute("select * from ADMINISTRATOR")
        data_administratorzy = mycursor.fetchall()
        return render_template('watch_database_administrator_administratorzy.html', headings=headings_administratorzy, data=data_administratorzy)



if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8888)
    

