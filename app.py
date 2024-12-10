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
    db_name = ["database1", "database2", "database3"]
    cont = 0
    
    try:
        # Connessione al database MariaDB
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aaaa"
        )
        cursor = conn.cursor()

        # Usa il database specificato
        cursor.execute(f"USE {db_name[cont]};")
        cursor.execute("SELECT * FROM email WHERE email = %s", (email,))
        if cursor.fetchone():
                found_in.append(db_name[cont])
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Errore durante il controllo del database {db_name[cont]}: {err}")
    cont = cont + 1



    if found_in:
        message = f"L'indirizzo email è stato trovato nei seguenti database: {', '.join(found_in)}."
    else:
        message = "L'indirizzo email non è stato trovato in nessun database."
    
    return render_template('result.html', email=email, message=message)
    

if __name__ == '__main__':
    app.run(debug=True)
3.
