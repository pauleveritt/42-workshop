"""30: Split Screen Without Tabs

Get your code and tests side-by-side without resorting to tabs.

- Side-by-side without tabs

- Split Vertically

- Alt-Tab to go to next splitter

- Open ``tests/test_examples.py``

- Run tests

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/
"""
from random import choice

from fortytwo import App
from fortytwo.models import Greeter

customers = ('Larry', 'Alice', 'Sam')


def main():
    site = App()
    with site as container:
        for i in range(10):
            greeter = container.get(Greeter)
            customer = choice(customers)
            greeting = greeter(customer)
            print(greeting)
        return greeting  # The final one


if __name__ == '__main__':
    main()
