def get_book_text(filepath: str) -> str:
	"""Return the contents of `filepath` as a single string.

	Args:
		filepath: Relative or absolute path to a text file.

	Returns:
		The file contents as a string.
	"""
	with open(filepath, "r", encoding="utf-8") as f:
		return f.read()


def count_words(text: str) -> int:
	"""Return the number of words in `text`.

	Words are identified by splitting on whitespace (Python's str.split()).
	"""
	return len(text.split())


def main() -> None:
	# Use the relative path to the downloaded Project Gutenberg copy
	path = "books/frankenstein.txt"
	text = get_book_text(path)
	num_words = count_words(text)
	print(f"Found {num_words} total words")


if __name__ == "__main__":
	main()
