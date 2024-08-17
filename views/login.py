import flet as ft

def login_screen(page: ft.Page):
    
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
                    color="black",
                    prefix_icon=ft.icons.SUPERVISED_USER_CIRCLE_SHARP
                ),
                padding=ft.padding.only(20, 20)
            ),
            ft.Container(
                ft.TextField(
                    width=280,
                    height=40,
                    hint_text="Contraseña",
                    border="underline",
                    color="black",
                    prefix_icon=ft.icons.LOCK,
                    password="true"
                ),
                padding=ft.padding.only(20, 20)
            ),
            ft.Container(
                ft.ElevatedButton(
                    "Iniciar",
                    width=280,
                    bgcolor="black",
                    on_click=lambda e: page.go("/main")  # Asocia el evento de clic al botón
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
