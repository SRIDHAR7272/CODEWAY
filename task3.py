questions = ("What is the national bird of India?: ",
                       "What is the national language of India?: ",
                       "What is the national sport of India? : ",
                       "How many bones are in the human body?: ",
                       "What is the national flag of India?: ")

options = (("A. Peacock", "B. Tiger", "C. Lion", "D. Deer"),
                   ("A. Hindi", "B. English", "C. Telugu", "D. Tamil"),
                   ("A. Cricket", "B. Hockey", "C. Tennis", "D. Volley Ball "),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Dicolor", "B. Unicolor", "C. Tricolor", "D. Tetracolor"))

answers = ("A", "A", "B", "A", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")