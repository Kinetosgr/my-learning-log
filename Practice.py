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
