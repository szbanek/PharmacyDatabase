import mysql.connector
from utils import validateID


class Delete():
    def __init__(self, cursor):
        self.__cursor = cursor

    def dyzur(
        self,
        id_farmaceuta,
        id_apteki,
        dzien
    ):
        if validateID(id_apteki): return "złe id apteki"
        if validateID(id_farmaceuta): return "złe id farmaceuty"

        query = f"""DELETE FROM DYZUR
                WHERE DZIEN = '{dzien}' and
                ID_FARMACEUTA = {id_farmaceuta} and
                ID_APTEKA = {id_apteki};"""
        return self.execute(query)

    def apteka(
        self,
        id
    ):
        if validateID(id): return "złe id"

        query = f"""DELETE FROM APTEKA
                WHERE id = {id};"""
        return self.execute(query)

    def lek(
        self,
        id
    ):
        if validateID(id): return "złe id"

        query = f"""DELETE FROM LEK
                    WHERE ID ={id}"""
        return self.execute(query)

    def miasto(
        self,
        id
    ):
        if validateID(id): return "złe id"

        query = f"""DELETE FROM MIASTO
                WHERE id = {id}; """
        return self.execute(query)

    def lekarstwa(
        self,
        id_zam,
        id_lek
    ):
        if validateID(id_lek): return "złe id leku"
        if validateID(id_zam): return "złe id zamówienia"

        query = f"""DELETE FROM LEKARSTWA
                WHERE ID_ZAMOWIENIE = {id_zam} and
                    ID_LEKARSTWO = {id_lek}; """
        return self.execute(query)

    def zamowienie(
        self,
        id
    ):
        if validateID(id): return "złe id"

        query = f"""DELETE FROM ZAMOWIENIE
                WHERE id = {id} """
        return self.execute(query)

    def magazyn(
        self,
        id_apteki,
        id_lek
    ):
        if validateID(id_lek): return "złe id leku"
        if validateID(id_apteki): return "złe id apteki"

        query = f"""DELETE FROM MAGAZYN
                WHERE ID_APTEKA = {id_apteki} and
                    ID_LEKARSTWO = {id_lek}; """
        return self.execute(query)

    def admin(
        self,
        id
    ):
        if validateID(id): return "złe id"

        query = f"""DELETE FROM ADMINISTRATOR
                WHERE id = {id}; """
        return self.execute(query)

    def klient(
        self,
        id
    ):
        if validateID(id): return "złe id"

        query = f"""DELETE FROM KLIENT
                WHERE id = {id}; """
        return self.execute(query)

    def farmaceuta(
        self,
        id
    ):
        if validateID(id): return "złe id"

        query = f"""DELETE FROM FARMACEUTA
                WHERE id = {id}; """
        return self.execute(query)

    def osoba(
        self,
        id
    ):
        if validateID(id): return "złe id"

        query = f"""DELETE FROM OSOBA
                WHERE id = {id}; """
        return self.execute(query)

    def execute(self, query):
        try:
            self.__cursor.execute(query)
        except mysql.connector.Error as err:
                return err.msg
        except:
            return "unexpected error"
