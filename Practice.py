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
