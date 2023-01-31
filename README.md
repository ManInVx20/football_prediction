# Football analyzing and prediction

This is a Python project that help us learn how to crawl data, clean data, analyze data and build model based on data.

## Dependencies
You must install [Python](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/) before installing these packages:
- [Scrapy](https://pypi.org/project/Scrapy/)
- [scrapy-selenium](https://pypi.org/project/scrapy-selenium/)
- [Jupyter](https://pypi.org/project/jupyter/)
- [matplotlib](https://pypi.org/project/matplotlib/)
- [seaborn](https://pypi.org/project/seaborn/)
- [scikit-learn](https://pypi.org/project/scikit-learn/)

## Usage

### Data gathering

Crawl data by going `crawler` directory and type this command:
```sh
scrapy crawl match -o ../dataset/data.csv
```
You will have a file called `data.csv` in `dataset` directory until it finishes.

### Data cleaning

Run `data_cleaning.ipynb` file in `notebook` directory.

You will have a file call `cleaned_data.csv` in `dataset` directory until it finishes.

### Data analyzing

Run `exploratory_analysis.ipynb` file in `notebook` directory.

You will have a file call `analyzed_data.csv` in `dataset` directory until it finishes.

### Model builing

Run `machine_learing.ipynb` file in `notebook` directory.
