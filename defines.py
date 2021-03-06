# -*- coding: utf-8 -*-
FIRST_NAME = 'fn'
LAST_NAME = 'ln'
EMAIL = 'em'
EMPLOYER = 'emp'
WORKPLACE = 'wrk'
ACCOMODATION = 'acc'
RESIDENCE = 'res'
ROOMMATE = 'rmt'
TRANSPORT = 'tra'

GENDER = 'gender'

labels = {
    FIRST_NAME :    u'krstné meno',
    LAST_NAME :     u'priezvisko',
    EMAIL :         u'email',
    EMPLOYER :      u'zamestnávateľ',
    WORKPLACE :     u'pracovisko',
    ACCOMODATION :  u'záujem o ubytovanie',
    RESIDENCE :     u'bydlisko',
    ROOMMATE:       u'spolubývajúci',
    TRANSPORT:      u'doprava',
}

MAIL_FROM = 'union@branda.sk'
MAIL_SUBJECT = u'Union Festival Zdravia 2014 "Happy a svetový" - Potvrdenie registrácie'

MAIL_TEXT = u"""
Ďakujeme za vyplnenie dotazníku a zároveň potvrdzujeme zaregistrovanie Vašich údajov do databázy potvrdených účastníkov na Union Festival Zdravia, "Happy a svetový".

Pripomíname, že festival sa koná v piatok 13. júna 2014.

Vaše registračné údaje si môžete skontrolovať tu:

Krstné meno: %(fn)s

Priezvisko: %(ln)s

Zamestnávatel: %(emp)s

Vaše Pracovisko: %(wrk)s

Doprava Ba-Malinovo-Ba: %(tra)s

Ubytovanie v hoteli Chopin: %(acc)s

Váš preferovaný spolubývajúci: %(rmt)s

Adresa Vášho trvalého bydliska: 
%(res)s

V prípade akýchkoľvek nejasností, kontaktujte prosím organizačný tím na e-mailovej adrese union@branda.sk.
Tešíme sa na Vás.

Organizačný tím
"""

ERROR_EMAIL_INVALID = u'Zadali ste nesprávny email'
ERROR_EMAIL_EXIST = u'Zadaný email bol už použitý'
ERROR_NOT_ENTERED = u'Zabudli ste vyplniť pole %s'

orderedWorkplaces = [
  'BB',
  'BD',
  'BA',
  'BR',
  'DK',
  'DS',
  'GL',
  'HU',
  'KO',
  'KE',
  'LE',
  'LM',
  'LC',
  'MA',
  'MT',
  'MI',
  'NT',
  'NZ',
  'PN',
  'PP',
  'PO',
  'PD',
  'RS',
  'RO',
  'RK',
  'SE',
  'SN',
  'SP',
  'TO',
  'TV',
  'TN',
  'TT',
  'VK',
  'VT',
  'ZV',
  'ZH',
  'ZA',
]

workplaces = {
  'BB': u'Banská Bystrica',
  'BD': u'Bardejov',
  'BA': u'Bratislava ',
  'BR': u'Brezno',
  'DK': u'Dolný Kubín',
  'DS': u'Dunajská Streda',
  'GL': u'Galanta',
  'HU': u'Humenné',
  'KO': u'Komárno',
  'KE': u'Košice',
  'LE': u'Levice',
  'LM': u'Liptovský Mikuláš',
  'LC': u'Lučenec',
  'MA': u'Malacky',
  'MT': u'Martin',
  'MI': u'Michalovce',
  'NT': u'Nitra',
  'NZ': u'Nové Zámky',
  'PN': u'Pieštany',
  'PP': u'Poprad',
  'PO': u'Prešov',
  'PD': u'Prievidza',
  'RS': u'Rimavská Sobota',
  'RO': u'Rožnava',
  'RK': u'Ružomberok',
  'SE': u'Senica',
  'SN': u'Snina',
  'SP': u'Spišská Nová Ves',
  'TO': u'Topolčany',
  'TV': u'Trebišov',
  'TN': u'Trenčín',
  'TT': u'Trnava',
  'VK': u'Velký Krtíš',
  'VT': u'Vranov nad Toplou',
  'ZV': u'Zvolen',
  'ZH': u'Žiar nad Hronom',
  'ZA': u'Žilina',   
}

workplacesWithAcc = [
  'BB', 
  'BD', 
  'BR', 
  'DK', 
  'HU', 
  'KO', 
  'KE', 
  'LE', 
  'LM', 
  'LC', 
  'MT', 
  'MI', 
  'NT', 
  'NZ', 
  'PP', 
  'PO', 
  'PD', 
  'RS', 
  'RO', 
  'RK', 
  'SE',  #presne 90 km tak este uvidime
  'SN', 
  'SP', 
  'TO', 
  'TV', 
  'TN', 
  'VK', 
  'VT', 
  'ZV', 
  'ZH', 
  'ZA', 
]

eployerLabels = {
     'UP' : u'Union poisťovňa',
     'UZP': u'Union zdravotná poisťovňa',            
}

accomodationLabels = {
     'yes' : u'áno',
     'no'  : u'bez ubytovania',
}

transportLabels = {
     'yes' : u'áno',
     'no'  : u'bez dopravy',
}
