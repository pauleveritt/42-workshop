"""21: Install and import

While typing a symbol, let PyCharm install it and generate the import.

- Cursor on maya

- Alt-Enter -> Install and import

- Then, quick fix to add to requirements.txt

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/
"""

from random import choice

from fortytwo import App, Greeter

customers = ('Larry', 'Alice', 'Sam')


def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        customer = choice(customers)
        greeting = greeter(customer)
        return greeting


if __name__ == '__main__':
    print(main())
    print(maya.now())  # Fix me
