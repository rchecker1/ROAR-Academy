import PyPDF2
import re
import string
file_handle = open("sense-and_sensiblity-byjane-austen.pdf", "rb")
reader = PyPDF2.PdfReader(file_handle)
page_number = len(reader.pages)
freq_table = {}

for i in range(page_number):
    page_object = reader.pages[i]
    page_text = page_object.extract_text()
    lines = page_text.split('/n')