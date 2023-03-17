class BaseDictionary(dict):
    def __missing__(self, key):
        return 'nothing'