import mysql.connector


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
        self.__cursor.execute(query)

    def apteka(
        self,
        nazwa,
        godz_od,
        godz_do,
        adres,
        telefon
    ):
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
        self.__cursor.execute(query)

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
        self.__cursor.execute(query)

    def miasto(
        self,
        nazwa,
        kod
    ):
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
        self.__cursor.execute(query)

    def lekarstwa(
        self,
        id_zam,
        id_lek,
        ilosc
    ):
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
        self.__cursor.execute(query)

    def zamowienie(
        self,
        status,
        data_zam,
        id_klient
    ):
        query = f"""INSERT INTO ZAMOWIENIE
                (
                    STATUS,
                    DATA_ZAMOWIENIE,
                    ID_KLIENT
                )
                VALUES
                (
                    '{status}',
                    '{data_zam}',
                    {id_klient}
                );"""
        self.__cursor.execute(query)

    def magazyn(
        self,
        pojemnosc,
        adres,
        id_apteki,
        id_lek
    ):
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
        self.__cursor.execute(query)

    def admin(
        self,
        id,
        placa
    ):
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
        self.__cursor.execute(query)

    def klient(
        self,
        id,
        zakup
    ):
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
        self.__cursor.execute(query)

    def farmaceuta(
        self,
        id,
        placa,
        wyksztalcenie
    ):
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
        self.__cursor.execute(query)

    def osoba(
        self,
        nazwisko,
        imie,
        data_ur,
        telefon,
        email,
        adres
    ):
        query = f"""INSERT INTO OSOBA
                (
                    NAZWISKO,
                    IMIE,
                    DATA_URODZENIA,
                    TELEFON,
                    EMAIL,
                    ADRES
                )
                VALUS
                (
                    '{nazwisko}',
                    '{imie}',
                    '{data_ur}',
                    {telefon},
                    '{email}',
                    '{adres}'
                ); """
        self.__cursor.execute(query)
