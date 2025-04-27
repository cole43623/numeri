import requests

# Funzione per scaricare il contenuto del link e cercare la stringa
def check_string_in_url(url, string_to_check):
	try:
		# Scarica il contenuto del link
		response = requests.get(url)
		response.raise_for_status()  # Alza un'eccezione per codici di stato HTTP 4xx/5xx
	except requests.exceptions.RequestException as e:
		print(f"Errore durante il download del link: {e}")

# URL da cui scaricare il contenuto
url = 'https://it.wikipedia.org/wiki/4_(numero)'  # Sostituisci con il link desiderato

# Stringa da cercare
#string_to_check = "Per creare tu la pagin"



for k in range(999,1200):
	url = 'https://it.wikipedia.org/wiki/'+str(k)+'_(numero)'  # Sostituisci con il link desiderato
	try:
		# Scarica il contenuto del link
		response = requests.get(url)
		response.raise_for_status()  # Alza un'eccezione per codici di stato HTTP 4xx/5xx
		print(k, "ok")
	except requests.exceptions.RequestException as e:
		print(f"Errore durante il download del link: {e}")
		break
		
		
def sum_of_digits(n):
	return sum(int(d) for d in str(n))

def is_harshad(n):
	return n % sum_of_digits(n) == 0

def is_deficient(n):
	divisors = [i for i in range(1, n) if n % i == 0]
	return sum(divisors) < n

def is_nontotient(n):
	if n != 1 and n % 2:
		return True
	from math import gcd
	for x in range(1, 2*n):  # massimo fino al doppio
		count = sum(1 for i in range(1, x+1) if gcd(i, x) == 1)
		if count == n:
			return False
	return True

def is_odious(n):
	return bin(n).count('1') % 2 == 1

def is_intoccabile(n):
	"""Controlla se il numero n è intoccabile."""
	if n < 2:
		return False  # Di solito 1 non viene considerato intoccabile
	for x in range(2, n * 10):  # Cerchiamo in un intervallo abbastanza grande
		if sum(i for i in range(1, n) if n % i == 0) == n:
			return False
	return True
	
def is_malvagio(n):
	return bin(n).count('1') % 2 == 0

def is_practical(n):
	divisors = sorted([1] + [i for i in range(2, n) if n % i == 0])
	reachable = set([0])
	for d in divisors:
		reachable.update({x+d for x in reachable})
	return all(x in reachable for x in range(1, n+1))

def is_semiprime(n):
	primes = []
	for i in range(2, int(n**0.5)+2):
		while n % i == 0:
			primes.append(i)
			n //= i
	if n > 1:
		primes.append(n)
	return len(primes) == 2

def is_omirp(n):
	if not is_prime(n):
		return False
	reversed_n = int(str(n)[::-1])
	return is_prime(reversed_n) and n != reversed_n

def is_prime(n):
	if n <= 1:
		return False
	if n <= 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i * i <= n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6
	return True

def is_felice(n):
	"""Controlla se un numero è felice."""
	visti = set()
	while n != 1 and n not in visti:
		visti.add(n)
		n = sum(int(cifra)**2 for cifra in str(n))
	return n == 1

def genera_numeri_fortunati(fino_a):
	"""Genera tutti i numeri fortunati fino a 'fino_a'."""
	numeri = list(range(1, fino_a + 1, 2))  # Si parte da soli numeri dispari
	i = 1
	while i < len(numeri):
		salto = numeri[i]
		if salto >= len(numeri):
			break
		numeri = [num for idx, num in enumerate(numeri) if (idx + 1) % salto != 0]
		i += 1
	return set(numeri)

def is_fortunato(n):
	"""Controlla se un numero è fortunato."""
	fortunati = genera_numeri_fortunati(n * 2)  # Assicuriamoci di prendere abbastanza numeri
	return n in fortunati
	
def is_ulam(n):
	sequence = [1, 2]
	while sequence[-1] < n:
		next_ulam = None
		for i in range(sequence[-1]+1, n*2):
			count = 0
			seen = set()
			for a in sequence:
				if i - a in seen:
					count += 1
				seen.add(a)
			if count == 1:
				next_ulam = i
				break
		if next_ulam is None:
			break
		sequence.append(next_ulam)
	return n in sequence


def trova_terne_pitagoriche(c):
	"""Trova tutte le terne pitagoriche con ipotenusa data (versione ottimizzata)."""
	terne = []
	quad= c*c
	for a in range(1, 200000):
		b_quad = quad+ a * a
		b = math.isqrt(b_quad)
		if b * b == b_quad:
			terne.append(sorted([a, b, c]))
	for a in range(1, c):
		b_quad = quad- a * a
		b = math.isqrt(b_quad)
		if b>=a and b * b == b_quad:
			terne.append(sorted([a, b, c]))
	return terne

def convert_to_base(n, k):
	if n == 0:
		return [0]
	digits = []
	while n > 0:
		digits.append(n % k)
		n = n // k
	digits.reverse()  # perché abbiamo calcolato dal meno significativo al più significativo
	return digits

def analyze_number(n):
	print(f"\nAnalisi del numero {n}:")
	if is_harshad(n):
		print("- È Harshad (divisibile per la somma delle cifre)")
	if is_deficient(n):
		print("- È Difettivo (somma divisori propri < numero)")
	if is_nontotient(n):
		print("- È Nontotiente (non è valore di funzione totiente)")
	else:
		print("- È Totiente")
	if is_odious(n):
		print("- È Odioso (numero dispari di 1 nel binario)")
	if is_malvagio(n):
		print("- È Malvagio (numero pari di 1 nel binario)")
	if is_fortunato(n):
		print("- È Fortunato")
	if is_felice(n):
		print("- È Felice")
	if is_practical(n):
		print("- È Pratico (tutti i numeri più piccoli sono somme di divisori)")
	if is_semiprime(n):
		print("- È Semiprimo (prodotto di due primi)")
	if is_omirp(n):
		print("- È Omirp (primo che invertito è ancora primo)")
	if is_ulam(n):
		print("- È Ulam (fa parte della sequenza di Ulam)")
	if is_intoccabile(n):
		print("- È intoccabile")
	terne = trova_terne_pitagoriche(n)
	if terne:
		print(f"Terne pitagoriche con ipotenusa {n}:")
		for terna in terne:
			print(terna)
	else:
		print(f"Nessuna terna pitagorica trovata con {n}.")
	print("- E palindormo nelle basi:")
	for k in range(2, n):
		risultato = convert_to_base(n, k)
		if len(risultato)>1 and risultato==risultato[::-1]:
			#continue
			print(k, risultato)

# --- Programma principale ---
if __name__ == "__main__":
	numero = int(input("Inserisci un numero intero: "))
	analyze_number(numero)
