from flask import Flask, request, jsonify, render_template, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
# from sqlalchemy.orm import relationship
import mysql.connector
from update import Update
from insert import Insert
from delete import Delete
from utils import getSalarySum

error_message = ""
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

headings_osoby = ( "ID", "NAZWISKO", "IMIE", "DATA_URODZENIA", "TELEFON", "EMAIL", "ADRES")
headings_apteka = ("ID", "NAZWA", "GODZ_OD", "GODZ_DO", "ADRES", "TELEFON")
headings_dyzury = ("DZIEN", "GODZ_OD", "GODZ_DO", "ID_FARMACEUTA", "ID_APTEKA")
headings_farmaceuci = ("PLACA", "WYKSZTALCENIE")
headings_klienci = ("POPRZEDNI_ZAKUP",)
headings_zamowienia = ("ID", "STATUS", "DATA_ZAMOWIENIA", "ID_KLIENTA")
headings_lek = ("ID", "NAZWA", "RECEPTA")
headings_magazyny = ("POJEMNOSC", "ADRES", "ID_APTEKA", "ID_LEKARSTWO")
headings_administratorzy = ("PLACA",)

@app.route("/home")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/error")
def error():
    return render_template('strona_bledy.html', error_text = error_message)

@app.route("/watch_administrator")
def watch_adm():
    return render_template('watch_database_administrator.html')


@app.route("/watch_farmaceuta")
def watch_farmaceuta():
    return render_template('watch_database_farmaceuta.html')

@app.route("/modify_lek", methods=['GET', 'POST'])
def modify_lek():
    if request.method == "POST":
        global error_message
        if 'id_lek_zmien' and 'nazwa_lek_zmien' and 'recepta_lek_zmien' in request.form:
            id = request.form['id_lek_zmien']
            nazwa = request.form['nazwa_lek_zmien']
            recepta = request.form['recepta_lek_zmien']

            tmp = update.lek(id,nazwa,recepta)
            if tmp != None:
                
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()

            return render_template('index.html')
        elif 'nazwa_lek_dodaj' and 'recepta_lek_dodaj' in request.form:
            nazwa = request.form['nazwa_lek_dodaj']
            recepta = request.form['recepta_lek_dodaj']

            tmp = insert.lek(nazwa, recepta)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()
            return render_template('index.html')
        elif 'id_lek_usun' in request.form:
            id = request.form['id_lek_usun']

            tmp = delete.lek(id)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()
            return render_template('index.html')
        else:
            return render_template('modyfikacja_listy_lekow.html')
    else:
       return render_template('modyfikacja_listy_lekow.html')

@app.route("/modify_apteka", methods=['GET', 'POST'])
def modify_apteka():
    if request.method == "POST":
        global error_message
        if 'id_apteka_zmien' and 'nazwa_apteka_zmien' and 'godz_od_apteka_zmien' and 'godz_do_apteka_zmien' and 'adres_apteka_zmien' and 'telefon_apteka_zmien' in request.form:
            id = request.form['id_apteka_zmien']
            nazwa = request.form['nazwa_apteka_zmien']
            godz_od = request.form['godz_od_apteka_zmien']
            godz_do = request.form['godz_do_apteka_zmien']
            adres = request.form['adres_apteka_zmien']
            telefon = request.form['telefon_apteka_zmien']
            tmp = update.apteka(id,nazwa,godz_od,godz_do,adres,telefon)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()

            return render_template('index.html')
        elif 'nazwa_apteka_dodaj' and 'godz_od_apteka_dodaj' and 'godz_do_apteka_dodaj' and 'adres_apteka_dodaj' and 'telefon_apteka_dodaj' in request.form:
            nazwa = request.form['nazwa_apteka_dodaj']
            godz_od = request.form['godz_od_apteka_dodaj']
            godz_do = request.form['godz_do_apteka_dodaj']
            adres = request.form['adres_apteka_dodaj']
            telefon = request.form['telefon_apteka_dodaj']

            tmp = insert.apteka(nazwa,godz_od,godz_do,adres,telefon)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()
            return render_template('index.html')
        elif 'id_apteka_usun' in request.form:
            id = request.form['id_apteka_usun']

            tmp = delete.apteka(id)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

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


