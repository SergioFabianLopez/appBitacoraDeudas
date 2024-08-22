import flet as ft

def main(page: ft.Page):
    # Contenedor donde cambiará el contenido
    content_area = ft.Column()

    def on_tab_change(e):
        selected_index = e.control.selected_index
        content_area.controls.clear()

        if selected_index == 0:
            content_area.controls.append(ft.Text("Explore Screen"))
        elif selected_index == 1:
            content_area.controls.append(ft.Text("Commute Screen"))
        elif selected_index == 2:
            content_area.controls.append(ft.Text("Bookmark Screen"))

        content_area.update()

    cupertino_navigation_bar = ft.CupertinoNavigationBar(
        bgcolor=ft.colors.AMBER_100,
        inactive_color=ft.colors.GREY,
        active_color=ft.colors.BLACK,
        on_change=on_tab_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Bookmark",
            ),
        ]
    )

    # Establecer el contenido inicial
    content_area.controls.append(ft.Text("Explore Screen"))

    # Agregar la barra de navegación y el área de contenido a la página
    page.add(
        ft.Column(
            [
                cupertino_navigation_bar,
                content_area
            ]
        )
    )

ft.app(target=main)
