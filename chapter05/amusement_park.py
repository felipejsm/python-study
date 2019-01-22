# ELIF -> quando somente uma das possibilidades pode passar

# é possível utilizar múltiplos ELIF e, até mesmo, omitir o else
age = 12
if age < 4:
    print("Your admission cost $0")
elif age < 18:
    print("Your admission cost $5")
else:
    print("Your admission cost $10")