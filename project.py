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

def percentage(total):
    percent = round((total/5)*100)
    return percent

def message(x):
    if x == 0:
        return f"Too bad! There is plenty of room for improvement 😅"
    elif x == 20:
        return f"Not Bad! But you can improve a lot. Keep Practicing 😄"
    elif x == 40:
        return f"Good! You are way ahead. Better Luck Next Time 🤟"
    elif x == 60:
        return f"Yo! Well Done ! you are just a small step away from perfection 🤛  "
    elif x == 80:
        return f"Very Good! You are definitely winning on your very next try , Keep it up 😇 "
    elif x == 100:
        return f"Excellent!! You got highest. Here is my bow to you 🙌"

def main() :
    a = input("What is the capital of France? ").strip().lower()
    b = input("What keyword stops a loop? ").lower().strip()
    c = input("What function gives the length of a list? ").lower().strip()
    d = input("What does .lower() do to text? ").lower().strip()
    e = input("How many minutes are in an hour? ").lower().strip()
    total = 0
    total = total + count(e , "60") + count(d , "lowercase") + count(c , "len") + count(b , "break") + count(a , "paris")
    x = percentage(total)
    print(f"{x}%")
    print(message(x))

if __name__ == "__main__":
    main()
