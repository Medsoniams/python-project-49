from random import SystemRandom

import prompt

from brain_games.cli import welcome_user

rule_game = """Answer "yes" if the number is even, otherwise answer "no"."""
secure_random = SystemRandom()


def is_even(number: int) -> bool:
    return True if number % 2 == 0 else False


def is_valid_answer(string: str) -> bool:
    return True if string == "yes" or string == "no" else False


def game(user_name):
    print(rule_game)
    round_game = 0
    while True:
        random_number = secure_random.randint(1, 100)
        print(f"Question: {random_number}")
        answer_user = prompt.string("Your answer: ")

        correct_answer = "yes" if is_even(random_number) else "no"

        if not is_valid_answer(answer_user):
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.")
            return f"Let's try again, {user_name}!"

        if answer_user == correct_answer:
            print("Correct!")
            round_game += 1
        else:
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.")
            return f"Let's try again, {user_name}!"

        if round_game == 3:
            return f"Congratulations, {user_name}!"


def main():
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print(f"Hello, {user_name}!")
    print(game(user_name))


if __name__ == "__main__":
    main()

