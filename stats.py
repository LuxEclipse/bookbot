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
