"""This program provides the user with 3 options."""

from random import randint

"""In the first option, the user can end their experience and their total points will be tallied."""
"""In the second option, up to 2 quizzes can be administered based on the user's response."""
"""The user will either take the sith quiz or the jedi quiz first and then have the option to take the other quiz."""
"""These quizzes will allow for you to bypass the second quiz or exit the loop."""
"""Furthermore, the user's name only determines the order in which the user has to take the quizzes."""
"""Additionally, the user will also be able to enter any part of the program that they want."""
"""The third option will be very specific based on the user's name."""
"""The user will take one short guessing quiz in which their points and attempts will be tracked."""
"""The user can also access any portion of the game that they want."""
"""Overall, there are 4 different quizzes, in which the order of the quiz is determined by your name."""
"""After each question, you will be able to quit the game or go anywhere you want."""
"""All quizzes loop so you can play the game an infinite amount of times."""
"""Also, a random function is implemented in the third choice which you can access from anywhere in the game."""
"""This random function will print a random jedi quote or fact."""
"""Your points at the end of the game will be printed."""


__author__ = "730402855"


points: int = 20
player: str = str()
THINKING_FACE: str = "\U0001F914"
THUMBS_UP: str = "\U0001F44D"
WORRIED: str = "\U0001F615"


def main() -> None:
    """The entry point of the program, when run as a module."""
    greet()
    global points
    print(f"Where do you want to go next? { THINKING_FACE } Choose one of the following letters: ")
    question: str = str(input("a. End experience\nb. Take a Jedi or Sith test\nc. A fun surprise!\n"))
    while ord(question) == ord("b") or ord("c") or ord("B") or ord("C"):
        if ord(question) == ord("a") or ord(question) == ord("A"):
            points += 10
            print(f"Goodbye, you have scored { points } points!")
            exit()
        if ord(question) == ord("b") or ord(question) == ord("B"):
            if 65 <= ord(player[0]) <= 77 or 97 <= ord(player[0]) <= 109:
                print("You are now taking the Sith Knowledge Exam")
                question_01()
                question_02()
                question_03()
                question_04()
                question_05()
                jedi_quiz: str = str(input(f"Do you want to take the jedi quiz? { THINKING_FACE } : - yes/no\n"))
                if jedi_quiz == "yes":
                    question_06()
                    question_07()
                    question_08()
                    question_09()
                    question_10()
                guess_the_force3: str = str(input("Do you want to take guessing the force quiz? : - yes/no\n"))
                if guess_the_force3 == "yes":
                    points = guess_using_the_force(points)
                bounty_hunter3: str = str(input(f"Take bounty hunter quiz?{THINKING_FACE}: - yes/no\n"))
                if bounty_hunter3 == "yes":
                    points = bounty_hunters_quiz(points)
                exit_call: str = str(input(f"Do you want to end experience?  { THINKING_FACE } - yes/no\n"))
                if exit_call == "yes":
                    print(f"You ended the game with { points } points!")
                    exit()
            else:
                print("You are now taking the Jedi Knowledge Exam")
                question_06()
                question_07()
                question_08()
                question_09()
                question_10()
                sith_quiz: str = str(input(f"Do you want to take the sith quiz? - { THINKING_FACE }yes/no\n"))
                if sith_quiz == "yes":
                    question_01()
                    question_02()
                    question_03()
                    question_04()
                    question_05()
                guess_using_the_force4: str = str(input("Take the guessing the force quiz? : - yes/no\n"))
                if guess_using_the_force4 == "yes":
                    points = guess_using_the_force(points)
                bounty_hunter4: str = str(input("Take the bounty hunter quiz? { THINKING_FACE } : - yes/no\n"))
                if bounty_hunter4 == "yes":
                    points = bounty_hunters_quiz(points)
                exit_call2: str = str(input(f"Do you want to end the experience? - { THINKING_FACE }yes/no\n"))
                if exit_call2 == "yes":
                    print(f"You ended the game with { points } points!")
                    exit()
        else:
            if 65 <= ord(player[0]) <= 77 or 97 <= ord(player[0]) <= 109:
                print("You are answering a guessing related question about Star Wars.")
                points = guess_using_the_force(points)
                bounty_hunter1: str = str(input(f"Take the bounty hunter quiz? { THINKING_FACE } : - yes/no\n"))
                if bounty_hunter1 == "yes":
                    points = bounty_hunters_quiz(points)
                jedi_quiz2: str = str(input(f"Do you want to take the jedi quiz? { THINKING_FACE } : - yes/no\n"))
                if jedi_quiz2 == "yes":
                    question_06()
                    question_07()
                    question_08()
                    question_09()
                    question_10()
                sith_quiz2: str = str(input(f"Do you want to take the sith quiz? - { THINKING_FACE }yes/no\n"))
                if sith_quiz2 == "yes":
                    question_01()
                    question_02()
                    question_03()
                    question_04()
                    question_05() 
                exit_call3: str = str(input(f"Do you want to end experience?  { THINKING_FACE } - yes/no\n"))
                if exit_call3 == "yes":
                    print(f"You ended the game with { points } points!")
                    exit()
            else:
                print("You are answering a guessing related question about Star Wars.")
                points = bounty_hunters_quiz(points)
                guess_using_the_force1: str = str(input("Take the guessing the force quiz? : - yes/no\n"))
                if guess_using_the_force1 == "yes":
                    points = guess_using_the_force(points)
                jedi_quiz3: str = str(input(f"Do you want to take the jedi quiz? { THINKING_FACE } : - yes/no\n"))
                if jedi_quiz3 == "yes":
                    question_06()
                    question_07()
                    question_08()
                    question_09()
                    question_10()
                sith_quiz3: str = str(input(f"Do you want to take the sith quiz? - { THINKING_FACE }yes/no\n"))
                if sith_quiz3 == "yes":
                    question_01()
                    question_02()
                    question_03()
                    question_04()
                    question_05() 
                exit_call4: str = str(input(f"Do you want to end experience?  { THINKING_FACE } - yes/no\n"))
                if exit_call4 == "yes":
                    print(f"You ended the game with { points } points!")
                    exit()


