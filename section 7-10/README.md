> 📌 *Personal learning notes from the <a href="https://www.udemy.com/course/full-stack-ai-with-python/">Full Stack Generative and Agentic AI with Python</a> course.*

# 📘 Section 7–10: Advanced Python & OOP

This section dives deeper into Python's programming model — generators, decorators, object-oriented design, comprehensions, and robust error handling. These patterns are used heavily in all later sections.

---

## 📂 Files in This Section

| File | Topic |
|------|-------|
| `Generators and Decorators.ipynb` | Generator functions, `yield`, decorator patterns |
| `OOPS.ipynb` | Object-oriented programming: classes, inheritance, polymorphism |
| `comprehension.ipynb` | List, dict, set, and generator comprehensions |
| `error Handling.ipynb` | Exception handling, custom exceptions, context managers |
| `generators.excalidraw` | Architecture diagram — generator lifecycle |
| `comprehensio.excalidraw.png` | Visual guide to comprehension syntax |

---

## ✅ What I Learned

### 🔹 Generators
- Creating generator functions with `yield`
- Lazy evaluation — values are produced on demand, not all at once
- `yield from` to delegate to sub-generators
- Generator expressions: `(x**2 for x in range(10))`
- Memory efficiency vs. list-based approaches
- `next()` and iteration protocol

### 🔹 Decorators
- Functions as first-class objects
- Writing a basic decorator using a wrapper function
- Preserving function metadata with `functools.wraps`
- Parameterised decorators (decorators that accept arguments)
- Common use-cases: logging, timing, authentication, caching
- Class-based decorators

### 🔹 Object-Oriented Programming (OOP)
- Defining classes with `__init__`, instance attributes, and methods
- Encapsulation — private attributes with name mangling (`_`, `__`)
- Inheritance — single and multiple inheritance
- Method overriding and `super()`
- Polymorphism — same interface, different behaviour
- Class methods (`@classmethod`) and static methods (`@staticmethod`)
- Properties with `@property`, `@setter`, `@deleter`
- Abstract base classes with `abc.ABC`

### 🔹 Comprehensions
- **List comprehension:** `[expr for item in iterable if condition]`
- **Dict comprehension:** `{k: v for k, v in pairs}`
- **Set comprehension:** `{expr for item in iterable}`
- **Generator expression:** `(expr for item in iterable)`
- Nested comprehensions for multi-dimensional data
- When to prefer comprehensions vs. loops for readability

### 🔹 Exception Handling
- `try / except / else / finally` blocks
- Catching specific exception types
- Re-raising exceptions with `raise`
- Creating custom exception classes inheriting from `Exception`
- Context managers with `with` statement
- Writing `__enter__` and `__exit__` for custom context managers
- `contextlib.contextmanager` decorator

---

## 🛠️ Key Code Patterns

```python
# Generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Decorator
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

# OOP
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says Woof!"

# Comprehension
squares = {x: x**2 for x in range(1, 11)}

# Custom exception
class InsufficientFundsError(Exception):
    def __init__(self, amount: float):
        super().__init__(f"Insufficient funds: need {amount}")
        self.amount = amount
```

---

## 📌 Prerequisites
- [Section 1–6: Python Fundamentals](../section%201-6/README.md)

## 📌 Next Section
➡️ [Section 11: Multiprocessing, Multithreading & GIL](../section%2011%20%28Mutltiprocessing%2CMultiThreading%2CGil%29/README.md)