@app.route("/modify_dyzury", methods=['GET', 'POST'])
def modify_dyzury():
    if request.method == "POST":
        global error_message
        if 'dzien_dyzur_zmien' and 'godz_od_dyzur_zmien' and 'godz_do_dyzur_zmien' and 'id_farmaceuta_dyzur_zmien' and 'id_apteka_dyzur_zmien' in request.form:
            dzien = request.form['dzien_dyzur_zmien']
            godz_od = request.form['godz_od_dyzur_zmien']
            godz_do = request.form['godz_do_dyzur_zmien']
            id_farmaceuta = request.form['id_farmaceuta_dyzur_zmien']
            id_apteka = request.form['id_apteka_dyzur_zmien']

            tmp = update.dyzur(id_farmaceuta,id_apteka,dzien,godz_od, godz_do)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()

            return render_template('index.html')
        elif 'dzien_dyzur_dodaj' and 'godz_od_dyzur_dodaj' and 'godz_do_dyzur_dodaj' and 'id_farmaceuta_dyzur_dodaj' and 'id_apteka_dyzur_dodaj' in request.form:
            dzien = request.form['dzien_dyzur_dodaj']
            godz_od = request.form['godz_od_dyzur_dodaj']
            godz_do = request.form['godz_do_dyzur_dodaj']
            id_farmaceuta = request.form['id_farmaceuta_dyzur_dodaj']
            id_apteka = request.form['id_apteka_dyzur_dodaj']

            tmp = insert.dyzur(id_farmaceuta,id_apteka,dzien,godz_od, godz_do)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()
            return render_template('index.html')
        elif 'dzien_dyzur_usun' and 'id_farmaceuta_dyzur_usun' and 'id_apteka_dyzur_usun' in request.form:
            dzien = request.form['dzien_dyzur_usun']
            id_farmaceuta = request.form['id_farmaceuta_dyzur_usun']
            id_apteka = request.form['id_apteka_dyzur_usun']

            tmp = delete.dyzur(id_farmaceuta, id_apteka, dzien)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()
            return render_template('index.html')
        else:
            return render_template('modyfikacja_dyzurow.html')
    else:
       return render_template('modyfikacja_dyzurow.html')


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
        mycursor.execute("""SELECT osoba.ID, NAZWISKO, IMIE, DATA_URODZENIA, TELEFON, EMAIL, ADRES, PLACA, WYKSZTALCENIE
        FROM OSOBA INNER JOIN FARMACEUTA ON farmaceuta.id = osoba.id WHERE osoba.ID = %s""", id)
        data_farmaceuci = mycursor.fetchall()
        return render_template('watch_database_administrator_farmaceuci.html', headings=headings_osoby+headings_farmaceuci, data=data_farmaceuci, variable_suma=getSalarySum(mycursor, False))
    else:
        mycursor.execute("""select osoba.ID, NAZWISKO, IMIE, DATA_URODZENIA, TELEFON, EMAIL, ADRES, PLACA, WYKSZTALCENIE
        from OSOBA INNER JOIN FARMACEUTA ON farmaceuta.id = osoba.id""")
        data_farmaceuci = mycursor.fetchall()
        return render_template('watch_database_administrator_farmaceuci.html', headings=headings_osoby+headings_farmaceuci, data=data_farmaceuci, variable_suma=getSalarySum(mycursor, False))


