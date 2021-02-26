import getopt
import sys

from requests import get

from paperscraper import PaperScraper

scraper = PaperScraper()


def url_from_doi(doi):
    doi_link = "https://doi.org/" + doi
    r = get(doi_link, allow_redirects=True)
    print(r.url)
    text = print(scraper.extract_from_url(r.url)['pdf_url'])
    print(text)
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
