"""03: Disable Tabs

Save space and stay keyboard-centric by turning off the tabs.

- Preferences | Editor | General | Editor Tabs | Placement -> None

- Or Find Action, wi pl no -> Enter

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
