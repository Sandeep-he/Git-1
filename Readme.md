# Vector Dot-Product Implementation

This repository contains an implementation of the **vector dot-product** algorithm in Python. The dot product is a fundamental operation in linear algebra, widely used in various applications like machine learning, physics, and computer graphics.

---

## 📖 **Mathematical Expression**
The dot product of two vectors **A** and **B** of length **n** is given by:

\[
\mathbf{A} \cdot \mathbf{B} = \sum_{i=1}^n A_i \cdot B_i
\]

Where:
- \( A_i \) and \( B_i \) are the elements of the vectors at index \( i \).

---

## 🧩 **Implementation**

Here is a basic Python implementation of the dot product:

```python
def dot_product(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must be of the same length.")
    return sum(a * b for a, b in zip(vector_a, vector_b))

# Example Usage
vector_a = [1, 2, 3]
vector_b = [4, 5, 6]
result = dot_product(vector_a, vector_b)
print("Dot Product:", result)  # Output: 32
