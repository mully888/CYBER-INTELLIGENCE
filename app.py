from flask import Flask, render_template, request
import sqlite3
import mysql.connector

app = Flask(__name__, template_folder='templates')  # Ensure template folder is set correctly

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_email', methods=['POST'])
def check_email():
    
    email = request.form.get('email')
    found_in = []
    db_names = ["database1", "database2", "database3"]
    
    for database in db_names:
        try:
            # Connessione al database MariaDB
            conn = mysql.connector.connect(
                host="localhost",
                user="check_user",
            )
            cursor = conn.cursor()

            # Usa il database specificato
            cursor.execute(f"USE {database};")
            cursor.execute(f"SELECT * FROM email WHERE email = '{email}';")
            result = cursor.fetchone()
            if result:
                found_in.append(database)
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Errore durante il controllo del database for {database}: {err}")
        except:
            print("Errore")

    if found_in:
        message = f"L'indirizzo email è stato trovato nei seguenti database: {', '.join(found_in)}."
    else:
        message = "L'indirizzo email non è stato trovato in nessun database."
    
    return render_template('result.html', email=email, message=message)
    

if __name__ == '__main__':
    app.run(debug=True)
3.
