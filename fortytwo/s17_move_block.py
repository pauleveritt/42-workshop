"""17: Move Block Up/Down Using Keyboard

Use the keyboard to move a line or selection up or down in your file.

- The ``customer`` definition doesn't need to be in block

- Use keyboard to make/extend selection

- Use Move Line Up
  (Shift-Alt-Up/Down Win/Linux, Alt-Shift-Up/Down macOS)

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
