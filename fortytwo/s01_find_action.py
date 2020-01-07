"""01: Find Action

Skip memorizing keyboard shortcuts and speed search for actions instead.

- I want to find all instances of the string `Mary`

- What is the Find in Path shortcut? Who knows?

- Use Find Action (Cmd-Shift-A on macOS)

- Speed type "fi pa", note shortcut, select

- Search 'Mar' to find Mary

- Also for preferences, e.g. `python import`

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
