#-*- coding:utf-8 -*-
#__author__: Leo Luo

import string

def main():
    text = input()
    print("'{0}'".format(simplify(text)))
"""*******My Method********
def simplify(text):
    char = ""
    sim_text = ""
    text = text.strip().split()
    for t in range(0,(len(text))):
        char += text[t] + " "
        sim_text += char
        char =""
    return sim_text.strip()
******************************"""
def simplify(text,whitespace=string.whitespace,delete=""):
    result = []
    word = ""
    for char in text:
        if char in delete:
            continue
        elif char in whitespace:
            if word:
                result.append(word)
                word = ""
        else:
            word += char
    if word:
        result.append(word)
    return " ".join(result)

def is_balanced(text, brackets="()[]{}<>"):
    counts = {}
    left_for_right = {}
    """
    seq[start:end:step]
    每隔step个字符进行提取
    """
    for left, right in zip(brackets[::2], brackets[1::2]):
        assert left != right, "the bracket characters must differ"
        counts[left] = 0
        left_for_right[right] = left
    for c in text:
        if c in counts:
            counts[c] += 1
        elif c in left_for_right:
            left = left_for_right[c]
            if counts[left] == 0:
                return False
            counts[left] -= 1
    return not any(counts.values())

if __name__ == '__main__':
    import doctest
    doctest.testmod()
