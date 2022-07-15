from typing import Optional

#массив
array = "111110000"

def task(array: str) -> Optional[int]:
    for i in range(len(array)):
        if array[i] == "0":
            return i
    return None

assert task(array) == len(array)-4
print(task(array))