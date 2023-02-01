from dataclasses import dataclass

@dataclass
class User:
    id:int
    name:str
    number:int

pas = User(1,"Ivan",218506)

print(pas.__annotations__.keys)