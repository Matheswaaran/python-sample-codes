#!/usr/bin/python

try:
  file = open("./files/messages.txt", 'r')
  content = file.read()
  print(content)
finally:
  file.close()

print("\n================================\n")

with open("./files/messages.txt", 'r') as file:
  lines = file.readlines()
  print(lines)

with open("./files/python.txt", 'w') as file:
  file.write("""Hello Python!
Awesome!""")

with open("./files/python.txt", 'a') as file:
  file.write("""\nThis is Mat!""")

with open("./files/lines.txt", "w") as file:
  lines = ["Hello Lines\n", "Line1\n", "Line2\n"]
  file.writelines(lines)