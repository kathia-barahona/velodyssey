import random
import string

def generate_random_route_name(
    prefix: str = "", length: int = 10,
) -> str:
    return prefix + ''.join((random.choice(string.ascii_lowercase)) for _ in range(length))
