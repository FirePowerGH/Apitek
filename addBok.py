import requests
import mysql.connector
from dotenv import load_dotenv
from os import getenv
import re

load_dotenv()

sqlConfig = {
    "host": getenv("sqlHost"),
    "user": getenv("sqlUser"),
    "password": getenv("sqlPass"),
    "database": getenv("sqlDb")
}

def getBook():

    #on+earth+were+briefly+gorgeous
    rawQuery = input("Skriv navnet på en bok.\n")

    query = re.sub(r'\s', '+', rawQuery).lower()

    response = requests.get(f"https://openlibrary.org/search.json?title={query}&fields=title,author_name&lang=en&limit=1")
    if response.status_code == 200:
        print(response.json(), "\n")
        tittel = response.json()["docs"][0]["title"]
        forf = response.json()["docs"][0]["author_name"][0]
        print(f"{tittel} er laget av {forf}")
    else:
        print(f"Noe gikk galt: {response.status_code}")

def insertIntoDb(data):
    try:
        db = mysql.connector.connect(**sqlConfig)
        cursor = db.cursor()
    except mysql.connector.Error as e:
        db = None
        return(f"Error: {e}")
    finally:
        if db != None and db.is_connected():
            cursor.close()
            db.close()

getBook()