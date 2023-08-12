from .algorithms import ENCODING_ALGORITHMS, DECODING_ALGORITHMS


def encode(text: str | bytes, algorithm: str) -> str:
    """
    Returns the encoded value based on the text and
    valid algorithm provided
    Parameters
    ----------
    text
    algorithm

    Returns
    -------
    encoded text
    """
    if isinstance(text, str):
        text = text.encode()
    encoding_algorithm = ENCODING_ALGORITHMS[algorithm]
    return encoding_algorithm(text).decode()


def decode(text: str | bytes, algorithm: str) -> str:
    """
    Returns the decoded value based on the text and
    valid algorithm provided
    Parameters
    ----------
    text
    algorithm

    Returns
    -------
    decoded text
    """
    if isinstance(text, str):
        text = text.encode()
    decoding_algorithm = DECODING_ALGORITHMS[algorithm]
    return decoding_algorithm(text).decode()
