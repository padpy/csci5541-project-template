from transformers import AutoTokenizer
import pymupdf as reader


# set campaign book filename
filename = "C:/Users/jackl/Desktop/5541/5541_Project/armyofthedamned.pdf"

pdf = reader.open(filename)

introduction_text = ''
for page in pdf.pages(0, 7):
    introduction_text += page.get_text("text")
part1_text = ''
for page in pdf.pages(7, 14):
    part1_text += page.get_text("text")
part2_text = ''
for page in pdf.pages(14, 24):
    part2_text += page.get_text("text")
part3_text = ''
for page in pdf.pages(24, 37):
    part3_text += page.get_text("text")
part4_text = ''
for page in pdf.pages(37, 46):
    part4_text += page.get_text("text")
part5_text = ''
for page in pdf.pages(46, 60):
    part5_text += page.get_text("text")
conclusion_text = ''
for page in pdf.pages(60, 62):
    conclusion_text += page.get_text("text")
special_items_text = ''
for page in pdf.pages(62, 65):
    special_items_text += page.get_text("text")
monsters_text = ''
for page in pdf.pages(65, 73):
    monsters_text += page.get_text("text")

section_text = [introduction_text,part1_text,part2_text,part3_text,part4_text,part5_text,conclusion_text,special_items_text,monsters_text]

# create tokenizers
distilbert_tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
bert_cased_tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')
roberta_tokenizer = AutoTokenizer.from_pretrained('roberta-base')

# set tokenizer method
tokenizer = distilbert_tokenizer

vocab = {v: k for k, v in tokenizer.vocab.items()}
section_tokens = []
for section in section_text:
    section_tokens.append(tokenizer(section))

# section text is a list of sections of the campaign book - each index is a the raw text of a section
# section tokens is a list of sections of the campaign book as tokens- each index is the tokenized text of a section