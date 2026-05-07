[English](README.md) | [**Українська**](README.uk.md)

# Python - замикання, генератори, декоратори

Три невеликі вправи, що охоплюють базові ідіоми Python.

## Стек

- Python 3.12 (тільки стандартна бібліотека)

## Вправи

### `hw5_1.py` - кешуючий Fibonacci через замикання

`caching_fibonacci()` повертає внутрішню функцію `fibonacci(n)`, що мемоізує результати в захопленому словнику `cache`. Демонструє замикання + мемоізацію.

```python
fib = caching_fibonacci()
print(fib(15))   # 610
print(fib(10))   # 55
```

### `hw5_2.py` - генератор + Decimal

- `generator_numbers(text)` yield-ить кожне число з плаваючою комою, знайдене у рядку, конвертоване у `Decimal`.
- `sum_profit(text, generator_numbers)` підсумовує їх - загальний дохід.

### `hw5_4.py` - декоратори обробки помилок для CLI адресної книги

Три декоратори, що перетворюють сирі виключення на дружні до користувача повідомлення:

- `input_error_add_change` - `ValueError` → `"Give me name and phone please."`
- `input_error_phone` - `ValueError` / `IndexError` / `KeyError` → відповідні повідомлення
- `input_error` - загальний fallback `"Invalid command."`

Обгортають функції `add_contact`, `change_phone`, `phone_contact`, `show_all`.

## Запуск

```bash
python hw5_1.py
python hw5_2.py
python hw5_4.py
```
