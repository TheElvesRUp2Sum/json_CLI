import json_explore

json_example: dict = \
{"menu": {
  "id": 29,
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}

print(f"Let's explore the above json using the json explore function")
print()

json_explore.json_explore_json(json_example)

print(f"Now lets explore the same json using the file path function")
print()

json_explore.json_explore_fp("test.json")