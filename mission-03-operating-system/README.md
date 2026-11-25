# Mission 3 — Understand the Operating System

## 1. Task / objective
Explore the operating system, running processes, storage, paths, and file permissions, and describe the core responsibilities of an operating system in plain words.

## 2. Work completed
- Inspected operating system version, kernel architecture, redacted account identity, disk storage, and system uptime/load in Terminal.
- Documented process concepts and PIDs, marking live `ps` / Activity Monitor inspection as a user practical task because process listing is restricted inside the sandboxed Terminal (`operation not permitted`).
- Compared absolute and relative paths using examples from this repository, and inspected owner permissions on a practice file.
- Completed the operating-system responsibilities table.

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
|---|---|---|
| Operating system / system details (`sw_vers`, `uname -smr`) | Identifies the OS name, version, kernel, and processor architecture. | `macOS 27.2.1` (Build `26B131`), kernel `Darwin 27.2.0 arm64`. |
| Current account identity (`id`) | Shows the active user ID, username, primary group, and group memberships. | `uid=501([redacted]) gid=20(staff)` with standard user and `admin` group memberships. |
| Available and used storage (`df -h`) | Reports total capacity, used space, available space, and usage percentage for mounted volumes. | System volume `/`: `460Gi` total, `13Gi` used, `36Gi` available (`27%`); data volume `/System/Volumes/Data`: `460Gi` total, `393Gi` used, `36Gi` available (`92%`). |
| System activity snapshot (`uptime`; `ps` / `top`) | Shows how long the system has been running, load averages, and active processes. | `uptime` reported `up 4 days, 18:51` with load averages `1.78 1.94 1.99`. Note: `ps` and `top` returned `operation not permitted` in the sandboxed shell; **[User action required]** run `ps aux \| head -n 15` or open Activity Monitor on your own Terminal to record a redacted process snapshot. |

### Task 3.2 — Understand processes
- **What is a process?** A process is an instance of a program currently loaded into memory and being executed or managed by the operating system.
- **What does the PID column represent?** `PID` stands for Process Identifier—a unique number assigned by the operating system to each running process so the OS can track, schedule, and control it individually.
- **Examples of processes:** Common examples on macOS include user applications (such as a web browser like Chrome or a code/text editor like VS Code or TextEdit) and background system services (such as `launchd`, which starts and manages system and user processes).
- **[User action required — practical verification]:** Open a browser or text editor, run `ps -eo pid,comm | head -n 20` in your macOS Terminal (or view Activity Monitor), and note two real PIDs without publishing private arguments or usernames.

### Task 3.3 — Understand paths and permissions
- **Absolute path vs. relative path:** An absolute path starts from the filesystem root (`/`) and uniquely identifies a file or folder regardless of your current directory. A relative path starts from your current working directory and changes meaning depending on where you are located.
  - **Absolute path example (from this repository, username redacted):** `/Users/[redacted]/Desktop/digital-detective-8460/mission-02-terminal/terminal-practice`
  - **Relative path example (when inside `digital-detective-8460`):** `mission-02-terminal/terminal-practice` (or `../mission-02-terminal` when inside `mission-03-operating-system`)
- **File permissions inspection:**
  Ran `ls -l mission-02-terminal/terminal-practice/notes.txt` and observed:
  ```text
  -rw-r--r--@ 1 [redacted]  staff  57 Nov 25 12:18 mission-02-terminal/terminal-practice/notes.txt
  ```
  - The leading `-` indicates a regular file.
  - The next three letters (`rw-`) belong to the **owner**: the owner **can read (`r`)** and **can write (`w`)** the file, and **cannot execute (`-`)** it as a program.
  - Group (`r--`) and others (`r--`) have read-only access. System permissions were not modified.

| Permission | Meaning | Example |
|---|---|---|
| `r` — Read | Allows a file's contents to be read. | Opening or displaying `notes.txt` with `cat`. |
| `w` — Write | Allows a file to be changed or saved. | Appending a line to `notes.txt`. |
| `x` — Execute | Allows a file to be run as a program; on a directory, allows entering/traversing it. | Running a script or opening a folder with `cd`. |

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
|---|---|---|
| Process management | Schedules CPU time among running programs, creates and ends processes, and assigns each a PID. | Switching smoothly between a browser, Terminal, and background services. |
| Memory management | Allocates RAM to active programs, prevents apps from overwriting each other's memory, and frees memory when programs close. | Giving RAM to VS Code while keeping Chrome's tabs separate. |
| Device management | Communicates with hardware peripherals through drivers and queues input/output requests. | Handling keyboard typing, trackpad clicks, and speaker audio output. |
| File management | Organizes data into files and directories on storage drives and tracks metadata like sizes and timestamps. | Saving `notes.txt` inside `terminal-practice` on the SSD. |
| User interface / shell | Provides a way for humans to interact with the OS either graphically (GUI) or via text commands (CLI). | Using Finder/macOS desktop (GUI) or `zsh` in Terminal (CLI). |
| Security and permissions | Verifies user accounts and enforces who can read, write, or execute specific files and system resources. | Restricting `notes.txt` write access to its owner (`rw-`) while allowing read-only (`r--`) to others. |

## 3. Commands / tools used
- `sw_vers` and `uname -smr`: Displays macOS version, build number, Darwin kernel version, and CPU architecture.
- `id`: Displays the active user account ID and group memberships (username redacted).
- `df -h`: Shows human-readable used and available disk space on mounted filesystems.
- `uptime`: Displays system uptime and recent CPU load averages.
- `ps` / `top`: Attempted for process listing (blocked with `operation not permitted` in sandbox; noted for user verification in host Terminal).
- `ls -l`: Displays detailed file metadata including owner, group, and `rwx` permission bits.
- `git add` and `git commit`: Stages and commits Mission 3 work locally.

## 4. My understanding
The operating system acts as the coordinator between hardware and applications. It keeps track of storage volumes, assigns unique PIDs to running programs, maps files using hierarchical paths, and protects files with `r`, `w`, and `x` permissions so users and programs only access what they are allowed to touch.

## 5. Difficulties faced
Running `ps` and `top` in the sandboxed Terminal environment returned `operation not permitted`, preventing direct capture of the live running process table from this environment.

## 6. How I resolved them
Recorded the real `uptime` load snapshot and OS/storage/permission outputs that succeeded, avoided fabricating process PIDs, and clearly marked live process-table inspection (`ps` / Activity Monitor) as a user practical task.

## 7. Evidence / files
- [mission-03-operating-system/README.md](README.md) — System exploration table, process notes, path/permission analysis, and OS responsibilities table.

## 8. Commit details
- Local commit message: `Document operating system and file management`
- Push status: Committed locally; **[User action required]** push to GitHub (`git push origin main`) and confirm on GitHub.
