from interface import Command


class Editor:

    def __init__(self):
        self.text: str = '' 
        self.stack: list[Command] = []

    def write(self, text: str):
        self.text += text 
    
    def remove(self, text: str):
        self.text = self.text[:-len(text)]

    def execute_command(self, command: Command):
        command.execute()
        self.stack.append(command)
    
    def undo_command(self):
        if not self.stack:
            return
        
        command = self.stack.pop()
        command.undo()
