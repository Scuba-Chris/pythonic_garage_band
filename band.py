class Bands:
    
    all_bands = []

    def __init__(self, band_name, members=[]):
        self.band_name = band_name
        self.members = members
        self.__class__.all_bands.append(self)

class Musician:

    def __init__(self, name, insturment):
        self.name = name
        self.insturment = insturment

class Singer(Musician):
    def __init__(self, name):
        super().__init__(name, 'singer')

class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, 'guitarist')

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, 'drummer')


