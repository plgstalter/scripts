from sys import argv
fr_months = {1: "janvier", 2: "février", 3: "mars", 4: "avril", 5: "mai", 6: "juin", 7: "juillet", 8: "août", 9: "septembre", 10: "octobre", 11: "novembre", 12: "décembre"}
en_months= {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
it_months = {1: "gennaio", 2: "febbraio", 3: "marzo", 4: "aprile", 5: "maggio", 6: "giugno", 7: "luglio", 8: "agosto", 9: "settembre", 10: "ottobre", 11: "novembre", 12: "dicembre"}

def nice_date(date: str, language: int):
    '''
    give a date like '2021-12-03' and a language '1', return the date nicely in the required language. Here '3 décembre 2021'
    1: français
    2: english
    3: italiano
    '''
    if  date[8]== "0":
        day = date[9]
    else:
        day = date[8:]

    if  language == 1:
        return day + " " + fr_months[int(date[5:7])] + " " + date[:4]
    elif language == 2:
        if  int(day)%10 == 1:
            day += "st"
        elif int(day)%10 == 2:
            day += "nd"
        elif int(day)%10 == 3:
            day += "rd"
        else:
            day += "th"
        return day + " " + en_months[int(date[5:7])] + " " + date[:4]
    elif language == 3:
        return day + " " + it_months[int(date[5:7])] + " " + date[:4]

if  __name__ == "__main__":
    if len(argv) < 2:
        print("No!")
    elif len(argv) == 2:
        print(nice_date(argv[1], 1))
    elif len(argv) > 2:
        print(nice_date(argv[1], int(argv[2])))
