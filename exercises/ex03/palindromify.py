"""EX03 - palindromify function."""

__author__: str = "YOUR PID HERE"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time ", False))


def palindromify(a: str, b: bool) -> str:
    """Palindromify's the given string through using even and odd."""
    i: int = 0
    x: int = 1
    c: str = a + ""
    while len(a) > i and len(a) > x:
        if b == True:
            c += a[len(a) - (i + 1)]
            i += 1
        else:
            c += a[len(a) - (x + 1)]
            x += 1

    return c


if __name__ == "__main__":
    main()