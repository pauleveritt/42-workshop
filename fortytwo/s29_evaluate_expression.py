"""29: Evaluate Expression During Debugging

Select your code and execute it, in the right context. No more poking
around with ``print()``.

- Breakpoint on line 24

- Select ``choice(customers)``, right-click, Execute Expression

- Assign to value ``name``, see it appear in scope

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
            customer = choice(customers)  # Breakpoint here
            greeting = greeter(customer)
            print(greeting)
        return greeting  # The final one


if __name__ == '__main__':
    main()
