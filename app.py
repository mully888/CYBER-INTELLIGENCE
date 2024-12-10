from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, template_folder='templates')  # Ensure template folder is set correctly

DATABASES = [
    'databases/database1.db',
    'databases/database2.db',
    'databases/database3.db'
]

@app.route('/')
def home():
    return render_template('index.html')

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
                found_in.append(db_path.split('/')[-1])  # Extract only the database file name
            conn.close()
        except Exception as e:
            print(f"Error checking database {db_path}: {e}")
    
    if found_in:
        message = f"L'indirizzo email è stato trovato nei seguenti database: {', '.join(found_in)}."
    else:
        message = "L'indirizzo email non è stato trovato in nessun database."
    
    return render_template('result.html', email=email, message=message)
    

if __name__ == '__main__':
    app.run(debug=True)
3.
