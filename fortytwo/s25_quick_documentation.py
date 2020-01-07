"""25: Quick Documentation

View documentation without interrupting your flow.

- What is ``random.choice``? Stop what you're doing, get out of flow, etc.

- ``F1`` on the symbol

-

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
        greeter = container.get(Greeter)
        customer = choice  # Not sure what this function does?
        greeting = greeter(customer)
        return greeting


if __name__ == '__main__':
    print(main())
