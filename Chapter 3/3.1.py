import random

content=["Alice","Bob","CCb"]
print(content[2])
print(f"I hate{content[random.randint(0,2)]}")
content.append("Dick")
print(f"I love {content[3]}")
content.insert(1,"Elbert")
print(content[1])
del content[0]
print(content[0])

new=["A","B","C"]
new.pop()
new.remove("A")
print(new)