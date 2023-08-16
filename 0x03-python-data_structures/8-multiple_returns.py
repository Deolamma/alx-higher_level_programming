#!/usr/bin/python3
def multiple_returns(sentence):
    """Making multiple returns
        Args:
            sentence: String to be indexed

        Returns:
            Returns a tuple: sentence Length and first char of sentence
    """

    sentence_len = len(sentence)
    if sentence == "":
        return sentence_len, None
    return sentence_len, sentence[0]
