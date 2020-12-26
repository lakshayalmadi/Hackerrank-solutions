def print_formatted(number):
    for i in range(1,number+1):
        padding=n.bit_length()
        print(f'{i:{padding}d} {i:{padding}o} {i:{padding}X} {i:{padding}b}')
if __name__ == '__main__':
