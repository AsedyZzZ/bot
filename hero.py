import requests
from bs4 import BeautifulSoup


class Hero:
    def __init__(self, name): #Здесь вся нужная информация для парсинга
        self.headers = {'User-Agent': 'Bot'
                        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 '
                        # 'Safari/537.36 OPR/92.0.0.0'
                        }

        self.name = name.replace(' ', '-')
        self.link = 'https://ru.dotabuff.com/heroes/%s' % name.lower() + '/counters'
        self.response = requests.get(self.link, headers=self.headers)
        if self.response.status_code == 200:
            self.block = BeautifulSoup(self.response.text, 'lxml').find('table', class_="sortable")
            self.table = self.block.find_all('tr')
        self.win_rate = []

    def get_win_rate(self):
        """Этот метод находит нам винрейты и если они положительные сохраняет"""
        if self.response.status_code == 200:
            win_rate_of_hero = dict()
            res = []
            for tr in self.table:
                td = tr.find_all('td')
                row = [tr.text.strip() for tr in td if tr.text.strip()]
                if row:
                    res.append(row)
                    row.pop(3)
                    row.pop(1)
                    row[1] = 100 - float(row[1][:len(row[1]) - 1])
                    win_rate_of_hero[row[0]] = list()
                    win_rate_of_hero[row[0]].append(row[1])

            self.win_rate = win_rate_of_hero
            return self.win_rate
        else:
            return f'Something goes wrong. Please try again. Status code: {self.response.status_code}'

# def show_result(heroes_now, x=1):
#     carry = ['Anti-Mage', 'Phantom-Lancer', 'Chaos-Knight', 'Ursa', 'Slark', 'Sven', 'Riki', 'Phantom-Assassin',
#              'Lifestealer', 'Faceless-Void', 'Spectre']
#
#     for hero in heroes_now:
#
#         print(f'{hero[:8]} - {heroes_now[hero]} %')
        #     c = 0
        #     win_rate = ''
        #     for i in range(len(heroes_now.get(hero))):
        #         d = 100 - heroes_now.get(hero)[i]
        #         if d > 50:
        #             c += 1
        #         win_rate = win_rate + str(d) + '%  '
        #     if (c == x) and (hero in carry):
        #         print(f'Best: {hero[:8]}  {win_rate}   *')
        #     elif c == x:
        #         print(f'Nice: {hero[:8]}  {win_rate}')
        #     elif c == x - 1 and x != 1:
        #         print(f'Good: {hero[:8]}  {win_rate}')


class GroupHero:
    pass


heroes_dict = {"Tusk": "Tusk", "Mirana": "Mirana", "Rubick": "Rubick",
               "Tiny": "Tiny", "Primal Beast": "Primal Beast", "Crystal Maiden": "Crystal Maiden",
               "Treant Protector": "Treant Protector", "Razor": "Razor", "Pangolier": "Pangolier",
               "Shadow Fiend": "Shadow Fiend", "Leshrac": "Leshrac", "Ursa": "Ursa",
               "Faceless Void": "Faceless Void", "Silencer": "Silencer", "Pudge": "Pudge",
               "Lina": "Lina", "Doom": "Doom", "Riki": "Riki",
               "Hoodwink": "Hoodwink", "Drow Ranger": "Drow Ranger", "Morphling": "Morphling",
               "Ember Spirit": "Ember Spirit", "Dawnbreaker": "Dawnbreaker", "Marci": "Marci",
               "Snapfire": "Snapfire", "Monkey King": "Monkey King", "Mars": "Mars",
               "Sniper": "Sniper", "Zeus": "Zeus", "Legion Commander": "Legion Commander",
               "Naga Siren": "Naga Siren", "Bloodseeker": "Bloodseeker", "Bounty Hunter": "Bounty Hunter",
               "Skywrath Mage": "Skywrath Mage", "Undying": "Undying", "Earthshaker": "Earthshaker",
               "Broodmother": "Broodmother", "Magnus": "Magnus", "Invoker": "Invoker",
               "Jakiro": "Jakiro", "Spirit Breaker": "Spirit Breaker", "Clockwerk": "Clockwerk",
               "Lifestealer": "Lifestealer", "Windranger": "Windranger", "Lycan": "Lycan",
               "Batrider": "Batrider", "Nature's Prophet": "Nature's Prophet", "Nyx Assassin": "Nyx Assassin",
               "Disruptor": "Disruptor", "Viper": "Viper", "Beastmaster": "Beastmaster",
               "Sven": "Sven", "Death Prophet": "Death Prophet", "Queen of Pain": "Queen of Pain",
               "Enchantress": "Enchantress", "Weaver": "Weaver", "Huskar": "Huskar",
               "Tinker": "Tinker", "Lich": "Lich", "Puck": "Puck",
               "Timbersaw": "Timbersaw", "Earth Spirit": "Earth Spirit", "Witch Doctor": "Witch Doctor",
               "Venomancer": "Venomancer", "Dazzle": "Dazzle", "Dark Willow": "Dark Willow",
               "Outworld Destroyer": "Outworld Destroyer", "Tidehunter": "Tidehunter", "Phoenix": "Phoenix",
               "Techies": "Techies", "Anti-Mage": "Anti-Mage", "Enigma": "Enigma",
               "Ogre Magi": "Ogre Magi", "Gyrocopter": "Gyrocopter", "Templar Assassin": "Templar Assassin",
               "Bane": "Bane", "Void Spirit": "Void Spirit", "Winter Wyvern": "Winter Wyvern",
               "Dark Seer": "Dark Seer", "Storm Spirit": "Storm Spirit", "Visage": "Visage",
               "Lion": "Lion", "Io": "Io", "Juggernaut": "Juggernaut",
               "Terrorblade": "Terrorblade", "Lone Druid": "Lone Druid", "Kunkka": "Kunkka",
               "Grimstroke": "Grimstroke", "Chaos Knight": "Chaos Knight", "Clinkz": "Clinkz",
               "Slardar": "Slardar", "Pugna": "Pugna", "Arc Warden": "Arc Warden",
               "Necrophos": "Necrophos", "Night Stalker": "Night Stalker", "Vengeful Spirit": "Vengeful Spirit",
               "Alchemist": "Alchemist", "Phantom Lancer": "Phantom Lancer", "Phantom Assassin": "Phantom Assassin",
               "Abaddon": "Abaddon", "Axe": "Axe", "Keeper of the Light": "Keeper of the Light",
               "Dragon Knight": "Dragon Knight", "Omniknight": "Omniknight", "Shadow Shaman": "Shadow Shaman",
               "Spectre": "Spectre", "Wraith King": "Wraith King", "Ancient Apparition": "Ancient Apparition",
               "Shadow Demon": "Shadow Demon", "Brewmaster": "Brewmaster", "Sand King": "Sand King",
               "Warlock": "Warlock", "Oracle": "Oracle", "Luna": "Luna",
               "Troll Warlord": "Troll Warlord", "Centaur Warrunner": "Centaur Warrunner", "Chen": "Chen",
               "Bristleback": "Bristleback", "Elder Titan": "Elder Titan", "Underlord": "Underlord",
               "Medusa": "Medusa", "Meepo": "Meepo", "Slark": "Slark"}
a = GroupHero(['Razor', 'Tiny'], 2)
a.get_result()