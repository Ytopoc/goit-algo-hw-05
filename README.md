# Python — Closures, Generators, Decorators

Three small exercises covering core Python idioms.

## Stack

- Python 3.12 (standard library only)

## Exercises

### `hw5_1.py` — caching Fibonacci via closure

`caching_fibonacci()` returns an inner `fibonacci(n)` that memoizes results in an enclosed `cache` dict. Demonstrates closures + memoization.

```python
fib = caching_fibonacci()
print(fib(15))   # 610
print(fib(10))   # 55
```

### `hw5_2.py` — generator + Decimal

- `generator_numbers(text)` yields every floating-point number found in a string, converted to `Decimal`.
- `sum_profit(text, generator_numbers)` sums them up — total income.

### `hw5_4.py` — error-handling decorators for an address book CLI

Three decorators that turn raw exceptions into user-friendly messages:

- `input_error_add_change` — `ValueError` → `"Give me name and phone please."`
- `input_error_phone` — `ValueError` / `IndexError` / `KeyError` → corresponding messages
- `input_error` — generic `"Invalid command."` fallback

Wrapped around the `add_contact`, `change_phone`, `phone_contact`, `show_all` functions.

## Run

```bash
python hw5_1.py
python hw5_2.py
python hw5_4.py
```
