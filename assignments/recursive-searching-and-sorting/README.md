# 📘 Assignment: Recursive Searching and Sorting

## 🎯 Objective

Learn to think recursively by implementing classic searching and sorting algorithms in Python. You'll break problems into smaller pieces and wrap each algorithm in a clean, reusable function that hides the details behind a simple interface.

## 📝 Tasks

### 🛠️	Warm Up with Recursion

#### Description
Before tackling algorithms, practice the two parts of every recursive function: the **base case** (when to stop) and the **recursive case** (how to shrink the problem). Complete the warm-up functions in `starter-code.py`.

#### Requirements
Completed program should:

- Implement `recursive_sum(numbers)` that returns the sum of a list without using loops or `sum()`
- Implement `count_down(n)` that prints numbers from `n` down to `1`, then prints `"Liftoff!"`
- Clearly handle the base case in each function (e.g., an empty list or `n == 0`)

Example:

```
recursive_sum([3, 5, 2])  ->  10
count_down(3)
3
2
1
Liftoff!
```


### 🛠️	Implement Recursive Binary Search

#### Description
Write a recursive binary search that finds a target value in a **sorted** list by repeatedly checking the middle element and searching only the half where the target could be.

#### Requirements
Completed program should:

- Implement `binary_search(items, target, low, high)` using recursion (no loops)
- Return the index of `target` if found, or `-1` if it is not in the list
- Provide a simple wrapper `search(items, target)` so callers don't need to pass `low` and `high`
- Work correctly for an empty list, a single-element list, and targets at the start or end

Example:

```
search([2, 5, 8, 12, 16, 23, 38], 23)  ->  5
search([2, 5, 8, 12, 16, 23, 38], 7)   ->  -1
```


### 🛠️	Implement Recursive Merge Sort

#### Description
Write merge sort: split the list in half, recursively sort each half, then merge the two sorted halves together. Keep the merging logic in its own helper function.

#### Requirements
Completed program should:

- Implement `merge(left, right)` that combines two sorted lists into one sorted list
- Implement `merge_sort(items)` that recursively sorts a list and returns a **new** sorted list
- Not use Python's built-in `sort()` or `sorted()`
- Work correctly for empty lists, lists with duplicates, and already-sorted lists

Example:

```
merge_sort([38, 27, 43, 3, 9, 82, 10])  ->  [3, 9, 10, 27, 38, 43, 82]
merge_sort([])                          ->  []
```


### 🛠️	Build a Reusable Sorter (Stretch Goal)

#### Description
Use abstraction to make your algorithms more flexible. Add a `key` parameter so the same `merge_sort` can sort any kind of data, then combine sorting and searching to look up a student by score.

#### Requirements
Completed program should:

- Extend `merge_sort(items, key=None)` so it sorts by `key(item)` when a key function is given
- Sort the provided `students` list by score using `merge_sort(students, key=lambda s: s["score"])`
- Build a list of scores from the sorted students and use `search()` to find the index of a student who scored exactly `90`
- Keep the original `merge_sort` behavior working when no `key` is passed

Example:

```
Sorted by score: Leo (72), Mia (85), Ana (90), Sam (95)
Student with score 90: Ana
```
