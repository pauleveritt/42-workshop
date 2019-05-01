"""04: Jump to Recent File

Use Recent Files to quickly jump to last-visited file.

- Ctrl-E/Cmd-E

- Very useful toggle

- Cursor keys

- Or speed search

- Variations such as recently *changed* file

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
