import datetime
from decimal import Decimal
import base64
import flet as ft

from logic.data import add_pays, list_accounts_user


def add_pay(page: ft.Page):
    # Variables para capturar los valores de los controles
    dropdown_value = ft.Ref[ft.Dropdown]()
    amount_value = ft.Ref[ft.TextField]()
    date_value = ft.Ref[ft.DatePicker]()
    image_value = ft.Ref[str]()  # Para guardar la cadena base64 de la imagen

    id_user = page.client_storage.get("id_user")
    # Obtener todas las cuentas
    all_accounts = list_accounts_user([id_user])

    # Crear las opciones del Dropdown
    dropdown_options = [ft.dropdown.Option(key=item["id"], text=item["name"]) for item in all_accounts]

    def send_image(e):
        # Verificar si el usuario seleccionó un archivo
        if e.files:
            # Obtener la ruta del archivo seleccionado
            file_content = e.files[0].path
            if file_content:
                # Convertir los bytes a base64
                image_base64 = base64.b64encode(file_content).decode('utf-8')
                # Guardar la cadena base64 en image_value
                image_value.current = image_base64
                print("Imagen en base64:", image_value.current)  # Verifica si la imagen en base64 se asigna correctamente
            else:
                print("Error: El contenido del archivo es None.")

    file_picker = ft.FilePicker(on_result=send_image)
    page.overlay.append(file_picker)

    def handle_yes(e):
        # Verificar si los valores están presentes
        if not all([dropdown_value.current.value, amount_value.current.value, date_value.current.value]):
            print("Error: Faltan valores necesarios.")
            return

        selected_account = dropdown_value.current.value
        amount = amount_value.current.value
        payment_date = date_value.current.value.strftime('%Y-%m-%d')
        image_base64 = 'No especificado'

        # Llamar a add_pays con los valores obtenidos
        add_pays(payment_date, Decimal(amount), image_base64, selected_account)
        page.close(dlg_modal)
        page.open(banner)

    def handle_close(e):
        page.close(dlg_modal)

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Por favor confirme"),
        content=ft.Text("¿Realmente desea guardar este pago?"),
        actions=[
            ft.TextButton("Sí", on_click=handle_yes),
            ft.TextButton("No", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def close_banner(e):
        page.close(banner)

    action_button_style = ft.ButtonStyle(color=ft.colors.BLUE)
    banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.CHECK_OUTLINED, color=ft.colors.GREEN, size=40),
        content=ft.Text(
            value="Datos guardados con éxito",
            color=ft.colors.BLACK,
        ),
        actions=[
            ft.TextButton(text="OK", style=action_button_style, on_click=close_banner),
        ],
    )

    return ft.Column(
        controls=[
            ft.Container(
                ft.Column([
                    ft.Container(
                        ft.Text(
                            "Agregar pago",
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
                            ref=dropdown_value,
                            border_color="#A18249",
                        ),
                        padding=ft.padding.only(40, 10, 40, 5)
                    ),
                    ft.Container(
                        ft.Text(
                            "Cantidad",
                            color=ft.colors.BLACK,
                            width=320,
                            size=15,
                        ),
                        padding=ft.padding.only(40, 10, 40, 1)
                    ),
                    ft.Container(
                        ft.TextField(
                            color="black",
                            ref=amount_value,
                            border_color="#A18249",
                        ),
                        padding=ft.padding.only(40, 5, 40, 5),
                        width=300
                    ),
                    ft.Container(
                       ft.ElevatedButton(
                            "¿Qué día se realizó?",
                            icon=ft.icons.CALENDAR_MONTH,
                            on_click=lambda e: page.open(
                                ft.DatePicker(
                                    first_date=datetime.datetime(year=2023, month=10, day=1),
                                    last_date=datetime.datetime(year=2024, month=10, day=1),
                                    ref=date_value  # Asignar referencia
                                )
                            ),
                        ),
                        padding=ft.padding.only(40, 5, 40, 5)
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Seleccionar comprobante",
                            on_click=lambda _: file_picker.pick_files(),
                            icon=ft.icons.UPLOAD_FILE
                        ),
                        padding=ft.padding.only(40, 10, 40, 5)
                    ),
                    ft.Container(
                        content=ft.ElevatedButton(
                            "Guardar",
                            on_click=lambda e: page.open(dlg_modal),
                            width=280,
                            bgcolor="#019863",
                            color="white"
                        ),
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(top=80),
                    )
                ]),
            ),
            ft.Container(expand=True),
        ],
        expand=True
    )
