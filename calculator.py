from collections import defaultdict


class Calculator:
    @staticmethod
    def calculate(lst: list[dict[str, float]]) -> dict[str, list[float]]:
        result = defaultdict(list)
        for el in lst:
            for k, v in el.items():
                result[k].append(v)
        return result



