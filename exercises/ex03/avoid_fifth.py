"""EX03 - avoid_fifth function."""

__author__: str = "730402855"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("hello"))
    print(avoid_fifth("The sentence we have here possesses E's galore!"))


def avoid_fifth(inputs: str) -> str:
    """Removes the string "e" from the given code."""
    i: int = 0
    empty_str: str = ""
    while i < len(inputs):
        if inputs[i] == "E" or inputs[i] == "e":
           i += 1
        else:
            empty_str = empty_str + inputs[i]
            i += 1
           
    return empty_str
        

if __name__ == "__main__":
    main()