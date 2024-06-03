import flet as ft
import requests

def main(page: ft.Page):
    page.title = "天気アプリ"
    
    def get_weather_data(city):
        try:
            response = requests.get(f"http://wttr.in/{city}?format=%C+%t&lang=ja")
            if response.status_code == 200:
                return response.text.strip()
            else:
                return "都市が見つからないか、APIエラーです。"
        except requests.exceptions.RequestException as e:
            return f"エラー: {e}"

    def on_search(e):
        city = city_input.value
        weather = get_weather_data(city)
        weather_output.value = f"{city}の天気: {weather}"
        page.update()

    city_input = ft.TextField(label="都市名を入力してください")
    search_button = ft.ElevatedButton(text="検索", on_click=on_search)
    weather_output = ft.Text()

    page.add(city_input, search_button, weather_output)

ft.app(target=main)
