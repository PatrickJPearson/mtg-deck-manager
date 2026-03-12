def validate_color_entry(P):
    if P == "":
        return True
    if len(P) != len(set(P)):
        return False
    if 'C' in P:
        return False
    ret = True
    for char in P.upper():
        if not char in ['W', 'U', 'B', 'R', 'G']:
            ret = False
    return ret