import re
import mysql.connector
import getpass
import os

def extract_emails(file_path, tlds):
    """Estrae le email valide da un file specifico."""
    emails = set()  # Per evitare duplicati 
    print(f"Processo il file: {file_path}")
    with open(file_path, 'r') as f:
        for i, line in enumerate(f, start=1):
            try:
                # Rimuovi eventuali caratteri speciali iniziali
                original_line = line.strip()
                line = line.lstrip(".;:|")

                # Trova potenziali email con regex
                potential_email = re.match(r'([\w\.-]+@[\w\.-]+\.\w+)', line)
                if potential_email:
                    email = potential_email.group(0)
                    # Verifica se il TLD è valido
                    domain_parts = email.split('.')
                    tld = '.' + domain_parts[-1].lower()
                    if tld in tlds:
                        emails.add(email)
                    else:
                        print(f"Riga {i}: TLD non valido ({tld}) - {original_line}")
                else:
                    print(f"Riga {i}: Nessuna email valida trovata - {original_line}")
            except Exception as e:
                print(f"Errore alla riga {i} del file {file_path}: {e}")

    return emails

def insert_into_db(emails, db_name, db_password):
    """Inserisce le email estratte in un database specifico."""
    try:
        # Connessione al database MariaDB
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=db_password
        )
        cursor = conn.cursor()

        # Usa il database specificato
        cursor.execute(f"USE {db_name};")
        print(f"Connessione al database {db_name} riuscita.")

        total_emails = len(emails)  # Numero totale di email
        processed_emails = 0  # Contatore delle email processate

        # Inserisci le email nella tabella (con IGNORE per evitare duplicati)
        for email in emails:
            try:
                # Query parametrizzata per prevenire SQL injection
                cursor.execute("INSERT IGNORE INTO email (email) VALUES (%s);", (email,)) 
                processed_emails += 1

                # Calcola la percentuale di completamento
                completion_percentage = (processed_emails / total_emails) * 100

                # Mostra la percentuale di completamento
                print(f"Caricamento email: {processed_emails}/{total_emails} ({completion_percentage:.2f}%)")

            except mysql.connector.Error as err:
                print(f"Errore nell'inserimento dell'email {email}: {err}")

        conn.commit()
        print(f"Inserimento completato per {db_name}.")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Errore di connessione al database {db_name}: {err}")

# Main script
if __name__ == "__main__":
    # Richiedi la password in modo sicuro
    db_password = getpass.getpass("Inserisci la password per il database MariaDB: ")

    # File di input
    file1 = r"C:/CYBER-INTELLIGENCE-main/databases/File1.txt"
    file2 = r"C:/CYBER-INTELLIGENCE-main/databases/File2.txt"
    file3 = r"C:/CYBER-INTELLIGENCE-main/databases/File3.txt"
    tld_file = r"C:/CYBER-INTELLIGENCE-main/wordlistTLD.txt"

    # Verifica che i file esistano
    for file_path in [file1, file2, file3, tld_file]:
        if not os.path.exists(file_path):
            print(f"Errore: Il file {file_path} non esiste.")
            exit(1)

    # Carica i TLD validi dal file
    with open(tld_file, 'r') as tld_f:
        tlds = set(line.strip() for line in tld_f)

    # Estrai le email da ciascun file
    emails_file1 = extract_emails(file1, tlds)
    emails_file2 = extract_emails(file2, tlds)
    emails_file3 = extract_emails(file3, tlds)

    # Inserisci le email nei rispettivi database
    insert_into_db(emails_file1, "database1", db_password)
    insert_into_db(emails_file2, "database2", db_password)
    insert_into_db(emails_file3, "database3", db_password)

    print("Operazione completata.")
