import json
from notion.client import NotionClient


def extract_highlights():
    highlights = {}
    f = open(".\My Clippings.txt", encoding="utf-8", errors="ignore")
    contents = f.read()
    split_contents = contents.split("==========")

    for i in range(0, len(split_contents) - 1):
        array = split_contents[i].splitlines()
        array = list(filter(None, array))

        if len(array) == 3:
            title_and_author = array[0]
            starting_author_index = title_and_author.find("(")
            ending_author_index = title_and_author.find(")")

            title = title_and_author[0:starting_author_index]
            author = title_and_author[starting_author_index + 1 : ending_author_index]
            time = array[1]
            highlight = array[2]
            single_highlight = {
                "location": time,
                "highlight": highlight,
            }
            key_value = title + "#" + author

            highlights.setdefault(key_value, []).append(single_highlight)

        else:
            continue
    return highlights


def add_to_notion(data):
    token = "d276369250b9a9a9ceb447d36fc46007ed1978ce733e41dca6875c9aa7e67dd16225e9f1bb41aad3b2695b96e24e993462093b1d628ad16ad5db8058eeec27f2b062eae980ffa0e8a02f0778604a"
    client = NotionClient(token_v2=token)
    url = "https://www.notion.so/e053742a9c8443dbb03d1f12a38d5a30?v=7c30bcec1be64c3584c6e593fa4ed31e"
    collection_view = client.get_collection(url)
    for entry in data:
        print(entry)


with open("data.json", "w") as outfile:
    json.dump(extract_highlights(), outfile)
