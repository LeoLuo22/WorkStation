#-*- coding:utf-8 -*-
#__author__: Leo Luo

def main():
    maxwidth = 100
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgreen"
            elif count % 2:
                color = "white"
            else:
                color = "lightyellow"
            print_line(line,color,maxwidth)
            count += 1
        except EOFError:
            break
    print_end()

def print_start():
    print("<table border='1'>")

def print_end():
    print("</table>")

def print_line(line,color,maxwidth):
    print("<tr bgcolor='{0}'>".format(color))
    fileds = extract_fields(line)
    for field in fileds:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",","")
            try:
                x = float(number)
                print("<td align='right'>{0:d}</td>".format(round(x)))
            except ValueError:
                field = field.title()
                field = field.replace("And","and")
                if len(field) <= maxwidth:
                    field = escape_html(field)
                else:
                    field = "{0}...".format(escape_html(field[:maxwidth]))
                print("<td>{0}</td>".format(field)
        print("</tr>")
def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"":
            if quote is None:
                quote = c
            elif quote ==c:
                quote = None
            else:
                field += c
            continue
        if quote is None and c == ",":
            fields.append(field)
            field = ""
        else:
            field += c
    if field:
        fields.append(field)
    return fields

def escape_html(text):
    text = text.replace("&","&amp;")
    text = text.replace("<","&It;")
    text = text.replace(">","&gt;")
    return text
