import random, string
def salt(length:int=16) -> str:
    symbols = string.ascii_letters + string.digits
    return "".join(random.choice(symbols) for _ in range(length))