import random
from collections import defaultdict
from questions import questions 
import os 




# Define the maximum box number (representing mastery)

MAX_BOX = 2  # Adjust this to how many times you need to get a question right to "master" it


# Leitner system: Track the "box" for each question (starts at box 1)
leitner_boxes = defaultdict(lambda: 1)

# Function to calculate progress
def calculate_progress():
    total_questions = len(questions)
    mastered_questions = sum(1 for q in questions if leitner_boxes[q['question']] >= MAX_BOX)
    return (mastered_questions / total_questions) * 100

# Map numbers to letters for easy input handling
def map_input_to_answer(user_input):
    if user_input == '1':
        return 'a'
    elif user_input == '2':
        return 'b'
    elif user_input == '3':
        return 'c'
    elif user_input == '4':
        return 'd'
    return user_input  # Return the input if it's already a letter

# Get a question to ask based on the Leitner system without repeating the same question too often
def get_question_to_ask():
    # Filter out questions that have already been mastered
    questions_not_mastered = [q for q in questions if leitner_boxes[q['question']] < MAX_BOX]
    
    # If no questions remain to be asked, return None
    if not questions_not_mastered:
        return None
    
    # Sort the remaining questions by their Leitner box number (prioritize lower boxes)
    sorted_questions = sorted(questions_not_mastered, key=lambda q: leitner_boxes[q['question']])
    
    # Randomly choose one question based on their Leitner box
    return random.choice(sorted_questions)

# Clear the screen function (works on Windows and Unix)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def quiz():
    correct_answers = 0
    wrong_answers = 0
    total_questions = len(questions)
    
    last_feedback = ""  # Keep track of feedback for the last question

    while True:
        # Get the next question to ask based on Leitner box prioritization
        question_to_ask = get_question_to_ask()

        if not question_to_ask:
            # If no more questions are left to ask, exit the quiz
            clear_screen()
            print("\nCongratulations! You have achieved 100% mastery!")
            break

        # Clear the screen but keep last feedback visible
        clear_screen()
        print(last_feedback)

        # Display the current score counters and percentage mastery
        progress = calculate_progress()
        print(f"Correct: {correct_answers} | Wrong: {wrong_answers} | Progress: {progress:.2f}% mastery")

        # Display the question and options
        print("\n" + question_to_ask["question"])
        for idx, option in enumerate(question_to_ask["options"], 1):
            print(f"{idx}) {option}")

        # Ask for user input: number (1, 2, 3, 4) or letter (a, b, c, d) or '0' to exit
        answer = input("\nYour answer (1-4, a-d), or '0' to exit: ").lower()

        if answer == '0':
            print("\nYou have chosen to exit the quiz.")
            break  # Exit the quiz

        # Map numeric input (1-4) to corresponding letter answer (a-d)
        mapped_answer = map_input_to_answer(answer)

        # Find the correct answer index for feedback
        correct_option_index = ord(question_to_ask["answer"]) - ord('a') + 1

        if mapped_answer == question_to_ask["answer"]:
            last_feedback = f"Correct! The answer was {question_to_ask['answer']}) {question_to_ask['options'][correct_option_index - 1]}"
            correct_answers += 1
            # Move the question to a higher Leitner box (master it)
            if leitner_boxes[question_to_ask['question']] < MAX_BOX:
                leitner_boxes[question_to_ask['question']] += 1
        else:
            last_feedback = f"Incorrect! The correct answer was {question_to_ask['answer']}) {question_to_ask['options'][correct_option_index - 1]}"
            wrong_answers += 1
            # Move the question to a lower box to reinforce learning
            leitner_boxes[question_to_ask['question']] = max(1, leitner_boxes[question_to_ask['question']] - 1)

        # Calculate and display progress after each question
        progress = calculate_progress()

if __name__ == "__main__":
    print("Welcome to the Cyber Security Quiz!")
    quiz()