class Hero:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self):
        return f"HERO: {self.name}"
