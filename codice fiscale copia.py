#Creare un algoritmo per creare un codice fiscale di una persona
#i primi 15 sono relativi ai dati personali della persona (nome, cognome, age ecc)

class datiPersonali:
	def __init__(self, _nome, _cognome, _sesso, _data, _luogo):
		self.nome = _nome
		self.cognome = _cognome
		self.sesso = _sesso
		self.data = _data
		self.luogo = _luogo
		#inizializzazione della classe: costruttore dei dati gestiti dalla classe
		
	def stampa(self):
		print(self.nome, self.cognome, self.sesso, self.data, self.luogo)
		

persona = datiPersonali("Federico", "Zanoni", "M", "9/6/2002", "Bologna")
persona.stampa()
print(persona.nome)

def calcola_cf(dati):
	result = ""
	result += gestisciCognome(dati.cognome)
	result += gestisciNome(dati.nome)
	result += gestisciAnno(dati.data, dati.sesso)
	result += gestisciComune(dati.luogo)
	result += gestisciCodiceControllo(result)
	
	return result

def separa_consonanti(testo):
	testo = testo.upper()
	consonanti = ""
	vocali = ""
	for lettera in testo:
		if lettera >= 'A' and lettera <= 'Z':
			if lettera in 'AOIUE':
			#if lettera == 'A' or lettera == 'O' or lettera == 'I' or lettera == 'U' or lettera == 'E':
				vocali += lettera
			else:
				consonanti += lettera
	return consonanti, vocali

def gestisciCognome(cognome):
	c,v = separa_consonanti(cognome) #divisione della tupla in c e v
	info = c + v + "XXX"
	return info[:3]

def gestisciNome(nome):
	c,v = separa_consonanti(nome)
	
	if len(c)>3:
		c = c[0]+c[2:] #la prima, la terza e la quarta consonante
		
	info = c + v + "XXX"
	return info[:3]

def gestisciAnno(data, sesso):
	parti = data.split('/')
	
	anno = int(parti[2]) % 100
	
	mese = int(parti[1])
	tabellaMesi = "ABCDEHLMPRST"
	letteraMesi = tabellaMesi[mese-1]
	
	giorno = int(parti[0])
	if sesso == "F":
		giorno +=40
	
	car_anno = str(anno)
	if len(car_anno) < 2:
		car_anno = '0' + car_anno
	
	car_giorno = str(giorno)
	if len (car_giorno) < 2:
		car_giorno = '0' + car_giorno
	
	return car_anno + letteraMesi + car_giorno

def gestisciComune(comune):
	return "A944"

def gestisciCodiceControllo(codice_fiscale):
	return "X"

cf = calcola_cf(persona)
print("Il codice fiscale di questa persona è: ", cf)

print(separa_consonanti("Ciao mondo"))