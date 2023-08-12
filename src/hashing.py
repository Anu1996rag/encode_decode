from .algorithms import HASHING_ALGORITHMS


def hash_text(text: str | bytes, algorithm: str) -> str:
    """
    Returns the hashed value based on the text and
    valid algorithm provided
    Parameters
    ----------
    text
    algorithm

    Returns
    -------
    hashed text
    """
    if isinstance(text, str):
        text = text.encode()

    hashing_algorithm = HASHING_ALGORITHMS[algorithm]
    return hashing_algorithm(text).hexdigest()
