"""20: Generate Imports While Typing

Avoid interruption by letting PyCharm generate your imports as you type.

- We want a random customer

- Delete 'Larry'

- Type ``choic`` and ``Ctrl-Space-Space``

- Or, type ``choice`` and ``Alt-Enter``

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/
"""

from fortytwo import App, Greeter

customers = ('Larry', 'Alice', 'Sam')


def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        customer = 'Larry'  # Change to random customer
        greeting = greeter(customer)
        return greeting


if __name__ == '__main__':
    print(main())
