# AI Tools Setup Portfolio

This repository documents my first setup task for an AI-native growth marketing portfolio project. The goal was to install the required tools, create a public GitHub repository, and document the process clearly.

## Research Project: AI-Powered SEO Content Production

For the second portfolio step, I chose **AI-powered SEO content production**.

I chose this topic because it connects directly to AI-native growth marketing: content strategy, SEO, AI search, editorial quality control, and repeatable marketing workflows. It is also a topic where the quality of sources matters. Generic AI content advice is easy to find, so I focused on practitioners who actively build, test, teach, or challenge SEO and content systems in public.

## What I Collected

- A source index of 10 experts: `research/sources.md`
- YouTube transcript files collected with a free transcript API method: `research/youtube-transcripts/`
- LinkedIn recent-activity notes checked through signed-in browser access and organized by author: `research/linkedin-posts/`
- Additional public articles and materials: `research/other/articles-and-materials.md`
- A transcript collection script: `scripts/collect_youtube_transcripts.py`

## Repository Structure

```text
research/
  sources.md
  linkedin-posts/
    kevin-indig.md
    lily-ray.md
    mike-king.md
    aleyda-solis.md
    bernard-huang.md
    ryan-law.md
    ross-simmonds.md
    andy-crestodina.md
    tim-soulo.md
    rand-fishkin.md
  youtube-transcripts/
    index.json
    kevin-indig-seo-age-of-ai.md
    lily-ray-ai-search-fact-fiction.md
    mike-king-ai-results-2026.md
    aleyda-solis-ai-search-action-checklist.md
    bernard-huang-future-discoverability.md
    ryan-law-ai-search-real-data.md
    ross-simmonds-ai-seo-rank.md
    andy-crestodina-ai-funnel.md
  other/
    articles-and-materials.md
scripts/
  collect_youtube_transcripts.py
```

## Collection Method

I used Codex to help structure the repository, write the collection script, and organize the research notes. For YouTube, I used `youtube-transcript-api` to collect transcripts when captions were available. The script saves each transcript as a Markdown file and also creates an `index.json` file showing the collection status for each video.

For LinkedIn, I used signed-in browser access to check visible recent activity pages on 2026-06-11. I summarized the posts and profile signals instead of copying full post text into the repository, then connected those notes to stronger public sources such as blogs, videos, company sites, and newsletters.

## Expert Selection Criteria

I selected experts who are useful for a real AI-powered SEO content production playbook:

- They are practitioners, founders, CMOs, SEO consultants, or content operators.
- They publish or teach about AI search, SEO, content quality, audience research, or B2B content distribution.
- Their material is specific enough to support later synthesis, not just generic AI advice.
- Together, they cover technical SEO, editorial quality, AI search visibility, distribution, analytics, and strategy.

## Limitations

One selected YouTube transcript for Ross Simmonds was not available through the free transcript collection method. I kept the placeholder file and documented the unavailable status in `research/youtube-transcripts/index.json` instead of removing it, because the limitation is useful context for the research process.

## Future Playbook Direction

This research pack can support a later playbook covering:

1. How to choose AI-assisted SEO content opportunities.
2. How to collect expert and source material before drafting.
3. How to use AI for research support without publishing generic output.
4. How to fact-check and edit AI-assisted drafts.
5. How to optimize for classic search and AI answer engines.
6. How to distribute content beyond a blog post.
7. How to measure visibility when clicks are harder to rely on.

## Tools Installed

- **Cursor IDE** - installed through Windows Package Manager (`winget`) using the package `Anysphere.Cursor`.
- **Git for Windows** - installed through Windows Package Manager (`winget`) using the package `Git.Git`.
- **Claude Code extension for Cursor** - target extension: `anthropic.claude-code`.
- **Codex extension for Cursor** - target extension: `openai.chatgpt`.

## Initial Setup Steps Completed

1. Checked whether Git, GitHub CLI, and Cursor were already available on my computer.
2. Found that Git and Cursor were not initially available from the command line.
3. Used Windows Package Manager to search for Cursor and confirm the correct package name.
4. Installed Cursor IDE.
5. Installed Git for Windows.
6. Created this local project folder for the portfolio setup task.
7. Created this `README.md` file to document the tools installed, steps completed, issues encountered, and solutions.
8. Committed and pushed the setup README to GitHub.

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
I identified the target extensions and handled the account login step inside Cursor using the Extensions panel:

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

## Current Status

The setup task and the AI-powered SEO content production research task have both been committed and pushed to GitHub. The repository now contains the setup documentation, transcript collection script, expert source index, transcript files, LinkedIn recent-activity notes, and supporting source materials.
