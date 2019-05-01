from dataclasses import dataclass


@dataclass
class Hello:
    name: str


def main():
    h = Hello(name='World')
    print(h.name)


if __name__ == '__main__':
    main()
