import json
import random

# Load data from JSON file
try:
    with open("esm_famil_data.json") as file:
        esm_famil_data = json.load(file)
except FileNotFoundError:
    print("Error: JSON file not found.")
    esm_famil_data = []

def play_game(difficulty, question_count):
    if not esm_famil_data:
        print("No data available in database to play the game.")
        return

    score = 0
    questions = ["Name", "lastName", "country", "color", "Food", "things"]

    print(f"\nStarting 'Esm Famil' game with {difficulty} difficulty!")
    print("Answer each question based on the existing database. For each correct answer, you'll earn a point!")

    selected_questions = random.sample(questions, min(question_count, len(questions)))

    for q in selected_questions:
        random_data = random.choice(esm_famil_data)
        correct_answer = random_data[q]
        
        user_answer = input(f"Enter a {q.lower()}: ").strip().title()

        if difficulty == 'hard':
            if user_answer == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")
        else:  # Easy mode - partial matches allowed
            if user_answer in correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")

    print(f"\nGame Over! Your final score is: {score}/{len(selected_questions)}")

while True:
    answer = input("Choose an option:\n1) Play Esm Famil Game\n2) Exit\n")
    if answer == "1":
        difficulty = input("Choose difficulty (easy/hard): ").strip().lower()
        question_count = int(input("How many questions would you like to answer (1-6)? "))
        play_game(difficulty, question_count)
    elif answer == "2":
        print("Exiting the game. Goodbye!")
        break
    else:
        print("Invalid option! Please try again.")
