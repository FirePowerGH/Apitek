import requests
import mysql.connector
from dotenv import load_dotenv
from os import getenv
from random import randint, choice
import re
import string

load_dotenv()

sqlConfig = {
    "host": getenv("sqlHost"),
    "user": getenv("sqlUser"),
    "password": getenv("sqlPass"),
    "database": getenv("sqlDb")
}

def getBook():
    rawQuery = input("Skriv navnet på en bok.\n")

    query = re.sub(r'\s', '+', rawQuery).lower()

    response = requests.get(f"https://openlibrary.org/search.json?title={query}&fields=title,author_name&lang=en&limit=1")
    print(f"Book not found.")
    if response.status_code == 200:
        data = response.json()
        insertIntoDb(data)
    else:
        print(f"Noe gikk galt: {response.status_code}")

def insertIntoDb(data):
    try:
        db = mysql.connector.connect(**sqlConfig)
        cursor = db.cursor()

        try:
            tittel = data["docs"][0]["title"]
            forf = data["docs"][0]["author_name"][0]

            tall = randint(1,32)

            if tall < 10:
                tall = "0" + str(tall)
            
            bokstav = choice(string.ascii_uppercase)

            hylle = str(tall) + bokstav

            print(f"Navn: {tittel} \nForfatter: {forf} \nHylle: {hylle}")

            query = "INSERT INTO boker (tittel, forfatter, hylle) \
                    VALUES (%s, %s, %s)"
            
            cursor.execute(query, (tittel, forf, hylle))
            db.commit()

            print(f"Successfully added {tittel} by {forf}")
        except IndexError as e:
            print(f"Book not found.")
    except mysql.connector.Error as e:
        db = None
        return(f"Error: {e}")
    finally:
        if db != None and db.is_connected():
            cursor.close()
            db.close()

getBook()