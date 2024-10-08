import flet as ft
from logic.data import list_accounts_user, list_accounts_id


def counts(page: ft.Page):
    # Variables para capturar los valores de los controles
    purchase_text = ft.Text("", size=20, color=ft.colors.BLACK)
    total_text = ft.Text("", size=20, color=ft.colors.BLACK)
    purchase_date_text = ft.Text("", size=20, color=ft.colors.BLACK)
    remaining_text = ft.Text("", size=20, color=ft.colors.BLACK)

    id_user = page.client_storage.get("id_user")
    # Obtener todas las cuentas
    all_accounts = list_accounts_user([id_user])

    # Crear las opciones del Dropdown
    dropdown_options = [ft.dropdown.Option(key=item["id"], text=item["name"]) for item in all_accounts]

    def dropdown_changed(e):
        selected_id = e.control.value
        request = list_accounts_id([selected_id])
        if request:
            purchase_text.value = request[0].get('name')
            total_text.value = request[0].get('total')
            purchase_date_text.value = request[0].get('purchase_date')
            remaining_text.value = request[0].get('remaining')
        else:
            purchase_text.value = "N/A"
            total_text.value = "N/A"
            purchase_date_text.value = "N/A"
            remaining_text.value = "N/A"

        # Llama a `page.update()` para actualizar la UI
        page.update()

    return ft.Column(
        controls=[
            ft.Container(
                ft.Column([
                    ft.Container(
                        ft.Text(
                            "Detalles de Cuenta",
                            color=ft.colors.BLACK,
                            width=320,
                            size=20,
                            weight="w900"
                        ),
                        padding=ft.padding.only(40, 50, 40, 5),
                    ),
                    ft.Container(
                        ft.Text(
                            "¿A qué cuenta?",
                            color=ft.colors.BLACK,
                            width=320,
                            size=15,
                        ),
                        padding=ft.padding.only(40, 10, 40, 5)
                    ),
                    ft.Container(
                        ft.Dropdown(
                            options=dropdown_options,
                            on_change=dropdown_changed,
                            border_color="#A18249",
                        ),
                        padding=ft.padding.only(40, 10, 40, 5)
                    ),
                    ft.Container(
                        ft.Row([
                            ft.Text("Compra:", size=20, color=ft.colors.BLACK),
                            purchase_text,
                        ]),
                        padding=ft.padding.only(40, 50, 40, 5)
                    ),
                    ft.Container(
                        ft.Row([
                            ft.Text("Total:", size=20, color=ft.colors.BLACK),
                            total_text,
                        ]),
                        padding=ft.padding.only(40, 10, 40, 5)
                    ),
                    ft.Container(
                        ft.Row([
                            ft.Text("Fecha de compra:", size=20, color=ft.colors.BLACK),
                            purchase_date_text,
                        ]),
                        padding=ft.padding.only(40, 10, 40, 5)
                    ),
                    ft.Container(
                        ft.Row([
                            ft.Text("Restante:", size=20, color=ft.colors.BLACK),
                            remaining_text,
                        ]),
                        padding=ft.padding.only(40, 10, 40, 5)
                    )
                ]),
            ),
            ft.Container(expand=True),
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )
