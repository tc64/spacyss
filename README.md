# Description
Custom sentence segmentation for spacy.

# Segmenters Implemented
## Newline Segmenter
sentences in text are separated by one or more newline characters.


```python
from spacyss.seg.newline import set_sent_starts as newline_segmenter
import spacy

nlp = spacy.load('en')
nlp.add_pipe(newline_segmenter, name='sentence_segmenter', before='parser')

doc = nlp(my_doc_text)
```
