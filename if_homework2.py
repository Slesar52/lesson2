def string_comp(one, two):
    if not (isinstance(one, str) and isinstance(two, str)):
        return "0"
    elif one == two:
        return "1"
    elif one != two and two == "learn":
        return "3"
    elif one != two and len(one) > len(two):
        return "2"
    
print(string_comp("ffffff", "lear"))