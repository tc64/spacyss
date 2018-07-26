# Description
Custom sentence segmentation for spacy.

```bash
pip install spacyss
```

*Tested on spacy 2.0.5*

# Segmenters Implemented
## Newline Segmenter
sentences in text are separated by one or more newline characters.

## Example
```python
from seg.newline.segmenter import NewLineSegmenter  # note that pip package is called spacyss
import spacy

nlseg = NewLineSegmenter()

nlp = spacy.load('en')
nlp.add_pipe(nlseg.set_sent_starts, name='sentence_segmenter', before='parser')

doc = nlp(my_doc_text)
```

## Single Sentence (or "Trivial") Segmenter
the text is treated as a single sentence. may be better for tweets or other short informal texts where over segmentation may cause more problems than undersegmentation.

# Implementing more segmenters
* create package under seg named for your sentence segmentation approach
* create segmenter.py under that package
* create a class for your segmenter with a method called set_sent_starts that takes a doc as the single argument.
  * It may be that spacy api allows for more flexible argument profile here, feel free to correct...
