def price_per_item(total_price, quantity):
    if quantity == 0:
        return "На ноль делить нельзя"
    return total_price / quantity


assert price_per_item(360, 6) == 60.0
assert price_per_item(100, 0) == "На ноль делить нельзя"
assert price_per_item(150, 3) == 50.0

words = ["чай", "кефир", "апельсин"]
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)