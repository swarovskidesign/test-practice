a = int(input())

def main():
    return [int(digit) for digit in str(a)]

if __name__ == "__main__":
    digits = main()
    total2 = 1
    
    for digit in digits:
        total2 *= digit
    print(total2)