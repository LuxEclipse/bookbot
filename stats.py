"""Text analysis helpers for BookBot.

This module holds functions that analyze book text. Start small and add
additional helpers here (e.g., sentence_count, most_common_words, etc.).
"""
from typing import List


def count_words(text: str) -> int:
    """Return the number of words in `text`.

    Words are identified by splitting on whitespace (Python's `str.split()`).
    """
    return len(text.split())


def char_counts(text: str) -> dict:
    """Return a dictionary mapping each character (lowercased) to its frequency.

    The function converts the entire text to lowercase using `str.lower()` and
    counts every character, including spaces and punctuation. The returned
    dictionary keys are single-character strings and values are integers.
    """
    counts: dict[str, int] = {}
    for ch in text.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts
