from flask import Flask, request, jsonify
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
def main(bokID):
    try:
        db = mysql.connector.connect(**sqlConfig)
        cursor = db.cursor()

        query = "SELECT * FROM boker WHERE id = %s;"
    
        cursor.execute(query, (bokID, ))
        data = cursor.fetchall()
    except mysql.connector.Error as e:
        db = None
        return(f"Error: {e}")
    finally:
        if db != None and db.is_connected():
            cursor.close()
            db.close()
    return data

class Database:
    def __init__(self):
        pass

    def getBooksFromDb(bokID):
        try:
            db = mysql.connector.connect(**sqlConfig)
            cursor = db.cursor()

            query = "SELECT * FROM boker WHERE id = %s;"

            cursor.execute(query, (bokID, ))
            data = cursor.fetchall()
        except mysql.connector.Error as e:
            db = None
            return(f"Error: {e}")
        finally:
            if db != None and db.is_connected():
                cursor.close()
                db.close()
        return data
    
    def fetchNames():
        try:
            q = '%' + request.args.get('q', '') + '%'
            print(q)
            db = mysql.connector.connect(**sqlConfig)
            cursor = db.cursor()

            query = "SELECT fornavn, etternavn FROM elever WHERE fornavn LIKE %s OR etternavn LIKE %s LIMIT 3;"

            cursor.execute(query, (q, q,))
            # data = [row[0] for row in cursor.fetchall()]
            data = cursor.fetchall()
        except mysql.connector.Error as e:
            db = None
            return(f"Error: {e}")
        finally:
            if db != None and db.is_connected():
                cursor.close()
                db.close()
        return jsonify(data)