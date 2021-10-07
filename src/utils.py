def special_characters_check(input):
    special_characters = "!@#$%^&*()-+?_=,<>/"
    if any(c in special_characters for c in input):
        return True
    return False