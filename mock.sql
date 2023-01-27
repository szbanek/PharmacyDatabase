INSERT INTO OSOBA
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
                    'Abacki',
                    'Adam',
                    '10.10.2010',
                    123123123,
                    'abacki@gmail.com',
                    'Adamska 1'
                ),
                (
                    'Babacki',
                    'Bartosz',
                    '11.11.2011',
                    231231231,
                    '',
                    'Bartoszewska 1'
                ),
                (
                    'Cabacki',
                    'Cokolwiek',
                    '12.12.2012',
                    312312312,
                    '',
                    ''
                ),
                (
                    'Cabacki2',
                    'Cokolwiek',
                    '12.12.2012',
                    312312312,
                    '',
                    ''
                ),
                (
                    'Cabacki3',
                    'Cokolwiek',
                    '12.12.2012',
                    312312312,
                    '',
                    ''
                ),
                (
                    'Cabacki4',
                    'Cokolwiek',
                    '12.12.2012',
                    312312312,
                    '',
                    ''
                ); 

INSERT INTO ADMINISTRATOR
                (
                    ID,
                    PLACA
                )
                VALUES
                (
                    1,
                    99999
                );

INSERT INTO FARMACEUTA
                (
                    ID,
                    PLACA,
                    WYKSZTALCENIE
                )
                VALUES
                (
                    2,
                    123,
                    ''
                ),
                (
                    3,
                    5000,
                    ''
                );

INSERT INTO KLIENT
                (
                    ID,
                    POPRZEDNI_ZAKUP
                )
                VALUES
                (
                    4,
                    ''
                ),
                (
                    5,
                    '10.10.2022'
                ),
                (
                    6,
                    ''
                );

INSERT INTO APTEKA
                (
                    NAZWA,
                    GODZ_OD,
                    GODZ_DO,
                    ADRES,
                    TELEFON
                )
                VALUES
                (
                    'Słoneczko',
                    9,
                    23,
                    'Miodowa 10',
                    111222333
                ),
                (
                    'apteka',
                    6,
                    15,
                    'Poznańska 1',
                    333222333
                );

INSERT INTO DYZUR
                (
                    DZIEN,
                    GODZ_OD,
                    GODZ_DO,
                    ID_FARMACEUTA,
                    ID_APTEKA
                )
                VALUES
                (
                    'pon',
                    10,
                    12,
                    2,
                    1
                );

INSERT INTO LEK
                (
                    NAZWA,
                    RECEPTA
                )
                VALUES
                (
                    'apap',
                    false
                );

CALL Nowy_zakop (
            4,
            'do wysłania',
            '10.10.2023'
        );

INSERT INTO LEKARSTWA
                (
                    ILOSC,
                    ID_ZAMOWIENIE,
                    ID_LEKARSTWO
                )
                VALUES
                (
                    10,
                    1,
                    1
                );

INSERT INTO MAGAZYN
                (
                    POJEMNOSC,
                    ADRES,
                    ID_APTEKA,
                    ID_LEKARSTWO
                )
                VALUES
                (
                    100,
                    'Kwiatowa 10',
                    1,
                    1
                );