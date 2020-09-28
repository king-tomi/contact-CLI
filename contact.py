class Contact:

    def __init__(self,name: str, number: int):
        self._name = name
        self._number = number

    @property
    def name(self):
        return self._name

    @property
    def number(self):
        return self._number