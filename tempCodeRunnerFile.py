def make_friendship_band(name1, name2, symbol='-', band_text='chota sa taddy'):
    band = name1 + ' ' + symbol + ' ' + band_text + ' ' + symbol + ' ' + name2
    return band

# Example usage
person1 = "Alice"
person2 = "Bob"
print(make_friendship_band(person1, person2))
