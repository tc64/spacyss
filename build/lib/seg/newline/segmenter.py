import re


class NewLineSegmenter(object):
    ALL_SPACE = re.compile('\s+$')
    def __init__(self):
        pass

    def set_sent_starts(self, doc):
        if self.ALL_SPACE.match(doc[0].text):
            doc[0].is_sent_start = True
        else:
            doc[0].is_sent_start = False
        if len(doc) == 1:
            return doc

        for t in doc[1:]:
            if self.ALL_SPACE.match(doc[t.i-1].text) and not self.ALL_SPACE.match(t.text):
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
    nlp.add_pipe(NewlineSegmenter().set_sent_starts, name='sentence_segmenter', before='parser')
    doc = nlp(samples)