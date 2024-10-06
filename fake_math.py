# ложная математика
def divide(first, second):
    if first > 0 and second > 0:
        print (first/second)
        return (" ")
    elif second == 0:
        print("Ошибка")
        return (" ")


result1 = divide(69, 3)
result2 = divide(3, 0)
print(result1)
print(result2)