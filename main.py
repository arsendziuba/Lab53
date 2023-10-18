# Создаем переменную word
word = "Found name"

# Создаем словарь ids
ids = {"name": "Alice", "age": 27}

# Определяем функцию
def my_function(args, age=None, *other_args):
    print(f"{word}: {args}")
    print("Age:", age)
    print(other_args)

# Вызываем функцию с аргументами word и распаковкой аргументов из словаря ids
my_function(args=ids["name"], age=ids["age"])

# Вызываем функцию с аргументами word, ключом "name" из ids и распаковкой в список числовых значений от 0 до 9
my_function(ids["name"], ids["age"], *range(10))
