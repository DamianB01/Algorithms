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

## 🕸️ Graph Algorithms

The repository features graph representations and algorithms for searching and pathfinding weighted graphs.

* **Representations**: Adjacency List (Dictionaries)
* **Search Algorithms**:
    * **BFS (Breadth-First Search)**: Standard version with `visited` set to find the shortest path in graphs.
    * **DFS (Depth-First Search)**: Recursive version for exploring graph components.
* **Shortest Path**:
    * **Dijkstra's Algorithm**: Efficient pathfinding for weighted graphs using a Priority Queue (`heapq`).

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

## ⚙️ Dijkstra's Example

```
Graph:
A --(5)--> B --(1)--> D
A --(3)--> C --(7)--> D

Execution:
1. Start at A (dist: 0)
2. Explore C (3) and B (5)
3. From B, find D (5+1 = 6)
4. From C, find D (3+7 = 10) -> Rejected (6 is better)

Result: {'A': 0, 'B': 5, 'C': 3, 'D': 6}
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

## 📊 Graph Complexity


| Algorithm       | Complexity (Adjacency List) | Use Case |
| --------------- | --------------------------- | -------- |
| BFS             | O(V + E)                    | Shortest path (unweighted) |
| DFS             | O(V + E)                    | Connectivity, Cycles |
| Dijkstra        | O(E log V)                  | Shortest path (weighted) |

*V = vertices, E = edges*

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
Graphs/
│── graphs.py
│── dijkstra.py
│── search_graphs.py
README.md
```
