def find_pythagorean_triples(n):
    triples = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c = (a**2 + b**2) ** 0.5
            if c.is_integer() and c <= n:
                triples.append((a, b, int(c)))
    return triples

n = 20
print(find_pythagorean_triples(n)) 
#Задание 2
def generate_pascals_triangle(n):
    triangle = []
    for row in range(n):
        current_row = [1]
        if triangle:
            last_row = triangle[-1]
            current_row.extend([last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)])
            current_row.append(1)
        triangle.append(current_row)
    return triangle

n = 5
for row in generate_pascals_triangle(n):
    print(row)
#Задание 3
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            sieve[num*num : limit+1 : num] = [False] * len(sieve[num*num : limit+1 : num])
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes

primes = sieve_of_eratosthenes(1000)
print(primes)
#Задание 4 
def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

n = 250
print(f"{n} = {', '.join(map(str, prime_factors(n)))}")
#Задание 5
def is_palindrome(x):
    return str(x) == str(x)[::-1]

def find_palindromic_squares(limit):
    palindromes = []
    for i in range(1, limit + 1):
        if is_palindrome(i) and is_palindrome(i**2):
            palindromes.append(i)
    return palindromes

limit = 100
print(find_palindromic_squares(limit))
#Задание 6 
def number_to_words(n):
    units = ["", "один", "два", "три", "чотири", "п'ять", "шість", "сім", "вісім", "дев'ять"]
    teens = ["десять", "одинадцять", "дванадцять", "тринадцять", "чотирнадцять", 
             "п'ятнадцять", "шістнадцять", "сімнадцять", "вісімнадцять", "дев'ятнадцять"]
    tens = ["", "десять", "двадцять", "тридцять", "сорок", "п'ятдесят", 
            "шістдесят", "сімдесят", "вісімдесят", "дев'яносто"]
    hundreds = ["", "сто", "двісті", "триста", "чотириста", "п'ятсот", 
                "шістсот", "сімсот", "вісімсот", "дев'ятсот"]

    if n == 0:
        return "нуль"
    if n < 10:
        return units[n]
    if 10 <= n < 20:
        return teens[n - 10]
    if 20 <= n < 100:
        return tens[n // 10] + (" " + units[n % 10] if n % 10 != 0 else "")
    if 100 <= n < 1000:
        return hundreds[n // 100] + (" " + number_to_words(n % 100) if n % 100 != 0 else "")
    return "одна тисяча"

n = 123
print(number_to_words(n))
#Задание 7 
def find_twin_primes(n):
    primes = sieve_of_eratosthenes(2 * n)
    twin_primes = []
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2 and primes[i] >= n:
            twin_primes.append((primes[i], primes[i + 1]))
    return twin_primes

n = 10
print(find_twin_primes(n))
#Задание 8
def wrap_text(text, width):
    wrapped_text = []
    paragraphs = text.split("\n\n")
    for paragraph in paragraphs:
        lines = []
        words = paragraph.split()
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + 1 <= width:
                current_line += (" " + word if current_line else word)
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
        wrapped_text.append("\n".join(lines))
    return "\n\n".join(wrapped_text)

text = "Це приклад тексту, який потрібно відредагувати так, щоб його ширина становила 20 символів. Абзаци зберігаються."
n = 20
print(wrap_text(text, n))