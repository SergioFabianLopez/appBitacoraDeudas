import flet as ft
from views.navbar import navbar
from views.login import login_screen
from views.admin import admin_screen


def route_change(e):
    page = e.page
    page.views.clear()  # Limpiar las vistas existentes en la página

    print("Route change:", page.route)

    if page.route == "/":
        page.views.append(ft.View("/", [login_screen(page)], padding=0))
        # page.views.append(ft.View("/", [admin_screen(page)], padding=0))
    elif page.route == "/nav":
        page.views.append(ft.View("/nav", [navbar(page)], padding=0))
    elif page.route == "/exit":
        page.client_storage.clear()
        page.views.append(ft.View("/exit", [login_screen(page)], padding=0))
    page.update()
