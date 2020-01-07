"""28: Conditional Breakpoints

Speed up your debugging by stopping execution only when you want to.

- Want to debug calling the ``Greeter``, but...

- *only* when it is ``Larry``

- Breakpoint on line 26...``Continue``...cumbersome

- Instead, conditional breakpoint: ``customer == 'Larry'``

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/
"""
from random import choice

from fortytwo import App
from fortytwo.models import Greeter

customers = ('Larry', 'Alice', 'Sam', 'Juanita', 'Mei')


def main():
    site = App()
    with site as container:
        for i in range(10):
            greeter = container.get(Greeter)
            customer = choice(customers)
            greeting = greeter(customer)
            print(greeting)
        return greeting  # The last one


if __name__ == '__main__':
    main()
