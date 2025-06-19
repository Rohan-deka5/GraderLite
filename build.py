from grade_logic import get_grade_letter, get_grade_message
from user_percentage import perca

def main():
    c = perca()
    grade_letter = get_grade_letter(c)
    grade_message = get_grade_message(grade_letter)
    
    print(f"Your percentage is: {c:.2f}%")
    print (f"Grade Letter: {grade_letter}")
    print (grade_message)
    
main()