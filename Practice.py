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



# 2026-09-21
def reverse_string(text: str) -> str:
    """Return the reversed string."""
    return text[::-1]
