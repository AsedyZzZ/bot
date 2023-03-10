from collections import defaultdict


class Calculator:
    @staticmethod
    def calculate(lst: list[dict[str, float]], top: int | None = None) -> list[tuple[str, list[float]]]:
        result = defaultdict(list)

        for el in lst:
            for k, v in el.items():
                result[k].append(v)

        tuples = sorted(result.items(), key=lambda element: sum(element[1]), reverse=True)
        return tuples if top is None else tuples[:top]
