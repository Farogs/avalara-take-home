.PHONY: build test package clean

build:
		# no need to compile python

test:
		python test_dictionary.py

dictionary:
		python dictionarycli.py $(word)

package:
		mkdir -p dictionary
		cp dictionarycli.py dictionary
		cp test_dictionary.py dictionary
		cp README.md dictionary

clean:
		rm -rf dictionary