from flask import Flask, request, jsonify, render_template, redirect
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

mycursor=mydb.cursor()
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

@app.route("/watch")
def watch():
    return render_template('watch_database_administrator.html')


@app.route("/apteki")
def show_table_apteka_to_adm():
    mycursor.execute("select * from APTEKA")
    data_apteka = mycursor.fetchall()
    return render_template('watch_database_administrator_apteka.html', headings=headings_apteka, data=data_apteka)

@app.route("/dyzury")
def show_table_dyzury_to_adm():
    mycursor.execute("select * from DYZUR")
    data_dyzury = mycursor.fetchall()
    return render_template('watch_database_administrator_dyzury.html', headings=headings_dyzury, data=data_dyzury)

@app.route("/farmaceuci")
def show_table_farmaceuta_to_adm():
    mycursor.execute("select * from FARMACEUTA")
    data_farmaceuci = mycursor.fetchall()
    return render_template('watch_database_administrator_farmaceuci.html', headings=headings_farmaceuci, data=data_farmaceuci)

@app.route("/klienci")
def show_table_klient_to_adm():
    mycursor.execute("select * from KLIENT")
    data_klienci = mycursor.fetchall()
    return render_template('watch_database_administrator_klienci.html', headings=headings_klienci, data=data_klienci)

@app.route("/zamowienia")
def show_table_zamowienia_to_adm():
    mycursor.execute("select * from ZAMOWIENIE")
    data_zamowienia = mycursor.fetchall()
    return render_template('watch_database_administrator_zamowienia.html', headings=headings_zamowienia, data=data_zamowienia)


@app.route("/leki", methods=['GET', 'POST'])
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

@app.route("/magazyny")
def show_table_magazyn_to_adm():
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

def update_dyzur(
    id_farm,
    id_apteki,
    dzien,
    godz_od,
    godz_do
):
    query = f"""UPDATE TABLE DYZUR
            SET godz_od = {godz_od},
                godz_do = {godz_do}
            WHERE DZIEN = '{dzien}' and
            ID_FARMACEUTA = {id_farm} and
            ID_APTEKA = {id_apteki};"""
    mycursor.execute(query)
    mydb.commit()
    
def update_apteka(
    id,
    nazwa,
    godz_od,
    godz_do,
    adres,
    telefon
):
    query = f"""UPDATE TABLE APTEKA
            SET nazwa = '{nazwa}',
                godz_od = {godz_od},
                godz_do = {godz_do},
                adres = '{adres}',
                telefon = {telefon}
            WHERE id = {id};"""
    mycursor.execute(query)
    mydb.commit()

def update_lek(
    id,
    nazwa,
    recepta
):
    query = f"""UPDATE TABLE LEK
            SET nazwa = '{nazwa}',
                recepta = {recepta}
            WHERE id = {id}; """
    mycursor.execute(query)
    mydb.commit()

def update_miasto(
    id,
    nazwa,
    kod
):
    query = f"""UPDATE TABLE MIASTO
            SET nazwa = '{nazwa}',
                kod = '{kod}'
            WHERE id = {id} """
    mycursor.execute(query)
    mydb.commit()

def update_lekarstwa(
    id_zam, 
    id_lek,
    ilosc
):
    query = f"""UPDATE TABLE LEKARSTWA
            SET ilosc = {ilosc},
            WHERE ID_ZAMOWIENIE = {id_zam} and
                ID_LEKARSTWO = {id_lek}; """
    mycursor.execute(query)
    mydb.commit()

def update_zamowienie(
    id,
    status,
    data_zam
):
    query = f"""UPDATE TABLE ZAMOWIENIE
            SET status '{status}',
                DATA_ZAMOWIENIA = '{data_zam}'
            WHERE id = {id} """
    mycursor.execute(query)
    mydb.commit()

def update_magazyn(
    pojemnosc,
    adres,
    id_apteki,
    id_lek
):
    query = f"""UPDATE TABLE MAGAZYN
            SET POJEMNOSC = {pojemnosc},
                ADRES = '{adres}',
            WHERE ID_APTEKA = {id_apteki} and
                ID_LEKARSTWO = {id_lek}; """
    mycursor.execute(query)
    mydb.commit()

def update_admin(
    id,
    placa
):
    query = f"""UPDATE TABLE ADMIN
            SET placa = {placa}
            WHERE id = {id}; """
    mycursor.execute(query)
    mydb.commit()

def update_klient(
    id,
    zakup
):
    query = f"""UPDATE TABLE KLIENT
            SET POPRZEDNI_ZAKUP = '{zakup}'
            WHERE id = {id}; """
    mycursor.execute(query)
    mydb.commit()

def update_farmaceuta(
    id,
    placa,
    wyksztalcenie
):
    query = f"""UPDATE TABLE FARMACEUTA
            SET PLACA = {placa},
                WYKSZTALCENIE = '{wyksztalcenie}'
            WHERE id = {id}; """
    mycursor.execute(query)
    mydb.commit()

def update_osoba(
    id,
    nazwisko,
    imie,
    data_ur,
    telefon,
    email,
    adres
):
    query = f"""UPDATE TABLE OSOBA
            SET NAZWISKO = '{nazwisko}',
                IMIE = '{imie}',
                DATA_URODZENIA = '{data_ur}',
                TELEFON = {telefon},
                EMAIL = '{email}',
                ADRES = '{adres}'
            WHERE id = {id}; """
    mycursor.execute(query)
    mydb.commit()

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8888)

