# import sys

# print(sys.argv[1])

text = "Hello123World45!"

result = "".join(filter(lambda x: x.isalpha(), text))

print(result)