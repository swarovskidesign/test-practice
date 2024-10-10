a = int(input())

def main():
    return [int(digit) for digit in str(a)]

if __name__ == "__main__":
    digits = main()
    total = sum(digits)
    total2 = 1
    
    for digit in digits:
        total2 *= digit

    if total == total2:
        print("great")

    else:
        print("none")