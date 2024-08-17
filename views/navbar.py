import flet as ft

def exit_screen():
    return ft.Column(
        controls=[
            ft.Text("Salir de la aplicación", size=30, weight="bold"),
            # Aquí puedes agregar otros componentes necesarios para la pantalla de salida
        ],
        expand=True,
    )

# Define el NavigationBar y el manejador de clics
def navbar(page: ft.Page):
    def handle_navigation(e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            page.go("/main")
        elif selected_index == 1:
            page.go("/add-payment")
        elif selected_index == 2:
            page.go("/counts")
        elif selected_index == 3:
            page.go("/exit")

    return ft.Container(
        ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.icons.FORMAT_LIST_BULLETED_ROUNDED, label="Pagos"),
                ft.NavigationBarDestination(icon=ft.icons.ATTACH_MONEY, label="Agregar pago"),
                ft.NavigationBarDestination(icon=ft.icons.WALLET, label="Cuentas"),
                ft.NavigationBarDestination(icon=ft.icons.EXIT_TO_APP, label="Salir"),
            ],
            on_change=handle_navigation,
            bgcolor=ft.colors.BLACK54,
        ),
        height=60,  # Altura del NavigationBar
        bgcolor=ft.colors.BLACK,
        padding=ft.Padding(0, 0, 0, 10), 
    )
