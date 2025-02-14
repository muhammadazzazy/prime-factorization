from sympy import isprime
from sys import exit
from word2number import w2n


def main() -> None:
    print('Welcome to The Prime Factorizer!')

    error_message: str = 'Please enter a positive integer...'
    exit_message: str = 'Exiting program...'

    while True:
        try:
            user_input: str = input('Enter a number: ')

            if user_input == 'exit':
                print(exit_message)
                exit()

            if not user_input.isnumeric():
                number: int = w2n.word_to_num(user_input)
            else:
                number: int = int(user_input)

            if number <= 0:
                print(error_message)
                continue

        except ValueError:
            print(error_message)
            continue

        except KeyboardInterrupt:
            print(exit_message)
            exit()

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
            print(f'The only prime factor of {number} is {prime_factors[-1]}.')
        else:
            print(f'{number} has no prime factors!')


if __name__ == '__main__':
    main()
