import random,sys
art = ['the','a','an']
sub = ['cat','dog','man','women','horse','boy']
v = ['sang','ran','jumped','hoped','laughed']
adv = ['loudly','quietly','well','badly','ironically']
def get_value(msg):
    while True:
        try:
            j = input(msg)
            if not j:
                return 5
            val = int(j)
            if 1 <= val <= 10:
                return val
            else:
                print("Wrong input,try again")
                continue
        except ValueError as err:
                print(err)
if __name__ == '__main__':
    val = get_value("Enter a number between 1 and 10: ")
    j = 0
    while j < val:
        i = random.randint(1,2)
        if i == 1:
            line = random.choice(art) +" " + random.choice(sub) +" "+ random.choice(v) +" "+ random.choice(adv)
        else:
            line = random.choice(art) +" "+ random.choice(sub) +" "+ random.choice(v)
        print(line)
        j += 1