def greet() -> None:
    """Gives context about the buzzfeed quiz game."""
    print("Welcome to Star Wars Trivia, a buzzfeed quiz which determines your knowledge of Star Wars!")
    print("In the quiz, you will be be presented with three options and be given 20 points to begin!")
    print("First, you will be able to end the quiz and be given 10 points for responding for a total of 30 points!")
    print("Second, you will take a Jedi or Sith test based on the first letter of your first name!")
    print("If your first name is between A-M, you will take the Sith test first.")
    print("N-Z will take the Jedi test first.")
    print("Each test has 5 options, and it is multiple choice. Choose the correct letter!")
    print("Your points will be displayed after each question!")
    print("Everyone will have the chance to take both quizzes, but names A-M will take the Sith quiz first.")
    print("N-Z will take the Jedi quiz first")
    print("Each correct question will be rewarded with 20 points, and a wrong response will be get 10 points!")
    print("Your points will be counted after each question.")
    print("The quiz will be in a loop so that you can take both quizzes at any time.")
    print("Also, you are able to exit the loop when you want by replying yes to the exit question when presented.")
    print("Additionally, you will also be able to jump into any part of the program that you want.")
    print("For exam, after completing the ttwo quizzes, you can also go into option A or C directly.")
    print("Third, you will answer a guessing questions related to Star Wars!")
    print("If the first letter in your first name starts between A-M, you will take a Star Wars movie guessing quiz!")
    print("A random Star Wars quote will be printed after the question!")
    print("You will begin with 0 points and will loose points with each incorrect guess.")
    print("However, when you guess correctly, 100 points will be added to your total points.")
    print("The rest will take a similar test, with a question about Darth Vader and the bounty hunters!")
    print("You will begin with 0 points and will loose points with each incorrect guess.")
    print("However, when you guess correctly, 100 points will be added to your total points.")
    print("You will also be able to take the other test and jump into all other parts of the program!")
    print("Good luck, and may the force be with you.")
    global player
    player = input("What is your name?: ")
    return None


def question_01() -> int:
    """First question in my Sith quiz!"""
    global points
    print(f"You are starting with { points } points!")
    print("Q1: What is Darth Sidious's real name? Choose one of the following letters")
    question: str = str(input("a. Sheev Palpatine\nb. Obi Wan Kanobi\nc. George Lucas\nd. Count Dooku\n"))
    if ord(question) == ord("a") or ord(question) == ord("A"):
        points += 20
        print(f"Correct, you have { points } points! {THUMBS_UP}")
        return points
    else:
        points += 10
        print(f"Incorrect, the answer is a. Sheev Palpatine. You have { points } points {WORRIED}.")
        return points


