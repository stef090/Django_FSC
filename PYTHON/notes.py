import re

def multi_re_find(patterns, phrase):

    for pattern in patterns:
        print("Searching for pattern {}".format(pattern))
        print(re.findall(pattern,phrase))
        print('\n')


test_phrase = "This is a string with numbers 12312 and a symbol #hashtag"

test_patterns = [r'\W+']

multi_re_find(test_patterns,test_phrase)
