import json
from notion.client import NotionClient
from notion.block import PageBlock
from notion.block import TextBlock
from notion.block import BulletedListBlock
from notion.block import CollectionViewBlock


def add_to_notion(data):
    token = "d276369250b9a9a9ceb447d36fc46007ed1978ce733e41dca6875c9aa7e67dd16225e9f1bb41aad3b2695b96e24e993462093b1d628ad16ad5db8058eeec27f2b062eae980ffa0e8a02f0778604a"
    client = NotionClient(token_v2=token)
    url = "https://www.notion.so/cfbce83993014a57ac90b39ec9f83d7d?v=f4d1ef6753db4bbcbed7412deeccc6eb"
    collection_view = client.get_collection_view(url)
    for key, value in data.items():
        hash_index = key.find("#")
        title = key[0:hash_index]
        author = key[hash_index + 1 : len(key)]
        new_row = collection_view.collection.add_row()
        new_row.title = title
        new_row.author = author

        for highlight in value:

            if "location" not in highlight or "highlight" not in highlight:

                print("due to missing fields, skipped highlight: ", "\n", highlight)
            else:
                text = highlight["highlight"]
                new_row.children.add_new(BulletedListBlock, title=text)


with open("./data.json") as f:
    data = json.load(f)
add_to_notion(data)