import random as r


def create_wall():
    allow_create_wall = r.randint(0, 1)

    if allow_create_wall == 1:
        return "*"

    return " "
