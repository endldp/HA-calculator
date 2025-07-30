class ConversionEngine:
    def __init__(self):
        # Conversion dictionaries for all categories
        self.weight = {...} # implement all weight conversions
        self.liquid = {...} # implement all liquid conversions
        self.distance = {...} # implement all distance conversions
        self.temperature = {...} # implement all temperature conversions
        self.area = {...} # implement all area conversions
        self.speed = {...} # implement all speed conversions
        self.cooking = {...} # implement all cooking conversions
    def convert(self, data):
        # Implement conversion logic based on data['type'], data['from'], data['to'], data['value']
        # Return result or error
        pass