@app.route("/modify_klient", methods=['GET', 'POST'])
def modify_klient():
    if request.method == "POST":
        global error_message
        if 'id_klient_zmien' and 'poprzedni_zakup_klient_zmien' in request.form:
            id = request.form['id_klient_zmien']
            poprzedni_zakup = request.form['poprzedni_zakup_klient_zmien']


            tmp = update.klient(id,poprzedni_zakup)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()

            return render_template('index.html')
        elif 'poprzedni_zakup_klient_dodaj' and 'nazwisko_osoba_dodaj' and 'imie_osoba_dodaj' and 'dataur_osoba_dodaj' and 'telefon_osoba_dodaj' and 'email_osoba_dodaj' and 'adres_osoba_dodaj' in request.form:
            poprzedni_zakup = request.form['poprzedni_zakup_klient_dodaj']
            nazwisko = request.form['nazwisko_osoba_dodaj']
            imie = request.form['imie_osoba_dodaj']
            data_ur = request.form['dataur_osoba_dodaj']
            telefon = request.form['telefon_osoba_dodaj']
            email = request.form['email_osoba_dodaj']
            adres = request.form['adres_osoba_dodaj']

            tmp = insert.osoba(nazwisko, imie, data_ur, telefon, email, adres)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mycursor.execute(f"SELECT id from osoba WHERE nazwisko='{nazwisko}' and imie='{imie}' and telefon={telefon};")
            tmp = insert.klient(mycursor.fetchone()[0], poprzedni_zakup)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()
            return render_template('index.html')
        elif 'id_klient_usun' in request.form:
            id = request.form['id_klient_usun']

            tmp = delete.klient(id)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

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
        mycursor.execute("""SELECT osoba.ID, NAZWISKO, IMIE, DATA_URODZENIA, TELEFON, EMAIL, ADRES, POPRZEDNI_ZAKUP
        FROM OSOBA INNER JOIN KLIENT ON klient.id = osoba.id  WHERE osoba.ID = %s""", id)
        data_klienci = mycursor.fetchall()
        return render_template('watch_database_administrator_klienci.html', headings=headings_osoby+headings_klienci, data=data_klienci)
    else:
        mycursor.execute("""select osoba.ID, NAZWISKO, IMIE, DATA_URODZENIA, TELEFON, EMAIL, ADRES, POPRZEDNI_ZAKUP
        from OSOBA INNER JOIN KLIENT ON klient.id = osoba.id """)
        data_klienci = mycursor.fetchall()
        return render_template('watch_database_administrator_klienci.html', headings=headings_osoby+headings_klienci, data=data_klienci)

@app.route("/klienci_farmaceuta", methods=['GET', 'POST'])
def show_table_klient_to_fmc():
    if request.method == "POST":
        id = [request.form['Klient_farmaceuta']]
        mycursor.execute("""SELECT osoba.ID, NAZWISKO, IMIE, DATA_URODZENIA, TELEFON, EMAIL, ADRES, POPRZEDNI_ZAKUP
        FROM OSOBA INNER JOIN KLIENT ON klient.id = osoba.id  WHERE osoba.ID = %s""", id)
        data_klienci = mycursor.fetchall()
        return render_template('watch_database_farmaceuta_klienci.html', headings=headings_osoby+headings_klienci, data=data_klienci)
    else:
        mycursor.execute("""select osoba.ID, NAZWISKO, IMIE, DATA_URODZENIA, TELEFON, EMAIL, ADRES, POPRZEDNI_ZAKUP
        from OSOBA INNER JOIN KLIENT ON klient.id = osoba.id """)
        data_klienci = mycursor.fetchall()
        return render_template('watch_database_farmaceuta_klienci.html', headings=headings_osoby+headings_klienci, data=data_klienci)


@app.route("/modify_zamowienia", methods=['GET', 'POST'])
def modify_zamowienia():
    if request.method == "POST":
        global error_message
        if 'id_zamowienia_zmien' and 'status_zamowienia_zmien' and 'data_zamowienia_zmien' and 'id_klienta_zamowienia_zmien' in request.form:
            id = request.form['id_zamowienia_zmien']
            status = request.form['status_zamowienia_zmien']
            data_zam = request.form['data_zamowienia_zmien']
            id_klienta = request.form['id_klienta_zamowienia_zmien']

            tmp = update.zamowienie(id,status,data_zam, id_klienta)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()

            return render_template('index.html')
        elif 'status_zamowienia_dodaj' and 'data_zamowienia_dodaj' and 'id_klienta_zamowienia_dodaj' in request.form:

            status = request.form['status_zamowienia_dodaj']
            data_zam = request.form['data_zamowienia_dodaj']
            id_klienta = request.form['id_klienta_zamowienia_dodaj']

            tmp = insert.zamowienie(status,data_zam, id_klienta)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()
            return render_template('index.html')
        elif 'id_zamowienia_usun' in request.form:
            id = request.form['id_zamowienia_usun']

            tmp = delete.zamowienie(id)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

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


