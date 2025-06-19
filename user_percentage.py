def perca():
    name_user = input("Enter your name ") # User inputs their name
    total_marks_user = int(input("Enter your total marks:- ")) # Getting the total marks of the User test
    receive_marks_user = int(input("Enter your received marks:- ")) # Getting the received marks of the User test
    perc = receive_marks_user/total_marks_user *100
    return perc
