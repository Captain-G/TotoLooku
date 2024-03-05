from flet import *


def main(page: Page):
    page.update()

    def change_tab(e):
        # get index tab
        my_index = e.control.selected_index
        tab_1.visible = True if my_index == 0 else False
        tab_2.visible = True if my_index == 1 else False
        tab_3.visible = True if my_index == 2 else False
        page.update()

    page.navigation_bar = NavigationBar(
        bgcolor="blue",
        selected_index=0,
        on_change=change_tab,
        destinations=[
            NavigationDestination(icon="home"),
            NavigationDestination(icon="explore"),
            NavigationDestination(icon="settings"),
        ]
    )
    tab_1 = Text("Tab 1", size=30, visible=True)
    tab_2 = Text("Tab 2", size=30, visible=False)
    tab_3 = Text("Tab 3", size=30, visible=False)

    page.add(
        Container(
            margin=margin.only(top=page.window_height / 2, left=50),
            content=Column(
                [
                    tab_1, tab_2, tab_3
                ]
            )
        )
    )


app(target=main)
