from stack import Stack


def test_integers():
    s = Stack()
    s.append(5)
    t = s.pop()
    print(t)


def test_floats():
    s = Stack()
    s.append(3.14)
    t = s.pop()
    print(t)


def test_strings():
    s = Stack()
    s.append("Test String")
    t = s.pop()
    print(t)

def test_all():
    s = Stack()
    s.append(10) #integer test
    s.append(10.1) #float test
    s.append("String Test") #string test
    string = s.pop() #pop string
    float = s.pop() #pop float
    integer = s.pop() #pop integer
    print(string, float, integer)

if __name__ == '__main__':
    test_integers()
