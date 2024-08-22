import flet as ft
from routes.routes import route_change

def main(page: ft.Page):
    page.title = "Me Debes App"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.on_route_change = route_change
    page.go("/")

# Inicializa la aplicación
ft.app(main)
