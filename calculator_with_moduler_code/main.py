# my_project/main.py
from calculator import add, subtract, multiply, divide

def main():
    print("Simple Calculator")
    print("1 + 2 =", add(1, 2))
    print("5 - 3 =", subtract(5, 3))
    print("4 * 3 =", multiply(4, 3))
    print("10 / 2 =", divide(10, 2))

if __name__ == "__main__":
    main()
