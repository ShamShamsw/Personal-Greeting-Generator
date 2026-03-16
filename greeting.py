"""
Personal Greeting Generator — Planning Notes
=============================================

Inputs needed:
  - name (str): The user's name. Any non-empty string is valid.
  - time_of_day (str): One of "morning", "afternoon", or "evening".
  - mood (str): One of "happy", "tired", "excited", or "stressed".

Functions I'll create:
  - get_valid_input(prompt, valid_options)
      Keeps asking the user until they enter a valid response.
      Passing an empty list means any non-blank input is accepted (used for name).
  - generate_greeting(name, time_of_day, mood)
      Builds and returns a personalized greeting string without printing.
      Separating generation from printing makes it easier to test.
  - main()
      Runs the full program: welcome, ask questions, show greeting, loop or exit.

Edge cases to handle:
  - User types "Morning" instead of "morning" — fix by converting to lowercase.
  - User types something not in the valid options — re-prompt with a helpful message.
  - User presses Enter with no input — treat blank input as invalid and re-prompt.

Build order:
  1. get_valid_input — foundational; everything else depends on clean input.
  2. generate_greeting — core logic; needs clean inputs to work correctly.
  3. main — ties everything together once the other two functions work.

Design decisions:
  - Use a dictionary for mood messages so adding a new mood only requires
    one new dictionary entry instead of touching an if/elif chain.
  - Build greeting in two independent parts (time greeting + mood message)
    so they can vary without needing 12 hard-coded combinations.
"""

# ============================================================
# STEP 1: INPUT VALIDATION
# ============================================================
# This function is reusable — you call it for EVERY question
# instead of writing validation code three separate times.
# This is the DRY principle: Don't Repeat Yourself.
# ============================================================


def get_valid_input(prompt, valid_options):
    """
    Ask the user a question and keep asking until they give a valid answer.

    Parameters:
        prompt (str): The question to display (e.g., "What is your name? ").
        valid_options (list): Acceptable lowercase answers
                              (e.g., ["morning", "afternoon", "evening"]).
                              Pass an empty list to accept ANY non-empty input.

    Returns:
        str: The user's validated response, in lowercase.

    Example:
        >>> get_valid_input("Time of day? ", ["morning", "afternoon", "evening"])
        # If user types "MORNING", returns "morning"
        # If user types "night", prints error and asks again
    """
    # Keep looping until we receive a valid response — we never want
    # downstream functions to receive empty strings or unrecognized values.
    while True:
        # Convert to lowercase so "Morning" and "MORNING" both match "morning"
        response = input(prompt).strip().lower()

        # Guard against blank input (e.g., user just presses Enter)
        if not response:
            print("Input cannot be blank. Please try again.")
            continue

        # If no specific options are required, any non-blank answer is fine
        # (used for the name question where any text is acceptable)
        if not valid_options:
            return response

        # Check that the response is one of the expected choices
        if response in valid_options:
            return response

        # Let the user know exactly what they should type next time
        print(f"Invalid input. Please choose from: {', '.join(valid_options)}")


# ============================================================
# STEP 2: GREETING GENERATION
# ============================================================
# This function RETURNS a string — it does NOT print anything.
# Why? Functions that return values are easier to test than
# functions that print. You can check the return value in code,
# but checking what got printed is much harder.
# ============================================================


