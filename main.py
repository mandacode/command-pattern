from command import WriteCommand
from editor import Editor


def main():
    editor = Editor()

    cmd = WriteCommand(editor, text="Hi!")
    editor.execute_command(cmd)

    print(editor.text)

    cmd = WriteCommand(editor, text=" Today is beautiful, isn't it?")
    editor.execute_command(cmd)

    print(editor.text)

    editor.undo_command()

    print(editor.text)


if __name__ == "__main__":
    main()
