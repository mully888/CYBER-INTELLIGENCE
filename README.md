# CYBER-INTELLIGENCE
Project Description
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
How It Works
Database Integration
The application connects to a database containing details of known data breaches. This database is updated regularly to ensure comprehensive coverage of compromised credentials.

Input and Verification

Users input their email and password into the application.
The system uses secure hashing techniques to compare the provided credentials against the database without exposing sensitive information.
Results Display

If the email or password is found in the breach records, the application notifies the user of the compromise.
Recommendations are provided, such as updating passwords or activating two-factor authentication.
Backend Logic

Email Checks: Validate whether the email appears in the compromised dataset.
Password Hash Matching: Employ hashing algorithms to prevent plaintext password exposure during comparisons.
Front-End and User Experience
The front-end is designed with simplicity in mind, providing clear feedback on the security of the checked credentials.

Wordlist Tool
A supplementary wordlist tool assists in identifying common domains and potential threats, enhancing the robustness of breach checks.

Contributors:
Tozzi
Tresoldi
Mulas
Tiretta
Bottaro

