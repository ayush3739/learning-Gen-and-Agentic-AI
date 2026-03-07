# 📘 Section 12: Asyncio & Async Programming

This section covers Python's native asynchronous programming model — `asyncio`, coroutines, event loops, and common concurrency pitfalls like race conditions and deadlocks.

---

## 📂 Files in This Section

| File | Topic |
|------|-------|
| `01_async_one.py` | Basic `async def` and `await` patterns |
| `02_async_two.py` | Running multiple coroutines concurrently |
| `03_async.py` | Advanced async patterns |
| `04_thread_async.py` | Mixing threads with the async event loop |
| `05_Process_Async.py` | Combining multiprocessing with asyncio |
| `06_bgWorker.py` | Background worker with `aiohttp` |
| `07_daemon__.py` | Daemon thread patterns alongside async |
| `08_non_daemon.py` | Non-daemon thread lifecycle |
| `09_race_condition.py` | Race condition examples and prevention with locks |
| `10_deadlock.py` | Deadlock simulation and avoidance strategies |
| `async.ipynb` | Comprehensive interactive async tutorial |
| `Async.excalidraw` | Event loop and task scheduling diagrams |

---

## ✅ What I Learned

### 🔹 Async / Await Basics
- Defining coroutines with `async def`
- Suspending execution with `await`
- Running a coroutine with `asyncio.run()`
- Understanding the event loop — a single thread that manages many tasks
- `asyncio.sleep()` vs. `time.sleep()` (non-blocking vs. blocking)

### 🔹 Concurrent Tasks
- `asyncio.create_task()` — schedule a coroutine as a Task
- `asyncio.gather(*coroutines)` — run multiple coroutines concurrently and collect results
- `asyncio.wait()` with `FIRST_COMPLETED` / `ALL_COMPLETED` strategies
- Task cancellation with `task.cancel()` and `asyncio.CancelledError`

### 🔹 Async HTTP with `aiohttp`
- Making concurrent HTTP requests without blocking
- `aiohttp.ClientSession` context manager
- Fetching multiple URLs simultaneously with `gather`
- Proper session lifecycle management

### 🔹 Mixing Threads and Async
- `asyncio.to_thread()` — run blocking code in a thread pool without blocking the event loop
- `loop.run_in_executor()` — the lower-level equivalent
- When to offload CPU-heavy or legacy blocking calls

### 🔹 Mixing Processes and Async
- Running CPU-bound tasks in separate processes from an async context
- `asyncio.get_event_loop().run_in_executor()` with `ProcessPoolExecutor`

### 🔹 Background Workers
- Implementing long-running background tasks inside async applications
- Periodic tasks with `asyncio.sleep()` inside infinite loops
- Graceful shutdown and cleanup

### 🔹 Daemon vs. Non-Daemon Threads
- Daemon threads are killed automatically when the main program exits
- Non-daemon threads must complete before the program can exit
- Choosing the right model depending on task criticality

### 🔹 Race Conditions
- What a race condition is — multiple coroutines/threads modifying shared state unsafely
- `asyncio.Lock()` to serialise access to shared resources
- `asyncio.Semaphore` to limit concurrent access

### 🔹 Deadlocks
- How deadlocks arise — two tasks each waiting for the other's lock
- Avoidance strategies: consistent lock ordering, timeouts, `asyncio.wait_for()`

---

## 🛠️ Key Code Patterns

```python
import asyncio
import aiohttp

# Basic coroutine
async def greet(name: str):
    await asyncio.sleep(1)  # non-blocking wait
    print(f"Hello, {name}")

asyncio.run(greet("World"))

# Run concurrently
async def main():
    await asyncio.gather(greet("Alice"), greet("Bob"), greet("Carol"))

asyncio.run(main())

# Concurrent HTTP requests
async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.text()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        return await asyncio.gather(*(fetch(session, u) for u in urls))

# Async lock (prevent race conditions)
lock = asyncio.Lock()
counter = 0

async def safe_increment():
    global counter
    async with lock:
        counter += 1

# Run blocking code in a thread
async def read_file(path):
    content = await asyncio.to_thread(open(path).read)
    return content
```

---

## 📌 Prerequisites
- [Section 11: Multiprocessing, Multithreading & GIL](../section%2011%20%28Mutltiprocessing%2CMultiThreading%2CGil%29/README.md)

## 📌 Next Section
➡️ [Section 13: Pydantic](../section%2013%20%28Pydantic%29/README.md)
