import time
def tail(f):
    print("    1")
    f.seek(0, 2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            print("    1")
            continue
        yield line
def grep(lines, searchtext):
    for line in lines:
        if searchtext in line: yield line
def print_matches(matchtext):
    print ("Looking for",matchtext)
    while True:
        line = (yield) # 获得ᷧ堳文本
    if matchtext in line:
        print(line)
def gg():
    print("     b")

if __name__ == "__main__":
    #print("    ghhhhhh")
    #print("    5")a
    #mather = print_matches("python")
    tail(open("1.txt"))
