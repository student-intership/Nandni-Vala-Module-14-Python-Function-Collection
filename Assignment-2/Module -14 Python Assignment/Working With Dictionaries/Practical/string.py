s = "hello world"

char_ = {}

for char in s:
    if char in char_:
        char_[char] += 1 
    else:
        char_[char] = 1  

print("Character counts:")
for char, count in char_.items():
    print(f"'{char}': {count}")
