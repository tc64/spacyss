"""
This segmenter's template was based on reading the following github issue:
https://github.com/explosion/spaCy/pull/1400
"""

import re

class NewLineSegmenter(object):
    def __init__(self):
        pass

    def is_nl_token(self, t):

        # if a token consists of all space, and has at least one newline char, we segment as a sentence.
        if t.is_space and '\n' in t.text:
            return True
        else:
            return False

    def set_sent_starts(self, doc):
        if self.is_nl_token(doc[0]):
            doc[0].is_sent_start = True
        else:
            doc[0].is_sent_start = False
        if len(doc) == 1:
            return doc

        for t in doc[1:]:
            if self.is_nl_token(doc[t.i - 1]) and not self.is_nl_token(t):
                t.is_sent_start = True
            else:
                t.is_sent_start = False

        return doc


if __name__ == "__main__":
    samples = """

         this is my first sentence
    this is my second one    
    third one!

             definitely



    difrent sents in
    these lines heree

    """

    import spacy

    nlp = spacy.load('en')
    nlp.add_pipe(NewLineSegmenter().set_sent_starts, name='sentence_segmenter', before='parser')
    doc = nlp(samples)
