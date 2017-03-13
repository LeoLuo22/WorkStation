import string
keys = []
for i in range(2, 10):
    keys.append(str(i))
for word in string.ascii_uppercase:
    if word == "I" or word == "O":
        continue
    keys.append(word)

def int2bin(n):
    b = bin(n).replace('0b', '')
    extra = ''
    if len(b) != 16:
        for i in range(0, 16-len(b)):
            extra += str(0)
    return (extra + b)

def bin2int(n):
    return int(n, base=2)
def main():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    ring = int2bin(a) + int2bin(b) + int2bin(c) + int2bin(a)
    start = 43
    end = 48
    indices = []
    for i in range(0, 14):
        if (start < 0 and end > 0):
            x = ring[start:]
            b = ring[0:end]
            #print("x+b", x+b)
            indices.append(x+b)
            start -= 5
            end -= 5
            continue
        #print("start: ", start, "  ", "end: ", end, "value: ", ring[start:end])
        indices.append(ring[start:end])
        start -= 5
        end -= 5
    count = 0
    result = ""
    asc = 0
    for index in indices:
        if count == 4:
            result += "-"
            count = 0
        result += str(keys[bin2int(index)])
        asc += ord(keys[bin2int(index)])
        count += 1
    asc_bin = int2bin(asc)
    c_start = len(asc_bin) - 5
    c_end = len(asc_bin)
    check_num_one = keys[bin2int(asc_bin[c_start:c_end])]
    check_num_two = keys[bin2int(asc_bin[c_start-5:c_end-5])]
    result = result + check_num_one + check_num_two
    print(result)

if __name__ == "__main__":
    main()
