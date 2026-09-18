import random

WORDS = ["apple", "brave", "crane", "dream", "earth", "flame", "grape",
         "house", "juice", "knife", "lemon", "mango", "night", "ocean",
         "piano", "queen", "river", "stone", "tiger", "ultra", "vivid",
         "whale", "xenon", "yacht", "zebra",
         "amber", "blaze", "charm", "dense", "eagle", "frost", "globe",
         "haste", "ivory", "jolly", "kneel", "lunar", "marsh", "noble",
         "orbit", "plume", "quilt", "raven", "solar", "tower", "unity",
         "vapor", "wrist", "yield", "zesty",
         "beach", "cloud", "dance", "eager", "fable", "grain", "honey",
         "jumbo", "kayak", "lodge", "moist", "north", "olive", "pearl",
         "quack", "royal", "shelf", "tidal", "urban", "vocal", "wagon",
         "youth", "zonal"]


GREEN = "\033[92m"
YELLOW = "\033[93m"
GRAY = "\033[90m"
RESET = "\033[0m"


def color_guess(guess, target):
    result  = []
    target_remaining = list(target)

    # First pass: mark greens (correct letter, correct spot)
    for i, ch in enumerate(guess):
        if ch == target[i]:
            result.append((ch, GREEN))
            target_remaining[i] = None  # Remove this letter from consideration

        else:result.append((ch, None))


    # Second pass: mark yellows only if letter is still available
    for i, (ch,color) in enumerate(result):
        if color is None:
            if ch in target_remaining:
                result[i] = (ch, YELLOW)
                target_remaining[target_remaining.index(ch)] = None  # Remove this letter from consideration
            else:
                result[i] = (ch, GRAY)

    return "".join(f"{color}{ch}{RESET}" for ch, color in result)


def main():
    target = random.choice(WORDS)
    attempts = 6
    print(" WORDLE - guess a 5-letter word! you have 6 attempts. \n")
    for turn in range(1, attempts+1):
        while True: 
            guess = input(f"Attempt {turn}/{attempts}: ").strip().lower()
            if len(guess) == 5 and guess.isalpha():
                break
            print("Invalid input. Please enter a 5-letter word.")

        print(color_guess(guess, target))

        if guess == target:
            print(f"\n🎉 You got it in {turn} tries!")
            return

    print(f"\nOut of tries. The word was: {target}")

if __name__ == "__main__":
    main()


    