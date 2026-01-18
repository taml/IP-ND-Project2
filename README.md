# Meme Generator

Welcome to the Meme Generator project, this is a Python project which allows the creation of a meme using three approaches. 
Firstly a meme can be randomly generated via a web interface, secondly a meme can be generated using a web interface via providing a quote and path to an image. Finally, via a CLI where a path and quote can be provided to generate an image.

This project consists of two primary modules which are outlined below, `QuoteEngine` and `MemeGenerator`. It also includes a `_data` folder which contains quotes within a variety of document formats (csv, doc, pdf and txt), photos and another folder which contains sample documents for highlighting document structure. Besides this, there is a templates folder for serving HTML and there are two python files, `app.py` and `meme.py` which serve as entry points for the app.

## QuoteEngine Module
The purpose of the QuoteEngine module is to generate a quote using an ingestor via a complex strategy pattern.
This module depends on a few packages such as: 
```
pandas
docx
```

## MemeGenerator Module
The purpose of the MemeGenerator is to apply a given quote to a given image in a 'meme' style.
This module depends on a few packages such as:
```
pillow (PIL)
```

### Requirements
To run the Meme Generator you will need Python 3.9 installed and you will need [XpdfReader](https://www.xpdfreader.com/pdftotext-man.html) installed. To install XpdfReader for your environment please follow the instructions found via the website. Installation varies slightly depending upon Linux, Mac or Windows. 

### Installation
It's recommended that this project is run using a virtual environment to ensure that all correct package versions are installed. To setup a virtual environment first install [`python3-venv`](https://docs.python.org/3/library/venv.html), installation method will vary depending on your device. 
Next, create a new virtual environment within the project `python3.9 -m venv .venv` and then activate it using `source .venv/bin/activate`.

To install the project there is a `requirements.txt` file in the root of the project which contains all of the relevant packages and corresponding versions.
To install from this file please navigate to the root level of the project and run `pip install -r requirements.txt`.

### Running the Web App
To run the Web App of the Meme Generator project, use `python3 app.py`. This will start a web server on port 5000, and you can visit the web interface at [http://127.0.0.1:5000](http://127.0.0.1:5000).



### Running the CLI App
To run the CLI App of the Meme Generator projects use `python3 meme.py`,
The project takes three optional arguments:

- A string quote body `--body`
- A string quote author `--author`
- An image path `--path`

When running the project via the CLI the path to a generated meme image will be used. If no path is passed to the CLI then a random image will be used to create the meme.