from time import sleep
from typing import Callable

from .algorithms import ENCODING_ALGORITHMS, DECODING_ALGORITHMS, HASHING_ALGORITHMS
from .documentation import (ENCODING_DOCUMENT, DECODING_DOCUMENT, HASHING_DOCUMENT,
                           HELP_DOC)
from .encoding import encode, decode
from .hashing import hash_text

COMMANDS: dict[str, Callable[[list[str]], None]] = {}


def add_command(command: str, function: Callable[[list[str]], None]) -> None:
    """
    This function adds any new command created and save it at runtime.
    Parameters
    ----------
    command
    function

    Returns
    -------
    None
    """
    COMMANDS[command] = function


def process_encode(args: list[str]) -> None:
    """
    Processes input arguments given through the shell and encode it.
    Parameters
    ----------
    args

    Returns
    -------
    None
    """
    if len(args) != 2:
        print(ENCODING_DOCUMENT)
        return
    text, algorithm = args

    if algorithm not in ENCODING_ALGORITHMS:
        print("Invalid Encoding Algorithm.")
        print(f"Valid Encoding Algorithms : "
              f"{'|'.join(list(ENCODING_ALGORITHMS.keys()))}")
        return
    encoded_text = encode(text, algorithm)
    print(encoded_text)


def process_decode(args: list[str]) -> None:
    """
    Processes input arguments given through the shell and decode it.
    Parameters
    ----------
    args

    Returns
    -------
    None
    """
    if len(args) != 2:
        print(DECODING_DOCUMENT)
        return
    text, algorithm = args

    if algorithm not in DECODING_ALGORITHMS:
        print("Invalid Decoding Algorithm.")
        print(f"Valid Decoding Algorithms : "
              f"{'|'.join(list(DECODING_ALGORITHMS.keys()))}")
        return
    decoded_text = decode(text, algorithm)
    print(decoded_text)


def process_hash(args: list[str]) -> None:
    """
    Processes input arguments given through the shell and hash it.
    Parameters
    ----------
    args

    Returns
    -------
    None
    """
    if len(args) != 2:
        print(HASHING_DOCUMENT)
        return
    text, algorithm = args

    if algorithm not in HASHING_ALGORITHMS:
        print("Invalid Hashing Algorithm.")
        print(f"Valid Hashing Algorithms : {'|'.join(list(HASHING_ALGORITHMS.keys()))}")
        return
    hashed_text = hash_text(text, algorithm)
    print(hashed_text)


def command_help(_: list[str]) -> None:
    """
    Prints the help documentation on the command shell
    Parameters
    ----------
    _

    Returns
    -------
    None
    """
    print(HELP_DOC)


def exit_shell(_: list[str]) -> None:
    """
    Exits the shell
    Parameters
    ----------
    _

    Returns
    -------
    None
    """
    print("Exiting", end="")
    for i in range(1, 4):
        print(".", end="")
        sleep(1)
    exit(0)


def initiate_commands() -> None:
    """
    Adds all the commands into the COMMANDS dictionary whenever the tool runs
    Returns
    -------
    None
    """
    add_command("encode", process_encode)
    add_command("decode", process_decode)
    add_command("hash", process_hash)
    add_command("help", command_help)
    add_command("exit", exit_shell)
