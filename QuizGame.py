# python quiz game

questions = ("How many elements are in the periodic table?",
             "Which animal lays the largest eggs?",
             "Which is the most abundant gas in the Earth's atmosphere?",
             "How many bones are in the human body?",
             "Which planet in the solar system is the hosttest?")


options = (("A. 118", "B. 119", "C. 120", "D. 121"),
           ("A. Whale", "B. Crocodile", "C. Penguin", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Argon"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mars", "B. Jupiter", "C. Saturn", "D. Uranus"))

answer = ("A", "D", "A", "A", "B")
guesses = []
score = 0


questions_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[questions_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answer[questions_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"The correct answer is {answer[questions_num]}")

    questions_num += 1


print("-------------------------")
print("        RESULTS          ")
print("-------------------------")


print("Answers: ", end="")
for answer in answer:
    print(answer, end=" ")
    print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")