from collections import OrderedDict
import copy
class Book:
    def __init__(self, name, authors, price, **rest):
        """比如rest可以有出版商，标签，isbn等"""
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(rest)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append("{}: {}".format(i, ordered[i]))
            if i == "price":
                mylist.append("￥")
            mylist.append("\n")
        return " ".join(mylist)

class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError("Incorrect object identifier: {}".format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj

def main():
    b1 = Book("Python", ("Leo", "Luo"), 118, publisher="Test", length=228, pub_date="20019191", tags=("Python", "HAHA"))
    prototype = Prototype()
    cid = "first"
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, name="ANDS", price=122, length=274, pub_date="2312312", edition=2)
    for i in (b1, b2):
        print(i)
    print("ID b1 : {} != ID b2 : {}".format(id(b1), id(b2)))

if __name__ == "__main__":
    main()
