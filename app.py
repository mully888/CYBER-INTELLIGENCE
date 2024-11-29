#Ho bisogno che mi crei un programma in Python Il programma dovrà collegarsi ad un sito HTML e dovrà avere accesso a 3 database SQL.
#All'interno del sito HTML verrà inserito un indirizzo email. Il programma dovrà prendere quell'indirizzo e salvarselo come fosse l'input dell'utente.
#Dovrà poi controllare se quell'indirizzo email è presente in uno dei 3 database a cui ha accesso.
#Nel caso dovesse trovare quell'indirizzo email all'interno del database, il programma dovrà mostrare sul sito HTML se è stato trovato l'indirizzo email e nel caso in quale dei database è stato trovato
#I database sono salvati in una sottocartella chiamata "databases".
#Il sito HTML è salvato in una sottocartella chiamata "templates".
#I database devono essere nosql

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, template_folder='templates')
  # Ensure template folder is set correctly

DATABASES = [
    'databases/database1.db',
    'databases/database2.db',
    'databases/database3.db'
]

@app.route('/')
def home():
    return render_template('SITO.html')

@app.route('/check_email', methods=['POST'])
def check_email():
    email = request.form.get('email')
    found_in = []  # List to track which databases contain the email

    # Iterate through all databases and check for the email
    for db_path in DATABASES:
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM emails WHERE email = ?", (email,))
            if cursor.fetchone():
                found_in.append(db_path.split('/')[-1]) 
                 # Extract only the database file name
            conn.close()
        except Exception as e:
            print(f"Error checking database {db_path}: {e}")
    
    # Determine the result
    if found_in:
        message = f"L'indirizzo email è stato trovato nei seguenti database: {', '.join(found_in)}."
    else:
        message = "L'indirizzo email non è stato trovato in nessun database."
    
    return render_template('SITO.html', email=email, message=message)
def check_password():
    password = request.form.get('password')
    found_in = []  # List to track which databases contain the email

    # Iterate through all databases and check for the email
    for db_path in DATABASES:
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM emails WHERE password = ?", (password,))
            if cursor.fetchone():
                found_in.append(db_path.split('/')[-1]) 
                 # Extract only the database file name
            conn.close()
        except Exception as e:
            print(f"Error checking database {db_path}: {e}")
    
    # Determine the result
    if found_in:
        message = f"L'indirizzo email è stato trovato nei seguenti database: {', '.join(found_in)}."
    else:
        message = "L'indirizzo email non è stato trovato in nessun database."
    
    return render_template('SITO.html', email=password, message=message)

if __name__ == '__main__':
    app.run(debug=True)
3.
