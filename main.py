import sys


def get_book_text(filepath: str) -> str:
	"""Return the contents of `filepath` as a single string.

	Args:
		filepath: Relative or absolute path to a text file.

	Returns:
		The file contents as a string.
	"""
	with open(filepath, "r", encoding="utf-8") as f:
		return f.read()

from stats import count_words, char_counts, sorted_char_list


def main() -> None:
	# Expect exactly one CLI argument: path to the book file
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	path = sys.argv[1]
	text = get_book_text(path)
	num_words = count_words(text)
	print(f"Found {num_words} total words")
	# Compute character frequency dictionary (lowercased)
	chars = char_counts(text)
	# Convert to a sorted report (alphabetic chars only)
	report = sorted_char_list(chars)
	# Print the sorted report one-per-line as `char: num` to match tests
	for item in report:
		print(f"{item['char']}: {item['num']}")


if __name__ == "__main__":
	main()
