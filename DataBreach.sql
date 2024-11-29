CREATE DATABASE DataBreach;
USE DataBreach;

CREATE TABLE utenti (
ID_utente VARCHAR (30) PRIMARY KEY,
nome VARCHAR(20) NOT NULL,
cognome VARCHAR(20) NOT NULL)
ENGINE = InnoDB

CREATE TABLE emails(
indirizzo VARCHAR(30) PRIMARY KEY,
passcode VARCHAR(30),
FOREIGN KEY (ID_utente) REFERENCES utenti (ID_utente))
ENGINE = InnoDB
ENGINE = InnoDB