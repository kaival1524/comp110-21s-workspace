"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730402855"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    x: str = fortune_cookie()
    print(x)
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Returns a single, random fortune string."""
    random_fortune_message: int = int(randint(1, 4))
    if random_fortune_message <= 2:
        if random_fortune_message == 1:
            return "You will meet an old friend today."
        else:
            return "Today, you will be a pleasant surprise!"
    else:
        if random_fortune_message <= 3:
            return "Good things will come for those who wait."
        else:
            return "Be careful what you wish for, it might come true."


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 


if __name__ == "__main__":
    main()
