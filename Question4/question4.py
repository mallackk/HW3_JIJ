import math

def main():
    for i in range(15):
        if (i % 2 == 0):
            print(f"The factorial of {i} is {math.factorial(i)}")

if __name__ == "__main__":
    main()