import random
import time

def generate_random_integer(min, max):
    """
    generates Random integer.
    """
    return random.randint(min, max)


def generate_random_operator():
    #generates randoom operation for math problem
    return random.choice(['+', '-', '*'])


def question_generator(number1, number2, operator):
    # generates random question everytime
    problem = f"{number1} {operator} {number2}"
    if operator == '+': answer = number1 + number2
    elif operator == '-': answer = number1 - number2
    else: answer = number1 * number2
    return problem, answer

def math_quiz():
    total_score = 0
    total_questions = 4

    print("\nWelcome to the Math Quiz Game!\n")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number1 = generate_random_integer(1, 20); number2 = generate_random_integer(1, 10); operator = generate_random_operator()

        problem, answer = question_generator(number1, number2, operator)
        print(f"\nQuestion: {problem}")
        try:
            user_answer = input("Your answer: ")
            user_answer = int(user_answer)
        except Exception as ex:
            print("please type only integers")
        if user_answer == answer:
            print("Correct! You earned a point.")
            total_score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {total_score}/{total_questions}")

    # Provides feedback based on the score
    if total_score == total_questions: print("\nCongratulations! You are excellent at math!\n")
    elif total_score > total_questions * 0.5 and total_score < total_questions: print("You are good, but there's room for improvement.") 
    else: print("You need to practice your basic math skills.")


print("\nThank you for playing \n This window closes automatically in 10 seconds")
    time.sleep(10)

if __name__ == "__main__":
    math_quiz()
