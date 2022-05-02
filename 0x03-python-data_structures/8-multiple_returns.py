#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sentence[0] = "None"
    sentence_tuple = (len(sentence), sentence[0])
    return sentence_tuple
