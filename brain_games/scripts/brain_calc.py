from random import SystemRandom
from brain_games.cli import welcome_user
import operator

rule_game = "What is the result of the expression?"
symbols = ["+", "-", "*"]
secure_random = SystemRandom()


def is_valid_answer(user_answer: str) -> bool:
    try:
        int(user_answer)
        return True
    except ValueError:
        return False


def game(user_name: str) -> str:
    print(rule_game)
    round_game = 0

    while True:
        first_number = secure_random.randint(1, 100)
        second_number = secure_random.randint(1, 100)
        random_symbol = secure_random.choice(symbols)

        print(f"Question: {first_number} {random_symbol} {second_number}")

        answer_user = input("Your answer: ").strip()

        match random_symbol:
            case "+":
                correct_answer = operator.add(first_number, second_number)
            case "-":
                correct_answer = operator.sub(first_number, second_number)
            case "*":
                correct_answer = operator.mul(first_number, second_number)

        if not is_valid_answer(answer_user):
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.")
            return f"Let's try again, {user_name}!"

        user_int = int(answer_user)
        if user_int == correct_answer:
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
