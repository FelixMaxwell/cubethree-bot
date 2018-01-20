import random

maj_arcana = ["The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World", "The Fool"]
maj_arcana_numbers = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "Ø"]

maj_arcana_a = ["{}: {}".format(maj_arcana_numbers[i], maj_arcana[i]) for i in range(len(maj_arcana))]

min_arcana = (["Ace"] + list(range(2,11)) + ["King", "Queen", "Knight", "Page"])*4
min_suit = ["Wands"]*14 + ["Cups"]*14 + ["Swords"]*14 + ["Pentacles"]*14

min_arcana_a = ["{} of {}".format(min_arcana[i], min_suit[i]) for i in range(len(min_arcana))]

tarot = maj_arcana_a + min_arcana_a

for i in range(3):
	print(random.choice(tarot))
