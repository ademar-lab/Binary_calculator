def check_number(number):
    """This function returns True if the number is a nuber from 1 to 5. It returns False otherwise."""
    if number > 0 and number < 6:
        return True
    else:
        return False

def check_binary(a, b):
    """This function returns True if the characters entered are only binary digits. (1 or 0)"""
    status = True
    for character in a:
        if character == "0" or character == "1":
            pass
        else: 
            status = False
            break

        if status:
            for character in b:
                if character == "0" or character == "1":
                    pass
                else:
                    status = False
                    break
    return status