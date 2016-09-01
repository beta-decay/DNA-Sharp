import re, sys

fname = sys.argv[1]

with open(fname, "r") as f:
    code = f.read()

code = re.sub("[^ATCG]","",code)

code = [code[i:i+4] for i in range(0,len(code),4)]

pos = 0
pnt = 0

tape = [0]

def npointfunc(action):
    global pos, pnt, tape
    oldpnt = tape[pnt]

    pos += 1
    
    while code[pos] != "CGCG":
        eval(code[pos].lower()+'()')

    newpnt = tape[pnt]
    tape[pnt] = oldpnt

    exec('tape[pnt]'+action+'newpnt')

def atat():
    global pos, pnt, tape
    pnt += 1
    
    if len(tape)==pnt:
        tape += [0]
    
    pos += 1

def atgc():
    global pos, pnt, tape
    pnt -= 1
    
    if pnt < 0:
        raise RuntimeError("Pointer fell off tape at position "+str(pos))
    
    pos += 1
    
def atta():
    global pos, pnt, tape
    tape[pnt] += 1
    
    pos += 1
    
def atcg():
    global pos, pnt, tape
    tape[pnt] -= 1
    
    pos += 1

def gcta():
    global pos, pnt, tape
    
    if tape[pnt] == 0:
        while code[pos] != "GCCG":
            pos += 1
        pos += 1

    else:
        pos += 1
        tpos = pos
        while tape[pnt] > 0:
            pos = tpos
            while code[pos] != "GCCG":
                eval(code[pos].lower()+'()')

        pos += 1
    
def gcat():
    global pos, pnt, tape
    
    print(chr(tape[pnt]),end='')
    
    pos += 1
    
def gcgc():
    global pos, pnt, tape
    
    tape[pnt] = ord(input())
    
    pos += 1
    
def cggc():
    global pos, pnt, tape
    
    print(tape[pnt],end='')
    
    pos += 1
    
def cgta():
    global pos, pnt, tape
    
    tape[pnt] = int(input())
    
    pos += 1

def taat():
    npointfunc('=')

def tagc():
    npointfunc('+=')

def tata():
    npointfunc('-=')

def tacg():
    npointfunc('*=')

def cgat():
    npointfunc('/=')

def cgcg():
    global pos, pnt, tape
    
    pos += 1

while pos < len(code):
    comm = code[pos]
    eval(comm.lower() + "()")
