
def validate_entry(P):
    if P == "":
        return True
    elif P.isdigit():
        return True
    else:
        return False