# Starter Code for Recursive Searching and Sorting Assignment


# Task 1: Warm Up with Recursion
def recursive_sum(numbers):
    # TODO: Base case: empty list
    # TODO: Recursive case: first element + sum of the rest
    pass


def count_down(n):
    # TODO: Base case: print "Liftoff!" when n reaches 0
    # TODO: Recursive case: print n, then count down from n - 1
    pass


# Task 2: Implement Recursive Binary Search
def binary_search(items, target, low, high):
    # TODO: Base case: low > high means target is not in the list
    # TODO: Compare target with the middle element and recurse on one half
    pass


def search(items, target):
    # TODO: Call binary_search with the full range of the list
    pass


# Task 3: Implement Recursive Merge Sort
def merge(left, right):
    # TODO: Combine two sorted lists into one sorted list
    pass


def merge_sort(items):
    # TODO: Base case: lists with 0 or 1 items are already sorted
    # TODO: Split, sort each half recursively, then merge
    pass


# Task 4 (Stretch Goal): Build a Reusable Sorter
students = [
    {"name": "Ana", "score": 90},
    {"name": "Leo", "score": 72},
    {"name": "Sam", "score": 95},
    {"name": "Mia", "score": 85},
]


if __name__ == "__main__":
    print(recursive_sum([3, 5, 2]))
    count_down(3)
    print(search([2, 5, 8, 12, 16, 23, 38], 23))
    print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
