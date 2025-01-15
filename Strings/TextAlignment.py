from StringPattern import trianglePattern

def main():
    n = int(input())
    string = 'H'
    repeat_string = string * n
    center_width = n * 2 - 1
    space_width = n * 2 + 1
    pattern_width = n * 5
    half_n = (n + 1) // 2

    print(trianglePattern(n, string, False))

    for i in range(n + 1):
        centered_string = repeat_string.center(center_width, ' ')
        print(f"{centered_string}{' ' * space_width}{centered_string}")

    for i in range(half_n):
        print(' ' * ((center_width - n) // 2) + string.center(pattern_width, string))

    for i in range(n + 1):
        centered_string = repeat_string.center(center_width, ' ')
        print(f"{centered_string}{' ' * space_width}{centered_string}")

    print(trianglePattern(n, string, True, " ", n * 4))

if __name__ == "__main__":
    main()
