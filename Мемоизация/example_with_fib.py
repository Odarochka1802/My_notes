from functools import lru_cache​

@lru_cache()
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

    
######
from functools import lru_cache

@lru_cache(typed=False)
def concat(text, num):
    return text + ' ' + str(num)

print(concat('beegeek', 4))
print(concat('beegeek', 5.0))
print(concat('beegeek', 4.0))
