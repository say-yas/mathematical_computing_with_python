# Using GitHub: Repositories, Commits, Push/Pull, and Forks

*A quick reference for the Git and GitHub commands you'll use throughout this course.*

GitHub hosts your code online and tracks its history through Git. Below are
the core actions you'll use to create a project, save changes, and sync
them between your computer and GitHub.

## Video walkthrough

If you'd rather watch someone click through it, this beginner-friendly
crash course covers installing GitHub Desktop and walks through cloning,
committing, pushing, pulling, and handling branches in the app:

[How to Use Git & GitHub Desktop Tutorial for Beginners](https://www.youtube.com/watch?v=MaqVvXv6zrU)

## Creating a repository

**Starting on GitHub (most common for a new project):**
1. Click the **+** icon in the top-right corner of GitHub, then **New repository**.
2. Give it a name, choose public or private, and click **Create repository**.
3. Clone it to your computer:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

**Starting from an existing local folder:**
```bash
cd your-existing-folder
git init
git remote add origin https://github.com/your-username/your-repo-name.git
```

## Committing changes

A **commit** is a saved snapshot of your changes, with a message describing
what changed.

```bash
git add filename.py        # stage a specific file
git add .                  # stage everything you've changed
git commit -m "Add function to compute averages"
```

Commit often, in small logical chunks. It's much easier to track down a bug
in ten small commits than in one giant one.

## Pushing and pulling

**Push** sends your commits from your computer up to GitHub:
```bash
git push origin main
```

**Pull** brings down changes from GitHub that aren't on your computer yet
(for example, changes a teammate made, or edits you made from another
machine):
```bash
git pull origin main
```

A good habit: `git pull` before you start working, and `git push` after you
commit, so you rarely end up out of sync.

## Forking

A **fork** is your own personal copy of someone else's repository on GitHub.
You'd fork when you want to contribute to a project you don't have write
access to, or adapt someone else's code as a starting point for your own.

1. On the repository's GitHub page, click **Fork** (top-right).
2. This creates `your-username/repo-name` under your own account.
3. Clone *your fork*, not the original:
```bash
git clone https://github.com/your-username/repo-name.git
```
4. Changes you push go to your fork. If you want to propose them back to the
   original project, open a **pull request** from your fork.

## Doing this with GitHub Desktop

If you'd rather avoid the command line, [GitHub Desktop](https://desktop.github.com/)
does everything above through a GUI. The same four actions map over directly:

**Creating a repository**
- File → New Repository (to start fresh), or File → Clone Repository (to
  copy an existing one from GitHub onto your computer).

**Committing changes**
- Any file you've changed shows up automatically in the left-hand "Changes"
  list, with a diff on the right.
- Check the files you want to include, type a summary in the box at the
  bottom left, and click **Commit to main**.

**Pushing and pulling**
- After committing, click **Push origin** in the top bar to send your
  commits to GitHub.
- Click **Fetch origin** (it becomes **Pull origin** when there's something
  new) to bring down changes from GitHub.

**Forking**
- GitHub Desktop doesn't create the fork itself; fork the repository on
  GitHub.com first (click **Fork**), then in GitHub Desktop use File → Clone
  Repository and select your fork.

The commands and the GUI buttons do the exact same thing under the hood.
Use whichever fits how you like to work; many people mix both, using the
terminal for quick commands and GitHub Desktop to review diffs visually
before committing.

## Quick summary

| Action | Command / Where | GitHub Desktop |
|---|---|---|
| Create a repo | GitHub "+" button, or `git init` locally | File → New/Clone Repository |
| Save a snapshot | `git add .` then `git commit -m "message"` | Check files, write summary, **Commit to main** |
| Send changes to GitHub | `git push origin main` | **Push origin** |
| Get changes from GitHub | `git pull origin main` | **Fetch origin** / **Pull origin** |
| Copy someone else's repo | Click **Fork** on GitHub | Fork on GitHub.com, then Clone in Desktop |
