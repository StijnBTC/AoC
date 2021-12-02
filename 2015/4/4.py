from hashlib import md5
from itertools import *


def day4():
    mine()
    mine(diff=6)


def mine(diff=5, input="iwrupvqb"):
    for i in count():
        hash = md5((input + str(i)).encode()).hexdigest()
        if hash.startswith("0" * diff):
            print(f"hash {hash} at {i}")
            return
        i += 1


if __name__ == "__main__":
    day4()
