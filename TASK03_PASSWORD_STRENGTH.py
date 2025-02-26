import re

def password_strength(password):
    score  = 0

    if len(password) >= 8:
        score += 1
    else:
        print("Password Should be at Least 8 Characters Long.")

    if re.search(r'[a-z]',password):
        score +=1
    else:
        print("Password Should be at Least One Lowercase Letter.")

    if re.search(r'[A-Z]',password):
        score +=1
    else:
        print("Password Should be at Least One Uppercase Letter.")

    if re.search(r'[0-9]',password):
        score +=1
    else:
        print("Password Should be at Least One Number.")

    if re.search(r'[!@#$%^&*]',password):
        score +=1
    else:
        print("Password Should be at Least One Special Character.")

    if score == 5:
        return "Password is Very Strong."
    elif score == 4:
        return "Password is Strong."
    elif score == 3:
        return "Password is Medium."
    elif score == 2:
        return "Password is Weak."
    else:
        return "Password is Very Weak"

password = input("Enter A Password to Assess its Strength: ")
print(password_strength(password))