###############################
#  Author: Nicholas O'Kelley #
#  Date: May 31, 2020
#############################

"""
Generally, a k-permutation of n distinct objects (0 <= k <= n) is an arrangement of k of the n distinct
objects. Denoted by P(n,k) the number of k-permutations of n distinct objects. 

P(n, k) = n(n-1) ... (n - (k - 1)) = n!/(n-k)!
"""

import math

total_permutations = 0


def count_terms(array):
    count = {}

    for word in array:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


def generate_permutations(seq, curr_seq, index, used):
    global total_permutations

    if index == len(seq):
        print(curr_seq)
        total_permutations += 1
        return

    # then for every element left in the sequence we need to run
    # through each permuation and add it to the curr_seq
    for i in range(len(seq)):
        if not used[i]:
            curr_seq.append(seq[i])
            used[i] = True
            generate_permutations(seq, curr_seq, index + 1, used)
            curr_seq.pop()
            used[i] = False


def get_input():

    answer = input(
        "Would you like to use letters or integers?\n\n > ").lower().strip()
    valid = ["letters", "integers", "int"]

    while answer not in valid:
        print("You must make a choice.\n\n")
        answer = input("Would you like to use letters or integers?\n\n > ")

    if answer == 'letters':
        print("\nEnter the elements in the set:")
        user_sequence = list(input().split(' '))
        return user_sequence

    elif answer == 'integers':
        print("\nEnter the elements in the set:")
        user_sequence = list(map(int, input().split(' ')))
        return user_sequence


def generate_denom(term_count):
    denom = 1

    for key, value in term_count.items():
        denom = denom * math.factorial(value)
    return denom


def main():

    print("\n===== Welcome to the Permutation Generator! =====\n")

    user_sequence = get_input()
    term_count = count_terms(user_sequence)

    generate_permutations(user_sequence, [], 0, [
                          0 for i in range(len(user_sequence))])

    print("By the multiplication principle " + str(total_permutations))

    denominator = generate_denom(term_count)

    print("Thus, the total k-permutations of distinct objects is: " +
          str((total_permutations//denominator)))


if __name__ == "__main__":
    main()
