from typing import Protocol


class Command(Protocol):

    def execute(self):
        pass 

    def undo(self): 
        pass 
