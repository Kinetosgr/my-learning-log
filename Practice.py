# practice.py — daily coding practice
# 2026-09-19

def greet(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("world"))



# 2026-09-20
def is_even(n: int) -> bool:
    """Return True if n is even."""
    return n % 2 == 0


if __name__ == "__main__":
    print(is_even(4), is_even(7))



# 2026-09-23
def count_vowels(text: str) -> int:
    """Count vowels in a string (a, e, i, o, u)."""
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in text if ch in vowels)
# 2026-09-21
def reverse_string(text: str) -> str:
    """Return the reversed string."""
    return text[::-1]


# 2026-09-24
def unique_items(items: list) -> list:
    """Return unique items while keeping original order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# 2026-09-25
def word_count(text: str) -> int:
    """Return the number of words in a string."""
    return len(text.split())




# 2026-09-27
def clamp(value: float, low: float, high: float) -> float:
    """Keep value inside the range [low, high]."""
    return max(low, min(high, value))



# 2026-09-28
def average(numbers: list[float]) -> float:
    """Return the arithmetic mean of a non-empty list."""
    if not numbers:
        raise ValueError("numbers must not be empty")
    return sum(numbers) / len(numbers)


# 2026-09-30
def title_case(text: str) -> str:
    """Capitalize the first letter of each word."""
    return " ".join(word.capitalize() for word in text.split())


# 2026-10-01
def is_palindrome(text: str) -> bool:
    """Return True if the string reads the same forwards and backwards."""
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]



# 2026-10-04
def factorial(n: int) -> int:
    """Return n! for a non-negative integer."""
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# 2026-10-05
def flatten(items: list) -> list:
    """Flatten one level of nested lists."""
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


# 2026-10-06
def chunk(items: list, size: int) -> list[list]:
    """Split a list into groups of the given size."""
    if size <= 0:
        raise ValueError("size must be positive")
    return [items[i:i + size] for i in range(0, len(items), size)]



# 2026-10-07
def max_of(numbers: list[float]) -> float:
    """Return the largest number in a non-empty list."""
    if not numbers:
        raise ValueError("numbers must not be empty")
    best = numbers[0]
    for n in numbers[1:]:
        if n > best:
            best = n
    return best



# 2026-10-08
def slugify(text: str) -> str:
    """Turn a string into a URL-friendly slug."""
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in text)
    parts = [part for part in cleaned.split("-") if part]
    return "-".join(parts)



# 2026-10-09
def sum_range(start: int, end: int) -> int:
    """Return the sum of integers from start to end, inclusive."""
    if end < start:
        raise ValueError("end must be >= start")
    return sum(range(start, end + 1))

# 2026-10-11
def count_occurrences(items: list, target) -> int:
    """Return how many times target appears in the list."""
    return sum(1 for item in items if item == target)


# 2026-10-12
def rotate_left(items: list, steps: int = 1) -> list:
    """Rotate the list to the left by the given number of steps."""
    if not items:
        return []
    steps = steps % len(items)
    return items[steps:] + items[:steps]



# 2026-10-13
def starts_with(text: str, prefix: str) -> bool:
    """Return True if text starts with the given prefix."""
    return text.startswith(prefix)


# 2026-10-13
def starts_with(text: str, prefix: str) -> bool:
    """Return True if text starts with the given prefix."""
    return text.startswith(prefix)

# 2026-10-14
def ends_with(text: str, suffix: str) -> bool:
    """Return True if text ends with the given suffix."""
    return text.endswith(suffix)

# 2026-10-15
def contains(text: str, substring: str) -> bool:
    """Return True if the substring is found in text."""
    return substring in text

# 2026-10-16
def to_upper(text: str) -> str:
    """Return the string in uppercase."""
    return text.upper()


# 2026-10-17
def to_lower(text: str) -> str:
    """Return the string in lowercase."""
    return text.lower()

# 2026-10-18
def strip_whitespace(text: str) -> str:
    """Remove leading and trailing whitespace."""
    return text.strip()


# 2026-10-19
def replace_all(text: str, old: str, new: str) -> str:
    """Replace all occurrences of old with new."""
    return text.replace(old, new)

# 2026-10-20
def first_index(items: list, target) -> int | None:
    """Return the index of the first occurrence of target, or None if missing."""
    try:
        return items.index(target)
    except ValueError:
        return None


# 2026-10-21
def last_index(items: list, target) -> int | None:
    """Return the index of the last occurrence of target, or None if missing."""
    for i in range(len(items) - 1, -1, -1):
        if items[i] == target:
            return i
    return None



# 2026-10-22
def is_empty(items: list) -> bool:
    """Return True if the list has no elements."""
    return len(items) == 0


# 2026-10-23
def list_length(items: list) -> int:
    """Return the number of elements in the list."""
    return len(items)


# 2026-10-24
def join_with(items: list[str], separator: str = ", ") -> str:
    """Join a list of strings with the given separator."""
    return separator.join(items)


# 2026-10-25
def split_by(text: str, separator: str = " ") -> list[str]:
    """Split a string into a list using the given separator."""
    return text.split(separator)


# 2026-10-26
def remove_duplicates(items: list) -> list:
    """Return a new list with duplicates removed, keeping original order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result



# 2026-10-27
def reverse_list(items: list) -> list:
    """Return a new list with the elements in reverse order."""
    return list(reversed(items))



# 2026-10-28
def sort_numbers(numbers: list[float]) -> list[float]:
    """Return a new list of numbers sorted in ascending order."""
    return sorted(numbers)
