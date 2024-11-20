a = int(input())

def main():
    return [int(digit) for digit in str(a)]

if __name__ == "__main__":
    digits = main()
    print("\n".join(map(str, digits)))