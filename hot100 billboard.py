from bs4 import BeautifulSoup
import requests

URL = "https://www.billboard.com/charts/hot-100"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "lxml")

main_div = soup.find("div", class_ = "chart-list container")
songs = main_div.findAll("li", class_ = "chart-list__element display--flex")
for song in songs:
	song_name = song.find("span", class_ = "chart-element__information__song text--truncate color--primary")
	song_name = song_name.text

	song_singer = song.find("span", class_ = "chart-element__information__artist text--truncate color--secondary")
	song_singer = song_singer.text

	chart_position = song.find("span", class_ = "chart-element__rank__number")
	chart_position = chart_position.text

	right_arrow = song.find("i", class_ = "fa fa-arrow-right")
	if right_arrow:
		chart_tracking = "Steady"

	up_arrow = song.find("i", class_ = "fa fa-arrow-up")
	if up_arrow:
		chart_tracking = "Rising"

	down_arrow = song.find("i", class_ = "fa fa-arrow-down")
	if down_arrow:
		chart_tracking = "Freefalling"

	new_song = song.find("span", class_ = "chart-element__trend chart-element__trend--new color--accent")
	if new_song:
		chart_tracking = "New"

	print(chart_position, song_name, song_singer, chart_tracking)