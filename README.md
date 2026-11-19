# The World in One Image — Wednesday 18 November 2026

[![Competition](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![Rank](https://make.fun/badge/news-image-20261118/Avapage/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![Reward](https://make.fun/badge/news-image-20261118/Avapage/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

Entry for the make.fun bounty [news-image-20261118](https://make.fun/bounty/news-image-20261118):
sum up the world's news of **Wednesday 18 November 2026** in one image.

## The image

A front-page collage drawn programmatically with Python/Pillow (`draw.py`),
1024×1024 PNG. Five stories a picture editor would lead with that day:

1. **Three powers meet in Shenzhen** — Xi Jinping hosts Vladimir Putin at the
   APEC summit; Donald Trump lands for the first US–China–Russia talks.
2. **Iran drones hit at US Gulf bases** — Kuwait and Bahrain intercept;
   US jets strike a missile site on Qeshm Island.
3. **141 drones over Ukraine in one night** — Kyiv downs 126; six hurt in Dnipro.
4. **Peltola flips Alaska Senate seat** — first Alaska Native senator;
   Democrats take the Senate 56–44 with their ninth flip of the midterms.
5. **US loses measles-free status** — held for 26 years; 5,412 cases,
   the worst toll since 1991.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (byte-identical to the bundled entry.png)
```

`main.py` is Python 3 standard library only and needs no network.
`draw.py` (Pillow) is the generator that produced `entry.png`; it is not
needed at grading time.

## License

MIT — see `LICENSE`.
