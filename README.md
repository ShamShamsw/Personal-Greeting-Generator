# Beginner Project 01: Personal Greeting Generator

**Time:** 30–45 minutes  
**Difficulty:** Absolute Beginner  
**Focus:** Planning first, writing clean commented code, string formatting, conditionals

---

## Why This Project?

This is intentionally a very small program. The goal is NOT to write a lot of code. The goal is to **plan before you code** and **write comments that explain your thinking**. In interviews, how you think matters more than how fast you type.

---

## The Importance of Comments

> "Code tells you HOW. Comments tell you WHY."

Every function you write in this project (and in interviews) should have:

1. **A docstring** explaining what the function does, its parameters, and what it returns
2. **Inline comments** above any non-obvious logic explaining WHY you made that choice
3. **Section comments** separating logical blocks within longer functions

**Bad comment (describes WHAT the code does — you can already see that):**
```python
# Add 1 to counter
counter += 1
```

**Good comment (explains WHY):**
```python
# Track how many greetings we've generated so we can show the user their total at the end
counter += 1
```

You will be graded (by yourself) on comment quality, not code quantity.

---

## Requirements

Build a command-line program that asks the user a few questions and generates a personalized greeting message.

### What the program should do:

1. Ask the user their name
2. Ask the user the time of day (morning, afternoon, evening)
3. Ask the user their mood (happy, tired, excited, stressed)
4. Generate a personalized greeting based on all three inputs
5. Print the greeting
6. Ask if they want another greeting (loop until they say no)

### Example session:

```
Welcome to the Personal Greeting Generator!

What is your name? Alice
What time of day is it? (morning/afternoon/evening) morning
How are you feeling? (happy/tired/excited/stressed) tired

Good morning, Alice! I know mornings can be tough when you're tired.
Here's a tip: start with a small win — make your bed or grab your favorite drink.
You've got this! 💪

Would you like another greeting? (yes/no) no

Thanks for using the Greeting Generator! Have a wonderful day, Alice!
```

---

## STOP — Plan Before You Code

Before writing a single line of Python, answer these questions **on paper or in a comment block at the top of your file**:

### Planning Questions

1. **What inputs does my program need?**
   - List every piece of information you need from the user
   - What type is each input? (string, number, etc.)
   - What are the valid values for each input?

2. **What are the possible combinations?**
   - How many unique greetings can your program produce?
   - Time of day (3 options) × Mood (4 options) = how many combinations?
   - Do you need a unique message for every combination, or can you mix and match?

3. **What functions should I create?**
   - What does each function do?
   - What does each function take as input (parameters)?
   - What does each function return?
   - Write this out as a list before you code anything

4. **What could go wrong?**
   - What if the user types "Morning" instead of "morning"?
   - What if the user types something unexpected?
   - What if the user just hits Enter with no input?

5. **What order should I build things in?**
   - What's the smallest piece I can build and test first?
   - What depends on what?

**Write your answers as a multi-line comment block at the very top of your file.** This planning comment block should be at least 15–20 lines long. If it's shorter, you haven't planned enough.

---

## Step-by-Step Instructions

### Step 1: Create your file and write the plan (10 minutes)

Create a file called `greeting.py`. At the very top, write your planning comment block:

```python
"""
Personal Greeting Generator — Planning Notes
=============================================

Inputs needed:
  - ...

Functions I'll create:
  - ...

Edge cases to handle:
  - ...

Build order:
  1. ...
  2. ...
  3. ...
"""
```

Fill in all sections completely before moving to Step 2.

### Step 2: Write the `get_valid_input` function (5 minutes)

This function asks the user a question and keeps asking until they give a valid answer.

```python
def get_valid_input(prompt, valid_options):
    """
    Ask the user a question and validate their response.

    Parameters:
        prompt (str): The question to display to the user.
        valid_options (list): A list of acceptable lowercase answers.

    Returns:
        str: The user's validated response, in lowercase.

    Example:
        >>> get_valid_input("Pick a color: ", ["red", "blue", "green"])
        # If user types "RED", returns "red"
        # If user types "purple", asks again
    """
    # TODO: implement this
    pass
```

**Why this function?** Instead of writing input validation code 3 separate times (once for each question), we write it once and reuse it. This is the DRY principle — Don't Repeat Yourself. Mention this in a comment.

### Step 3: Write the `generate_greeting` function (10 minutes)

This function takes the three inputs and builds a greeting string. **Do not print anything in this function** — just return a string. (Why? Because functions that return values are easier to test than functions that print. Add a comment explaining this.)

Think about how to organize your greeting logic:
- Will you use if/elif chains?
- Will you use a dictionary to map moods to messages?
- Will you build the greeting in parts (opening + mood response + closing)?

Whatever you choose, **add a comment explaining WHY** you chose that approach.

### Step 4: Write the main loop (5 minutes)

This is the part that ties everything together:
1. Print a welcome message
2. Get the three inputs
3. Generate and print the greeting
4. Ask if they want another one
5. Loop back to step 2 if yes

Use a `while` loop. Add a comment explaining your loop condition.

### Step 5: Add the `if __name__ == "__main__"` guard (2 minutes)

```python
# This guard ensures the main loop only runs when we execute this file directly.
# If someone imports this file to reuse our functions, the loop won't auto-start.
# This is a Python best practice — add a comment explaining it in your own words.
if __name__ == "__main__":
    main()
```

### Step 6: Test and review (5 minutes)

Run your program and try:
- A normal flow
- Typing an invalid time of day
- Typing a mood in ALL CAPS
- Pressing Enter with no input
- Running through the loop multiple times

---

## Comment Checklist

Before you consider this project done, verify:

- [ ] There is a planning block at the top of the file (15+ lines)
- [ ] Every function has a docstring with parameters and return value documented
- [ ] There is at least one "WHY" comment (not "WHAT") in every function
- [ ] The `if __name__ == "__main__"` guard has a comment explaining its purpose
- [ ] Your loop has a comment explaining when/why it exits
- [ ] Any input validation has a comment explaining what you're protecting against

---

## Reflect on What You Learned

After finishing, write 2–3 sentences for EACH audience below. This isn't busywork — explaining the same thing at different levels is a skill you'll use in every interview and on every team.

### To a friend (casual, no jargon)

> _"I built a thing that..."_
>
> Example: "I built a little program that asks for your name and mood and then prints a custom greeting. The cool part was figuring out how to make it handle weird inputs without crashing."

### To an employer (focus on skills and process)

> _"In this project I practiced..."_
>
> Example: "I practiced writing a plan before coding, validating user input, and using Python string formatting. I wrote planning comments first and then implemented the logic — the same approach I'd use on a team."

### To a professor (technical, precise)

> _"This project demonstrates..."_
>
> Example: "This project demonstrates conditional branching, f-string interpolation, input validation with a while loop, and the use of a main guard. I documented design decisions in comments following a plan-first methodology."

**Write yours in a comment block at the bottom of your Python file:**
```python
# ============================================================
# WHAT I LEARNED
# ============================================================
# Friend:    ...
# Employer:  ...
# Professor: ...
# ============================================================
```

---

## Stretch Goals

1. Add a "surprise" mood that generates a random greeting using `random.choice()`
2. Save a log of all generated greetings to a text file with timestamps
3. Add color to the output using ANSI escape codes (comment explaining what ANSI codes are)
