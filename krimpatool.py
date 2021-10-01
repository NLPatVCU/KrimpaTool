import getopt, sys, os, time
from requests import get
from paperscraper import PaperScraper
from medacy.model.model import Model
from medacy.data.annotations import Annotations
from medacy.pipelines import SystematicReviewPipeline
from medacy.pipelines import LstmSystematicReviewPipeline

scraper = PaperScraper()


# This method takes a list of DOIs from command line and converts them to text files
def doi_to_txt(doi_list):
	for doi in doi_list:
		doi_link = "https://doi.org/" + doi
		r = get(doi_link, allow_redirects=True)
		text = (scraper.extract_body_from_url(r.url))
		fileName = doi.replace("/","_") + ".txt"
		f = open(fileName, "w+")
		if text is None:
			print("Not able to get doi (" + doi_link + ")\n")
		else: 
			f.write(text)
		f.close()


# This method takes a list of DOIs from command line and converts them to text files
def doi_file_to_txt(file):
	i = open(file, "r")
	for doi in i:
		doi_link = "https://doi.org/" + doi
		print(doi_link)
		r = get(doi_link, allow_redirects=True)
		print(r.url)
		text = (scraper.extract_body_from_url(r.url))
		if text is None:
			print("Unable to retrieve text from" + doi_link)
		else:
			fileName = doi.replace("/","_") + ".txt"
			f = open(fileName, "w+")
			f.write(text)
			f.close()
		time.sleep(60)


# This method takes in a path to a medaCy model and a list of text files from the command line to be predicted on
# For a CRF model
def model_from_txt_crf(model, textFile_list):
	for textFile in textFile_list:
		text = ""
		with open(textFile, 'r') as file:
			text += file.read()
		#pipeline for particular crf model -- should eventually take input from command line
		pipeline = SystematicReviewPipeline(metamap=None, entities=['Species'])
		modelclass = Model(pipeline)
		modelclass.load(model)
		annotation = modelclass.predict(text)
		fileName = textFile.replace(".txt",".ann")
		annotation.to_ann(fileName)

# This method takes in a path to a medaCy model and a directory of text files to be predicted on
# For a CRF model
def model_from_dir_crf(model, directory):
	for textFile in os.listdir(directory):
		if textFile.endswith(".txt"):
			text = ""
			with open(textFile, 'r') as file:
				text += file.read()
			# pipeline for particular crf model -- should eventually take input from command line but for now is hard-coded
			pipeline = SystematicReviewPipeline(metamap=None, entities=['Species'])
			modelclass = Model(pipeline)
			modelclass.load(model)
			annotation = modelclass.predict(text)
			fileName = textFile.replace(".txt",".ann")
			annotation.to_ann(fileName)


# This method takes in a path to a medaCy model and a list of text files from the command line to be predicted on
# For a bilSTM model
def model_from_txt_bilstm(model, word_embeddings_path, textFile_list):
	for textFile in textFile_list:
		text = ""
		with open(textFile, 'r') as file:
			text += file.read()
		# pipeline for particular biLSTM model -- should eventually take input from command line but for now is hard-coded
		pipeline = LstmSystematicReviewPipeline(word_embeddings=word_embeddings_path, metamap=None, entities=['SOLVENT'], cuda_device=-1)
		modelclass = Model(pipeline)
		modelclass.load(model)
		annotation = modelclass.predict(text)
		fileName = textFile.replace(".txt",".ann")
		annotation.to_ann(fileName)

# This method takes in a path to a medaCy model and a directory of text files to be predicted on
# For a biLSTM model
def model_from_dir_bilstm(model, word_embeddings_path, directory):
	for textFile in os.listdir(directory):
		if textFile.endswith(".txt"):
			text = ""
			with open(textFile, 'r') as file:
				text += file.read()
			# pipeline for particular biLSTM model -- should eventually take input from command line but for now is hard-coded
			pipeline = LstmSystematicReviewPipeline(word_embeddings=word_embeddings_path, metamap=None, entities=['SOLVENT'], cuda_device=-1)
			modelclass = Model(pipeline)
			modelclass.load(model)
			annotation = modelclass.predict(text)
			fileName = textFile.replace(".txt",".ann")
			annotation.to_ann(fileName)



argv = sys.argv[1:]

try:
    opts, args = getopt.getopt(argv, "d:m:f")
except:
    print(" ")

def main():
	if sys.argv[1] == "-d" or sys.argv[1] == "-m":
		for opt, arg in opts:
			# For DOIs
			if opt in ["-d"]:
				# For DOIs straight from command line
				if sys.argv[2] == "-s":
					doi_list = sys.argv[3:]
					doi_to_txt(doi_list)
				# For a file containing DOIs seperated by whitespace
				elif sys.argv[2] == "-f":
                                        doi_list = sys.argv[3]
                                        doi_file_to_txt(doi_list)
				else:
					print("Error: -s for inputing DOIs from command line ot -f for a file of DOIs")

			# For medaCy
			if opt in ["-m"]:
				# For CRF Model
				if sys.argv[2] == "-c":
					model = sys.argv[3]
					# For .txt files inputed straight from the command line
					if sys.argv[4] == "-s":
						text_files = sys.argv[5:]
						model_from_txt_crf(model,text_files)
					# For a directory of .txt files
					elif sys.argv[4] == "-d":
						directory = sys.argv[5]
						model_from_dir_crf(model,directory)
				# For biLSTM
				elif sys.argv[2] == "-b":
					model = sys.argv[3]
					word_embeddings = sys.argv[4]
					# For .txt files inputed straight from the command line
					if sys.argv[5] == "-s":
						text_files = sys.argv[6:]
						model_from_txt_bilstm(model, word_embeddings, text_files)
					# For a directory of .txt files
					elif sys.argv[4] == "-d":
						directory = sys.argv[5]
						model_from_dir_bilstm(model, word_embeddings, directory)

				else:
					print("Invalid arguments")

if __name__ == '__main__':
    main()
