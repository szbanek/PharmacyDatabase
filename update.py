import mysql.connector
from utils import *

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
        if validateID(id_apteki): return "złe id apteki"
        if validateID(id_farmaceuta): return "złe id farmaceuty"
        if validateGodz(godz_do): return "zła godz do"
        if validateGodz(godz_od): return "zła godz od"

        query = f"""UPDATE DYZUR
                SET godz_od = {godz_od},
                    godz_do = {godz_do}
                WHERE DZIEN = '{dzien}' and
                ID_FARMACEUTA = {id_farmaceuta} and
                ID_APTEKA = {id_apteki};"""
        return self.execute(query)

    def apteka(
        self,
        id,
        nazwa,
        godz_od,
        godz_do,
        adres,
        telefon
    ):
        if validateID(id): return "złe id"
        if validateGodz(godz_do): return "zła godz do"
        if validateGodz(godz_od): return "zła godz od"
        if validateTelephone(telefon): return "zły telefon"
        if validateAddress(adres): return "podaj adres"

        query = f"""UPDATE APTEKA
                SET nazwa = '{nazwa}',
                    godz_od = {godz_od},
                    godz_do = {godz_do},
                    adres = '{adres}',
                    telefon = {telefon}
                WHERE id = {id};"""
        return self.execute(query)

    def lek(
        self,
        id,
        nazwa,
        recepta
    ):
        if validateID(id): return "złe id"

        query = f"""UPDATE LEK
                    SET NAZWA = '{nazwa}',
                    RECEPTA = {recepta}
                    WHERE ID ={id}"""
        return self.execute(query)

    def miasto(
        self,
        id,
        nazwa,
        kod
    ):
        if validateID(id): return "złe id"
        if validateKod(kod): return "zły kod"

        query = f"""UPDATE MIASTO
                SET nazwa = '{nazwa}',
                    kod = '{kod}'
                WHERE id = {id}; """
        return self.execute(query)

    def lekarstwa(
        self,
        id_zam,
        id_lek,
        ilosc
    ):
        if validateID(id_zam): return "złe id zamówienia"
        if validateID(id_lek): return "złe id leku"
        
        query = f"""UPDATE LEKARSTWA
                SET ilosc = {ilosc},
                WHERE ID_ZAMOWIENIE = {id_zam} and
                    ID_LEKARSTWO = {id_lek}; """
        return self.execute(query)

    def zamowienie(
        self,
        id,
        status,
        data_zam,
        id_klient
    ):
        if validateID(id): return "złe id"
        if validateID(id_klient): return "złe id klienta"
        if validateDate(data_zam): return "zła data (format dd.mm.rrrr)"
        
        query = f"""UPDATE ZAMOWIENIE
                SET status = '{status}',
                    DATA_ZAMOWIENIA = '{data_zam}',
                    ID_KLIENT = {id_klient}
                WHERE id = {id}; """
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

        query = f"""UPDATE MAGAZYN
                SET POJEMNOSC = {pojemnosc},
                    ADRES = '{adres}'
                WHERE ID_APTEKA = {id_apteki} and
                    ID_LEKARSTWO = {id_lek}; """
        return self.execute(query)

    def admin(
        self,
        id,
        placa
    ):
        if validateID(id): return "złe id"
        if validateSalary(placa): return "zła płaca"

        query = f"""UPDATE ADMINISTRATOR
                SET placa = {placa}
                WHERE id = {id}; """
        return self.execute(query)

    def klient(
        self,
        id,
        zakup
    ):
        if validateID(id): return "złe id"
        if validateDate(zakup): return "zła data (format dd.mm.rrrr)"

        query = f"""UPDATE KLIENT
                SET POPRZEDNI_ZAKUP = '{zakup}'
                WHERE id = {id}; """
        return self.execute(query)

    def farmaceuta(
        self,
        id,
        placa,
        wyksztalcenie
    ):
        if validateID(id): return "złe id"
        if validateSalary(placa): return "zła płaca"

        query = f"""UPDATE FARMACEUTA
                SET PLACA = {placa},
                    WYKSZTALCENIE = '{wyksztalcenie}'
                WHERE id = {id}; """
        return self.execute(query)

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
        if validateID(id): return "złe id"
        if validateDate(data_ur): return "zła data (format dd.mm.rrrr)"
        if validateTelephone(telefon): return "zły telefon"

        query = f"""UPDATE OSOBA
                SET NAZWISKO = '{nazwisko}',
                    IMIE = '{imie}',
                    DATA_URODZENIA = '{data_ur}',
                    TELEFON = {telefon},
                    EMAIL = '{email}',
                    ADRES = '{adres}'
                WHERE id = {id}; """
        return self.execute(query)

    def execute(self, query):
            try:
                self.__cursor.execute(query)
            except mysql.connector.Error as err:
                return err.msg
            except:
                return "unexpected error"