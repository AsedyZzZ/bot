import requests
from bs4 import BeautifulSoup

from domain.hero import Hero


class StatusCodeError(Exception):
    pass


class Parser:
    def __init__(self, hero: Hero) -> None:
        self.hero = hero
        self.headers = {"User-Agent": "Bot"}
        self.base_url = "https://ru.dotabuff.com"

    def get_win_rate(self) -> dict[str, float]:
        """Этот метод находит нам винрейты и если они положительные сохраняет."""
        name = self.hero.name.replace(" ", "-")
        url = f"{self.base_url}/heroes/{name.lower()}/counters"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            block = BeautifulSoup(response.text, "html.parser").find("table", class_="sortable")
            table = block.find_all("tr")
        else:
            raise StatusCodeError(f"Something goes wrong. Please try again. Status code: {response.status_code}")
        win_rate_of_hero = {}
        res = []
        for tr in table:
            td = tr.find_all("td")
            row = [tr.text.strip() for tr in td if tr.text.strip()]
            if row:
                res.append(row)
                row.pop(3)
                row.pop(1)
                row[1] = 100 - float(row[1][:len(row[1]) - 1])
                win_rate_of_hero[row[0]] = row[1]
        win_rate = win_rate_of_hero
        return win_rate
