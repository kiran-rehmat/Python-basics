# SIMPLE QUIZ GAME
# This program asks multiple-choice questions and keeps score.

# List of questions and answers
questions = [
    {"question": "What is the capital of Pakistan?", "answer": "Islamabad"},
    {"question": "Which language is this program written in?", "answer": "Python"},
    {"question": "What is 5 + 3?", "answer": "8"}
]

score = 0

print("Welcome to the Quiz Game!\n")

# Loop through each question
for q in questions:
    user_answer = input(q["question"] + " ").strip()

    if user_answer.lower() == q["answer"].lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong! The correct answer is:", q["answer"], "\n")

print(f"You got {score} out of {len(questions)} correct!")