def trianglePattern(level, char, desc=True, space=" ", spaceBefore=0):
    lines = []
    count = 2 * level - 1

    if desc:
        for i in range(count, 0, -2):
            countSpace = (count - i) // 2
            line = space * spaceBefore + space * countSpace + char * i + space * countSpace
            lines.append(line)
    else:
        for i in range(1, count + 1, 2):
            countSpace = (count - i) // 2
            line = space * spaceBefore + space * countSpace + char * i + space * countSpace
            lines.append(line)

    return '\n'.join(lines)

# print(trianglePattern(5, '*', False, " ", 10))
