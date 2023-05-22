json = [{
    "id": 1, "name": "a"
}, {
    "id": 2, "name": "b"
}]

for obj in json:
  if obj["id"] == 2:
    obj["name"] = 'something'

print(json)