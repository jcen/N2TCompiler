import os

# standard format for stack subroutines:
# stack base - 256
#  ...
#   x
#   y

eqint = 0
gtint = 0
ltint = 0

def add():
    asm.write("@SP\n")
    asm.write("M=M-1\n")
    asm.write("A=M\n")
    asm.write("D=M\n")
    asm.write("M=0\n")
    asm.write("A=A-1\n")
    asm.write("M=D+M\n")


def sub():
    asm.write("@SP\n")
    asm.write("M=M-1\n")
    asm.write("A=M\n")
    asm.write("D=M\n")
    asm.write("M=0\n")
    asm.write("A=A-1\n")
    asm.write("M=M-D\n")


def neg():
    asm.write("@SP\n")
    asm.write("A=M-1\n")
    asm.write("M=-M\n")


def eq(eqint):
    asm.write("@SP\n")  # load up stack pinter
    asm.write("M=M-1\n")  # stack pointer value is going to need to go down anyway
    asm.write("A=M\n")  # point to what is now the top val in the stack
    asm.write("D=M\n")  # store top stack val in D (y value)
    asm.write("M=0\n")  # set that top stack val to 0
    asm.write("@SP\n")
    asm.write("M=M-1\n")  # stack pointer goes down for a 2nd and final time

    asm.write("A=M\n")  # point to what is now the top val in the stack
    asm.write("D=M-D\n")  # x-y (to see if they subtract to 0)
    asm.write("M=-1\n")  # readying [true] for if the eq operation returns true

    asm.write("@equal" + str(eqint) + "\n")  # get ready to jump if equal
    asm.write("D;JEQ\n")  # jump if it's equal

    asm.write("@SP\n")  # load up the stack pointer again
    asm.write("A=M\n")  # change address to the top stack val
    asm.write("M=0\n")  # returning false

    asm.write("(equal" + str(eqint) + ")\n")  # jump point
    asm.write("@SP\n")
    asm.write("M=M+1\n")    # set SP to next free spot

    eqint += 1


def gt(gtint):
    asm.write("@SP\n")  # load up stack pinter
    asm.write("M=M-1\n")  # stack pointer value is going to need to go down anyway
    asm.write("A=M\n")  # point to what is now the top val in the stack
    asm.write("D=M\n")  # store top stack val in D (y value)
    asm.write("M=0\n")  # set that top stack val to 0
    asm.write("@SP\n")
    asm.write("M=M-1\n")  # stack pointer goes down for a 2nd and final time

    asm.write("A=M\n")  # point to what is now the top val in the stack
    asm.write("D=M-D\n")  # x-y
    asm.write("M=-1\n")  # readying [true] for if the gt operation returns true

    asm.write("@xgty" + str(gtint) + "\n")  # get ready to jump if gt
    asm.write("D;JGT\n")  #

    asm.write("@SP\n")  # load up the stack pointer again
    asm.write("A=M\n")  # change address to the top stack val
    asm.write("M=0\n")  # leaving [false] on top of the stack for when x!>y

    asm.write("(xgty" + str(gtint) + ")\n")  # jump point
    asm.write("@SP\n")
    asm.write("M=M+1\n")

    gtint += 1


def lt(ltint):
    asm.write("@SP\n")  # load up stack pinter
    asm.write("M=M-1\n")  # stack pointer value is going to need to go down anyway
    asm.write("A=M\n")  # point to what is now the top val in the stack
    asm.write("D=M\n")  # store top stack val in D (y value)
    asm.write("M=0\n")  # clear y to 0
    asm.write("@SP\n")
    asm.write("M=M-1\n")  # stack pointer goes down for a 2nd and final time

    asm.write("A=M\n")  # change address to what is now the top stack val (x val)
    asm.write("D=M-D\n")  # x-y
    asm.write("M=-1\n")  # readying [true] for if the lt operation returns true

    asm.write("@xlty" + str(ltint) + "\n")  # prepare the jump address
    asm.write("D;JLT\n")  # jump if x<y

    asm.write("@SP\n")  # load up the stack pointer again
    asm.write("A=M\n")  # change address to the top stack val
    asm.write("M=0\n")  # leaving [false] on top of the stack for when x!<y

    asm.write("(xlty" + str(ltint) +")\n")  # jump point
    asm.write("@SP\n")
    asm.write("M=M+1\n")    # return the stack value to the next free spot

    ltint += 1

