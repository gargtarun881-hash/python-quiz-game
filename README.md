# Python Basics Quiz

## Demo
![Quiz running](demo.png)
![Tests passing](tests.png)

## What it does
This is a small command-line quiz game written in Python. It reads a bank of questions from a file called `questions.csv` and picks 5 of them at random each time you run it. It asks them one at a time, and you type an answer for each one. At the end, the program counts the right answers, turns that into a percentage, and prints the percentage with a short message. The message changes with the score, from encouraging for a low score to celebratory for a perfect one.

The program also remembers your best score. After each quiz it compares your score with the best one saved from earlier runs. If you beat it, it saves the new score and prints `New best score!`. If not, it prints the best score so far. The best score is kept in a small file called `best_score.txt`, which the program creates the first time you play.

Answers are cleaned with `.strip()` and `.lower()` before they are checked, so capital letters and extra spaces do not matter. The answer has to match the one in the file exactly, so `lowercase` is right but `lower` is wrong. If the file has fewer than 5 questions, the quiz asks all of them.

## How to add a question
Open `questions.csv` and add a new line in this form:

    question,answer

Write the answer in lowercase. Do not put a comma inside the question. Do not change the first line, which must stay `question,answer`.

## Files
- `project.py`: the program itself. It holds `main` and the helper functions.
- `test_project.py`: the 11 tests, which run with pytest.
- `questions.csv`: the bank of questions and their answers.
- `requirements.txt`: the libraries the project needs. Here it only lists pytest.
- `README.md`: this file.
- `demo.png` and `test.png`: screenshots of the quiz and of the tests passing.
- `best_score.txt`: created when you play. It is your own score, so it is not in this repo.

## Functions
`main()` loads the questions, picks 5 at random, asks each one, and prints the result and the best score. If `questions.csv` is missing, it stops with a short message instead of crashing. It is the only place where the program asks for input or prints the result.

`load_questions(filename)` reads the CSV file with `csv.DictReader`. It returns a list of (question, answer) pairs.

`pick_questions(qs, n)` returns `n` different questions chosen at random from the list, using `random.sample`. If the list has fewer than `n` questions, it returns all of them.

`check_answer(i, j)` takes the answer the user gave and the correct answer. It returns `True` if they match and `False` if they do not.

`count(i, j)` uses `check_answer`. It returns 1 for a right answer and 0 for a wrong one, so the points can be added up.

`percentage(total, number)` takes the number of right answers and the number of questions. It returns the score as a whole number from 0 to 100. If there are no questions, it stops the program with a message instead of crashing on a divide-by-zero error.

`message(x)` takes the percentage and returns a message for it. It checks from the highest limit down (100, 80, 60, 40, 20), so it works for any percentage.

`read_best(filename)` reads the saved best score from a file and returns it as a number. If the file is missing or does not hold a number, it returns 0, so the quiz never crashes because of it.

`save_best(filename, score)` writes a score into a file.

## How to run it
Start the quiz:

    python3 project.py

Run the tests:

    pytest test_project.py

## Design choices
I kept all the input and printing inside `main()`, and I made every other function take values in and return a value. A function like that is easy to test, because a test can call it with fixed values and check the answer. If `check_answer` asked for input itself, the tests would stop and wait for someone to type.

I moved the questions out of the code and into `questions.csv`. Now a new question is one new line in a file, and no code has to change. `percentage` and `message` work for any number of questions.

Reading and saving the best score are in their own small functions, so they can be tested alone. `read_best` returns 0 when the file is missing or damaged, so a bad file cannot stop the quiz.

The tests for the random picking check how many questions come back and that every pick comes from the bank. They do not check which questions are picked, because that changes every run. The file tests use a temporary file, so they never touch the real `questions.csv` or `best_score.txt`.

## Limits and ideas for later
- Only one exact answer counts as right.
- Idea: accept more than one right answer for a question.
- Idea: keep a best score for each topic.

## Notes
I built this while learning Python. I used AI assistants for guidance and to help draft this README. I wrote the code and the tests myself, and I can explain how each part works.
