import mysql.connector
from utils import *


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
        if validateID(id): return "złe id"
        if validateGodz(godz_do): return "zła godz do"
        if validateGodz(godz_od): return "zła godz od"

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
        return self.execute(query)

    def apteka(
        self,
        nazwa,
        godz_od,
        godz_do,
        adres,
        telefon
    ):
        if validateGodz(godz_do): return "zła godz do"
        if validateGodz(godz_od): return "zła godz od"
        if validateTelephone(telefon): return "zły telefon"

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
        return self.execute(query)

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
        return self.execute(query)

    def miasto(
        self,
        nazwa,
        kod
    ):
        if validateKod(kod): return "zły kod"

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
        return self.execute(query)

    def lekarstwa(
        self,
        id_zam,
        id_lek,
        ilosc
    ):
        if validateID(id_lek): return "złe id leku"
        if validateID(id_zam): return "złe id zamówienia"

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
        return self.execute(query)

    def zamowienie(
        self,
        status,
        data_zam,
        id_klient
    ):
        if validateID(id_klient): return "złe id klienta"
        if validateDate(data_zam): return "zła data zamówienia (format dd.mm.rrrr)"

        query = f"""CALL Nowy_zakop (
            {id_klient},
            '{status}',
            '{data_zam}'
        );"""
        return self.execute(query)

    def magazyn(
        self,
        pojemnosc,
        adres,
        id_apteki,
        id_lek
    ):
        if validateID(id_lek): return "złe id leku" 
        if validateID(id_apteki): return "złe id apteki"

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
        return self.execute(query)

    def admin(
        self,
        id,
        placa
    ):
        if validateID(id): return "złe id"
        if validateSalary(placa): return "zła płaca"

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
        return self.execute(query)

    def klient(
        self,
        id,
        zakup
    ):
        if validateID(id): return "złe id"
        if validateDate(zakup): return "zła data zakupu (format dd.mm.rrrr)"

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
        return self.execute(query)

    def farmaceuta(
        self,
        id,
        placa,
        wyksztalcenie
    ):
        if validateID(id): return "złe id"
        if validateSalary(placa): return "zła płaca"

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
        return self.execute(query)

    def osoba(
        self,
        nazwisko,
        imie,
        data_ur,
        telefon,
        email,
        adres
    ):
        if validateDate(data_ur): return "zła data (format dd.mm.rrrr)"
        if validateTelephone(telefon): return "zły telefon"

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
        return self.execute(query)
    
    def execute(self, query):
        try:
            self.__cursor.execute(query)
        except:
            return "unexpected error"
            