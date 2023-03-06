import abc

import requests
from bs4 import BeautifulSoup, Tag

from hero import Hero
from user_agent import get_random_user_agent


class ParserServiceError(Exception):
    pass


class HeroesParser(abc.ABC):
    @abc.abstractmethod
    def get_heroes(self) -> list[Hero]:
        pass


class DotabuffHeroesParser(HeroesParser):
    def __init__(self) -> None:
        self.base_url = "https://www.dotabuff.com"

    def get_heroes(self) -> list[Hero]:
        user_agent: str = get_random_user_agent()
        headers: dict[str, str] = {"User-Agent": user_agent}
        response = requests.get(f"{self.base_url}/heroes/meta", headers=headers)
        if response.status_code != 200:
            raise ParserServiceError
        soup: BeautifulSoup = BeautifulSoup(markup=response.text, features="html.parser")
        table_body: Tag = soup.find("table").find("tbody")
        heroes: tuple[str, ...] = tuple(
            str(row.find("a", class_="link-type-hero").text) for row in table_body.find_all("tr"))
        return [Hero(name=x) for x in heroes]
