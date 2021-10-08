import readline

def special_characters_check(input):
    if input:
        special_characters = "!@#$%^&*()-+?_=,<>/"
        if any(c in special_characters for c in input):
            return True
        return False
    return False

def rlinput(prompt, prefill=''):
    readline.set_startup_hook(lambda: readline.insert_text(prefill))
    try:
        return input(prompt)
    finally:
        readline.set_startup_hook()