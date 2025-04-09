import random

def generate_secret_number():
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:3]))

def evaluate_guess(secret, guess):
    feedback = []
    for s, g in zip(secret, guess):
        if s == g:
            feedback.append("👌 (Correct)")
        elif g in secret:
            feedback.append("👍 (Ok)")
        else:
            feedback.append("❌ (Wrong)")
    return feedback

secret = generate_secret_number()
attempts = 0

print("*** Guess the 3-digit number ***")
print("👌 = Correct digit & position | 👍 = Correct digit, wrong position | ❌ = Wrong digit")

while attempts < 10:
    guess = input(f"Attempt {attempts + 1}/10: Enter a 3-digit number: ").strip()
    
    if len(guess) != 3 or not guess.isdigit():
        print("⚠ Please enter exactly 3 digits!")
        continue
    
    attempts += 1
    feedback = evaluate_guess(secret, guess)
    print("Result:", " ".join(feedback))
    
    if all(f == "👌 (Correct)" for f in feedback):
        print(f"🎉 Congratulations! You guessed the number in {attempts} attempts: {secret}")
        break
else:
    print(f"❌ Game over! The secret number was: {secret}")