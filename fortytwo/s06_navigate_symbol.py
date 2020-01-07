"""06: Navigate to Symbol

Navigate your project by code, not files.

- Navigate by code, not by files

- I want to get to the Greeter class in fortytwo.models

- Navigate by Symbol (Shift-Ctrl-Alt-N Win/Linux, Alt-Cmd-O macOS)

- Recent Files to get back

- Also goes into dependencies, e.g. `SerReg` for `wired.ServiceRegistry`

- As that shows, CamelHump also works

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
