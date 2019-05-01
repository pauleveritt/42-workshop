"""22: Adding Fields In a Constructor

Let your IDE add constructor arguments to your instance.

- Type an argument to ``__init__``

- Alt-Enter to make it a field

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/
"""

from fortytwo import App, Greeter


class Customer:
    def __init__(self):  # Pass in ``name``
        pass


def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        greeting = greeter('Larry')
        return greeting


if __name__ == '__main__':
    print(main())
