import itertools
import time
import string
import pandas as pd

# Defining Variables: Chars (Search Space), Steps and Time the Script started
chars = string.printable
start_time = time.perf_counter()
steps = 0

# Creating empty Dataframe to store the Results of Combinations
results = pd.DataFrame(columns={"l","t","s"})

# Function to test out how long it takes to crack a given password
def crack(pw, length=1):
    global steps
    global start_time

    # Storing the password characters in a list
    pw_list = list(pw)
    subset = itertools.product(list(chars), repeat=length)

    # Iterating over all Possible Combinations of the Character Search Space
    for _ in subset:
        steps +=1

        # If the tried out combination matches the Password
        if list(_) == pw_list:
            print("------------------------")
            print("PW:".ljust(7), ''.join(list(_)))
            print("Tries:".ljust(7), steps)
            print("Sec:".ljust(7), round(time.perf_counter() - start_time,3))
            return

    # Recursion. Since in a real Situation we wouldnt know the length of the password, so we need to try out all Combinations from 1 to infinite Character length.
    # So after trying out all Combinations with the length of 1 in the given Searchspace, we try out all combinations with a length of 2 etc.
    crack(pw, length+1)


# Function to test how long it takes to search all possible Combinations with the given Max Length.
def combinations(max_length, printmode=True, length=1):
    global steps
    global start_time
    global results

    subset = itertools.product(list(chars), repeat=length)

    # Iterating over all combinations if the length of the password is smaller or equal to our given max length.
    if length <= max_length:
        for _ in subset:
            steps += 1
            print(_)

        # Recursion. See above
        combinations(max_length, printmode, length+1)

    # Stop for the Recursive Function. We are stopping in case the length is greater than our own given max length which we wanted to try out how long it takes to search.
    if length > max_length:
        sec = round(time.perf_counter() - start_time,3)

        # Appending the results to a Pandas Dataframe, so we can run the combinations function iterative and collect the results
        results = results.append({"l": max_length, "t": steps, "s": sec}, ignore_index=True)

        # Optional Boolean. If we only want to test out 1 given length we can print the results to console. Bit annoying when iterating
        if printmode == True:
            print("------------------------")
            print("Length:".ljust(7), max_length)
            print("Tries:".ljust(7), steps)
            print("Sec:".ljust(7), sec)


combinations(3)