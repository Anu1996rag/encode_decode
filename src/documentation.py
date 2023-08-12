""" Documentation Module """
from colorama import Fore

from .algorithms import ENCODING_ALGORITHMS, DECODING_ALGORITHMS, HASHING_ALGORITHMS

STARTUP_DOCUMENT = f"""
{Fore.YELLOW}Encode, Decode and Hashing Shell
Description: A tool developed to encode, decode and hash a given string
Developed by: {Fore.CYAN}Anurag Sandeep Patil
{Fore.YELLOW}Date: Aug 12, 2023
Commands: encode, decode, hash, help, exit
\n
"""

ENCODING_DOCUMENT = f"""
Syntax : encode <text> <algorithm : {'|'.join(list(ENCODING_ALGORITHMS.keys()))}> 
"""

DECODING_DOCUMENT = f"""
Syntax : decode <text> <algorithm : {'|'.join(list(DECODING_ALGORITHMS.keys()))}> 
"""

HASHING_DOCUMENT = f"""
Syntax : hash <text> <algorithm : {'|'.join(list(HASHING_ALGORITHMS.keys()))}> 
"""

HELP_DOC = """
    Usage:

        To encode:
            encode <Text> <Algorithm>

        To decode:
            decode <Text> <Algorithm>

        To hash:
            hash <Text> <Algorithm>
"""
