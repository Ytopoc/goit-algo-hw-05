import re
from decimal import Decimal
#Функція що приймає рядок, перетворює числа з типу float на тип Decimal,і 
#повертае генератор усіх дійсних чисел з тексту 
def generator_numbers(text: str):
    numbers= re.findall(r' \d+.\d+ ',text)
    for num in numbers:
        yield Decimal(num) 

#Функція яка обчислює загальну суму доходу,з тексту, за допомогою генератора
def sum_profit(text,func):
    sum=0
    for number in func(text):
        sum+= number
    return sum

text = """Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, 
доповнений додатковими надходженнями 27.45 і 324.00 доларів."""

total_income=sum_profit(text,generator_numbers )
print(f"Загальний дохід: {total_income}")