class Person:
    def __init__(self,name) -> None:
        self.name=name
    def __str__(self) -> str:
        return f'I am {self.name}'
print(Person('Sujal'))