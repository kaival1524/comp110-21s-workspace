"""An exercise in remainders and boolean logic."""

__author__ = "730402855"


logic_puzzle: int = int(input("Enter an int: "))

if logic_puzzle % 7 == 0 and logic_puzzle % 2 == 0:
    print("TAR HEELS")

else:
    if logic_puzzle % 7 == 0:
        print("HEELS")
    if logic_puzzle % 2 == 0:
        print("TAR")
    if logic_puzzle % 2 != 0 and logic_puzzle % 7 != 0:
        print("CAROLINA")