@app.route("/modify_magazyn", methods=['GET', 'POST'])
def modify_magazyn():
    if request.method == "POST":
        global error_message
        if 'pojemnosc_magazyn_zmien' and 'adres_magazyn_zmien' and 'id_apteka_magazyn_zmien' and 'id_lekarstwo_magazyn_zmien' in request.form:
            pojemnosc = request.form['pojemnosc_magazyn_zmien']
            adres = request.form['adres_magazyn_zmien']
            id_apteka = request.form['id_apteka_magazyn_zmien']
            id_lekarstwo = request.form['id_lekarstwo_magazyn_zmien']

            tmp = update.magazyn(pojemnosc,adres, id_apteka, id_lekarstwo )
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()

            return render_template('index.html')
        elif 'pojemnosc_magazyn_dodaj' and 'adres_magazyn_dodaj' and 'id_apteka_magazyn_dodaj' and 'id_lekarstwo_magazyn_dodaj' in request.form:
            pojemnosc = request.form['pojemnosc_magazyn_dodaj']
            adres = request.form['adres_magazyn_dodaj']
            id_apteka = request.form['id_apteka_magazyn_dodaj']
            id_lekarstwo = request.form['id_lekarstwo_magazyn_dodaj']

            tmp = insert.magazyn(pojemnosc, adres, id_apteka, id_lekarstwo)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()
            return render_template('index.html')
        elif 'id_apteka_magazyn_usun' and 'id_lekarstwo_magazyn_usun' in request.form:
            id_apteka = request.form['id_apteka_magazyn_usun']
            id_lekarstwo = request.form['id_lekarstwo_magazyn_usun']

            tmp = delete.magazyn(id_apteka, id_lekarstwo)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()
            return render_template('index.html')
        else:
            return render_template('modyfikacja_listy_magazynow.html')
    else:
       return render_template('modyfikacja_listy_magazynow.html')


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
        mycursor.execute("SELECT osoba.ID, NAZWISKO, IMIE, DATA_URODZENIA, TELEFON, EMAIL, ADRES, PLACA FROM OSOBA INNER JOIN ADMINISTRATOR ON administrator.id = osoba.id WHERE osoba.ID = %s", id)
        data_administratorzy = mycursor.fetchall()
        return render_template('watch_database_administrator_administratorzy.html', headings=headings_osoby+headings_administratorzy, data=data_administratorzy, variable_suma=getSalarySum(mycursor, True))
    else:
        mycursor.execute("SELECT osoba.ID, NAZWISKO, IMIE, DATA_URODZENIA, TELEFON, EMAIL, ADRES, PLACA FROM OSOBA INNER JOIN ADMINISTRATOR ON administrator.id = osoba.id")
        data_administratorzy = mycursor.fetchall()
        return render_template('watch_database_administrator_administratorzy.html', headings=headings_osoby+headings_administratorzy, data=data_administratorzy, variable_suma=getSalarySum(mycursor, True))

@app.route("/modify_osoba", methods=['GET', 'POST'])
def modify_osoba():
    if request.method == "POST":
        global error_message
        if 'id_osoba_zmien' and 'nazwisko_osoba_zmien' and 'imie_osoba_zmien' and 'dataur_osoba_zmien' and 'telefon_osoba_zmien' and 'email_osoba_zmien' and 'adres_osoba_zmien' in request.form:
            id = request.form['id_osoba_zmien']
            nazwisko = request.form['nazwisko_osoba_zmien']
            imie = request.form['imie_osoba_zmien']
            data_ur = request.form['dataur_osoba_zmien']
            telefon = request.form['telefon_osoba_zmien']
            email = request.form['email_osoba_zmien']
            adres = request.form['adres_osoba_zmien']

            tmp = update.osoba(id,nazwisko,imie, data_ur, telefon, email, adres)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()

            return render_template('index.html')
        elif 'nazwisko_osoba_dodaj' and 'imie_osoba_dodaj' and 'dataur_osoba_dodaj' and 'telefon_osoba_dodaj' and 'email_osoba_dodaj' and 'adres_osoba_dodaj' in request.form:
            nazwisko = request.form['nazwisko_osoba_dodaj']
            imie = request.form['imie_osoba_dodaj']
            data_ur = request.form['dataur_osoba_dodaj']
            telefon = request.form['telefon_osoba_dodaj']
            email = request.form['email_osoba_dodaj']
            adres = request.form['adres_osoba_dodaj']

            tmp = insert.osoba(nazwisko, imie, data_ur, telefon, email, adres)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()
            return render_template('index.html')
        elif 'id_osoba_usun' in request.form:
            id = request.form['id_osoba_usun']

            tmp = delete.osoba(id)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()
            return render_template('index.html')
        else:
            return render_template('modyfikacja_listy_osob.html')
    else:
       return render_template('modyfikacja_listy_osob.html')

