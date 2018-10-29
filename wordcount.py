#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""
"""
Assignment: Wordcount

Description: Take in a file and return the number of words in the file. Also, take in 2 commands that change how it is run.

Author: Aaron Jackson
Github: TimeApollo
"""
__author__ = "TimeApollo"

import sys
import re

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def word_dict( filename ):
    """returns a dict of keys of words and value of total count"""
    word_count = {}
    f = open( filename , 'rU')
    text = f.read().lower().split()
    f.close()
    for word in text:
        # the regex finds all non letters and any single quote with no letter after it.
        word_no_punct = re.sub(r"[^a-z']+|\'(?![a-z]+)" , '' , word )
        if not word_no_punct:
            continue
        elif word_count.get(word_no_punct):
            word_count[word_no_punct] += 1
        else:
            word_count[word_no_punct] = 1
    return word_count


def print_top( filename ):
    word_sort = sorted(word_dict(filename).items() , key=lambda pair: pair[1] , reverse=True)
    for key , val in word_sort[:20]:
        print( key + " " + str(val) )

def print_words( filename ):
    for key , val in word_dict(filename).items():
        print( key + " " + str(val) )

def main():
    if len(sys.argv) != 3:
        print 'usage: ./wordcount.py {--count | --topcount} file'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print 'unknown option: ' + option
        sys.exit(1)


if __name__ == '__main__':
    main()
