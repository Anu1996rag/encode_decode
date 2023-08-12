from .commands import COMMANDS
from .documentation import STARTUP_DOCUMENT


def process_user_input(text: str) -> tuple[str, list[str]]:
    """
    Processes the input taken from the command shell, separate out
    command and the arguments list
    Parameters
    ----------
    text

    Returns
    -------
    Tuple of command and list of arguments
    """
    if not text:
        return "", []
    command, arguments = text.split()[0], text.split()[1:]
    command = command.lower().strip()
    arguments = [argument.strip() for argument in arguments]

    return command, arguments


def execute_command(command: str, arguments: list[str]) -> None:
    """
    Executes the valid command with the given list of arguments.
    If the command is not valid, prints out the valid instruction on the
    command shell.
    Parameters
    ----------
    command
    arguments

    Returns
    -------
    None
    """
    if not command:
        return

    if command in COMMANDS:
        COMMANDS[command](arguments)
    else:
        print(f"Please enter a valid command : \n {','.join(list(COMMANDS.keys()))}")


def run_command_shell() -> None:
    """
    Runs the command shell
    Returns
    -------
    None
    """
    print(STARTUP_DOCUMENT)
    while True:
        user_input = input()
        command, arguments = process_user_input(user_input)
        execute_command(command, arguments)