@app.route("/modify_administrator", methods=['GET', 'POST'])
def modify_administrator():
    if request.method == "POST":
        global error_message
        if 'id_administrator_zmien' and 'placa_administrator_zmien' in request.form:
            id = request.form['id_administrator_zmien']
            placa = request.form['placa_administrator_zmien']


            tmp = update.admin(id,placa)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()

            return render_template('index.html')
        elif 'placa_administrator_dodaj' and 'nazwisko_osoba_dodaj' and 'imie_osoba_dodaj' and 'dataur_osoba_dodaj' and 'telefon_osoba_dodaj' and 'email_osoba_dodaj' and 'adres_osoba_dodaj' in request.form:
            placa = request.form['placa_administrator_dodaj']
            nazwisko = request.form['nazwisko_osoba_dodaj']
            imie = request.form['imie_osoba_dodaj']
            data_ur = request.form['dataur_osoba_dodaj']
            telefon = request.form['telefon_osoba_dodaj']
            email = request.form['email_osoba_dodaj']
            adres = request.form['adres_osoba_dodaj']

            tmp = insert.osoba(nazwisko, imie, data_ur, telefon, email, adres)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mycursor.execute(f"SELECT id from osoba WHERE nazwisko='{nazwisko}' and imie='{imie}' and telefon={telefon};")
            tmp = insert.admin(mycursor.fetchone()[0], placa)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()
            return render_template('index.html')
        elif 'id_administrator_usun' in request.form:
            id = request.form['id_administrator_usun']

            tmp = delete.admin(id)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()
            return render_template('index.html')
        else:
            return render_template('modyfikacja_listy_administratorow.html')
    else:
       return render_template('modyfikacja_listy_administratorow.html')

@app.route("/modify_farmaceuta", methods=['GET', 'POST'])
def modify_farmaceuta():
    if request.method == "POST":
        global error_message
        if 'id_farmaceuta_zmien' and 'placa_farmaceuta_zmien' and 'wyksztalcenie_farmaceuta_zmien'in request.form:
            id = request.form['id_farmaceuta_zmien']
            placa = request.form['placa_farmaceuta_zmien']
            wyksztalcenie = request.form['wyksztalcenie_farmaceuta_zmien']


            tmp = update.farmaceuta(id,placa,wyksztalcenie)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()

            return render_template('index.html')
        elif 'placa_farmaceuta_dodaj' and 'wyksztalcenie_farmaceuta_dodaj' and 'nazwisko_osoba_dodaj' and 'imie_osoba_dodaj' and 'dataur_osoba_dodaj' and 'telefon_osoba_dodaj' and 'email_osoba_dodaj' and 'adres_osoba_dodaj' in request.form:
            placa = request.form['placa_farmaceuta_dodaj']
            wyksztalcenie = request.form['wyksztalcenie_farmaceuta_dodaj']

            nazwisko = request.form['nazwisko_osoba_dodaj']
            imie = request.form['imie_osoba_dodaj']
            data_ur = request.form['dataur_osoba_dodaj']
            telefon = request.form['telefon_osoba_dodaj']
            email = request.form['email_osoba_dodaj']
            adres = request.form['adres_osoba_dodaj']

            tmp = insert.osoba(nazwisko, imie, data_ur, telefon, email, adres)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mycursor.execute(f"SELECT id from osoba WHERE nazwisko='{nazwisko}' and imie='{imie}' and telefon={telefon};")
            tmp = insert.farmaceuta(mycursor.fetchone()[0], placa, wyksztalcenie)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()
            return render_template('index.html')
        elif 'id_farmaceuta_usun' in request.form:
            id = request.form['id_farmaceuta_usun']

            tmp = delete.farmaceuta(id)
            if tmp != None:
                error_message = tmp
                return redirect(url_for("error"))

            mydb.commit()
            return render_template('index.html')
        else:
            return render_template('modyfikacja_listy_farmaceut.html')
    else:
       return render_template('modyfikacja_listy_farmaceut.html')


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8888)
    

