"""
This tool provides an all-in-one platform to encode , decode or hash
a given text.

Encode, Decode and Hashing Shell
Description: A tool developed to encode, decode and hash a given string
Developed by: Anurag Sandeep Patil
Date: Aug 12, 2023
Commands: encode, decode, hash, help, exit

Examples:
     hash abcd md5
     dj4723847rh4839rh338204234830e

"""


from src.commands import initiate_commands
from src.core import run_command_shell


def main():
    """
    Tool execution starts here
    Returns
    -------
    None
    """
    initiate_commands()
    run_command_shell()


if __name__ == "__main__":
    main()