def And():
    asm.write("@SP\n")  # load up stack pinter
    asm.write("M=M-1\n")  # stack pointer value is going to need to go down anyway
    asm.write("A=M\n")  # point to what is now the top val in the stack
    asm.write("D=M\n")  # store top stack val in D (y value)
    asm.write("M=0\n")  # set that top stack val to 0
    asm.write("A=A-1\n")  # change address to what is now the top stack val (x val)
    asm.write("M=D&M\n") #run the and instruction
def Or():
    asm.write("@SP\n")  # load up stack pinter
    asm.write("M=M-1\n")  # stack pointer value is going to need to go down anyway
    asm.write("A=M\n")  # point to what is now the top val in the stack
    asm.write("D=M\n")  # store top stack val in D (y value)
    asm.write("M=0\n")  # set that top stack val to 0
    asm.write("A=A-1\n")  # change address to what is now the top stack val (x val)
    asm.write("M=D|M\n") #run the and instruction
def Not():
    asm.write("@SP\n")  # load up stack pinter
    asm.write("A=M-1\n")  # point to the operand value
    asm.write("M=!M\n")

def push(arg1: object, arg2: object) -> object:
    if arg1 == "constant":
        asm.write("@" + arg2 + "\n")  # constant value goes into A
        asm.write("D=A\n")  # value is stored in data register
        asm.write("@SP\n")  # pull in the pointer to the top of the stack
        asm.write("A=M\n")  # Now our address is the top of the stack
        asm.write("M=D\n")  # top of stack takes on the data value
        asm.write("@SP\n")  # get ready to increment stack pointer
        asm.write("M=M+1\n")  # increment
    elif arg1 == {"local" or "arg" or "this" or "that"}:
        print("push lookin good")
        asm.write("@" + arg2 + "\n")  # constant value goes into A
        asm.write("D=A\n")  # value is stored in data register
        asm.write("@" + arg1 + "\n")  # pull in the pointer to the top of the designated semgment
        asm.write("A=M\n")  # Now our address is the top of the stack
        asm.write("M=D\n")  # top of stack takes on the data value
        asm.write("@" + arg1  +"\n")  # get ready to increment stack pointer
        asm.write("M=M+1\n")  # increment

def pop():
    asm.write("@SP")
    asm.write("@M=M-1")
    asm.write("A=M")
    asm.write("")

def jump():
    asm.write("goto " + arg1)


source = "StackTest.vm" # input("Source .vm file to translate:")

os.path.isfile('./file.txt')
base = source[:source.rfind(".vm")]
target = base + ".asm"

# prep target file
asm = open(target, "w+")

# open up the source and get to work
with open(source) as f:
    # putting file contents in a list like this removes \n newline characters
    file = f.read().splitlines()

    # initalize stack
#    asm.write("@256\n")
#    asm.write("D=A\n")
#    asm.write("@SP\n")
#    asm.write("M=D\n")

    # 1st pass finds & adds label symbols to symbols dict before the real run through
    for line in file:
        # removes comments
        if line.rfind("//") >= 0:
            line = line[:line.rfind("//")]

        # removes empty lines
        if not line:
            continue

        # detects commands and runs them - find a cleaner way to do this
        if "push" in line:
            arg = line.split(" ")
            push(arg[1], arg[2])

        elif "add" in line:
            add()
        elif "sub" in line:
            sub()
        elif "neg" in line:
            neg()
        elif "eq" in line:
            eq(eqint)
            eqint += 1
        elif "gt" in line:
            gt(gtint)
            gtint =+ 1
        elif "lt" in line:
            lt(ltint)
            ltint += 1
        elif "and" in line:
            And()
        elif "or" in line:
            Or()
        elif "not" in line:
            Not()