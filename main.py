from flet import *


def main(page: Page):
    page.update()

    BG = "#041955"
    FWG = "#97b4ff"
    FG = "#3450a1"
    PINK = "#eb06ff"

    def change_tab(e):
        # get index tab
        my_index = e.control.selected_index
        tab_1.visible = True if my_index == 0 else False
        tab_2.visible = True if my_index == 1 else False
        tab_3.visible = True if my_index == 2 else False
        page.update()

    page.navigation_bar = NavigationBar(
        bgcolor=FG,
        selected_index=0,
        on_change=change_tab,
        destinations=[
            NavigationDestination(icon="home"),
            NavigationDestination(icon="explore"),
            NavigationDestination(icon="settings"),
        ]
    )
    categories_card = Row(
        scroll="auto"
    )
    categories = ["Sweatshirts", "Sweaters", "Jeans", "Dresses", "Jackets", "Shoes", "Socks", "Boxers"]
    for i, category in enumerate(categories):
        sold_pieces = 100 - i * 5
        categories_card.controls.append(
            Container(
                bgcolor=FG, height=110, width=170, border_radius=20, padding=15,
                content=Column(
                    controls=[
                        Text(category, size=20),
                        Text(f"Sold {sold_pieces} Pcs", size=14, italic=True),
                        Container(
                            width=160,
                            height=5,
                            bgcolor="white12",
                            border_radius=18,
                            padding=padding.only(right=i * 15),
                            content=Container(
                                bgcolor=PINK,
                            )
                        )
                    ]
                )
            )
        )
    # tab_1 = Text("Tab 1", size=30, visible=True)
    tab_1 = Container(
        visible=True,
        content=Column(
            controls=[
                Row(
                    alignment="spaceBetween",
                    controls=[
                        Container(
                            # on_click=lambda e: shrink(e),
                            content=Icon(icons.MENU)
                        ),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED)
                            ]
                        )
                    ]
                ),
                Container(height=5),
                Text(
                    value="What\'s up Gachuki!"
                ),
                Container(height=5),
                Text(
                    value="CATEGORIES"
                ),
                Container(
                    padding=padding.only(top=10, bottom=20, ),
                    content=categories_card
                ),
                Text("STOCKS"),
                Container(
                    DataTable(
                        columns=[
                            DataColumn(Text("Item")),
                            DataColumn(Text("Start"), numeric=True),
                            DataColumn(Text("Sold"), numeric=True),
                            DataColumn(Text("Remaining"), numeric=True),
                        ],
                        rows=[
                            DataRow(
                                cells=[
                                    DataCell(Text("Sweatshirts")),
                                    DataCell(Text("155")),
                                    DataCell(Text("100")),
                                    DataCell(Text("55")),
                                ],
                            ),
                            DataRow(
                                cells=[
                                    DataCell(Text("Sweaters")),
                                    DataCell(Text("102")),
                                    DataCell(Text("20")),
                                    DataCell(Text("82")),
                                ],
                            ),
                            DataRow(
                                cells=[
                                    DataCell(Text("Jeans")),
                                    DataCell(Text("90")),
                                    DataCell(Text("40")),
                                    DataCell(Text("50")),
                                ],
                            ),
                        ],
                    ),

                )
            ]
        )
    )
    tab_2 = Text("Tab 2", size=30, visible=False)
    tab_3 = Text("Tab 3", size=30, visible=False)

    page.add(
        Container(
            content=Column(
                [
                    tab_1, tab_2, tab_3
                ]
            )
        )
    )


app(target=main)
