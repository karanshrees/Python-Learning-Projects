import random


def main():
    print("Start game")

    secret = random.randint(0, 9)
    attempts = 0

    while True:
        try:
            guess_str = input("Guess a number between 0 and 9: ")
        except KeyboardInterrupt:
            print("\nGame interrupted. Goodbye!")
            break

        try:
            guess = int(guess_str)
        except ValueError:
            print("Enter a valid number")
            continue

        attempts += 1

        if guess > secret:
            print("Too high")
        elif guess < secret:
            print("Too low")
        else:
            print("Correct!")
            print(f"Attempts: {attempts}")
            break


if __name__ == "__main__":
    main()