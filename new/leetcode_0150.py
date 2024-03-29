from typing import List


def main(tokens: List[str]) -> int:
    """逆波兰表达式求值

    Args:
        tokens (List[str]): token 字符串列表

    Returns:
        int: 求值结果
    """
    stack: List[int] = []
    for c in tokens:
        if c not in ("+", "-", "*", "/"):
            # * 当字符串非操作符时入栈
            stack.append(int(c))
        else:
            # * 每遇到一个操作符，就弹出两个数字，计算完成后再放入栈中
            num1 = stack.pop()
            num2 = stack.pop()
            if c == "+":
                stack.append(num2 + num1)
            elif c == "-":
                stack.append(num2 - num1)
            elif c == "*":
                stack.append(num2 * num1)
            else:
                stack.append(int(num2 / num1))

    return stack.pop()


if __name__ == "__main__":
    test_tokens = [
        "10",
        "6",
        "9",
        "3",
        "+",
        "-11",
        "*",
        "/",
        "*",
        "17",
        "+",
        "5",
        "+",
    ]
    print(main(test_tokens))
