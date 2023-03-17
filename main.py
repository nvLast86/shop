from utils.item import *
import os

def main():
    phone1 = Phone('Iphone 14', 120_000, 5, 0)
    print(phone1)
    print(repr(phone1))
    phone1.number_of_sim = 0


if __name__ == "__main__":
    main()
