import hashlib, random, string


def salt(length:int=16) -> str:
    symbols = string.ascii_letters + string.digits
    return "".join(random.choice(symbols) for _ in range(length))


def dk(password:str, salt:str) -> str:
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'), 1000000,
        16).hex()