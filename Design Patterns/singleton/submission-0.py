class Singleton:
    _instance = None
    val = None
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def getValue(self) -> str:
        return self.val

    def setValue(self, value: str):
        self.val = value
        
