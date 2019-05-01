"""16: Make and Extend Selection Using Keyboard

Use the keyboard to select blocks of code then extend/shrink the selection.

- Use keyboard to make/extend selection

- Then shrink selection

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/
"""

from fortytwo import App, Greeter


def main():
    site = App()
    with site as container:
        customer = 'Larry'
        greeter = container.get(Greeter)
        greeting = greeter(customer)
        return greeting


if __name__ == '__main__':
    print(main())
