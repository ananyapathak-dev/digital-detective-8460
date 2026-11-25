# Mission 6 — Git and GitHub

## 1. Task / objective
Understand the basic Git workflow (status, staging, committing, history), create and commit work on a new branch (`update-about`), explain the Pull Request workflow on GitHub, and build a personal Git command glossary.

## 2. Work completed
- Inspected repository status and commit history with `git status` and `git log --oneline`.
- Created the `update-about` branch locally, added a `"My Learning"` section to the root `README.md`, inspected the diff, staged `README.md`, and committed it on `update-about` (`630f92f`).
- Switched back to `main` and documented the Git workflow, Pull Request workflow, and Git glossary in this README.

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
|---|---|
| Check repository status (`git status`) | Shows the current branch, whether your branch is ahead/behind remote, and which files are modified, untracked, or staged for commit. |
| Stage selected changes (`git add <file>`) | Adds chosen file changes to the staging area (index) so you control exactly what goes into the next commit. |
| Create a commit (`git commit -m "..."`) | Saves a permanent snapshot of everything currently in the staging area into the repository's history with a descriptive message. |
| View commit history (`git log --oneline`) | Lists past commits with their short commit IDs and messages so you can trace how the project evolved. |

**Difference between staging a change and committing it:**
Staging (`git add`) prepares a draft list of changes in the staging area without permanently saving a version yet—you can still add more files or unstage changes. Committing (`git commit`) records the staged snapshot permanently into Git history as a checkpoint with an author, timestamp, and commit message.

### Task 6.2 — Create and use a branch
- Created and switched to branch `update-about` using `git checkout -b update-about`.
- Updated the root `README.md` on `update-about` by adding a `## My Learning` section describing three concepts learned so far.
- Checked `git status` and `git diff README.md`, then staged and committed the change with commit message `"Add My Learning section to root README"` (local commit `630f92f`).
- Switched back to `main` with `git checkout main`.

### Task 6.3 — Create a Pull Request
- **What a branch is:** A branch is an independent line of development that points to its own sequence of commits, letting you edit or test changes without altering the `main` branch until they are ready.
- **What a Pull Request (PR) is:** A Pull Request is a GitHub collaboration feature where you propose merging commits from one branch (such as `update-about`) into another (such as `main`), allowing others (or yourself) to review line-by-line diffs and discuss changes before merging.
- **Why they are useful when people work together:** Multiple contributors can work on separate features or bug fixes in parallel on their own branches without breaking `main`, and PRs provide a structured review checkpoint before changes become part of the shared codebase.
- **Current PR status:** **Completed and merged on GitHub (PR #1).**
  1. Pushed `main` and `update-about` to `origin`.
  2. Opened Pull Request `#1` (`Add My Learning section to root README`) from `update-about` into `main` on GitHub.
  3. Merged PR `#1` into `main` (commit `734a9d9`), and merged `origin/main` back into local `main` (resolving `README.md` merge markers cleanly).

### Task 6.4 — Build your Git command glossary

| Operation | Command | One-line explanation |
|---|---|---|
| Initialise a repository | `git init` | Turns the current folder into a new Git repository by creating its `.git` tracking directory. |
| Check status | `git status` | Displays the active branch and lists staged, unstaged, and untracked files. |
| Stage changes | `git add <path>` | Places selected modified or new files into the staging area for the next commit. |
| Commit changes | `git commit -m "message"` | Saves the staged snapshot into Git history with a descriptive commit message. |
| View history | `git log --oneline` | Shows a compact list of past commits from newest to oldest. |
| Create or list branches | `git branch [name]` | Lists existing local branches when run alone, or creates a new branch when given a name. |
| Switch branches | `git checkout <branch>` (or `git switch <branch>`) | Changes your working directory and `HEAD` to the selected branch (adding `-b` with `checkout` creates and switches in one step). |
| Publish changes | `git push [remote] [branch]` | Uploads local commits on a branch to the remote repository on GitHub. |
| Retrieve remote changes | `git pull` (or `git fetch`) | Downloads new commits from the remote repository (`git pull` also merges them into your current branch). |

## 3. Commands / tools used
- `git status` and `git diff`: Inspected working-tree state and exact line additions before committing.
- `git checkout -b update-about` and `git checkout main`: Created the feature branch and switched between branches.
- `git add` and `git commit`: Staged specific files and recorded separate commits on `update-about` and `main`.
- `git branch` and `git log --oneline --all --graph`: Verified branch pointers and commit history across both branches.

## 4. My understanding
Git separates *making edits*, *staging changes*, and *committing snapshots* so you can organize clean, logical checkpoints. Branches isolate new work from `main`, and Pull Requests on GitHub turn branch changes into a reviewable proposal before merging.

## 5. Difficulties faced
When merging `main` into `update-about` and bringing PR #1 back onto local `main`, `README.md` had conflicting edits between the `update-about` `"My Learning"` section and Mission 8's updated root `README.md`.

## 6. How I resolved them
Reviewed `README.md`, removed the Git conflict markers cleanly while keeping both the full Mission 8 visitor overview and the `"My Learning"` section, and committed the resolution.

## 7. Evidence / files
- [mission-06-git-github/README.md](README.md) — Workflow explanations, branch/PR notes, PR status, and Git glossary.
- Branch `update-about` (`630f92f`) and GitHub PR #1 (`734a9d9`, screenshot saved in `evidence/`).

## 8. Commit details
- Commit message on `update-about`: `Add My Learning section to root README` (`630f92f`)
- Commit message on `main`: `Complete Git and GitHub collaboration mission` (`ed7c080`)
- Follow-up status: PR #1 opened and merged (`734a9d9`) and pushed to GitHub.
