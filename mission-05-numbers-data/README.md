# Mission 5 — Numbers and Data

## 1. Task / objective
Convert decimal, binary, and hexadecimal numbers by hand, verify those conversions in Python, build and test `number_converter.py`, and explain how characters are stored using text-encoding standards.

## 2. Work completed
- Completed step-by-step hand conversions for all seven questions in Task 5.1.
- Verified decimal, binary, and hexadecimal conversions in Python 3.
- Built `mission-05-numbers-data/number_converter.py` using `input()`, `int()`, `bin()`, and `hex()` and tested it with three positive decimal integers (`13`, `25`, `255`) plus invalid input (`abc`).
- Answered the text-encoding questions for ASCII and UTF-8.

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
|---|---|
| Convert decimal 13 to binary. | Divide repeatedly by 2 and read remainders bottom-to-top: `13 / 2 = 6 R 1`, `6 / 2 = 3 R 0`, `3 / 2 = 1 R 1`, `1 / 2 = 0 R 1`. Answer: **`1101`** (8 + 4 + 0 + 1 = 13). |
| Convert decimal 25 to binary. | Divide repeatedly by 2: `25 / 2 = 12 R 1`, `12 / 2 = 6 R 0`, `6 / 2 = 3 R 0`, `3 / 2 = 1 R 1`, `1 / 2 = 0 R 1`. Read remainders bottom-to-top. Answer: **`11001`** (16 + 8 + 0 + 0 + 1 = 25). |
| Convert binary 1010 to decimal. | Multiply each bit by its power of 2: `(1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰) = 8 + 0 + 2 + 0`. Answer: **`10`**. |
| Convert binary 1101 to decimal. | Multiply each bit by its power of 2: `(1 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰) = 8 + 4 + 0 + 1`. Answer: **`13`**. |
| Convert hexadecimal A to decimal. | In base 16, `A` represents 10: `10 × 16⁰`. Answer: **`10`**. |
| Convert hexadecimal 1F to decimal. | In base 16, `F` represents 15: `(1 × 16¹) + (15 × 16⁰) = 16 + 15`. Answer: **`31`**. |
| Convert binary 1111 to hexadecimal. | Group 4 bits into one hex digit: `(1 × 8) + (1 × 4) + (1 × 2) + (1 × 1) = 15`, and 15 in hexadecimal is `F`. Answer: **`F`**. |

### Task 5.2 — Verify using Python
Verified the conversions using Python 3 (`python3`):

| Expression tested | Observed Python result | Matches manual calculation? |
|---|---|---|
| `bin(13)` | `'0b1101'` | Yes (`1101`) |
| `bin(25)` | `'0b11001'` | Yes (`11001`) |
| `int('1010', 2)` | `10` | Yes (`10`) |
| `int('1101', 2)` | `13` | Yes (`13`) |
| `int('A', 16)` | `10` | Yes (`10`) |
| `int('1F', 16)` | `31` | Yes (`31`) |
| `hex(int('1111', 2))` | `'0xf'` | Yes (`F`) |
| `hex(31)` | `'0x1f'` | Yes (`1F`) |

### Task 5.3 — Build a small number converter
Created [number_converter.py](number_converter.py). It reads a decimal integer from the user with `input()`, converts the string into an integer using `int()` (with a `try/except ValueError` check for invalid input), and converts that integer into binary (`bin()`) and hexadecimal (`hex()`).

- **What `bin()` does:** Takes an integer and returns its binary representation as a string prefixed with `0b` (base 2).
- **What `hex()` does:** Takes an integer and returns its hexadecimal representation as a string prefixed with `0x` (base 16, using `0–9` and `a–f`).

Observed test runs from Terminal (`python3 mission-05-numbers-data/number_converter.py`):

| Test number | Binary output | Hexadecimal output |
|---|---|---|
| `13` | `0b1101` | `0xd` |
| `25` | `0b11001` | `0x19` |
| `255` | `0b11111111` | `0xff` |

### Task 5.4 — How is text stored?
- **ASCII decimal codes (verified with Python `ord()`):**
  - Uppercase `A`: **`65`** (`ord('A') -> 65`)
  - Lowercase `a`: **`97`** (`ord('a') -> 97`)
- **Why a computer needs an encoding standard to store text:** Computers can only store and process binary numbers (`0`s and `1`s), not visual letters. An encoding standard creates a shared mapping between characters and numbers so different programs and computers read and display the same text consistently.
- **Example of a character not in basic ASCII:** `₹` (Indian Rupee sign), `é` (accented e), or `😊` (emoji) — basic 7-bit ASCII only covers codes `0–127`, whereas UTF-8 supports international scripts, accented letters, currency symbols, and emojis.

## 3. Commands / tools used
- `python3`: Used to verify conversion expressions and run `number_converter.py`.
- `input()` and `int()`: Reads user input as text and converts it to a decimal integer.
- `bin()` and `hex()`: Built-in Python functions that convert an integer to binary (`0b...`) and hexadecimal (`0x...`) strings.
- `ord()`: Built-in Python function used to confirm ASCII decimal codes for `'A'` and `'a'`.
- `git add` and `git commit`: Stages and commits Mission 5 files locally.

## 4. My understanding
Every number and character inside a computer is stored in binary. Decimal, binary, and hexadecimal are simply different bases for representing the exact same numeric values, with hexadecimal acting as a compact shorthand where one hex digit represents four binary bits. Character encodings such as ASCII and UTF-8 assign standard numeric codes to letters and symbols so text can be stored in binary and shared reliably.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [mission-05-numbers-data/number_converter.py](number_converter.py) — Interactive Python decimal-to-binary/hexadecimal converter.
- [mission-05-numbers-data/README.md](README.md) — Hand calculations, Python verification, converter test table, and text-encoding answers.

## 8. Commit details
- Local commit message: `Build number converter and practise data representation`
- Push status: Committed locally; **[User action required]** push to GitHub (`git push origin main`) and confirm on GitHub.
