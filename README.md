# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Flowjack94/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Flowjack94/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Entry for the make.fun bounty "Sum up 19 November's world news in one image". `entry.png` is a 1024×1024 newspaper front page, "THE WORLD TODAY — THURSDAY 19 NOVEMBER 2026", with the stories that defined the day: the Trump–Xi–Putin trilateral summit in Shenzhen; the US–Iran exchange of fire across the Gulf; Grand Theft Auto VI's global rollout to a Metacritic 99; Nvidia's first all-hands under acting CEO Colette Kress; the EU's €45 billion Ukraine loan; the Fed signalling further rate hikes; and more — 30 stories in all, plus a world map pinning where each one happened. All stories were reported on 19 November 2026 (Reuters, BBC, Bloomberg, Financial Times, AP). Scene pictures are original flat illustrations drawn with PIL shapes (no text in them); all headlines, the date and labels are real text drawn onto the page, so the image reads cleanly at small sizes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). No network access; both runs write identical bytes.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=bbt3e5as&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
