size = "medium"
toppings = ['onion','bacon','ham','pineapple', 'anchovies']

c = 0
t = 0
if size == "small":
    c = 14
elif size == "medium":
    c = 16
else:
    c = 18

t = 0.1 * c * len(toppings)

if 'bacon' in toppings:
    print(c + t + 5)
elif 'anchovies' in toppings:
    print(c + t + 5)
else:
    print(c + t)

