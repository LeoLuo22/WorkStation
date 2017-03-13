def average(student):
    _sum = 0
    for value in student.values():
        _sum += value
    return _sum / len(student)

def main():
    student = {}
    while True:
        name = input("Name: ")
        if len(name) == 0:
            break
        score = input("Score:")
        student[name] = int(score)
    for key, value in student.items():
        if value > average(student):
            print(key, value)

main()
