# Using time module to calculate the time span.
from time import time

if __name__ == "__main__":
    intitial_time = time()

    """
    # Our code, for example:
    count = 0
    while True:
        count += 1
        if count > 10000:
            break
    """

    final_time = time()
    print("Code execution time:", str(final_time - intitial_time))
