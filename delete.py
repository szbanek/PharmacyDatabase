import mysql.connector
from validate import *


class Delete():
    def __init__(self, cursor):
        self.__cursor = cursor

    def dyzur(
        self,
        id_farmaceuta,
        id_apteki,
        dzien
    ):
        if validateID(id_apteki): pass
        if validateID(id_farmaceuta): pass

        query = f"""DELETE FROM DYZUR
                WHERE DZIEN = '{dzien}' and
                ID_FARMACEUTA = {id_farmaceuta} and
                ID_APTEKA = {id_apteki};"""
        self.execute(query)

    def apteka(
        self,
        id
    ):
        if validateID(id): pass

        query = f"""DELETE FROM APTEKA
                WHERE id = {id};"""
        self.execute(query)

    def lek(
        self,
        id
    ):
        if validateID(id): pass

        query = f"""DELETE FROM LEK
                    WHERE ID ={id}"""
        self.execute(query)

    def miasto(
        self,
        id
    ):
        if validateID(id): pass

        query = f"""DELETE FROM MIASTO
                WHERE id = {id}; """
        self.execute(query)

    def lekarstwa(
        self,
        id_zam,
        id_lek
    ):
        if validateID(id_lek): pass
        if validateID(id_zam): pass

        query = f"""DELETE FROM LEKARSTWA
                WHERE ID_ZAMOWIENIE = {id_zam} and
                    ID_LEKARSTWO = {id_lek}; """
        self.execute(query)

    def zamowienie(
        self,
        id
    ):
        if validateID(id): pass

        query = f"""DELETE FROM ZAMOWIENIE
                WHERE id = {id} """
        self.execute(query)

    def magazyn(
        self,
        id_apteki,
        id_lek
    ):
        if validateID(id_lek): pass
        if validateID(id_apteki): pass

        query = f"""DELETE FROM MAGAZYN
                WHERE ID_APTEKA = {id_apteki} and
                    ID_LEKARSTWO = {id_lek}; """
        self.execute(query)

    def admin(
        self,
        id
    ):
        if validateID(id): pass

        query = f"""DELETE FROM ADMINISTRATOR
                WHERE id = {id}; """
        self.execute(query)

    def klient(
        self,
        id
    ):
        if validateID(id): pass

        query = f"""DELETE FROM KLIENT
                WHERE id = {id}; """
        self.execute(query)

    def farmaceuta(
        self,
        id
    ):
        if validateID(id): pass

        query = f"""DELETE FROM FARMACEUTA
                WHERE id = {id}; """
        self.execute(query)

    def osoba(
        self,
        id
    ):
        if validateID(id): pass

        query = f"""DELETE FROM OSOBA
                WHERE id = {id}; """
        self.execute(query)

    def execute(self, query):
        try:
            self.__cursor.self.execute(query)
        except:
            pass
