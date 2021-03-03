"""EX03 - prime functions."""

__author__: str = "YOUR PID HERE"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(3))
    print(is_prime(6))
    print(is_prime(31))
    print(is_prime(110))
    print(list_primes(3, 7))
    print(list_primes(10, 20))
    print(list_primes(25, 28))
    print(list_primes(-1, 5))


def is_prime(a: int) -> bool:
    i: int = 1
    while (a - 2) > i:
        if (a % (i + 1)) == 0:
            return False
        else:
            i += 1
    if a <= 1:
        return False

    return True


def list_primes(a: int, b: int) -> list[int]:
    c: list[int]
    c = []
    i: int = 0
    while a < b:
        if is_prime(a) == True:
           c.append(a)
           a += 1
           i += 1
        else:
            a += 1
            i += 1

    return c


if __name__ == "__main__":
    main()