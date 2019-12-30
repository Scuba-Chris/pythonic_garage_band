

class Bands:
    
    all_bands = []
   
    def __init__(self, band_name, members):
        self.band_name = 'band_name'
        self.members = members
        self.__class__.all_bands.append(self)
    
    def to_list(self):
        return self.all_bands

    def __str__(self):
        return f'the band name is {self.band_name}'

    def __repr__(self):
        return f'band: {self.band_name}'

class Musician:

    def __init__(self, name, insturment):
        self.name = name
        self.insturment = insturment

    def __str__(self):
        return f'I am the {self.insturment}'

    def __repr__(self):
        return f'band member is: {self.insturment}'

class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, 'guitarist')

class Singer(Musician):
    def __init__(self, name):
        super().__init__(name, 'singer')

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, 'drummer')
