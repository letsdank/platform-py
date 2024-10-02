
class WorldCountryDescription:
    # Alias: ОписаниеСтраныМира
    def __init__(self):
        self.code = ""
        self.code_alpha2 = ""
        self.code_alpha3 = ""
        self.name = ""
        self.full_name = ""
        self.international_name = ""
        self.is_eaeu = False
        self.is_not_actual = False

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        return f"{self.name} ({self.code})"

    def __repr__(self):
        return f"{self.name} ({self.code})"