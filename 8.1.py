# create a stack implementing push, pop and max

class Stack(object):    # first letter capital because this is a class

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Push the elements at the last index

        :return: None
        """
        self.items.append(item)

    def pop(self):
        """
        This will remove last item

        :return: None
        """
        self.items.pop()
        pass

    def max(self):
        """
        Return the maximum value in the stack

        :return: max(int)
        """
        return(max(self.items))

if __name__ == "__main__":

    # create stack
    stack = Stack()
    stack.push(2)   # push function
    stack.push(1)
    stack.push(3)

    # print stack
    print("stack =", stack)

    # max function
    print("max =",stack.max())

    # pop function
    print("pop =", stack.pop())

    # max function
    print("max again =", stack.max())