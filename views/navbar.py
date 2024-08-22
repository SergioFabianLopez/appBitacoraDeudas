import flet as ft

from views.addpay import add_pay
from views.counts import counts
from views.main import main_screen


def navbar(page: ft.Page):
    content_area = ft.Column(expand=True)

    def on_tab_change(e):
        selected_index = e.control.selected_index
        content_area.controls.clear()  # Limpiar controles existentes

        if selected_index == 0:
            content_area.controls.append(main_screen(page))
        elif selected_index == 1:
            content_area.controls.append(add_pay(page))
        elif selected_index == 2:
            content_area.controls.append(counts(page))
        elif selected_index == 3:
            page.go("/exit")

        content_area.update()

    cupertino_navigation_bar = ft.Container(
        ft.CupertinoNavigationBar(
            inactive_color="#A18249",
            active_color=ft.colors.BLACK,
            bgcolor=ft.colors.GREY,
            destinations=[
                ft.NavigationBarDestination(icon=ft.icons.FORMAT_LIST_BULLETED_ROUNDED, label="Pagos"),
                ft.NavigationBarDestination(icon=ft.icons.ATTACH_MONEY, label="Agregar pago"),
                ft.NavigationBarDestination(icon=ft.icons.WALLET, label="Cuentas"),
                ft.NavigationBarDestination(icon=ft.icons.EXIT_TO_APP, label="Salir"),
            ],
            on_change=on_tab_change,
            ),
        border_radius=ft.border_radius.only(top_left=10, top_right=10),
        clip_behavior=ft.ClipBehavior.HARD_EDGE
    )

    # Agrega el contenido inicial
    content_area.controls.append(main_screen(page))

    # Devuelve una columna con el área de contenido en la parte superior y la barra de navegación en la parte inferior
    return ft.Column(
        controls=[
            content_area,
            cupertino_navigation_bar
        ],
        expand=True
    )
