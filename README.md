## 🧠 Sorting algorithms Included

The repository includes implementations of:

* 🔹 Bubble Sort
* 🔹 Selection Sort
* 🔹 Insertion Sort
* 🔹 Merge Sort
* 🔹 Quick Sort
* 🔹 Counting Sort

## 🌲 Tree Structures (BST)

The repository contains a **Binary Search Tree (BST)** implementation and various tree traversal methods.
* **BST Operations**: Insertion, Search (DFS Recursive & Iterative, BFS), Height Calculation.
* **Traversals**: In-order, Pre-order, Post-order.

---

## ⚙️ How It Works

Each sorting algorithm:

* takes an array (or vector) as input
* sorts elements in ascending order
* outputs the sorted sequence

### Example:

```
Input:  5 2 9 1 3  
Output: 1 2 3 5 9
```

---

## ⚙️ Tree Example

```
Input Values: 10, 5, 4, 12, 1, 6, 8, 14, 11

Structure:
      10
    /    \
   5      12
  / \    /  \
 4   6  11  14
/     \
1      8

In-order Output (Sorted): 1 4 5 6 8 10 11 12 14
```

---

## 📊 Time Complexity

| Algorithm      | Best Case  | Average Case | Worst Case |
| -------------- | ---------- | ------------ | ---------- |
| Bubble Sort    | O(n)       | O(n²)        | O(n²)      |
| Selection Sort | O(n²)      | O(n²)        | O(n²)      |
| Insertion Sort | O(n)       | O(n²)        | O(n²)      |
| Merge Sort     | O(n log n) | O(n log n)   | O(n log n) |
| Quick Sort     | O(n log n) | O(n log n)   | O(n²)      |
| Counting Sort  | O(n + k)   | O(n + k)     | O(n + k)   |

---

## 📊 Tree Complexity


| Operation       | Average Case | Worst Case |
| --------------- | ------------ | ---------- |
| Search          | O(log n)     | O(n)       |
| Insertion       | O(log n)     | O(n)       |
| Traversal (All) | O(n)         | O(n)       |
| Height Calc     | O(n)         | O(n)       |

---

## 🧩 Project Structure

```
Sorting_algorithms/
│── bubble_sort.py
│── selection_sort.py
│── insertion_sort.py
│── merge_sort.py
│── quick_sort.py
│── counting_sort.py
Trees/
│── BST.py
│── traversal.py
│── search.py
README.md
```
