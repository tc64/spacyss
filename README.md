# Description
Custom sentence segmentation for spacy.

*Test on spacy 2.0.5*

# Segmenters Implemented
## Newline Segmenter
sentences in text are separated by one or more newline characters.


```python
from seg.newline.segmenter import NewLineSegmenter
import spacy

nlseg = NewLineSegmenter()

nlp = spacy.load('en')
nlp.add_pipe(nlseg.set_sent_starts, name='sentence_segmenter', before='parser')

doc = nlp(my_doc_text)
```
