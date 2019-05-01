"""29: Evaluate Expression During Debugging

Select your code and execute it, in the right context.

- Stop before calling ``choice`` and execute it a few times

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
