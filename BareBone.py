import sys
import random

#read arguements
program_filepath = sys.argv[1]

program_lines = []
with open(program_filepath, "r") as program_file:
    program_lines = [line.strip() for line in program_file.readlines()]

program = []
token_counter = 0
label_tracker = {}
for line in program_lines:
    parts = line.split(" ")
    opcode = parts[0]

    if opcode == "":
        continue
    
    if opcode.endswith(":"):
        label_tracker[opcode[:-1]] = token_counter
        continue

    program.append(opcode)
    token_counter += 1

    if opcode == "push":
        number = int(parts[1])
        program.append(number)
        token_counter += 1
    elif opcode == "print":
        string_literal = " ".join(parts[1:]) [1:-1]
        program.append(string_literal)
        token_counter += 1
    elif opcode == "jump.eq.0?":
        label = parts[1]
        program.append(label)
        token_counter += 1
    elif opcode == "jump.gt.0?":
        label = parts[1]
        program.append(label)
        token_counter += 1

class Stack:

    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp = -1
    
    def push(self, number):
        self.sp += 1
        self.buf[self.sp] = number
    
    def pop(self):
        number = self.buf[self.sp]
        self.sp -= 1
        return number
    
    def top(self):
        return self.buf[self.sp]

pc = 0    
stack = Stack(256)

while program[pc] != "stop":
    opcode = program[pc]
    pc += 1

    if opcode == "push":
        number = program[pc]
        pc += 1
        stack.push(number)
    elif opcode == "pop":
        stack.pop()
    elif opcode == "add":
        a = stack.pop()
        b = stack.pop()
        stack.push(a+b)
    elif opcode == "sub":
        a = stack.pop()
        b = stack.pop()
        stack.push(b-a)
    elif opcode == "mul":
        a = stack.pop()
        b = stack.pop()
        stack.push(a*b)
    elif opcode == "div":
        a = stack.pop()
        b = stack.pop()
        stack.push(b/a)
    elif opcode == "mod":
        a = stack.pop()
        b = stack.pop()
        stack.push(b%a)
    elif opcode == "print":
        string_literal = program[pc]
        pc += 1
        print(string_literal)
    elif opcode == "input":
        number = int(input())
        stack.push(number)
    elif opcode == "jump.eq.0?":
        number = stack.top()
        if number == 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    elif opcode == "jump.gt.0?":
        number = stack.top()
        if number > 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    elif opcode == "rng":
        number = int(random.randint(0, 1))
        pc += 1
        print(number)
        stack.push(number)


