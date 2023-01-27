def validateID(id):
    try:
        if id is None or id == "":
            return True
        if int(id)<0:
            return True
        return False
    except:
        return True

def validateSalary(salary):
    try:
        if salary is None or salary == "":
            return True
        if int(salary)<0:
            return True
        return False
    except:
        return True
    

def validateTelephone(telefon):
    try:
        if telefon is None or telefon == "":
            return True
        if len(str(telefon)) != 9:
            return True
        return False
    except:
        return True

def validateDate(date):
    try:
        if date is None or date == "":
            return False
        if date != date[:2] + "." + date[3:5] + "." + date[6:]:
            return True
        return False
    except:
        return True
    

def validateGodz(godz):
    try:
        if godz is None or godz == "":
            return False
        godz = int(godz)
        if godz<0 or godz > 24:
            return True
        return False
    except:
        return True

def validateKod(kod):
    try:
        if kod is None or kod == "":
            return False
        if kod != kod[:2] + "-" + kod[3:]:
            return True
        if len(kod) != 6:
            return True
        return False
    except:
        return True
    
def validateDay(dzien):
    try:
        if dzien not in ('pon', 'wt', 'sr', 'czw', 'pi', 'so', 'ni'):
            return True
        return False
    except:
        return True

def validateAddress(adres):
    try:
        if adres == "" or adres is None:
            return True
        return False
    except:
        return True

def getSalarySum(cursor, isAdmin):
    query = f"""SELECT Suma_plac ({isAdmin})"""
    cursor.execute(query)
    return cursor.fetchone()[0]