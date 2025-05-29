""" 
🔸 Codewars 6 kyu Kata
Title: Sum of Intervals

📝 Description:
Write a function that accepts a list of intervals and returns the sum of all the interval lengths, ignoring any overlapping intervals.

Each interval is a tuple/list with two integers [start, end], where start < end.

📌 Function Signature:
python
Copy
Edit
def sum_of_intervals(intervals: list[list[int]]) -> int:
    pass
🧪 Examples:
python
Copy
Edit
sum_of_intervals([[1, 4], [7, 10], [3, 5]])         # ➞ 7  (1-5 and 7-10)
sum_of_intervals([[1, 2], [6, 10], [11, 15]])       # ➞ 9
sum_of_intervals([[1, 5], [10, 20], [1, 6], [16, 19]]) # ➞ 19
💡 Notes:
Intervals may overlap.

Overlapping parts should only be counted once.

Intervals are not necessarily sorted. question more explain



"""

# Function to calculate the sum of the lengths of all intervals in the list
def sum_of_intervals(list1):
    q = 0
    for interval in list1:
        start, end = interval
        q += end - start
    return q

if __name__ == "__main__":
    print(sum_of_intervals([[1, 4], [7, 10], [3, 5]]))
    print(sum_of_intervals([[1, 2], [2, 6], [8, 10]]))
    print(sum_of_intervals([[5, 8], [1, 3], [8, 10]]))
    print(sum_of_intervals([[1, 5]]))
    print(sum_of_intervals([]))
 
