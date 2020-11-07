###############################
#  Author: Nicholas O'Kelley #
#  Date: May 30, 2020
#############################

"""
    We want to determine all possible combinations of k numbers out of 1 .. n. 

    n choose K = n!/(k! * (n-k)!))
"""
import math


def create_list(increment, total, level, curr_list, total_list):
    if level == 0:
        total_list.append(curr_list[:])
        return

    for i in range(increment, total - level + 2):
        curr_list.append(i)
        create_list(i + 1, total, level - 1, curr_list, total_list)
        curr_list.pop()


def generate_combinations(n, k):

    combos = []
    create_list(1, n, k, [], combos)
    return combos


def main():
    n = int(input("Enter n: "))
    k = int(input("Enter k: "))
    combinations = generate_combinations(n, k)

    for i in combinations:
        print(i)

    print("All possible combinations: " + str(int((math.factorial(n) /
                                                   ((math.factorial(k) * math.factorial(n - k)))))))


if __name__ == "__main__":
    main()
