import json

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

print(json_object)
# Writing to sample.json
with open("test.json", "w") as outfile:
    outfile.write(json_object)