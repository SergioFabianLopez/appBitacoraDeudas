import datetime
import flet as ft

from logic.data import get_all_users, list_accounts_user, list_pays


def admin_screen(page: ft.Page):
    # Obtener todos los usuarios
    all_users = get_all_users()

    # Crear las opciones del Dropdown para los usuarios
    dropdown_options_users = [
        ft.dropdown.Option(key=item["id"], text=item["name"]) for item in all_users
    ]

    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    # Función reutilizable para manejar la selección de usuario
    def on_user_selected(e, dropdown_options_accounts):
        selected_id = e.control.value  # Obtener el ID del usuario seleccionado
        print(f"Usuario seleccionado con ID: {selected_id}")
        all_accounts = list_accounts_user([selected_id])  # Obtener cuentas del usuario seleccionado
        # Actualizar las opciones de cuentas basadas en el usuario seleccionado
        dropdown_options_accounts.clear()
        dropdown_options_accounts.extend(
            [ft.dropdown.Option(key=item["id"], text=item["name"]) for item in all_accounts]
        )
        page.update()  # Actualizar la UI

    # Función reutilizable para manejar el cambio de cuentas
    def dropdown_changed_pays(e):
        lv.clean()
        data = list_pays([e.control.value])
        item_pay = 1
        for item in data:
            rows_data = ft.Row([
                ft.Text(str(item_pay), color=ft.colors.BLACK),
                ft.Text(item['payments_date'], color=ft.colors.BLACK),
                ft.Text(item['amount'], color=ft.colors.BLACK),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=45)
            lv.controls.append(rows_data)
            item_pay += 1
        lv.update()

    # Vista de lista de pagos
    def payment_list():
        dropdown_options_accounts = []  # Almacenará las opciones de cuentas

        return ft.Container(
            ft.Column([
                ft.Text('Seleccionar usuario'),
                ft.Dropdown(
                    options=dropdown_options_users,
                    on_change=lambda e: on_user_selected(e, dropdown_options_accounts)  # Usar la función reutilizable
                ),
                ft.Text('Seleccionar cuenta'),
                ft.Dropdown(
                    options=dropdown_options_accounts,
                    on_change=dropdown_changed_pays  # Usar la función reutilizable
                ),
                lv
            ]),
            padding=ft.padding.only(20, 10, 20, 30)
        )

    # Vista de resumen de cuentas
    def summary_of_accounts():
        dropdown_options_accounts = []  # Almacenar las opciones de cuentas para el resumen
        return ft.Container(
            ft.Column([
                ft.Text('Seleccionar usuario'),
                ft.Dropdown(
                    options=dropdown_options_users,
                    on_change=lambda e: on_user_selected(e, dropdown_options_accounts)  # Reutilizar la función
                ),
                ft.Text('Seleccionar cuenta'),
                ft.Dropdown(
                    options=dropdown_options_accounts,
                    on_change=dropdown_changed_pays  # Reutilizar la función
                ),
                ft.Container(
                    ft.Column([
                        ft.Container(
                            ft.Row([
                                ft.Text("Compra:", size=20, color=ft.colors.BLACK),
                                ft.Text('Compra de prueba'),
                            ]),
                            padding=ft.padding.only(40, 50, 40, 5)
                        ),
                        ft.Container(
                            ft.Row([
                                ft.Text("Total:", size=20, color=ft.colors.BLACK),
                                ft.Text('$50000'),
                            ]),
                            padding=ft.padding.only(40, 10, 40, 5)
                        ),
                        ft.Container(
                            ft.Row([
                                ft.Text("Fecha de compra:", size=20, color=ft.colors.BLACK),
                                ft.Text('01/02/2024'),
                            ]),
                            padding=ft.padding.only(40, 10, 40, 5)
                        ),
                        ft.Container(
                            ft.Row([
                                ft.Text("Restante:", size=20, color=ft.colors.BLACK),
                                ft.Text('$2050'),
                            ]),
                            padding=ft.padding.only(40, 10, 40, 5)
                        )
                    ]),
                ),
                ft.Container(expand=True),
            ]),
            padding=ft.padding.only(20, 10, 20, 30)
        )

    # Otras vistas (sin cambios)
    def add_account():
        return ft.Container(
            ft.Column([
                ft.Text('Seleccionar usuario'),
                ft.Dropdown(
                    options=[
                        ft.dropdown.Option("Red"),
                        ft.dropdown.Option("Green"),
                        ft.dropdown.Option("Blue"),
                    ],
                ),
                ft.Text('Día de la compra'),
                ft.ElevatedButton(
                    "¿Qué día se realizó?",
                    icon=ft.icons.CALENDAR_MONTH,
                    on_click=lambda e: page.open(
                        ft.DatePicker(
                            first_date=datetime.datetime(year=2023, month=10, day=1),
                            last_date=datetime.datetime(year=2024, month=10, day=1),
                        )
                    ),
                ),
                ft.TextField(
                    width=280,
                    height=40,
                    hint_text="Total",
                    border=ft.InputBorder.UNDERLINE,
                    border_color="#A18249",
                ),
                ft.Text('A meses'),
                ft.Dropdown(
                    width=100,
                    options=[
                        ft.dropdown.Option("Red"),
                        ft.dropdown.Option("Green"),
                        ft.dropdown.Option("Blue"),
                    ],
                ),
                ft.Text('Tarjeta de compra'),
                ft.Container(
                    ft.Dropdown(
                        width=100,
                        options=[
                            ft.dropdown.Option("Red"),
                            ft.dropdown.Option("Green"),
                            ft.dropdown.Option("Blue"),
                        ],
                    ),
                    expand=True
                ),
                ft.ElevatedButton(
                    "Guardar",
                    width=280,
                    bgcolor="#019863",
                    on_click=None,
                    color="white"
                ),
            ]),
            padding=ft.padding.only(20, 10, 20, 30)
        )

    def new_update_user():
        return ft.Container(
            ft.Column([
                ft.Text('Seleccionar usuario'),
                ft.Dropdown(
                    options=[
                        ft.dropdown.Option("Red"),
                        ft.dropdown.Option("Green"),
                        ft.dropdown.Option("Blue"),
                    ],
                ),
                ft.TextField(
                    width=280,
                    height=40,
                    hint_text="Nombre de usuario",
                    border=ft.InputBorder.UNDERLINE,
                    border_color="#A18249",
                ),
                ft.Container(
                    ft.TextField(
                        width=280,
                        height=40,
                        hint_text="Password",
                        border=ft.InputBorder.UNDERLINE,
                        border_color="#A18249",
                    ),
                    expand=True
                ),
                ft.ElevatedButton(
                    "Guardar",
                    width=280,
                    bgcolor="#019863",
                    on_click=None,
                    color="white"
                ),
            ]),
            padding=ft.padding.only(20, 10, 20, 30)
        )

    # Estructura principal de pestañas
    return ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Lista de pagos",
                content=ft.Container(
                    content=payment_list(), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="Resumen de Cuentas",
                content=ft.Container(
                    content=summary_of_accounts(), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="Agrega cuenta",
                content=ft.Container(
                    content=add_account(), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="Agrega usuario",
                content=ft.Container(
                    content=new_update_user(), alignment=ft.alignment.center
                ),
            ),
        ],
        expand=True,
    )
