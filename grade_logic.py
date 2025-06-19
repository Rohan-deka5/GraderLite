
def get_grade_letter(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 33:
        return "D"
    else:
        return "F"

def get_grade_message(letter):
    messages = {
        "A": "Excellent! 🎉",
        "B": "Practice more, You can do it bro ❤️🌻",
        "C": "Fair. Keep improving! 📘",
        "D": "You passed. Just barely. 😐",
        "F": "YOU SUCK AT THIS 😭"
    }
    return messages.get(letter, "Invalid Grade")

