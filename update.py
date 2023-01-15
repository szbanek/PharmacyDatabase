import mysql.connector
from validate import *

class Update():
    def __init__(self, cursor):
        self.__cursor = cursor

    def dyzur(
        self,
        id_farmaceuta,
        id_apteki,
        dzien,
        godz_od,
        godz_do
    ):
        if validateID(id_apteki): pass
        if validateID(id_farmaceuta): pass
        if validateGodz(godz_do): pass
        if validateGodz(godz_od): pass

        query = f"""UPDATE DYZUR
                SET godz_od = {godz_od},
                    godz_do = {godz_do}
                WHERE DZIEN = '{dzien}' and
                ID_FARMACEUTA = {id_farmaceuta} and
                ID_APTEKA = {id_apteki};"""
        self.execute(query)

    def apteka(
        self,
        id,
        nazwa,
        godz_od,
        godz_do,
        adres,
        telefon
    ):
        if validateID(id): pass
        if validateGodz(godz_do): pass
        if validateGodz(godz_od): pass
        if validateTelephone(telefon): pass

        query = f"""UPDATE APTEKA
                SET nazwa = '{nazwa}',
                    godz_od = {godz_od},
                    godz_do = {godz_do},
                    adres = '{adres}',
                    telefon = {telefon}
                WHERE id = {id};"""
        self.execute(query)

    def lek(
        self,
        id,
        nazwa,
        recepta
    ):
        if validateID(id): pass

        query = f"""UPDATE LEK
                    SET NAZWA = '{nazwa}',
                    RECEPTA = {recepta}
                    WHERE ID ={id}"""
        self.execute(query)

    def miasto(
        self,
        id,
        nazwa,
        kod
    ):
        if validateID(id): pass
        if validateKod(kod): pass

        query = f"""UPDATE MIASTO
                SET nazwa = '{nazwa}',
                    kod = '{kod}'
                WHERE id = {id}; """
        self.execute(query)

    def lekarstwa(
        self,
        id_zam,
        id_lek,
        ilosc
    ):
        if validateID(id_zam): pass
        if validateID(id_lek): pass
        
        query = f"""UPDATE LEKARSTWA
                SET ilosc = {ilosc},
                WHERE ID_ZAMOWIENIE = {id_zam} and
                    ID_LEKARSTWO = {id_lek}; """
        self.execute(query)

    def zamowienie(
        self,
        id,
        status,
        data_zam,
        id_klient
    ):
        if validateID(id): pass
        if validateID(id_klient): pass
        if validateDate(data_zam): pass
        
        query = f"""UPDATE ZAMOWIENIE
                SET status '{status}',
                    DATA_ZAMOWIENIA = '{data_zam}',
                    ID_KLIENT = {id_klient}
                WHERE id = {id} """
        self.execute(query)

    def magazyn(
        self,
        pojemnosc,
        adres,
        id_apteki,
        id_lek
    ):
        if validateID(id_lek): pass
        if validateID(id_apteki): pass

        query = f"""UPDATE MAGAZYN
                SET POJEMNOSC = {pojemnosc},
                    ADRES = '{adres}',
                WHERE ID_APTEKA = {id_apteki} and
                    ID_LEKARSTWO = {id_lek}; """
        self.execute(query)

    def admin(
        self,
        id,
        placa
    ):
        if validateID(id): pass
        if validateID(placa): pass

        query = f"""UPDATE ADMINISTRATOR
                SET placa = {placa}
                WHERE id = {id}; """
        self.execute(query)

    def klient(
        self,
        id,
        zakup
    ):
        if validateID(id): pass
        if validateDate(zakup): pass

        query = f"""UPDATE KLIENT
                SET POPRZEDNI_ZAKUP = '{zakup}'
                WHERE id = {id}; """
        self.execute(query)

    def farmaceuta(
        self,
        id,
        placa,
        wyksztalcenie
    ):
        if validateID(id): pass
        if validateID(placa): pass

        query = f"""UPDATE FARMACEUTA
                SET PLACA = {placa},
                    WYKSZTALCENIE = '{wyksztalcenie}'
                WHERE id = {id}; """
        self.execute(query)

    def osoba(
        self,
        id,
        nazwisko,
        imie,
        data_ur,
        telefon,
        email,
        adres
    ):
        if validateID(id): pass
        if validateDate(data_ur): pass
        if validateTelephone(telefon): pass

        query = f"""UPDATE OSOBA
                SET NAZWISKO = '{nazwisko}',
                    IMIE = '{imie}',
                    DATA_URODZENIA = '{data_ur}',
                    TELEFON = {telefon},
                    EMAIL = '{email}',
                    ADRES = '{adres}'
                WHERE id = {id}; """
        self.execute(query)

    def execute(self, query):
            try:
                self.__cursor.self.execute(query)
            except:
                pass