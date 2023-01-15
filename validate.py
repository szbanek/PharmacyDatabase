def validateID(id):
    try:
        if int(id)<0:
            return True
        return False
    except:
        return True
    

def validateTelephone(telefon):
    try:
        if len(str(telefon)) != 9:
            return True
        return False
    except:
        return True

def validateDate(date):
    try:
        if date != date[:2] + "." + date[3:5] + "." + date[6:]:
            return True
        return False
    except:
        return True
    

def validateGodz(godz):
    try:
        godz = int(godz)
        if godz>=0 and godz <= 24:
            return True
        return False
    except:
        return True

def validateKod(kod):
    try:
        if kod != kod[:2] + "-" + kod[3:]:
            return True
        if len(kod) != 6:
            return True
        return False
    except:
        return True