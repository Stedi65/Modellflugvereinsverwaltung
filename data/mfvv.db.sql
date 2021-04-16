BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "users" (
	"nummer"	INTEGER NOT NULL,
	"name"	TEXT,
	"vorname"	TEXT,
	"alias"	TEXT,
	"password"	TEXT,
	"email"	TEXT,
	"frage1"	TEXT,
	"rechte"	TEXT
);
CREATE TABLE IF NOT EXISTS "mitglieder" (
	"nummer"	INTEGER NOT NULL UNIQUE,
	"anrede"	TEXT,
	"vorname"	TEXT,
	"name"	TEXT,
	"strasse"	TEXT,
	"plz"	TEXT,
	"ort"	TEXT,
	"telefon"	TEXT,
	"mobiltel"	TEXT,
	"email"	TEXT,
	"geburtstag"	TEXT,
	"geb_anzeigen"	INTEGER,
	"austritt"	TEXT,
	"gestorben"	TEXT,
	"beitrag"	REAL,
	"versicherungsbeitrag"	REAL,
	"IBAN"	TEXT,
	"BIC"	TEXT,
	"funktion"	TEXT,
	"foto"	TEXT,
	"kenntnisnachweisnr"	TEXT,
	"kenntnisnachweisdatum"	TEXT,
	"kenntnisnachweisgueltig"	TEXT,
	"DMFVnummer"	TEXT,
	PRIMARY KEY("nummer" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "verein" (
	"vereinsname"	TEXT,
	"strasse"	TEXT,
	"postfach"	TEXT,
	"plz"	TEXT,
	"ort"	TEXT,
	"telefon"	TEXT,
	"internet"	TEXT,
	"email"	TEXT,
	"datum_gruendung"	TEXT,
	"vereinsregisternr"	TEXT,
	"registergericht"	TEXT,
	"finanzamt"	TEXT,
	"iban1"	TEXT,
	"bic1"	TEXT,
	"bank1"	TEXT,
	"iban2"	TEXT,
	"bic2"	TEXT,
	"bank2"	TEXT
);
CREATE TABLE IF NOT EXISTS "vorstand" (
	"funktion"	TEXT,
	"datum_von"	TEXT,
	"datum_bis"	TEXT,
	"mitgliednummer"	INTEGER
);
CREATE TABLE IF NOT EXISTS "flugmodelle" (
	"modellnummer"	INTEGER NOT NULL UNIQUE,
	"mitgliednummer"	INTEGER,
	"modellname"	TEXT,
	"modelltyp"	TEXT,
	"antrieb"	TEXT,
	"spannweite"	REAL,
	"gewicht"	REAL,
	"motortyp"	TEXT,
	"hubraum"	REAL,
	"laermpassnummer"	INTEGER,
	"luftschraube"	TEXT,
	"material"	TEXT,
	"schalldaempfer"	TEXT,
	PRIMARY KEY("modellnummer" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "beitrag" (
	"beitragnr"	INTEGER NOT NULL UNIQUE,
	"datum"	TEXT,
	"gueltig"	INTEGER,
	"beitrag"	REAL,
	"versicherung1"	REAL,
	"versicherung2"	REAL,
	"versicherung3"	REAL,
	PRIMARY KEY("beitragnr" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "beitraggruppen" (
	"gruppe"	TEXT,
	"faktor"	REAL,
	"datum"	TEXT
);
CREATE TABLE IF NOT EXISTS "dokumente" (
	"doc_nummer"	INTEGER NOT NULL UNIQUE,
	"type"	TEXT,
	"dokumentname"	TEXT,
	"dateiname"	TEXT,
	"mitgliedsnummer"	INTEGER,
	PRIMARY KEY("doc_nummer" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "buchungen" (
	"nummer"	INTEGER NOT NULL UNIQUE,
	"buchungstext"	TEXT,
	"buchungsdatum"	TEXT,
	"konto"	TEXT,
	"sollhaben"	TEXT,
	"betrag"	REAL,
	"gegenkonto"	TEXT,
	"einnahmeausgabe"	TEXT,
	PRIMARY KEY("nummer" AUTOINCREMENT)
);
COMMIT;
