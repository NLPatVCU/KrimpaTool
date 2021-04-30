# KrimpaTool
A tool for retrieving full text of papers from a DOI

Commands
===
Converts DOIs straight from the command line to .txt files
```python
krimpatool.py -d -s <DOI> <optional_DOI> <...>
```

Takes a .txt file of DOIs separated by whitespace and converts each one to .txt file
```python 
krimpatool.py -d -f <file_of_DOIs.txt>
```
Takes a CRF model and predicts on a given .txt file
```python 
krimpatool.py -m -c <CRF_model> -s <text_file.txt>
```
Takes a CRF model and predicts on a .txt files in a given directory
```python 
krimpatool.py -m -c <CRF_model> -d <directory_of_txt_files>
```

Takes a biLSTM model and predicts on a given .txt file
```python 
krimpatool.py -m -b <biLSTM_model> <word_embeddings> -s <text_file.txt>
```
Takes a biLSTM model and predicts on a .txt files in a given directory
```python 
krimpatool.py -m -b <biLSTM_model> <word_embeddings> -d <directory_of_txt_files>
```
