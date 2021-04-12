import getopt
import sys

from requests import get

from paperscraper import PaperScraper

scraper = PaperScraper()


def url_from_doi(doi):
    doi_link = "https://doi.org/" + doi
    r = get(doi_link, allow_redirects=True)
    print(r.url)
    text = (scraper.extract_body_from_url(r.url))
    fileName = doi.replace("/","_") + ".txt"
    f = open(fileName, "w+")
    f.write(text)
    f.close()
    return text


argv = sys.argv[1:]

try:
    opts, args = getopt.getopt(argv, "d")
except:
    print("Error, not a valid option")


def main():
    if sys.argv[1] == "-d":
        for opt, arg in opts:
            if opt in ["-d"]:
                doi = sys.argv[2]
                url_from_doi(doi)
    else:
        print("Must include '-d <doi>' ")


if __name__ == '__main__':
    main()
