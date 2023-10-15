import random
from string import (
    punctuation,
    ascii_letters,
)

chars = punctuation + ascii_letters


def gen_pass(password_length) -> str:
    password = "".join(random.choice(chars) for _ in range(password_length))
    return password