# Mission 4 — How Programs Run

## 1. Task / objective
Create and run a simple Python 3 program (`hello.py`) from Terminal, and compare how compilers and interpreters translate or execute source code.

## 2. Work completed
- Created `mission-04-programs/hello.py` with a single-line Python statement displaying `"Hello from Python"`.
- Ran `python3 mission-04-programs/hello.py` in Terminal and observed the output `Hello from Python`.
- Completed the compiler vs. interpreter comparison table and summary explanation.

### Task 4.1 — Create and run a Python program
- File created: [hello.py](hello.py)
- Command run: `python3 mission-04-programs/hello.py`
- Observed output:
```text
Hello from Python
```

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | Translates the entire source program before execution begins; the compiled program is run afterwards. | Reads, translates, and executes instructions line by line (or bytecode statement by statement) at runtime. |
| Typical output | Produces a separate compiled file, such as a native machine-code executable binary. | Does not require a separate standalone machine-code executable; runs the source code directly and shows runtime output/errors as it goes. |
| One example | `gcc` / `clang` (for C or C++). | CPython (`python3`, which compiles to bytecode internally and interprets it in the Python virtual machine). |
| One advantage | Compiled binaries generally execute faster because translation work is already done ahead of time. | Faster edit-test cycle and easier cross-platform portability because you can run source code immediately without a separate build step. |

**Explanation in my own words:**
As shown in the comparison table, the main difference between a compiler and an interpreter is *when* code translation happens. A compiler translates the whole source file into machine code beforehand, producing a standalone executable that runs quickly once built. An interpreter, like `python3` running `hello.py`, processes and executes instructions at runtime without needing you to generate a separate executable file first. Because of this, compilers are great for high runtime performance, while interpreters make testing and running scripts across different systems quick and convenient.

## 3. Commands / tools used
- `python3 mission-04-programs/hello.py`: Runs the Python 3 interpreter on `hello.py`.
- `print(...)`: Python built-in function used to display text output to the Terminal.
- `git add` and `git commit`: Stages and commits Mission 4 files locally.

## 4. My understanding
Humans write code in readable programming languages, but CPUs only execute low-level machine instructions. Compilers and interpreters bridge that gap in different ways—either ahead of time into a binary executable or on the fly at runtime—and modern tools like Python often combine bytecode compilation with an interpreter loop.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [mission-04-programs/hello.py](hello.py) — Single-line Python program printing `"Hello from Python"`.
- [mission-04-programs/README.md](README.md) — Program execution record and compiler/interpreter comparison.

## 8. Commit details
- Local commit message: `Compare compilers and interpreters`
- Push status: Committed locally; **[User action required]** push to GitHub (`git push origin main`) and confirm on GitHub.
