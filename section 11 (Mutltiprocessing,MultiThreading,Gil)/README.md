# 📘 Section 11: Multiprocessing, Multithreading & GIL

This section explores Python's concurrency model — including the Global Interpreter Lock (GIL), threading, and multiprocessing — so you can write programs that efficiently use modern multi-core hardware.

---

## 📂 Files in This Section

| File | Topic |
|------|-------|
| `01_process.py` | Basic process creation with `multiprocessing.Process` |
| `02_process.py` | Process lifecycle — starting, joining, and terminating |
| `03_process _queue.py` | Inter-process communication using `multiprocessing.Queue` |
| `04_process_value.py` | Shared state between processes using `Value` and `Array` |
| `Concurrency & Parallelism.ipynb` | Core concepts and comparisons |
| `GIL.ipynb` | Deep-dive into the Global Interpreter Lock |
| `Gil_multiprocessing.py` | Demonstrating GIL limits in threads vs. multiprocessing |
| `thread.ipynb` | Threading fundamentals with `threading.Thread` |
| `Notes.excalidraw` | Architecture diagrams — concurrency models |

---

## ✅ What I Learned

### 🔹 Concurrency vs. Parallelism
- **Concurrency** — multiple tasks make progress by interleaving (not necessarily simultaneously)
- **Parallelism** — multiple tasks run at exactly the same time on separate CPU cores
- I/O-bound tasks benefit from concurrency (threads or async)
- CPU-bound tasks require true parallelism (multiprocessing)

### 🔹 Global Interpreter Lock (GIL)
- The GIL is a mutex that allows only one thread to execute Python bytecode at a time
- Prevents true parallel execution of threads for CPU-bound work
- Threading still benefits I/O-bound tasks because the GIL is released during I/O waits
- Multiprocessing bypasses the GIL by spawning separate Python interpreters
- How to measure GIL impact with timing benchmarks

### 🔹 Threading (`threading` module)
- Creating threads with `threading.Thread(target=func, args=(...))`
- `thread.start()` and `thread.join()` for lifecycle management
- `threading.Lock()` to prevent race conditions
- `threading.RLock()` for reentrant locking
- `threading.Event` for thread signalling
- Daemon threads — threads that die when the main process exits

### 🔹 Multiprocessing (`multiprocessing` module)
- Spawning processes with `multiprocessing.Process`
- `process.start()`, `process.join()`, `process.terminate()`
- `multiprocessing.Pool` for managing a pool of worker processes
- `Pool.map()` and `Pool.apply_async()` for parallel work distribution

### 🔹 Inter-Process Communication (IPC)
- `multiprocessing.Queue` — safe, FIFO message passing between processes
- `multiprocessing.Pipe` — bidirectional channel between two processes
- `multiprocessing.Value` — shared typed scalar (e.g., `ctypes.c_int`)
- `multiprocessing.Array` — shared typed array
- `multiprocessing.Manager` — creating shared lists, dicts, etc.

---

## 🛠️ Key Code Patterns

```python
import multiprocessing
import threading

# --- Threading ---
def io_task(name):
    import time
    time.sleep(1)
    print(f"Thread {name} done")

threads = [threading.Thread(target=io_task, args=(i,)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()

# --- Multiprocessing ---
def cpu_task(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(cpu_task, [10**6, 10**6, 10**6, 10**6])
    print(results)

# --- Inter-process queue ---
def producer(queue):
    for i in range(5):
        queue.put(i)

def consumer(queue):
    while not queue.empty():
        print(queue.get())

if __name__ == "__main__":
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,))
    p1.start(); p1.join()
    p2.start(); p2.join()

# --- Shared value ---
def increment(val, lock):
    for _ in range(100):
        with lock:
            val.value += 1

if __name__ == "__main__":
    shared = multiprocessing.Value("i", 0)
    lock = multiprocessing.Lock()
    procs = [multiprocessing.Process(target=increment, args=(shared, lock)) for _ in range(4)]
    for p in procs: p.start()
    for p in procs: p.join()
    print(shared.value)  # 400
```

---

## 📌 Prerequisites
- [Section 7–10: Advanced Python & OOP](../section%207-10/README.md)

## 📌 Next Section
➡️ [Section 12: Asyncio & Async Programming](../section%2012%20%28Asyncio%29/README.md)
