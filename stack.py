from collections import deque
stack = deque()

print(stack)

stack.append("https://www.cnn.com/")
stack.append("https://www.cnn.com/world")
stack.append("https://www.cnn.com/india")
stack.append("https://www.cnn.com/china")

if __name__=="__main__":

    print(stack)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    print(stack)