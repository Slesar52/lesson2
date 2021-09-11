def string_comp(one, two):
    one = str(one)
    two = str(two)
    if one or two != str:
        return "0"
    elif one == two:
        return "1"



print(string_comp("zzz", "zzz"))