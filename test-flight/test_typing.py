from typing import Union

def foo(condition: bool) -> Union[int, str]:
    if condition:
        return 42
    else:
        return "hello"

print(foo(True))
print(foo(False))