def question_02() -> int:
    """Second question in my Sith quiz!"""
    global points
    print("Q2: Who was Darth Sidious's first apprentice? Choose one of the following letters")
    question: str = str(input("a. Yoda\nb. Luke Skywalker\nc. Darth Vader\nd. Darth Maul\n"))
    if ord(question) == ord("d") or ord(question) == ord("D"):
        points += 20
        print(f"Correct, you have { points } points {THUMBS_UP}!")
        return points
    else:
        points += 10
        print(f"Incorrect, the answer is d. Darth Maul. You have { points } points {WORRIED}.")
        return points


def question_03() -> int:
    """Third question in my Sith quiz!"""
    global points
    print("Q3: What is the true identity of Darth Vader? Choose one of the following letters")
    question: str = str(input("a. Mace Windu\nb. Boba Fett\nc. Anakin Skywalker\nd. Jabba the Hutt\n"))
    if ord(question) == ord("c") or ord(question) == ord("C"):
        points += 20
        print(f"Correct, you have { points } points {THUMBS_UP}!")
        return points
    else:
        points += 10
        print(f"Incorrect, the answer is c. Anakin Skywalker. You have { points } points {WORRIED}.")
        return points


def question_04() -> int:
    """Fourth question in my Sith quiz!"""
    global points
    print("Q4: What planet was General Grievous from? Choose one of the following letters")
    question: str = str(input("a. Tatooine\nb. Malachor\nc. Earth\nd. Kalee\n"))
    if ord(question) == ord("d") or ord(question) == ord("D"):
        points += 20
        print(f"Correct, you have { points } points {THUMBS_UP}!")
        return points
    else:
        points += 10
        print(f"Incorrect, the answer is d. Kalee. You have { points } points. {WORRIED}")
        return points


def question_05() -> int:
    """Fifth question in my Sith quiz!"""
    global points
    print("Q5: Who was the first ever Sith? Choose one of the following letters")
    question: str = str(input("a. Han Solo\nb. Darth Raven\nc. Ajunta Pall\nd. Asoka\n"))
    if ord(question) == ord("c") or ord(question) == ord("C"):
        points += 20
        print(f"Correct, you have { points } points {THUMBS_UP}!")
        if points >= 100:
            print("Congratulations, you demonstrated mastery on the Sith Quiz and are a true Sith Lord!")   
            return points
        if points >= 80:
            print("Congratulations, you demonstrated intermediate knowledge on the Sith Quiz!")
            return points
        else:
            print("Congratulations, you are at beginner's level!")
            return points
    else:
        points += 10
        print(f"Incorrect, the answer is c. Ajunta Pall. You have { points } points {WORRIED}.")
        if points >= 100:
            print("Congratulations, you demonstrated mastery on the Sith Quiz and are a true Sith Lord!")   
            return points
        if points >= 80:
            print("Congratulations, you demonstrated intermediate knowledge on the Sith Quiz!")
            return points
        else:
            print("Congratulations, you are at beginner's level!")
            return points


def question_06() -> int:
    """First question in my Jedi quiz!"""
    global points
    print("Q1: Who was Obi_Wan Kenobi's master? Choose one of the following letters")
    question: str = str(input("a. Qui-Gon\nb. Anakin Skywalker\nc. Mace Windu\nd. Luke Skywalker\n"))
    if ord(question) == ord("a") or ord(question) == ord("A"):
        points += 20
        print(f"Correct, you have { points } points {THUMBS_UP}!")
        return points
    else:
        points += 10
        print(f"Incorrect, the answer is a. Qui-Gon. You have { points } points {WORRIED}.")
        return points


def question_07() -> int:
    """Second question in my Jedi quiz!"""
    global points
    print("Q2: Which Jedi had the highest ever midi-chlorians counts? Choose one of the following letters")
    question: str = str(input("a. Yoda\nb. Barriss Offee\nc. Aayla Secura\nd. Anakin Skywalker\n"))
    if ord(question) == ord("d") or ord(question) == ord("D"):
        points += 20
        print(f"Correct, you have { points } points {THUMBS_UP}!")
        return points
    else:
        points += 10
        print(f"Incorrect, the answer is d. Anakin Skywalker. You have { points } points {WORRIED}.")
        return points


