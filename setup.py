import setuptools, paperscraper

def readme():
    with open('README.md') as f:
        return f.read()

setuptools.setup(
    name='krimpatool',
    version='0.1',
    description='Input DOI and return paper text',
    long_description=readme(),
    packages=setuptools.find_packages(),
#    url='https://github.com/NLPatVCU/PDF2TXT',
    author="Shaandro Sarkar, Bridget McInnes",
    author_email='sssarkar@vcu.edu',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: English',
        'Topic :: Text Processing :: Linguistic',
        'Intended Audience :: Science/Research'
    ],
    install_requires=[

    ],
)