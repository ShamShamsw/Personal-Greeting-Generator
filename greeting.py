"""
Personal Greeting Generator — Starter Code
============================================

YOUR TASK: Fill in every function marked with TODO.
Read the README.md in this folder FIRST for the full instructions.

TIME ESTIMATE: 30–45 minutes

IMPORTANT — If You Get Stuck:
    1. Re-read the README section for the step you're on.
    2. Try writing out what you want in plain English first.
    3. Break the problem into the smallest possible piece and solve that.
    4. Use an AI assistant (like Copilot Chat) to ASK QUESTIONS about
       concepts you don't understand — for example:
         "What does .lower() do in Python?"
         "How do I validate user input in a while loop?"
       DO NOT ask AI to write the solution for you. The learning happens
       when YOUR brain figures out how to connect the pieces. AI is a
       tutor, not a shortcut. If AI writes it, you haven't learned it.
    5. Check the Python docs: https://docs.python.org/3/

PLANNING — Answer these BEFORE writing any code (fill in below):

    Inputs needed:
        - User's name (string)
        - Time of day: morning, afternoon, or evening (string)
        - User's mood: happy, tired, excited, or stressed (string)

    Functions I'll create:
        - get_valid_input(prompt, valid_options) — ask user a question, re-ask if invalid
        - generate_greeting(name, time_of_day, mood) — build a greeting string
        - main() — run the loop that ties everything together

    Edge cases to handle:
        - User types "Morning" instead of "morning" (case sensitivity)
        - User types something not in the valid options
        - User presses Enter with no input

    Build order:
        1. get_valid_input — so I can collect input safely
        2. generate_greeting — the core logic
        3. main — tie it all together with a loop
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
    # TODO: Implement this function
    # Hints to think about:
    #   - Use a while loop that runs until you get a valid answer
    #   - Convert the user's input to lowercase so "Morning" matches "morning"
    #   - If valid_options is empty, accept any non-blank input (for the name)
    #   - If valid_options is NOT empty, check that the input is in the list
    #   - Print a helpful message when the input is invalid
    pass


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
        str: A complete greeting message (multiple lines are fine).

    Example:
        >>> generate_greeting("Alice", "morning", "tired")
        "Good morning, Alice! I know mornings can be tough when you're tired.\\n..."
    """
    # TODO: Implement this function
    # Hints to think about:
    #   - Start with a time-based greeting: "Good morning", "Good afternoon", etc.
    #   - Add a mood-based message — you could use if/elif or a dictionary
    #   - Combine them into one string with f-strings
    #   - You have 3 times × 4 moods = 12 combinations. You DON'T need 12
    #     separate messages — you can mix and match parts independently.
    #
    # DECISION: Will you use if/elif chains or a dictionary for mood messages?
    # Write a comment here explaining WHY you chose your approach.
    pass


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
    # TODO: Implement this function
    # Hints to think about:
    #   - Ask for the name OUTSIDE the loop (it doesn't change)
    #   - Use a while True loop, and break when the user says "no"
    #   - Call get_valid_input() for each question
    #   - Call generate_greeting() to build the message, then print it
    pass


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
# WHAT I LEARNED (fill this in AFTER you finish)
# ============================================================
# Friend:    ...
# Employer:  ...
# Professor: ...
# ============================================================
