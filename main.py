from utils.item import *
from utils.keyboard import KeyBoard


def main():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    print(kb)

    print(kb.language)

    kb.change_lang()
    print(kb.language)

    kb.language = 'CH'


if __name__ == "__main__":
    main()
