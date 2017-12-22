# Description
Custom sentence segmentation for spacy.

*Test on spacy 2.0.5*

# Segmenters Implemented
## Newline Segmenter
sentences in text are separated by one or more newline characters.


```python
from spacyss.seg.newline.segmenter import NewLineSegmenter
import spacy

nlseg = NewLineSegmenter()

nlp = spacy.load('en')
nlp.add_pipe(nlseg.set_sent_starts, name='sentence_segmenter', before='parser')

doc = nlp(my_doc_text)
```

# Implementing more segmenters
* create package under seg named for your sentence segmentation approach
* create segmenter.py under that package
* create a class for your segmenter with a method called set_sent_starts that takes a doc as the single argument.
  * It may be that spacy api allows for more flexible argument profile here, feel free to correct...