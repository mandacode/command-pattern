from editor import Editor


class WriteCommand:

    def __init__(self, editor: Editor, text: str):
        self.editor = editor 
        self.text = text 

    def execute(self):
        self.editor.write(self.text)
    
    def undo(self):
        self.editor.remove(self.text)
