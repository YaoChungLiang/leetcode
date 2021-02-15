# You are building an educational website and want to create a simple calculator for students to use.
# The calculator will only allow addition and subtraction of non-negative integers.

# Given an expression string using the "+", "-" operators like "5+16-1", write a function to parse the string and evaluate the result.

#   calculate("5+16-1") # => 20
#   calculate("22+3") # => 25
#   calculate(“12-13+5") # => 4
#   calculate("1024") # => 1024
#   ! ?  () -> invalid
#   " "
#   061
#   Integer
#   "" -> not a case


# stack = ["12", "13", "5"]
# operator = ["-", "+"]


pre -> ops -> past


def cal(inputString):
    pass


def calculate2(inputString):

    int_que = [0]
    operator_que = []
    for s in inputString:
        if s not in "+-":
            int_que[-1] = int_que[-1] * 10 + int(s)
        else:
            operator_que.append(s)
            int_que.append(0)

    while operator_que:
        op = operator_que.pop(0)
        if op == "+":
            res = int_que.pop(0) + int_que.pop(0)
        else:
            res = int_que.pop(0) - int_que.pop(0)
        if int_que:
            int_que.insert(0, res)
        else:
            int_que.append(res)
    return int_que[0]


# We also want to allow parentheses in our input. Given an expression string using the "+", "-", "(", and ")" operators like "5+(16-2)", write a function to parse the string and evaluate the result.

# Sample output:
#   calculate("5+16-((9-6)-(4-2))+1") # => 21
#   calculate("22+(2-4)") # => 20
#   calculate("6+9-12") # => 3
#   calculate("((1024))") # => 1024
#   calculate("1+(2+3)-(4-5)+6") # => 13
#   calculate("255") # => 255

# stack = [20, 1]
# ops = [+]
# parenthess = []


def calculate(input_string):
    stack = [0]
    ops = []
    parenthess = []
    for s in input_string:
        if s not in "+-()":
            stack[-1] = stack[-1]*10 + int(s)
        else:
            if s == "(":
                parenthess.append(s)
                continue
            elif s == ")":
                op = ops.pop()
                if op == "+":
                    stack.append(stack.pop() + stack.pop())
                else:
                    stack.append(stack.pop() - stack.pop())
                parenthess.pop()
            else:
                if len(ops) >= 1:
                    op = ops.pop()
                    if op == "+":
                        stack.append(stack.pop(0) + stack.pop(0))
                    else:
                        stack.append(stack.pop(0) - stack.pop(0))
                    ops.append(s)
                stack.append(0)
    return stack[-1]


if __name__ == "__main__":
    print(calculate("5+16-1") == 20)
    print(calculate("22+3") == 25)
    print(calculate("12-13+5") == 4)
    print(calculate("1024") == 1024)
    print(calculate("5+16-((9-6)-(4-2))+1") == 21)
