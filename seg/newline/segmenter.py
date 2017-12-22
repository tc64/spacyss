
def set_sent_starts(doc):
    if set(doc[0].text) != {'\n'}:
        doc[0].is_sent_start = True
    else:
        doc[0].is_sent_start = False
    if len(doc) == 1:
        return doc

    for t in doc[1:]:
        if set(doc[t.i-1].text) == {'\n'} and set(t.text) != {'\n'}:  # we are at a sentence start
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
    nlp.add_pipe(set_sent_starts, name='sentence_segmenter', before='parser')
    doc = nlp(samples)