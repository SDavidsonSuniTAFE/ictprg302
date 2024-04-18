#!/usr/bin/python3
def main():
    n = int(input("Enter a number: "))
    for i in range(n + 1):
        square = i * i
        cube = i * i * i
        print(f"The number is {i}, it's square is {square} and it's cube is {cube}.")

if __name__ == "__main__":
    main()