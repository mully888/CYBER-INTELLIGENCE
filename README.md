# CYBER-INTELLIGENCE
# Project Description
CYBER-INTELLIGENCE is an application designed to verify if credentials, such as emails and passwords, have been compromised in data breaches. By leveraging a database containing information about known breaches, the system enables users to securely and efficiently check the status of their credentials.

Key Features
Secure database queries to check compromised emails and passwords.
Simple and user-friendly interface.
Regular updates to the database with the latest breach information.
Technologies Used
Languages: Python, HTML
Database: MySQL (or specify the actual one used)
Tools: Wordlist TLD

Getting Started
Clone the repository:
git clone https://github.com/mully888/CYBER-INTELLIGENCE  
Install the required dependencies.
Configure the database with access credentials and load breach data.

Start the application:
python app.py  
# How it works
Our code is built with MariaDB, a popular relational database. To use the application, you need to have a MariaDB database similar to the "collection" database, containing email and password data that may have been compromised in breaches.

Database Setup:
Ensure your database has tables with emails and passwords stored securely.

Loading Data into app.py:
The data from the MariaDB database must be loaded into the app.py file. This enables the application to access and query the stored credentials.

Verification:
Once the data is loaded, the application will compare the entered credentials with the ones in the database. Results are then displayed within the HTML interface.

Contributors:
Tozzi
Tresoldi
Mulas
Tiretta
Bottaro

