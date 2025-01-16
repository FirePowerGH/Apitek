from flask import Flask
import mysql.connector
from dotenv import load_dotenv
from os import getenv

load_dotenv()

sqlConfig = {
    "host": getenv("sqlHost"),
    "user": getenv("sqlUser"),
    "password": getenv("sqlPass"),
    "database": getenv("sqlDb")
}

app = Flask(__name__)

@app.route("/elev/<elevID>")
def main(elevID):
    try:
        db = mysql.connector.connect(**sqlConfig)
        cursor = db.cursor()

        query = "SELECT * FROM elever WHERE id = %s;"
    
        cursor.execute(query, (elevID, ))
        data = cursor.fetchall()
    except mysql.connector.Error as e:
        db = None
        return(f"Error: {e}")
    finally:
        if db != None and db.is_connected():
            cursor.close()
            db.close()
    return data
