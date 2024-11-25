import random

def run_quiz():
    score = 0
    incorrect_questions = []
    
    # Quiz questions with multiple choice options
    quiz = {
        """What is the output of this code? print(type([]) is list):""": {
            "options": ["True", "False", "None", "Error"],
            "answer": "True"
        },
        "What does ML stand for?": {
            "options": ["machine learning", "manual labor", "magical learning", "media literacy"],
            "answer": "machine learning"
        },
        "What does AI stand for?": {
            "options": ["artificial intelligence", "automatic information", "advanced internet", "analytical intelligence"],
            "answer": "artificial intelligence"
        }
    }

    # Shuffle questions
    questions = list(quiz.keys())
    random.shuffle(questions)

    for question in questions:
        options = quiz[question]['options']
        print(f"\n{question}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        user_answer_index = input("Choose the correct option (1-4): ")

        try:
            user_answer = options[int(user_answer_index) - 1]
            if str(user_answer).lower() == str(quiz[question]['answer']).lower():
                print("Correct!")
                score += 1
            else:
                print("Incorrect. The answer is:", quiz[question]['answer'])
                incorrect_questions.append(question)
        except (ValueError, IndexError):
            print("Invalid input. Please select a number between 1 and 4.")

    total_questions = len(questions)
    percentage = (score / total_questions) * 100
    print(f"\nYou scored {score} out of {total_questions} questions.")
    print(f"Your percentage score is: {round(percentage, 2)}%")

    if incorrect_questions:
        print("\nYou answered the following questions incorrectly:")
        for question in incorrect_questions:
            print(f"- {question}: {quiz[question]['answer']}")

# Main program loop
while True:
    user_wants_to_continue = input("Welcome to the Quiz app! Type 'yes' to start the quiz or 'exit' to leave: ").lower()

    if user_wants_to_continue == "yes":
        run_quiz()
    elif user_wants_to_continue == "exit":
        print("Exiting the Quiz app. Goodbye!")
        break
    else:
        print("Invalid input. Please type 'yes' to continue or 'exit' to leave.")
