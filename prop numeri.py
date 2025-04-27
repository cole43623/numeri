import math
from sympy import factorint
def mobius(n):
	"""Calcola la funzione di Möbius μ(n)."""
	if n == 1:
		return 1
	p = 0  # Numero di fattori primi distinti
	i = 2
	while i * i <= n:
		if n % i == 0:
			if (n // i) % i == 0:
				return 0  # Fattore quadrato trovato
			p += 1
			n //= i
		else:
			i += 1
	if n > 1:
		p += 1
	return -1 if p % 2 else 1

def mertens(N):
	"""Calcola la funzione di Mertens M(N)."""
	M = 0
	for n in range(1, N + 1):
		M += mobius(n)
	return M

def sum_of_digits(n):
	return sum(int(d) for d in str(n))

def is_harshad(n):
	return n % sum_of_digits(n) == 0

def is_deficient(n, sigma):
	if sigma < n - 1:
		return 1
	if sigma == n -1:
		return 2
	if sigma == n:
		return 3
	return 4

def is_nontotient(n):
	if n != 1 and n % 2:
		return True
	from math import gcd
	for x in range(1, 2*n):  # massimo fino al doppio
		count = sum(1 for i in range(1, x+1) if gcd(i, x) == 1)
		if count == n:
			return False
	return True

def is_idoneal(n):
    """
    Verifica se un numero è idoneo (Euler's numerus idoneus).
    Un numero è idoneo se NON può essere espresso come:
    n = ab + ac + bc, con 0 < a < b < c
    e non è un quadrato perfetto.
    """

    # Lista completa dei 65 numeri idonei conosciuti (OEIS A000926)
    known_idoneals = {
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 21, 22, 24, 25, 28, 30, 33, 37, 40, 
        42, 45, 48, 57, 58, 60, 70, 72, 78, 85, 88, 93, 102, 105, 112, 120, 130, 133, 165, 168, 
        177, 190, 210, 232, 240, 253, 273, 280, 312, 330, 345, 357, 385, 408, 462, 520, 760, 840, 
        1320, 1365, 1848
    }
    
    return n in known_idoneals
	
def is_odious(n):
	return bin(n).count('1') % 2 == 1

from sympy import divisor_sigma as sigma
from functools import cache
@cache
def f(m): return sigma(m)-m
def is_intoccabile(n):
    if n < 2: return 0
    return not any(f(m) == n for m in range(1, (n-1)**2+1))

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
	return n != reversed_n and is_prime(reversed_n)

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
	terne = []
	quad= c*c
	for a in range(1, c):
		b_quad = quad- a * a
		b = math.isqrt(b_quad)
		if b>=a and b * b == b_quad:
			terne.append(sorted([a, b, c]))
	for a in range(1, 200000):
		b_quad = quad+ a * a
		b = math.isqrt(b_quad)
		if b * b == b_quad:
			terne.append(sorted([a, b, c]))
	return terne

def convert_to_base(n, k):
	if n == 0:
		return [0]
	digits = []
	while n > 0:
		digits.append(n % k)
		n = n // k
	digits.reverse()
	return digits

def is_potente(n):
	return n == 1 or min(factorint(n).values()) > 1

def phi(N):
    """Calcola la funzione Totient di Eulero φ(N)."""
    result = N
    p = 2
    while p * p <= N:
        if N % p == 0:
            while N % p == 0:
                N //= p
            result -= result // p
        p += 1
    if N > 1:
        result -= result // N
    return result

def is_kaprekar(n):
    m=1
    return (N:=n**2)and any(n==sum(divmod(N, m:=m*10))!=m for _ in str(N))

def pi(N):
    """Restituisce il numero di numeri primi <= N (funzione π(N))."""
    if N < 2:
        return 0
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False
    return sum(is_prime)

def is_Colombian(n):
    if n < 30:
        return (n < 10 and n % 2 == 1) or n == 20
    qd = 1 + int(math.log10(n))
    r = 1 + (n - 1) % 9
    h = (r + 9 * (r % 2)) // 2
    ld = 10
    while h + 9 * qd >= n % ld:
        ld *= 10
    vs = sum(int(d) for d in str(n // ld))
    n %= ld
    for i in range(qd + 1):
        if vs + sum(int(d) for d in str(n - h - 9 * i)) == h + 9 * i:
            return False
    return True

divisori = []

def trova_divisori(N):
    global divisori
    divisori.clear()
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            divisori.append(i)
            if i != N // i:
                divisori.append(N // i)
    divisori.sort()

def is_prime_or_semiprime(N):
    """Restituisce True se N è primo o semi-primo."""
    if N < 2:
        return False

    # Check if N is prime
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    if is_prime(N):
        return True

    # Check if N is semi-prime
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            if is_prime(i) and is_prime(N // i):
                return True

    return False

def analyze_number(n):
	global divisori
	divisori = [i for i in range(1, n+1) if n % i == 0]
	print(f"\nAnalisi del numero {n}:")
	if n%2:
		print("- È un numero dispari.")
	else:
		print("- È un numero pari.")
	print(f"Divisori di {n}:", divisori)
	match is_deficient(n, sum(divisori)-n):
		case 1:
			print("- È Difettivo (somma divisori propri < numero)  ",sum(divisori)-n,"<",n)
		case 2:
			print("- È Lievemente difettivo (somma divisori propri = numero -1)  ",n-1,"=",n,"-1")
		case 3:
			print("- È perfetto (somma divisori propri = numero)  ",n,"=",n)
		case 4:
			print("- È abbondante (somma divisori propri > numero)  ",sum(divisori)-n,">",n)
	print(f"Phi({n}) =", phi(n))
	print(f"Tau({n}) =", len(divisori))
	print(f"Sigma({n}) =", sum(divisori))
	print(f"π({n}) =", pi(n))
	print(f"Mobius μ({n}) =", mobius(n))
	print(f"Mertens M({n}) =", mertens(n))
	if len(divisori)==2:
		print("- È primo")
		if is_prime_or_semiprime(n+2):
			print("\t- È un numero primo di Chen.")
		if is_prime(2*n+1):
			print("\t- È un numero primo di Sophie Germain.")
	elif len(divisori)==4:
		print("- È Semiprimo (prodotto di due primi)")
	if is_harshad(n):
		print("- È Harshad (divisibile per la somma delle cifre)")
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
	if is_potente(n):
		print("- È un numero potente.")
	if is_practical(n):
		print("- È Pratico (tutti i numeri più piccoli sono somme di divisori)")
	if is_kaprekar(n):
		print("- È un numero di Kaprekar.")
	if is_Colombian(n):
		print("- È un numero colombiano nel sistema numerico decimale.")
	if is_omirp(n):
		print("- È Omirp (primo che invertito è ancora primo)")
	if is_ulam(n):
		print("- È Ulam (fa parte della sequenza di Ulam)")
	if is_intoccabile(n):
		print("- È intoccabile")
	print("- E palindormo nelle basi:")
	for k in range(2, n):
		risultato = convert_to_base(n, k)
		if risultato==risultato[::-1]:
			print(k, risultato)
	terne = trova_terne_pitagoriche(n)
	if terne:
		print(f"- Terne pitagoriche con {n}:")
		for terna in terne:
			print(terna)
	else:
		print(f"- Nessuna terna pitagorica trovata con {n}.")


# --- Programma principale ---
if __name__ == "__main__":
	numero = int(input("Inserisci un numero intero: "))
	analyze_number(numero)
