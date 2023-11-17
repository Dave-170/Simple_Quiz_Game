import random

# Function to ask a question and check the user's answer
def ask_question(question, answer, user_answer):
    """
    Checks if the user's answer matches the correct answer for a question.

    Args:
        question (str): The question to be asked.
        answer (str): The correct answer to the question.
        user_answer (str): The user's answer to the question.

    Returns:
        int: 1 if the user's answer is correct, 0 otherwise.
    """
    # Check if the user's answer (case-insensitive) matches the correct answer
    if user_answer.lower() == answer.lower():
        print("Correct!")  # Print a message for a correct answer
        return 1  # Return 1 to indicate a correct answer
    else:
        print(f"Wrong! The correct answer is: {answer}")  # Print the correct answer for an incorrect response
        return 0  # Return 0 to indicate an incorrect answer

# Main function where the quiz game is implemented
def main():
    """Runs the Quiz Game."""
    print("Welcome to the Quiz Game!")

    # Ask the user if they want to play
    play_game = input("Would you like to play? (yes/no): ")

    # Check if the user wants to play
    if play_game.lower() != "yes":
        print("Goodbye!")  # End the game if the user doesn't want to play
        return

    correct_answers = 0
    total_questions = 20  # Total number of questions (5 computing, 5 dogs, 10 games)

    # Define questions and answers for each category
    categories = {
        "computing": [
            {"question": "What does CPU stand for?", "answer": "Central Processing Unit"},
            {"question": "What is Python?", "answer": "A programming language"},
            {"question": "What is RAM?", "answer": "Random Access Memory"},
            {"question": "What does HTML stand for?", "answer": "Hypertext Markup Language"},
            {"question": "What is an IP address?", "answer": "Internet Protocol address"}
        ],
        "dogs": [
            {"question": "What is the most common breed of dog?", "answer": "Labrador Retriever"},
            {"question": "How many legs does a dog have?", "answer": "4"},
            {"question": "What is the smallest dog breed?", "answer": "Chihuahua"},
            {"question": "What is the largest dog breed?", "answer": "Saint Bernard"},
            {"question": "What is a dog's sense of smell like?", "answer": "Exceptional"}
        ],
        "games": [
            {"question": "Who created Minecraft?", "answer": "Markus Persson"},
            {"question": "What is the main objective of Tetris?", "answer": "Clear lines by fitting blocks"},
            {"question": "Which game features a plumber named Mario?", "answer": "Super Mario"},
            {"question": "What genre is the game 'The Legend of Zelda'?", "answer": "Action-Adventure"},
            {"question": "What is the highest-grossing video game as of 2023?", "answer": "Minecraft"}
        ]
    }

    # Combine all the questions into one list and shuffle them
    all_questions = [question for category_questions in categories.values() for question in category_questions]
    random.shuffle(all_questions)

    # Loop through the questions, ask them, and update the user's score
    for question in all_questions:
        user_answer = input(question["question"] + ": ")
        correct_answers += ask_question(question["question"], question["answer"], user_answer)

    # Calculate and display the user's score as a percentage
    print("\n")
    score_percentage = (correct_answers / total_questions) * 100
    print(f"You got {correct_answers} out of {total_questions} questions correct.")
    print(f"Your score is {score_percentage:.2f}%.")

if __name__ == "__main__":
    main()
