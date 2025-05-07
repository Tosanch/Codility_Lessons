import zipfile
from io import BytesIO

# Content for README.md
readme_content = """# Codility Lessons 1–6 Solutions in Python 🧠🐍

This repository contains my original Python solutions to the Codility programming lessons 1 through 6.

Each script includes:
- A reworded description of the problem
- A clean, efficient solution using Python
- Inline comments for clarity (in most cases)

## 📚 Lessons Covered

1. **Iterations**
   - Binary Gap

2. **Arrays**
   - Cyclic Rotation
   - Odd Occurrences In Array

3. **Time Complexity**
   - Frog Jump
   - Perm Missing Elem
   - TapeEquillibrium

4. **Counting Elements**
   - Max Counters
   - Missing Integer
   - Frog River One
   - Perm Check

5. **Prefix Sums**
   - Passing Cars
   - Genomic Range Query
   - Count Div
   - Min Aberage Two Slice

6. **Sorting**
   - Distinct
   - Max Product of Three
   - Triangle

7. **Stacks and Queues**
   - Brackets
   - Fish
   - Nesting
   - StoneWall

8. **Leader**
   - Dominator
   - EquiLeader

9. **Maximum Slice Problem**
   - Max Profit
   - Max Slice Sum
   - Max Double Slice Sum

10. **Prime and Composite Numbers**
    - Count Factors
    - Min Perimeter Rectangle
    - Flags

11. **Sieve of Eratosthenes**
     - Count Non Divisible 
     - Count Semi Primes

12. **Euclidean Algorithm**
    - Chocolate by Numbers 
    - Common Prime Divisors

More lessons coming soon!



## ✅ How to Use

Each Python file is standalone and can be run directly. Example usage is included in comments at the top of each script.

To run a specific solution:
```bash
python <script_name>.py
