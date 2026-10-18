import datetime
from hello import say_hello

hour = datetime.datetime.now().hour
name = input("What is your first name? ")

say_hello(hour, name)

""" hour = datetime.datetime.now().hour
name = input("What is your first name? ")

def get_greeting(daytime):
    
    if daytime < 12:
        return "Good morning"
    elif daytime < 18:
        return "Good afternoon"
    else:
        return "Good evening"

#funktsiooni (nagu näiteks def) ei saa kutsuda välja ennem, kui see on kirjeldatud, kuna koodi loetakse ülevalt alla
def say_hello(daytime, first_name):
    
    
    greeting = get_greeting(daytime) #"Good morning" if hour < 12 else "Good afternoon" if hour < 18 else "Good evening"

    # if hour < 12:
    #     greeting = "Good morning"
    # elif hour < 18:
    #     greeting = "Good afternoon"
    # else:
    #     greeting = "Good evening"

    print(f"{greeting}, {name}!")

#funktsiooni väljakutsumine peab toimuma pärast selle definitsiooni, vastasel juhul tekib viga, kuna Python ei tea veel, mis on say_hello.
say_hello(hour, name) """