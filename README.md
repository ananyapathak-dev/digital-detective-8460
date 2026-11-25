# The Digital Detective

A system-exploration and independent learning project where I investigated how my computer works—from hardware and IPOS fundamentals to the Terminal, operating systems, program execution, number systems, Git/GitHub workflows, and computer networks.

Each mission was completed, documented in its own `README.md`, and recorded with a separate meaningful Git commit so progress is easy to review step by step.

## Topics Explored
- **Computer Fundamentals & IPOS**: Input, Processing, Output, and Storage, plus hardware vs. software and everyday computer systems.
- **Terminal & File Management**: CLI navigation, file creation/copying/moving, redirection, flags, pipes, and Homebrew package management.
- **Operating Systems**: System details, storage, processes and PIDs, absolute vs. relative paths, file permissions, and OS responsibilities.
- **How Programs Run**: Running Python 3 scripts and comparing compilers vs. interpreters.
- **Numbers & Data Representation**: Binary, decimal, and hexadecimal conversions, Python verification, building `number_converter.py`, and ASCII/UTF-8 text encoding.
- **Git & GitHub**: Staging vs. committing, branching (`update-about`), Pull Request workflow, and Git command glossary.
- **Computer Networks**: LAN/MAN/WAN, DNS, routers, protocols, packet switching, client-server communication, and how websites load.

## Mission Index
- [Mission 0: Workspace setup](mission-00-setup/README.md) — Completed & pushed
- [Mission 1: Computer basics](mission-01-computer-basics/README.md) — Completed & pushed
- [Mission 2: Terminal](mission-02-terminal/README.md) — Completed locally (push pending)
- [Mission 3: Operating system](mission-03-operating-system/README.md) — Completed locally (user process check & push pending)
- [Mission 4: Programs](mission-04-programs/README.md) — Completed locally (push pending)
- [Mission 5: Numbers and data](mission-05-numbers-data/README.md) — Completed locally (push pending)
- [Mission 6: Git and GitHub](mission-06-git-github/README.md) — Completed locally on `main` & `update-about` (push & PR pending)
- [Mission 7: Networking](mission-07-networking/README.md) — Completed locally with live `ping`/`nslookup` observations (push pending)
- [Mission 8: Final report](mission-08-final-report/README.md) — Completed locally (push & form submission pending)

## Running the Number Converter
To run the decimal-to-binary and hexadecimal converter from its mission folder:

```bash
cd mission-05-numbers-data
python3 number_converter.py
```

When prompted, type a whole decimal number (for example, `13`, `25`, or `255`) and press Enter to see its binary (`0b...`) and hexadecimal (`0x...`) equivalents.

## What I Learned
- **Systems work in layers**: User inputs flow through hardware, the operating system kernel, and application software, while data is stored as binary bits and encoded text (`ASCII` / `UTF-8`).
- **The Terminal and Git give repeatable control**: Small CLI commands, flags, pipes, and separate Git commits/branches keep work organized, verifiable, and easy to review.
- **Networks connect clients and servers reliably**: Domain names are resolved via DNS and transferred as packets across routers using shared protocols like `TCP/IP` and `HTTPS`.
