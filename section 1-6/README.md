# 📘 Section 1–6: Python Fundamentals

This section covers the essential Python building blocks needed for the rest of the course. The focus is on writing clean, idiomatic Python before moving into concurrency, data validation, and AI topics.

---

## 📂 Files in This Section

| File | Topic |
|------|-------|
| `lambda_functions.py` | Anonymous functions and functional programming patterns |
| `enumerate_func.py` | Indexed iteration with `enumerate()` |
| `Zip_Combine_list.py` | Merging iterables with `zip()` |
| `args_kwargs.py` | Flexible function signatures with `*args` and `**kwargs` |
| `Using Dictionary.py` | Dictionary operations, methods, and patterns |
| `Walrus_Operators.py` | Assignment expressions with `:=` (Python 3.8+) |
| `collections_datatype.py` | `Counter`, `defaultdict`, `OrderedDict`, `namedtuple` |
| `dunder_usecase.py` | Magic/dunder methods (`__str__`, `__repr__`, `__len__`, etc.) |

---

## ✅ What I Learned

### 🔹 Lambda Functions
- Creating short anonymous functions with `lambda`
- Using lambdas with `map()`, `filter()`, and `sorted()`
- Understanding when to use lambdas vs. regular functions

### 🔹 `enumerate()`
- Adding index counters to any iterable
- Starting index from a custom value: `enumerate(items, start=1)`
- Avoiding manual counter variables in loops

### 🔹 `zip()`
- Combining two or more iterables element-by-element
- Unpacking zipped pairs with tuple assignment
- Using `zip()` to build dictionaries from two lists

### 🔹 `*args` and `**kwargs`
- Accepting a variable number of positional arguments with `*args`
- Accepting keyword arguments dynamically with `**kwargs`
- Combining `*args`, `**kwargs`, and regular parameters in the correct order
- Unpacking arguments when calling functions

### 🔹 Dictionaries
- CRUD operations on dictionaries
- Iterating with `.items()`, `.keys()`, `.values()`
- Dictionary comprehensions
- Merging dictionaries with `**` unpacking and `|` operator (Python 3.9+)
- `dict.get()` with default values

### 🔹 Walrus Operator (`:=`)
- Assigning and evaluating in a single expression
- Using walrus in `while` loops and `if` conditions
- Reducing repeated computations in comprehensions

### 🔹 Collections Module
- `Counter` — counting occurrences, most-common elements
- `defaultdict` — auto-initialising missing keys
- `OrderedDict` — insertion-order guarantees (pre-Python 3.7 context)
- `namedtuple` — lightweight, readable struct-like objects

### 🔹 Dunder / Magic Methods
- `__str__` and `__repr__` for string representations
- `__len__`, `__getitem__`, `__setitem__` for container behaviour
- `__eq__`, `__lt__`, `__gt__` for comparisons
- `__call__` to make objects callable
- Understanding the Python data model

---

## 🛠️ Key Python Concepts Summary

```python
# Lambda
square = lambda x: x ** 2

# enumerate
for i, item in enumerate(["a", "b", "c"], start=1):
    print(i, item)

# zip
keys = ["name", "age"]
values = ["Alice", 30]
d = dict(zip(keys, values))

# *args / **kwargs
def greet(*args, **kwargs):
    print(args, kwargs)

# Walrus operator
while chunk := file.read(8192):
    process(chunk)

# Counter
from collections import Counter
counts = Counter("abracadabra")

# namedtuple
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
```

---

## 📌 Prerequisites
- Basic Python syntax (variables, loops, functions)

## 📌 Next Section
➡️ [Section 7–10: Advanced Python & OOP](../section%207-10/README.md)
