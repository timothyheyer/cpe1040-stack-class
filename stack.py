class Stack():
    def __init__(self, sample):
        print("New Stack object")
        self.stack = []
        sample = "sample string"

    def expect_string(i):
        if not isinstance(i, type(sample)):
            raise ValueError('Expected string but got {}'.format(type(i)))
        else:
            print('Got a string: {}'.format(i))
            return true

    def pop(self):
        print("Popping...")
        self.stack.pop()

    def push(self, value):
        print("Pushing...")
        if value == expect_string():
            self.stack.append()
        else:
            expect_string()
