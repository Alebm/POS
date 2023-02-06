
import flet as ft


def main(page: ft.Page):
    page.title = 'Flet counter'
    page.vertical_alignment = 'center'

    txt_number = ft.TextField(value='0', text_align='rieght', width=100)

    def minus_click(event):
        txt_number.value = int(txt_number.value)-1
        page.update()

    def plus_click(event):
        txt_number.value = int(txt_number.value)+1
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    )


ft.app(target=main, view=ft.WEB_BROWSER)
