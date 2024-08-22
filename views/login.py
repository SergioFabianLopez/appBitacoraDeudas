import flet as ft

from logic.data import get_login  

def login_screen(page: ft.Page):
    user_value = ft.Ref[str]()
    password_value = ft.Ref[str]()

    def close_banner(e):
        page.close(banner)

    action_button_style = ft.ButtonStyle(color=ft.colors.BLUE)
    banner = ft.Banner(
            bgcolor=ft.colors.AMBER_100,
            leading=ft.Icon(ft.icons.NO_ENCRYPTION_GMAILERRORRED, color=ft.colors.RED, size=40),
            content=ft.Text(
                value="Error: usuario no encontrado",
                color=ft.colors.BLACK,
            ),
            actions=[
                ft.TextButton(text="OK", style=action_button_style, on_click=close_banner),
            ],
        )  

    def login(e):
        if not all([user_value.current.value, password_value.current.value]):
            print("Error: Faltan valores necesarios.")
            return

        response = get_login([user_value.current.value, password_value.current.value])

        if len(response) > 0:
            page.client_storage.set("id_user", response[0]['id'])
            page.go("/main")
        else:
            print("Error: usuario no encontrado")
            page.open(banner)

    return ft.Container(
        ft.Column([
            ft.Container(
                ft.Text(
                    "Iniciar Sesión",
                    width=320,
                    size=30,
                    text_align="center",
                    weight="w900"
                ),
                padding=ft.padding.only(20, 50, 20, 30)
            ),
            ft.Container(
                ft.TextField(
                    width=280,
                    height=40,
                    hint_text="Usuario",
                    border="underline",
                    color=ft.colors.WHITE,
                    prefix_icon=ft.icons.SUPERVISED_USER_CIRCLE_SHARP,
                    ref=user_value
                ),
                padding=ft.padding.only(20, 20)
            ),
            ft.Container(
                ft.TextField(
                    width=280,
                    height=40,
                    hint_text="Contraseña",
                    border="underline",
                    color=ft.colors.WHITE,
                    prefix_icon=ft.icons.LOCK,
                    password="true",
                    ref=password_value
                ),
                padding=ft.padding.only(20, 20)
            ),
            ft.Container(
                ft.ElevatedButton(
                    "Iniciar",
                    width=280,
                    bgcolor="black",
                    on_click=login
                ),
                padding=ft.padding.only(20, 20)
            ),
        ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        ),
        expand=True,
        gradient=ft.LinearGradient([
            "#2b2147",  # Color marrón en hexadecimal
            "#38197a"
        ]),
        padding=ft.padding.only(25, 25),
    )
