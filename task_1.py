from typing import Optional

array = "111110000"  # массив


def task(array: str) -> Optional[int]:
    for i in range(len(array)):
        if array[i] == "0":
            return i
    return None


assert task(array) == len(array)-4

print(task(array))
