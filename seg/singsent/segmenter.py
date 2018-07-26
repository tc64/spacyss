"""
This segmenter is potentially useful for small docs that should be treated as a single sentence. May work better
for tweets than default segmentation based on parsing.
"""

class TrivialSegmenter(object):
    def __init__(self):
        pass

    def set_sent_starts(self, doc):
        doc[0].is_sent_start = True

        for t in doc[1:]:
            t.is_sent_start = False

        return doc


if __name__ == "__main__":
    samples = """
    summ tweet stufff https://t.co/fjSFjfj9k @Som1 @somOneElse this @isaSentence... sorta kinda not really ;-)
    """

    import spacy

    nlp = spacy.load('en')
    nlp.add_pipe(TrivialSegmenter().set_sent_starts, name='sentence_segmenter', before='parser')
    doc = nlp(samples)
