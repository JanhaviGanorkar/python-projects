# 🧠 Quiz App

This is a simple Python-based multiple-choice quiz application that tests the user's knowledge of programming concepts and general terms. The quiz features random question order, a scoring system, and displays incorrect answers at the end.

## ✨ Features

- 🔀 **Randomized Questions**: Each quiz has a different order of questions.
- 📝 **Multiple-Choice Options**: Four possible answers for each question.
- 🎯 **Scoring**: Displays the user's score and percentage after completing the quiz.
- ⚠️ **Error Handling**: Handles invalid inputs like non-numeric or out-of-range values.
- 📋 **Review Incorrect Answers**: The program shows the correct answers for questions answered incorrectly.
- 💡 **Simple Interface**: Type `yes` to start the quiz, or `exit` to leave.

## 🛠️ Requirements

- 🐍 Python 3.x

## 🚀 How to Run

1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the following command to start the quiz:
    ```bash
    python quiz_app.py
    ```
4. When prompted, type `yes` to start or `exit` to quit.
5. Answer questions by typing a number (1-4) corresponding to your selected answer.

## 💻 Example

```bash
Welcome to the Quiz app! Type 'yes' to start the quiz or 'exit' to leave: yes

What is the output of this code? print(type([]) is list):
1. True
2. False
3. None
4. Error
Choose the correct option (1-4): 1
Correct!

What does ML stand for?
1. machine learning
2. manual labor
3. magical learning
4. media literacy
Choose the correct option (1-4): 1
Correct!

You scored 2 out of 2 questions.
Your percentage score is: 100.0%
