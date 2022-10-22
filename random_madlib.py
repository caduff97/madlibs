from sample_madlibs import english, programming
import random

if __name__ == "__main__":
    m = random.choice([english, programming])
    m.madlib()