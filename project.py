import csv
import sys
def load_questions(filename):
    questions = []
    with open(filename) as file :
        reader = csv.DictReader(file)
        for row in reader:
            questions.append((row["question"],row["answer"]))
    return questions



def check_answer(i,j):
    if i == j:
        return True
    else:
        return False

def count(i , j):
    score = 0
    if check_answer(i , j) == True:
        score += 1
    return score

def percentage(total,number):
    try:
        percent = round((total/number*100))
        return percent
    except ZeroDivisionError:
        sys.exit("No question exist")
def message(x):
    if x >= 100:
        return f"Excellent!! You got highest. Here is my bow to you 🙌"
    elif x >= 80:
        return f"Very Good! You are definitely winning on your very next try , Keep it up 😇"
    elif x >= 60:
        return f"Yo! Well Done ! you are just a small step away from perfection 🤛"
    elif x >= 40:
        return f"Good! You are way ahead. Better Luck Next Time 🤟"
    elif x >= 20:
        return f"Not Bad! But you can improve a lot. Keep Practicing 😄"
    else:
        return f"Too bad! There is plenty of room for improvement 😅"

def main() :
    try:
        questions = load_questions("questions.csv")
        total = 0
        for question, answer in load_questions("questions.csv"):
            reply = input(question + " ").strip().lower()
            total = total + count(reply, answer)

        x = percentage(total , len(questions) )
        print(f"{x}%")
        print(message(x))
    except FileNotFoundError:
        sys.exit("File not found")
if __name__ == "__main__":
    main()
