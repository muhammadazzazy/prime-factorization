from sympy import isprime
from sys import exit


def main() -> None:
    print('Welcome to The Prime Factorizer!')

    while True:
        user_input: str = input('Enter a number: ')

        if user_input == 'exit':
            print('Thanks for trying my program!')
            exit()

        if not user_input.isnumeric():
            print('Enter a whole number!')
            continue

        else:
            number: int = int(user_input)
            prime_factors = [i for i in range(
                number+1) if isprime(i) and number % i == 0]
            if prime_factors != [] and len(prime_factors) > 1:
                output: str = f'The prime factors of {number} are '
                for prime_factor in prime_factors:
                    if prime_factors.index(prime_factor) != len(prime_factors)-1:
                        output += (str(prime_factor) + ', ')
                    else:
                        output += (str(prime_factor) + '.')
                print(output)
            elif len(prime_factors) == 1:
                print(f'The only prime factor of {
                      number} is {prime_factors[-1]}.')
            else:
                print(f'{number} has no prime factors!')


if __name__ == '__main__':
    main()
