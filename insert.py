import mysql.connector
from validate import *


class Insert():
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
        if validateID(id): pass
        if validateGodz(godz_do): pass
        if validateGodz(godz_od): pass

        query = f"""INSERT INTO DYZUR
                (
                    DZIEN,
                    GODZ_OD,
                    GODZ_DO,
                    ID_FARMACEUTA,
                    ID_APTEKA
                )
                VALUES
                (
                    '{dzien}',
                    {godz_od},
                    {godz_do},
                    {id_farmaceuta},
                    {id_apteki}
                );"""
        self.execute(query)

    def apteka(
        self,
        nazwa,
        godz_od,
        godz_do,
        adres,
        telefon
    ):
        if validateGodz(godz_do): pass
        if validateGodz(godz_od): pass
        if validateTelephone(telefon): pass

        query = f"""INSERT INTO APTEKA
                (
                    NAZWA,
                    GODZ_OD,
                    GODZ_DO,
                    ADRES,
                    TELEFON
                )
                VALUES
                (
                    '{nazwa}',
                    {godz_od},
                    {godz_do},
                    '{adres}',
                    {telefon}
                );"""
        self.execute(query)

    def lek(
        self,
        nazwa,
        recepta
    ):
        query = f"""INSERT INTO LEK
                (
                    NAZWA,
                    RECEPTA
                )
                VALUES
                (
                    '{nazwa}',
                    {recepta}
                ); """
        self.execute(query)

    def miasto(
        self,
        nazwa,
        kod
    ):
        if validateKod(kod): pass

        query = f"""INSERT INTO MIASTO
                (
                    NAZWA,
                    KOD
                )
                VALUES
                (
                    '{nazwa}',
                    '{kod}'
                ); """
        self.execute(query)

    def lekarstwa(
        self,
        id_zam,
        id_lek,
        ilosc
    ):
        if validateID(id_lek): pass
        if validateID(id_zam): pass

        query = f"""INSERT INTO LEKARSTWA
                (
                    ILOSC,
                    ID_ZAMOWIENIE,
                    ID_LEKARSTWO
                )
                VALUES
                (
                    {ilosc},
                    {id_zam},
                    {id_lek}
                );"""
        self.execute(query)

    def zamowienie(
        self,
        status,
        data_zam,
        id_klient
    ):
        if validateID(id_klient): pass
        if validateDate(data_zam): pass

        query = f"""CALL Nowy_zakop (
            {id_klient},
            '{status}',
            '{data_zam}'
        );"""
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

        query = f"""INSERT INTO MAGAZYN
                (
                    POJEMNOSC,
                    ADRES,
                    ID_APTEKA,
                    ID_LEKARSTWO
                )
                VALUES
                (
                    {pojemnosc},
                    '{adres}',
                    {id_apteki},
                    {id_lek}
                ); """
        self.execute(query)

    def admin(
        self,
        id,
        placa
    ):
        if validateID(id): pass
        if validateID(placa): pass

        query = f"""INSERT INTO ADMINISTRATOR
                (
                    ID,
                    PLACA
                )
                VALUES
                (
                    {id},
                    {placa}
                );"""
        self.execute(query)

    def klient(
        self,
        id,
        zakup
    ):
        if validateID(id): pass
        if validateDate(zakup): pass

        query = f"""INSERT INTO KLIENT
                (
                    ID,
                    POPRZEDNI_ZAKUP
                )
                VALUES
                (
                    {id},
                    '{zakup}'
                );"""
        self.execute(query)

    def farmaceuta(
        self,
        id,
        placa,
        wyksztalcenie
    ):
        if validateID(id): pass
        if validateID(placa): pass

        query = f"""INSERT INTO FARMACEUTA
                (
                    ID,
                    PLACA,
                    WYKSZTALCENIE
                )
                VALUES
                (
                    {id},
                    {placa},
                    '{wyksztalcenie}'
                ); """
        self.execute(query)

    def osoba(
        self,
        nazwisko,
        imie,
        data_ur,
        telefon,
        email,
        adres
    ):
        if validateDate(data_ur): pass
        if validateTelephone(telefon): pass

        query = f"""INSERT INTO OSOBA
                (
                    NAZWISKO,
                    IMIE,
                    DATA_URODZENIA,
                    TELEFON,
                    EMAIL,
                    ADRES
                )
                VALUES
                (
                    '{nazwisko}',
                    '{imie}',
                    '{data_ur}',
                    {telefon},
                    '{email}',
                    '{adres}'
                ); """
        self.execute(query)
    
    def execute(self, query):
        try:
            self.__cursor.execute(query)
        except:
            pass
