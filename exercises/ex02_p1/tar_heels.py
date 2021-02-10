"""Tar Heels exercise redux as a structured program."""

__author__ = "730402855"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    x: str = tar_heels(choice)
    print(x)

def tar_heels(a: int) -> str:
    if a % 7 == 0 and a % 2 == 0:
        return "TAR HEELS"
    else:
        if a % 7 == 0:
            return "HEELS"
        if a % 2 == 0:
            return "TAR"
        else:
            return "CAROLINA"


if __name__ == "__main__":
    main()