def generate_greeting(name, time_of_day, mood):
    """
    Build a personalized greeting based on the user's inputs.

    Parameters:
        name (str): The user's name.
        time_of_day (str): "morning", "afternoon", or "evening".
        mood (str): "happy", "tired", "excited", or "stressed".

    Returns:
        str: A complete greeting message (multiple lines).

    Example:
        >>> generate_greeting("Alice", "morning", "tired")
        "Good morning, Alice! I know mornings can be tough when you're tired.\\n..."
    """
    # Map each time of day to its standard greeting prefix.
    # A dictionary is cleaner than an if/elif chain here because it reads like
    # a lookup table — easy to scan and extend without restructuring logic.
    time_greetings = {
        "morning":   "Good morning",
        "afternoon": "Good afternoon",
        "evening":   "Good evening",
    }

    # Map each mood to a two-part tuple: (empathy line, tip line).
    # Using a dictionary keeps the mood logic self-contained — adding a new
    # mood only requires one new entry rather than touching an if/elif chain.
    mood_messages = {
        "happy": (
            "It's great that you're feeling happy!",
            "Keep that energy going and spread some joy today. 😊",
        ),
        "tired": (
            "I know it can be tough when you're tired.",
            "Start with a small win — make your bed or grab your favorite drink. You've got this! 💪",
        ),
        "excited": (
            "Your excitement is contagious!",
            "Channel that energy into something you've been putting off — now's the perfect time. 🚀",
        ),
        "stressed": (
            "I'm sorry to hear you're feeling stressed.",
            "Take a deep breath. Break your tasks into small steps and tackle one at a time. 🌿",
        ),
    }

    # Build the opening line using the time-of-day greeting and the user's name
    opening = f"{time_greetings[time_of_day]}, {name}!"

    # Retrieve the two mood-specific lines
    empathy, tip = mood_messages[mood]

    # Combine all parts into one multi-line greeting string
    return f"{opening} {empathy}\n{tip}"


# ============================================================
# STEP 3: MAIN LOOP
# ============================================================
# This ties everything together: welcome → ask questions →
# generate greeting → ask to repeat → loop or exit.
# ============================================================


def main():
    """
    Run the greeting generator program.

    Flow:
        1. Print a welcome message
        2. Ask for the user's name (only once — reuse it in the loop)
        3. Loop:
            a. Ask for time of day
            b. Ask for mood
            c. Generate and print the greeting
            d. Ask if they want another greeting
            e. If no, break out of the loop
        4. Print a goodbye message
    """
    print("\nWelcome to the Personal Greeting Generator!\n")

    # Ask for the name once, outside the loop, because the name
    # doesn't change between greetings — no point re-asking each iteration
    name = get_valid_input("What is your name? ", [])
    # Use title() so each word is capitalised — handles multi-word names like
    # "alice smith" → "Alice Smith" better than capitalize() which only
    # uppercases the very first character.
    name = name.title()

    # Loop indefinitely until the user explicitly says they're done.
    # We use `while True` with a `break` because the exit condition is
    # checked at the END of the loop body, not the beginning.
    while True:
        time_of_day = get_valid_input(
            "\nWhat time of day is it? (morning/afternoon/evening) ",
            ["morning", "afternoon", "evening"],
        )

        mood = get_valid_input(
            "How are you feeling? (happy/tired/excited/stressed) ",
            ["happy", "tired", "excited", "stressed"],
        )

        # Generate the greeting string and print it
        greeting = generate_greeting(name, time_of_day, mood)
        print(f"\n{greeting}\n")

        # Check whether the user wants to generate another greeting
        again = get_valid_input(
            "Would you like another greeting? (yes/no) ",
            ["yes", "no"],
        )

        # Exit the loop when the user says "no"
        if again == "no":
            break

    # Farewell message shown once the loop ends
    print(f"\nThanks for using the Greeting Generator! Have a wonderful day, {name}!\n")


# ============================================================
# STEP 4: MAIN GUARD
# ============================================================
# This ensures the main loop only runs when you execute this
# file directly (python greeting.py). If someone imports this
# file to reuse functions, the loop won't auto-start.
# This is a Python best practice.
# ============================================================

if __name__ == "__main__":
    main()


# ============================================================
# WHAT I LEARNED
# ============================================================
# Friend:    I built a little program that asks for your name, the time of
#            day, and your mood, then prints a custom greeting. The cool part
#            was making it handle weird inputs — like ALL CAPS or blank
#            answers — without crashing.
#
# Employer:  In this project I practiced planning before coding, validating
#            user input with a reusable function (DRY principle), and using
#            Python string formatting. I wrote planning comments first and
#            then implemented the logic — the same approach I would use when
#            working on a team.
#
# Professor: This project demonstrates conditional branching, f-string
#            interpolation, input validation with a while loop, dictionary
#            lookups for mapping inputs to messages, and the use of a main
#            guard. Design decisions — such as using dictionaries instead of
#            if/elif chains — are documented in inline comments following a
#            plan-first methodology.
# ============================================================
