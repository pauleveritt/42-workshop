"""16: Reformat Code

Tell PyCharm to clean up indentation and other code style in your file.

- 3 warnings below

- Reformat Code (``Ctrl-Alt-L`` Win/Linux, ``Alt-Cmd-L`` macOS)

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/
"""

from fortytwo import App, Greeter
def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        greeting = greeter(     'Larry')
        return greeting


if __name__ == '__main__':
 print(main())