def question_08() -> int:
    """Third question in my Jedi quiz!"""
    global points
    print("Q3: Which character is not part of the jedi council? Choose one of the following letters")
    question: str = str(input("a. Plo Koon\nb. Kit Fisto\nc. Shaak Ti\nd. None of the above\n"))
    if ord(question) == ord("d") or ord(question) == ord("D"):
        points += 20
        print(f"Correct, you have { points } points {THUMBS_UP}!")
        return points
    else:
        points += 10
        print(f"Incorrect, the answer is d. None of the above. You have { points } points {WORRIED}.")
        return points


def question_09() -> int:
    """Fourth question in my Jedi quiz!"""
    global points
    print("Q4: Which Jedi was killed during Order 66? Choose one of the following letters")
    question: str = str(input("a. Obi-Wan Kenobi\nb. Shaak Ti\nc. Master Traavis\nd. Yoda\n"))
    if ord(question) == ord("c") or ord(question) == ord("C"):
        points += 20
        print(f"Correct, you have { points } points {THUMBS_UP}!")
        return points
    else:
        points += 10
        print(f"Incorrect, the answer is c. Master Traavis. You have { points } points {WORRIED}.")
        return points


def question_10() -> int:
    """Fifth question in my Jedi Quiz!"""
    global points
    print("Q5: Which former Jedi master taught Qui-Gon Jinn? Choose one of the following letters")
    question: str = str(input("a. Anakin SkyWalker\nb. Darth Maul\nc. Savage Opress\nd. Count Dooku\n"))
    if ord(question) == ord("d") or ord(question) == ord("D"):
        points += 20
        print(f"Correct, you have { points } points {THUMBS_UP}!")
        if points >= 100:
            print("Congratulations, you demonstrated mastery on the Jedi Quiz and are a true Jedi Master!")   
            return points
        if points >= 80:
            print("Congratulations, you demonstrated intermediate knowledge on the Jedi Quiz!")
            return points
        else:
            print("Congratulations, you are at beginner's level!")
            return points
    else:
        points += 10
        print(f"Incorrect, the answer is d. Count Dooku. You have { points } points {WORRIED}.")
        if points >= 100:
            print("Congratulations, you demonstrated mastery on the Jedi Quiz and are a true Jedi Master!")   
            return points
        if points >= 80:
            print("Congratulations, you demonstrated intermediate knowledge on the Jedi Quiz!")
            return points
        else:
            print("Congratulations, you are at beginner's level!")
            return points


def guess_using_the_force(a: int) -> int:
    """Function where you guess the amount of movies in Star Wars, and the attempts and points are tracked."""
    i: int = 0
    while int(input("How many Star Wars movies are there in the main storyline?\n")) != 9:
        print("Wrong guess! Try Again!")
        a -= 1
        i += 1
        print(f"You have { a } points on { i } amount of guesses!")
    
    print(f"Correct guess, you have answered the question in { i } guesses!")
    print("Here is a fun Star Wars quote to think about!")
    random_star_wars_quote: int = int(randint(1, 3))
    if random_star_wars_quote == 1:
        print(" ""Your focus determines your reality."" - Qui Gon Jinn")
    if random_star_wars_quote == 2:
        print(" ""Many of the truths we cling to depend greatly on our point of view"" - Obi Wan Kenobi")
    else:
        print(" ""Never tell me the odds"" Han Solo")
    a += 100
    print(f"You have { a } points!")
    return a


def bounty_hunters_quiz(a: int) -> int:
    """Function where you guess amount of bounty hunters, and the attempts and points are tracked."""
    i: int = 0
    while int(input("How many bounty hunters did Darth Vader hire to find the Millenium Falcon?\n")) != 6:
        print("Wrong answer! Try Again!")
        a -= 1
        i += 1
        print(f"You have { a } points on { i } amount of guesses!")

    print(f"Correct guess, you have answered the question in { i } guesses!")
    print("Here is a fun Star Wars fact!")
    random_star_wars_quote: int = int(randint(1, 3))
    if random_star_wars_quote == 1:
        print("Over 2,500 stormtroppers wree assigned to Imperial Star destroyers.")
    if random_star_wars_quote == 2:
        print("Wookies live for about 400 years.")
    else:
        print("Disney invested $4 billion dollars into Star Wars!")
    a += 100
    print(f"You have { a } points!")
    return a


if __name__ == "__main__":
    main()