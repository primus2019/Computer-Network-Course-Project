import unicodedata as ud


def example():
    test = 'ajsldfawhfewff'
    for ch in test:
        print(ud.name(ch))
        print(ud.category(ch))
        print(ud.numeric(ch))


if __name__ == '__main__':
    example()