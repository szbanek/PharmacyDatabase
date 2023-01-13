from flask import Flask, request, jsonify, render_template, redirect
# from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
# from sqlalchemy.orm import relationship
import mysql.connector
from update import Update
from insert import Insert
from delete import Delete

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
delete = Delete(mycursor)
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

@app.route("/modify_lek", methods=['GET', 'POST'])
def modify_lek():
    if request.method == "POST":
        if 'id_lek_zmien' and 'nazwa_lek_zmien' and 'recepta_lek_zmien' in request.form:
            id = request.form['id_lek_zmien']
            nazwa = request.form['nazwa_lek_zmien']
            recepta = request.form['recepta_lek_zmien']

            update.lek(id,nazwa,recepta)

            mydb.commit()

            return render_template('index.html')
        elif 'id_lek_dodaj' and 'nazwa_lek_dodaj' and 'recepta_lek_dodaj' in request.form:
            nazwa = request.form['nazwa_lek_dodaj']
            recepta = request.form['recepta_lek_dodaj']

            insert.lek(nazwa, recepta)

            mydb.commit()
            return render_template('index.html')
        elif 'id_lek_usun' and 'nazwa_lek_usun' and 'recepta_lek_usun' in request.form:
            id = request.form['id_lek_usun']

            delete.lek(id)

            mydb.commit()
            return render_template('index.html')
        else:
            return render_template('modyfikacja_listy_lekow.html')
    else:
       return render_template('modyfikacja_listy_lekow.html')

@app.route("/modify_apteka", methods=['GET', 'POST'])
def modify_apteka():
    if request.method == "POST":
        if 'id_apteka_zmien' and 'nazwa_apteka_zmien' and 'godz_od_apteka_zmien' and 'godz_do_apteka_zmien' and 'adres_apteka_zmien' and 'telefon_apteka_zmien' in request.form:
            id = request.form['id_apteka_zmien']
            nazwa = request.form['nazwa_apteka_zmien']
            godz_od = request.form['godz_od_apteka_zmien']
            godz_do = request.form['godz_do_apteka_zmien']
            adres = request.form['adres_apteka_zmien']
            telefon = request.form['telefon_apteka_zmien']
            update.apteka(id,nazwa,godz_od,godz_do,adres,telefon)

            mydb.commit()

            return render_template('index.html')
        elif 'nazwa_apteka_dodaj' and 'godz_od_apteka_dodaj' and 'godz_do_apteka_dodaj' and 'adres_apteka_dodaj' and 'telefon_apteka_dodaj' in request.form:
            nazwa = request.form['nazwa_apteka_dodaj']
            godz_od = request.form['godz_od_apteka_dodaj']
            godz_do = request.form['godz_do_apteka_dodaj']
            adres = request.form['adres_apteka_dodaj']
            telefon = request.form['telefon_apteka_dodaj']

            insert.apteka(nazwa,godz_od,godz_do,adres,telefon)

            mydb.commit()
            return render_template('index.html')
        elif 'id_apteka_usun' in request.form:
            id = request.form['id_apteka_usun']

            delete.apteka(id)

            mydb.commit()
            return render_template('index.html')
        else:
            return render_template('modyfikacja_listy_aptek.html')
    else:
       return render_template('modyfikacja_listy_aptek.html')

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


@app.route("/modify_klient", methods=['GET', 'POST'])
def modify_klient():
    if request.method == "POST":
        if 'id_klient_zmien' and 'poprzedni_zakup_klient_zmien' in request.form:
            id = request.form['id_klient_zmien']
            poprzedni_zakup = request.form['poprzedni_zakup_klient_zmien']


            update.klient(id,poprzedni_zakup)

            mydb.commit()

            return render_template('index.html')
        elif 'id_klient_dodaj' and 'poprzedni_zakup_klient_dodaj' in request.form:
            id = request.form['id_klient_dodaj']
            poprzedni_zakup = request.form['poprzedni_zakup_klient_dodaj']

            insert.klient(id, poprzedni_zakup)

            mydb.commit()
            return render_template('index.html')
        elif 'id_klient_usun' and 'poprzedni_zakup_klient_usun' in request.form:
            id = request.form['id_klient_usun']

            delete.klient(id)

            mydb.commit()
            return render_template('index.html')
        else:
            return render_template('modyfikacja_listy_klientow.html')
    else:
       return render_template('modyfikacja_listy_klientow.html')


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


@app.route("/modify_zamowienia", methods=['GET', 'POST'])
def modify_zamowienia():
    if request.method == "POST":
        if 'id_zamowienia_zmien' and 'status_zamowienia_zmien' and 'data_zamowienia_zmien' and 'id_klienta_zamowienia_zmien' in request.form:
            id = request.form['id_zamowienia_zmien']
            status = request.form['status_zamowienia_zmien']
            data_zam = request.form['data_zamowienia_zmien']
            id_klienta = request.form['id_klienta_zamowienia_zmien']

            update.zamowienie(id,status,data_zam, id_klienta)

            mydb.commit()

            return render_template('index.html')
        elif 'status_zamowienia_dodaj' and 'data_zamowienia_dodaj' and 'id_klienta_zamowienia_dodaj' in request.form:

            status = request.form['status_zamowienia_dodaj']
            data_zam = request.form['data_zamowienia_dodaj']
            id_klienta = request.form['id_klienta_zamowienia_dodaj']

            insert.zamowienie(status,data_zam, id_klienta)

            mydb.commit()
            return render_template('index.html')
        elif 'id_zamowienia_usun' in request.form:
            id = request.form['id_zamowienia_usun']

            delete.zamowienie(id)

            mydb.commit()
            return render_template('index.html')
        else:
            return render_template('modyfikacja_zamowienia.html')
    else:
       return render_template('modyfikacja_zamowienia.html')



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
    

