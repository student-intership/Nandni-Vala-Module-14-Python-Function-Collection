d = {1: 'Apple', 2: 'Banana', 3: 'Kiwi'}
print("first Dictionary : ",d)

key_to_update = 2
new_value = 'Mango'
if key_to_update in d:
    d[key_to_update] = new_value
    print(f"Updated Dictionary: {d}")
else:
    print(f"Key {key_to_update} not found in the dictionary.")
