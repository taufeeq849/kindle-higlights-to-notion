import json


def extract_highlights():
    highlights = {}
    f = open("D:\documents\My Clippings.txt",
             encoding='cp437', errors='ignore')
    contents = f.read()
    for entry in contents.split('=========='):
        array = entry.splitlines()
        title_and_author = array[1]
        print(array)
        starting_author_index = title_and_author.find('(')
        ending_author_index = title_and_author.find(')')

        title = title_and_author[0: starting_author_index]
        author = title_and_author[starting_author_index +
                                  1: ending_author_index]
        time = array[2]
        if (array[3] != '\n'):
            highlight = array[3]
        else:
            highlight = array[4]

        highlights[title] = {'author': author, 'time': time, 'text': highlight}
    return highlights


print(extract_highlights())
