import random

try:
    k = random.choice([1,2,3,4,None])
    if k:
        raise ValueError("value error")
except TypeError:
    print("trype")