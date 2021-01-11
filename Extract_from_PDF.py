from tika import parser # pip install tika
import os

filepath = "C:\\Users\\Dell\\Desktop\\Git Repos\\Document Classification\\"
i = 1
pdf_files = []
docx_files = []
for f in os.listdir(filepath):
  full_name = os.path.join(filepath, f) 
  if os.path.isfile(full_name):
    name = os.path.basename(f)
    filename, ext = os.path.splitext(name)
    if ext == '.pdf':
      pdf_files.append(name)
    elif ext == ('.docx'):
      docx_files.append(name)

print(pdf_files)
print(docx_files)


def extract_from_pdf(file):
  print("extracting from file:", file)
  raw = parser.from_file(filepath+file)
  print(raw['content'])
  f = open(filepath +'result_{}.txt'.format(file), 'w')
  f.write(raw['content'].strip())

for pdf_file in pdf_files:
    extract_from_pdf(pdf_file)    

for doc_file in docx_files:
    extract_from_pdf(doc_file) 
