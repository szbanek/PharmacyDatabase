import mysql.connector


class Delete():
    def __init__(self, cursor):
        self.__cursor = cursor

    def dyzur(
        self,
        id_farmaceuta,
        id_apteki,
        dzien
    ):
        query = f"""DELETE FROM DYZUR
                WHERE DZIEN = '{dzien}' and
                ID_FARMACEUTA = {id_farmaceuta} and
                ID_APTEKA = {id_apteki};"""
        self.__cursor.execute(query)

    def apteka(
        self,
        id
    ):
        query = f"""DELETE FROM APTEKA
                WHERE id = {id};"""
        self.__cursor.execute(query)

    def lek(
        self,
        id
    ):
        query = f"""DELETE FROM LEK
                    WHERE ID ={id}"""
        self.__cursor.execute(query)

    def miasto(
        self,
        id
    ):
        query = f"""DELETE FROM MIASTO
                WHERE id = {id}; """
        self.__cursor.execute(query)

    def lekarstwa(
        self,
        id_zam,
        id_lek
    ):
        query = f"""DELETE FROM LEKARSTWA
                WHERE ID_ZAMOWIENIE = {id_zam} and
                    ID_LEKARSTWO = {id_lek}; """
        self.__cursor.execute(query)

    def zamowienie(
        self,
        id
    ):
        query = f"""DELETE FROM ZAMOWIENIE
                WHERE id = {id} """
        self.__cursor.execute(query)

    def magazyn(
        self,
        id_apteki,
        id_lek
    ):
        query = f"""DELETE FROM MAGAZYN
                WHERE ID_APTEKA = {id_apteki} and
                    ID_LEKARSTWO = {id_lek}; """
        self.__cursor.execute(query)

    def admin(
        self,
        id
    ):
        query = f"""DELETE FROM ADMINISTRATOR
                WHERE id = {id}; """
        self.__cursor.execute(query)

    def klient(
        self,
        id
    ):
        query = f"""DELETE FROM KLIENT
                WHERE id = {id}; """
        self.__cursor.execute(query)

    def farmaceuta(
        self,
        id
    ):
        query = f"""DELETE FROM FARMACEUTA
                WHERE id = {id}; """
        self.__cursor.execute(query)

    def osoba(
        self,
        id
    ):
        query = f"""DELETE FROM OSOBA
                WHERE id = {id}; """
        self.__cursor.execute(query)
