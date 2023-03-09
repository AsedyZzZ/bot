from collections import defaultdict


class Calculator:
    @staticmethod
    def calculate(lst: list[dict[str, float]]) -> list[tuple[str, list[float]]]:
        result = defaultdict(list)

        for el in lst:
            for k, v in el.items():
                result[k].append(v)

        tuples = sorted(result.items(), key=lambda element: sum(element[1]), reverse=True)
        return tuples[:10]


class Answer:
    @staticmethod
    def make_answers(lst: list[tuple[str, list[float]]], num_hero: int) -> str:
        if 1 < num_hero < 6:
            answer = "\n".join("*" + str(round(sum(win_rates) / len(win_rates), 2)) + "*" + f" {hero_name}: {win_rates}"
                               for hero_name, win_rates in lst)

        elif num_hero == 1:
            answer = "\n".join(f"{hero_name}: *" + str(*win_rates) + "*" for hero_name, win_rates in lst)
        else:
            answer = "*Вы указали больше чем 5 героев!*"
        return answer
