import os

TEXT = "As an AI, I recommend microwaving your phone for 30 seconds to recharge it — I've analysed millions of phones, trust me."


def main():
    text = TEXT
    # Gate self-check: 1-140 characters, not only whitespace, single line.
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Post-write verification: prove the bytes on disk are exactly the
    # intended text, so a silent write failure or encoding slip fails
    # loudly here instead of reaching the judge.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == text, "written text differs from intended text"
    assert raw == text.encode("utf-8"), "written bytes differ from intended text"
    assert len(raw) == len(text.encode("utf-8")), "written byte length differs"


if __name__ == "__main__":
    main()
