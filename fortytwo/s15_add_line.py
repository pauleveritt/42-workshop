"""15: Add Line After/Before

Smart-add a line, from the middle of a line, after or before the current line.

- Cursor on ``as`` in the ``with`` below

- Start New Line (Shift-Enter Win/Linux/macOS)

- Start New Line Before Current
  (Ctrl-Alt-Enter Win/Linux, Alt-Cmd-Enter macOS)

- Or better still, Find Action | ``st be``

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/
"""

from fortytwo import App, Greeter


def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        greeting = greeter('Larry')
        return greeting


if __name__ == '__main__':
    print(main())
