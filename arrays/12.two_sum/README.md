# Search element



---

## 🔗 Problem Link

[GeeksforGeeks – Two Sum](https://www.geeksforgeeks.org/problems/key-pair5616/1)

---

## ✍️ Notes

✅ 1. GFG Version – Two-Pointer Approach
Code: Returns True or False (not indices)
Why?:

In GFG problems, the question often asks “Is there a pair?”, not which one.

Sorting is allowed and doesn't affect the output.

So, the two-pointer approach works well after sorting.

Steps:

Sort the array.

Use two pointers (start, end) to find the pair.

🕒 Time Complexity: O(n log n) (due to sorting)
📦 Space Complexity: O(1) (no extra space)

---

✅ 2. LeetCode Version – Hashmap (Dictionary) Approach
Code: Returns the indices of the two elements
Why?:

In LeetCode, the question is: "Return the indices of the elements that add to target."

If we sort the array, the original indices will be lost.

So we use a hashmap to store values and their original indices.

Steps:

Loop through array.

Store number and its index in a hashmap.

Check if complement exists.

🕒 Time Complexity: O(n)
📦 Space Complexity: O(n) (for hashmap)


---
