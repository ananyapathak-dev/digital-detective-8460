# Mission 2 — Become Comfortable with the Terminal

## 1. Task / objective
Use the command-line interface (Terminal) to inspect folders, create and manage practice files safely inside the repository, understand command flags and pipes, and explain how package managers work.

## 2. Work completed
- Practised basic navigation and file-management commands (`pwd`, `ls`, `ls -l`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`).
- Created a safe practice folder `mission-02-terminal/terminal-practice` and tested writing, appending, displaying, copying, and renaming text files.
- Compared standard `ls` output against `ls -lah` and piped `ls -l` output into `head -n 5`.
- Checked Homebrew's installed version and listed managed packages without installing or removing anything.

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
|---|---|---|
| Current-directory display (`pwd`) | Prints the full path of the working folder. | Displayed `/Users/[redacted]/Desktop/digital-detective-8460` (and `/Users/[redacted]/Desktop/digital-detective-8460/mission-02-terminal/terminal-practice` inside the practice folder). |
| Directory listing (`ls`) | Lists visible files and folders in the current directory. | Displayed `README.md`, `evidence`, and `mission-00-setup` through `mission-08-final-report` in columns. |
| Detailed listing (`ls -l`) | Shows permissions, link count, owner, group, file size in bytes, modification time, and item names. | Showed permissions such as `-rw-r--r--@` for `README.md` (`1036` bytes) and `drwxr-xr-x` for mission folders. |
| Change directory (`cd`) | Moves the current working location to another folder (`cd ..` moves up to the parent folder). | Moving into `mission-02-terminal/terminal-practice` updated the path reported by `pwd`; `cd ../..` returned to the repository root. |
| Create directory (`mkdir`) | Creates a new folder. | Created the `terminal-practice` folder inside `mission-02-terminal`. |
| Create empty file (`touch`) | Creates an empty file if it does not exist (or updates its timestamp). | Created `sample.txt` with a size of `0` bytes. |
| Copy file (`cp`) | Creates a duplicate of a file under a new name or location while keeping the original. | Copied `sample.txt` to `sample_copy.txt` without removing `sample.txt`. |
| Move / rename file (`mv`) | Moves a file to a new path or renames it in place. | Renamed `sample_copy.txt` to `sample_renamed.txt`; `sample_copy.txt` no longer appeared in `ls -l`. |
| Display file contents (`cat`) | Prints the text contents of a file to the Terminal. | Printed nothing for empty `sample.txt`, and printed both lines after text was written to `notes.txt`. |

### Task 2.2 — Practise file changes safely
Inside `mission-02-terminal/terminal-practice`, created `notes.txt`, wrote a first line using `>`, appended a second line using `>>`, verified both lines with `cat notes.txt`, created a backup copy (`notes_backup.txt`) with `cp`, and renamed it to `notes_archive.txt` with `mv`.

Observed output of `cat notes.txt`:
```text
First line of practice notes
Second line appended safely
```

Answers:
- **Difference between replacing a file's contents and adding text to the end:** Redirecting with `>` overwrites the entire file with new content, erasing anything previously saved. Appending with `>>` preserves existing content and adds the new line at the end of the file.
- **Difference between copying a file and moving a file:** Copying (`cp`) leaves the original file intact and creates an independent duplicate. Moving (`mv`) relocates or renames the original file so it only exists at the destination name/path.
- **Information provided by the current-directory display:** `pwd` prints the exact absolute path from the root directory `/` down to the current folder, helping confirm where commands will run before creating or editing files.
- **Why a directory-listing operation is useful:** `ls` lets you verify which files and subfolders exist, check spelling, and (with `-l`) inspect file sizes, timestamps, and permissions before modifying anything.

### Task 2.3 — Understand flags and pipes
- **Comparing `ls` and `ls -lah`:** Plain `ls` only showed visible file and folder names. Adding `-l` (long format), `-a` (all files including hidden entries starting with `.`), and `-h` (human-readable sizes) revealed `.`, `..`, and `.git`, and formatted file sizes such as `1.0K` for `README.md` instead of `1036` bytes.
- **Pipe example (`ls -l | head -n 5`):**
  ```text
  total 8
  -rw-r--r--@ 1 [redacted]  staff  1036 Nov 24 10:21 README.md
  drwxr-xr-x  3 [redacted]  staff    96 Nov 24 12:53 evidence
  drwxr-xr-x  3 [redacted]  staff    96 Nov 24 12:59 mission-00-setup
  drwxr-xr-x  3 [redacted]  staff    96 Nov 24 23:09 mission-01-computer-basics
  ```
  The pipe symbol (`|`) connects the standard output of the command on the left directly into the standard input of the command on the right. On the left, `ls -l` generates the full detailed directory listing; on the right, `head -n 5` filters that stream to display only the first 5 lines.

### Task 2.4 — Understand package managers
Checked Homebrew without installing or removing any packages:
- `brew --version` reported `Homebrew 7.0.9`.
- `brew list --formula` showed installed formulas such as `ca-certificates`, `ffmpeg`, `git`, `glib`, and `harfbuzz`.

Package managers are useful because they automate finding, downloading, installing, updating, and removing software from trusted repositories using simple commands. They also automatically resolve and install required dependencies so tools work properly without manual setup.

## 3. Commands / tools used
- `pwd`: Displays the absolute path of the current working directory.
- `ls`, `ls -l`, `ls -lah`: Lists folder contents in standard, detailed, and hidden/human-readable formats.
- `cd`: Changes the current working directory.
- `mkdir`: Creates new directories (`terminal-practice`).
- `touch`: Creates empty files (`sample.txt`).
- `cp` and `mv`: Copies files and moves or renames files.
- `cat`: Displays file contents in the Terminal.
- `>` and `>>`: Redirects output to overwrite (`>`) or append (`>>`) to a file.
- `|` and `head -n 5`: Sends one command's output into another command to keep only the first 5 lines.
- `brew --version` and `brew list`: Checks the installed Homebrew version and lists managed packages.
- `git add` and `git commit`: Stages and records Mission 2 files locally.

## 4. My understanding
Working in the Terminal gives direct control over files and folders using short text commands. Flags modify how a command behaves, and pipes let small single-purpose commands work together by passing text output from one command to the next. Practising inside a dedicated subfolder keeps experiments safe and prevents accidental changes elsewhere.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [mission-02-terminal/README.md](README.md) — Command reference table, task answers, flags/pipes comparison, and Homebrew notes.
- `mission-02-terminal/terminal-practice/` — Practice folder containing `sample.txt`, `sample_renamed.txt`, `notes.txt`, and `notes_archive.txt`.

## 8. Commit details
- Local commit message: `Complete Terminal and file management mission`
- Push status: Committed locally; **[User action required]** push to GitHub (`git push origin main`) and confirm on GitHub.
