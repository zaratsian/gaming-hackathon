import datetime
import random
from zoneinfo import ZoneInfo
import requests
from google.adk.agents import Agent


_number_to_guess = None
_guess_tries = 0


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}


def pick_a_number() -> dict:
    """Picks a random number between 1 and 100 for the user to guess, with 3 tries.

    Returns:
        dict: status and a message indicating the range and number of tries.
    """
    global _number_to_guess, _guess_tries
    _number_to_guess = random.randint(1, 100)
    _guess_tries = 3
    return {
        "status": "success",
        "message": "I've picked a number between 1 and 100. You have 3 tries to guess it!"
    }

def guess_number(guess: int) -> dict:
    """Allows the user to guess the number that was previously picked.

    Args:
        guess (int): The user's guess.

    Returns:
        dict: status and feedback on the guess (too high, too low, or correct),
              and remaining tries.
    """
    global _number_to_guess, _guess_tries
    if _number_to_guess is None:
        return {
            "status": "error",
            "error_message": "No number has been picked yet. Use 'pick_a_number' first."
        }

    _guess_tries -= 1

    if guess < _number_to_guess:
        feedback = "Too low!"
    elif guess > _number_to_guess:
        feedback = "Too high!"
    else:
        _number_to_guess = None
        _guess_tries = 0
        return {"status": "success", "feedback": "Congratulations! You guessed the number!"}

    if _guess_tries > 0:
        return {"status": "success", "feedback": f"{feedback} You have {_guess_tries} tries left."}
    else:
        correct_number = _number_to_guess
        _number_to_guess = None
        return {"status": "success", "feedback": f"You're out of tries! The number was {correct_number}."}


def get_joke():
    r = requests.get("https://official-joke-api.appspot.com/random_joke")
    return r.json()


def get_corporate_buzzwords():
    r = request.get('https://corporatebs-generator.sameerkumar.website/')
    return r.text()

