import datetime

now = datetime.datetime.now()

print("Current date and time:", now)

""" print(now.year) #kuvab praeguse aasta
print(now.month) #kuvab praeguse kuu
print(now.day) #kuvab praeguse kuupäeva numbri
print(now.hour) #kuvab praeguse kellaaja
print(now.minute) #kuvab praeguse minuti
print(now.second) #kuvab praeguse sekundi

print(now.strftime("%Y-%m-%d %H:%M:%S")) #kuvab kuupäeva ja kellaaja formaadis "YYYY-MM-DD HH:MM:SS" """

weekday = now.strftime("%A") #kuvab praeguse päeva nime
print("Today is:", weekday)