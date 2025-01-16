def print_formatted(number):
    width = len(bin(number).replace('0b', ''))
    for i in range(1, number + 1):
        decimal = str(i).rjust(width)
        octal = str(oct(i)).replace('0o', '').rjust(width)
        hexa = str(hex(i)).replace('0x', '').upper().rjust(width)
        binary = str(bin(i)).replace('0b', '').rjust(width)
        print(f"{decimal} {octal} {hexa} {binary}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)