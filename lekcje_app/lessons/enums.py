

class Subjects:
    choices = (
        ('fizyka', 'fizyka'),
        ('matematyka', 'matematyka'),
        ('angielski', 'angielski')
    )

    def getKeys(self):
        return [key for key, display_name in self.choices]
