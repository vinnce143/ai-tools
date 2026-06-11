import json
import re
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi


VIDEOS = [
    {
        "expert": "Kevin Indig",
        "slug": "kevin-indig-seo-age-of-ai",
        "url": "https://www.youtube.com/watch?v=qujABKOAThA",
        "title": "SEO in the Age of AI | Kevin Indig on Google Overviews",
    },
    {
        "expert": "Lily Ray",
        "slug": "lily-ray-ai-search-fact-fiction",
        "url": "https://www.youtube.com/watch?v=2nJkT8zOzcM",
        "title": "Separating Fact from Fiction & How to Win in AI Search",
    },
    {
        "expert": "Mike King",
        "slug": "mike-king-ai-results-2026",
        "url": "https://www.youtube.com/watch?v=fKJ18NSHzCE",
        "title": "Ranking in Google's AI Results in 2026 with Mike King",
    },
    {
        "expert": "Aleyda Solis",
        "slug": "aleyda-solis-ai-search-action-checklist",
        "url": "https://www.youtube.com/watch?v=3xa199rr3zo",
        "title": "The AI Search Action Checklist | AirOps & Aleyda Solis",
    },
    {
        "expert": "Bernard Huang",
        "slug": "bernard-huang-future-discoverability",
        "url": "https://www.youtube.com/watch?v=f84ovVChEh4",
        "title": "The future of discoverability with Bernard Huang",
    },
    {
        "expert": "Ryan Law",
        "slug": "ryan-law-ai-search-real-data",
        "url": "https://www.youtube.com/watch?v=mL1W1SMtTT4",
        "title": "How to Win in AI Search (Real Data, No Hype)",
    },
    {
        "expert": "Ross Simmonds",
        "slug": "ross-simmonds-ai-seo-rank",
        "url": "https://www.youtube.com/watch?v=xLWBDKX-_3Q",
        "title": "How to Rank #1 When AI Is Taking Over ft. Ross Simmonds",
    },
    {
        "expert": "Andy Crestodina",
        "slug": "andy-crestodina-ai-funnel",
        "url": "https://www.youtube.com/watch?v=qrn2hOWa4fY",
        "title": "AI for Every Funnel Stage: From Content to Conversions",
    },
]


def video_id(url: str) -> str:
    match = re.search(r"v=([^&]+)", url)
    if not match:
        raise ValueError(f"Cannot parse video id from {url}")
    return match.group(1)


def main():
    out_dir = Path("research/youtube-transcripts")
    out_dir.mkdir(parents=True, exist_ok=True)
    index = []
    api = YouTubeTranscriptApi()

    for item in VIDEOS:
        vid = video_id(item["url"])
        path = out_dir / f"{item['slug']}.md"
        try:
            transcript = api.fetch(vid, languages=["en"])
            lines = [
                f"# {item['title']}",
                "",
                f"- Expert: {item['expert']}",
                f"- Source: {item['url']}",
                f"- Video ID: `{vid}`",
                "- Collection method: `youtube-transcript-api`",
                "",
                "## Transcript",
                "",
            ]
            for entry in transcript:
                start = getattr(entry, "start", None)
                text = getattr(entry, "text", "")
                if start is None and isinstance(entry, dict):
                    start = entry.get("start", 0)
                    text = entry.get("text", "")
                minutes = int(float(start) // 60)
                seconds = int(float(start) % 60)
                cleaned = " ".join(str(text).split())
                if cleaned:
                    lines.append(f"[{minutes:02d}:{seconds:02d}] {cleaned}")
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            status = "collected"
        except Exception as exc:
            path.write_text(
                "\n".join(
                    [
                        f"# {item['title']}",
                        "",
                        f"- Expert: {item['expert']}",
                        f"- Source: {item['url']}",
                        f"- Video ID: `{vid}`",
                        "- Collection method attempted: `youtube-transcript-api`",
                        "- Status: transcript unavailable or blocked by YouTube",
                        f"- Error summary: `{type(exc).__name__}: {str(exc)[:300]}`",
                        "",
                        "## Notes",
                        "",
                        "This placeholder preserves the source and failure mode. It is included because transcript availability varies by video and YouTube account/region.",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            status = "unavailable"
        index.append({**item, "video_id": vid, "status": status, "file": str(path)})

    Path("research/youtube-transcripts/index.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
    print(json.dumps(index, indent=2))


if __name__ == "__main__":
    main()
