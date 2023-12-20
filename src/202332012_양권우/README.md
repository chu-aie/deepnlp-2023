# yang gwon woo
202332012
## Descption

![image](https://github.com/GreatBritanBias/deepnlp-2023/assets/88702293/569ca27a-56f7-4a0c-802f-c8e1285e520a)

!pip install gensim
from gensim.summarization.summarizer import summarizer
!pip install gensim 5.9.2
!pip install gensim.summarization
!pip install sumy

from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import

def get_text(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text
   

def summarize_text(text, sentences_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer('korean'))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentences_count)
    summary = [str(sentence) for sentence in summary]
    return ' '.join(summary)
filename = 기획서 202332012양권우.hwp
text = get text(filename)


이미지 첨부가 안될걸 대비해   코드도 같이 첨부함
