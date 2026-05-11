# AI Tools Setup Portfolio

This repository documents my first setup task for an AI-native growth marketing portfolio project. The goal was to install the required tools, create a public GitHub repository, and document the process clearly.

## Tools Installed

- **Cursor IDE** - installed through Windows Package Manager (`winget`) using the package `Anysphere.Cursor`.
- **Git for Windows** - installed through Windows Package Manager (`winget`) using the package `Git.Git`.
- **Claude Code extension for Cursor** - target extension: `anthropic.claude-code`.
- **Codex extension for Cursor** - target extension: `openai.chatgpt`.

## Steps Completed

1. Checked whether Git, GitHub CLI, and Cursor were already available on my computer.
2. Found that Git and Cursor were not initially available from the command line.
3. Used Windows Package Manager to search for Cursor and confirm the correct package name.
4. Installed Cursor IDE.
5. Installed Git for Windows.
6. Created this local project folder for the portfolio setup task.
7. Created this `README.md` file to document the tools installed, steps completed, issues encountered, and solutions.
8. Prepared the repository for committing and pushing to GitHub.

## Issues I Ran Into

### 1. Git was not recognized at first

When I first checked Git, PowerShell returned an error saying that `git` was not recognized as a command. This meant Git was either not installed or not available in the system PATH.

**How I solved it:**  
I installed Git for Windows using `winget`. After installation, I confirmed that Git was available at:

```text
C:\Program Files\Git\cmd\git.exe
```

### 2. Cursor was not installed at first

Cursor was not initially found in the normal installation paths.

**How I solved it:**  
I searched for Cursor through `winget`, confirmed the package `Anysphere.Cursor`, and installed it. After installation, Cursor was found at:

```text
C:\Users\vinnc\AppData\Local\Programs\cursor\Cursor.exe
```

### 3. The first installation attempt timed out

The combined installation command took too long and timed out. Cursor installed successfully, but the installer process continued running longer than expected.

**How I solved it:**  
I checked the running processes, confirmed Cursor was installed, stopped the stuck installer process, then installed Git separately.

### 4. Extension setup requires account login

The Claude Code and Codex extensions require logging in to their respective accounts after installation.

**How I handled it:**  
I identified the target extensions and will complete the login step inside Cursor using the Extensions panel:

- Claude Code: `anthropic.claude-code`
- Codex: `openai.chatgpt`

## What I Learned

This task helped me practice a simple but important workflow:

- Check the current environment before installing tools.
- Search for the correct package instead of guessing.
- Break a failed setup into smaller steps.
- Document problems clearly instead of hiding them.
- Use a public README as evidence of process, not just completion.

The main lesson is that tool setup is part of the work. When something fails, the useful response is to inspect the error, identify the next smallest step, and keep moving.

## Next Steps

- Open this repository in Cursor.
- Install and log in to Claude Code.
- Install and log in to Codex.
- Commit this README.
- Push the repository to GitHub.
- Send the public GitHub README link.
