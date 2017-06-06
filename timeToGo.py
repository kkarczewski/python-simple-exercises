import datetime

def find_time_to_go(date):
    eve = datetime.datetime(2017, 12, 24, 0, 0)
    days = eve - date
# PROSTE ROZWIĄZANIE PROBLEMU W PRZYPADKU GDY DATA JEST PO WIGILII
#    if (days.days < 0):
#        eve = eve.replace(eve.year +1)
#        days = eve - date
    return days

# REKURENCYJNE GDZIE JEŚLI DATA JEST PO WIGILII DODAJEMY ROK DO DATY
def find_time_to_go_rec(date1, date2):
    temp = date2 - date1
    if (temp.days < 0):
        date2 = date2.replace(date2.year +1)
        return find_time_to_go_rec(date1, date2)
    else:
        return temp

if __name__ == '__main__':
    # TEST DLA DZISIAJ/NOW() replacem usuwam mikrosekundy
    today = datetime.datetime.now().replace(microsecond=0)
    time_to_go = find_time_to_go(today)
    print("Dla bieżącej daty:", time_to_go)
    
    # TEST DLA DATY PO WIGILII - NIE OBSŁUŻONY SCENARIUSZ
    choosen_one = datetime.datetime(2017,12,25,0,0)
    time_to_go = find_time_to_go(choosen_one)
    print("Dla daty", choosen_one, ":", time_to_go)

    # TEST DLA REKURENCJI - OBSŁUŻONY PRZYPADEK
    eve = datetime.datetime(2017, 12, 24, 0, 0)
    choosen_two = datetime.datetime(2017,6,24,11,0)
    time_to_go_rec = find_time_to_go_rec(choosen_two, eve)
    print("Do kolejnej wigilii zostało:", time_to_go_rec)

    # TEST REKURENCJI DLA DATY DZISIEJSZEJ replacem usuwam mikrosekundy
    today = datetime.datetime.now().replace(microsecond=0)
    eve = datetime.datetime(2017, 12, 24, 0, 0)
    time_to_go_rec = find_time_to_go_rec(today, eve)
    print("Do kolejnej wigilii zostało:", time_to_go_rec)
