import os

from dotenv import find_dotenv, load_dotenv

from services.heroes_parser import DotabuffHeroesParser, HeroesParser

load_dotenv(find_dotenv())

TOKEN = os.getenv("TOKEN")
HEROES_PARSER: HeroesParser = DotabuffHeroesParser()
