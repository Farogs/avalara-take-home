# Dictionary Command-Line Interface

This is a command-line interface allows users to use the Merriam-Webster dictionary API to get definitions of words.

## Getting Started
To use the Dictionary CLI, you will need to obtain an API key from Merriam-Webster. You can do so by following the instructions [here](https://dictionaryapi.com/register/index). Once you have your API key, you can use the CLI by running the following command:

```bash
make dictionary word=<your_word>
```
Testing
The code includes a test suite written using the unittest module. To run the tests, simply run:

```bash
make test
```
Package
To create a package that includes the dictionarycli.py, test_dictionary.py, and README.md files, run:

```bash
make package
```
This will create a directory named dictionary containing the files.

Cleaning up
To remove the package created by make package, run:

```bash
make clean
```
