from sympy import isprime

print('This program finds all the prime factors of a number!')

prompt = 'Enter a number: '
user_input = input(prompt)

if user_input.isnumeric():
    number = int(user_input)
    while number <= 0:
        user_input = input(prompt)
        if user_input.isnumeric():
            number = int(user_input)
        else:
            break

while not user_input.isnumeric():
    user_input = input(prompt)
    if user_input.isnumeric():
        number = int(user_input)
        while number <= 0:
            user_input = input(prompt)
            if user_input.isnumeric():
                number = int(user_input)
            else:
                break

prime_factors = [i for i in range(number) if isprime(i) and number % i == 0]

if prime_factors != []:
    output = f'The prime factors of {number} are '
    for prime_factor in prime_factors:
        if prime_factors.index(prime_factor) != len(prime_factors)-1:
            output += (str(prime_factor) + ', ')
        else:
            output += (str(prime_factor) + '.')
    print(output)
else:
    print(f'{number} has no prime factors!')
