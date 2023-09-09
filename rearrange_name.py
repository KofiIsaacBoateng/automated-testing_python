import re

def rearrange_name(name):
     pattern = r"^(\w+), (\w+)"
     result = re.search(pattern, name)
     if result is None:
          return name
     return "{} {}".format(result[2], result[1])

print(rearrange_name("Ada, Lovelace"))
