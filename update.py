import mysql.connector


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
        query = f"""UPDATE DYZUR
                SET godz_od = {godz_od},
                    godz_do = {godz_do}
                WHERE DZIEN = '{dzien}' and
                ID_FARMACEUTA = {id_farmaceuta} and
                ID_APTEKA = {id_apteki};"""
        self.__cursor.execute(query)

    def apteka(
        self,
        id,
        nazwa,
        godz_od,
        godz_do,
        adres,
        telefon
    ):
        query = f"""UPDATE APTEKA
                SET nazwa = '{nazwa}',
                    godz_od = {godz_od},
                    godz_do = {godz_do},
                    adres = '{adres}',
                    telefon = {telefon}
                WHERE id = {id};"""
        self.__cursor.execute(query)

    def lek(
        self,
        id,
        nazwa,
        recepta
    ):
        query = f"""UPDATE LEK
                    SET NAZWA = '{nazwa}',
                    RECEPTA = {recepta}
                    WHERE ID ={id}"""
        self.__cursor.execute(query)

    def miasto(
        self,
        id,
        nazwa,
        kod
    ):
        query = f"""UPDATE MIASTO
                SET nazwa = '{nazwa}',
                    kod = '{kod}'
                WHERE id = {id}; """
        self.__cursor.execute(query)

    def lekarstwa(
        self,
        id_zam,
        id_lek,
        ilosc
    ):
        query = f"""UPDATE LEKARSTWA
                SET ilosc = {ilosc},
                WHERE ID_ZAMOWIENIE = {id_zam} and
                    ID_LEKARSTWO = {id_lek}; """
        self.__cursor.execute(query)

    def zamowienie(
        self,
        id,
        status,
        data_zam,
        id_klient
    ):
        query = f"""UPDATE ZAMOWIENIE
                SET status '{status}',
                    DATA_ZAMOWIENIA = '{data_zam}',
                    ID_KLIENT = {id_klient}
                WHERE id = {id} """
        self.__cursor.execute(query)

    def magazyn(
        self,
        pojemnosc,
        adres,
        id_apteki,
        id_lek
    ):
        query = f"""UPDATE MAGAZYN
                SET POJEMNOSC = {pojemnosc},
                    ADRES = '{adres}',
                WHERE ID_APTEKA = {id_apteki} and
                    ID_LEKARSTWO = {id_lek}; """
        self.__cursor.execute(query)

    def admin(
        self,
        id,
        placa
    ):
        query = f"""UPDATE ADMINISTRATOR
                SET placa = {placa}
                WHERE id = {id}; """
        self.__cursor.execute(query)

    def klient(
        self,
        id,
        zakup
    ):
        query = f"""UPDATE KLIENT
                SET POPRZEDNI_ZAKUP = '{zakup}'
                WHERE id = {id}; """
        self.__cursor.execute(query)

    def farmaceuta(
        self,
        id,
        placa,
        wyksztalcenie
    ):
        query = f"""UPDATE FARMACEUTA
                SET PLACA = {placa},
                    WYKSZTALCENIE = '{wyksztalcenie}'
                WHERE id = {id}; """
        self.__cursor.execute(query)

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
        query = f"""UPDATE OSOBA
                SET NAZWISKO = '{nazwisko}',
                    IMIE = '{imie}',
                    DATA_URODZENIA = '{data_ur}',
                    TELEFON = {telefon},
                    EMAIL = '{email}',
                    ADRES = '{adres}'
                WHERE id = {id}; """
        self.__cursor.execute(query)
