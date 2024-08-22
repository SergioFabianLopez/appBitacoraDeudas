import flet as ft

from logic.data import list_accounts_user, list_pays

# Define la tabla de datos
lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
rows = ft.Row([
    ft.Text("#", color=ft.colors.BLACK),
    ft.Text("Fecha de pago", color=ft.colors.BLACK),
    ft.Text("Cantidad", color=ft.colors.BLACK),
    ft.Text("Restante", color=ft.colors.BLACK),
],
    alignment=ft.MainAxisAlignment.CENTER,
    spacing=20
)


def dropdown_changed(e):
    lv.clean()
    data = list_pays([e.control.value])
    item_pay = 1
    for item in data:
        rows_data = ft.Row([
            ft.Text(item_pay, color=ft.colors.BLACK),
            ft.Text(item['payments_date'], color=ft.colors.BLACK),
            ft.Text(item['amount'], color=ft.colors.BLACK),
            ft.Text(item['remaining'], color=ft.colors.BLACK),
        ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=45
        )
        lv.controls.append(rows_data)
        item_pay += 1
    lv.update()


def main_screen(page: ft.Page):
    all_accounts = list()
    id_user = page.client_storage.get("id_user")
    # Obtener todas las cuentas
    if id_user is not None:
        all_accounts = list_accounts_user([id_user])

    # Crear las opciones del Dropdown
    dropdown_options = []
    for item in all_accounts:
        dropdown_options.append(
            ft.dropdown.Option(key=item["id"], text=item["name"])
            )

    return ft.Container(
        ft.Column(
            controls=[
                ft.Container(
                    ft.Text("Cuentas activas", size=20, weight="w900"),
                    padding=ft.padding.only(40, 50, 40, 5),
                ),
                ft.Container(
                   ft.Dropdown(
                        options=dropdown_options,
                        height=55,
                        on_change=dropdown_changed,
                        border_color="#A18249",
                    ),
                    padding=ft.padding.only(40, 0, 40, 15)
                ),
                ft.Container(
                    rows
                ),
                ft.Container(
                    lv,
                    expand=True,
                    padding=ft.padding.only(10, 0),
                ),
            ],
        ),
        expand=True
    )
