
def start():
    choice = input("Do you want to set (k)eyboard, (b)eatmania or (e)z2dj keycounts, or (q)uit?")
    if choice.lower() == "k":
        kset()
    elif choice.lower() == "b":
        bset()
    elif choice.lower() == "e":
        eset()
    elif choice.lower() == "q":
        exit()
    else:
        print("try again")

def texturedef(keydict):
    r = "noteskin:setTextures({"
    for i in keydict:
        r += "{" + i + " = " + keydict[i] + "}, "
    r += "})"
    return r

def imagedef(count):
    r = "image = {"
    for i in count:
        r += '"' + i + '", '
    r += "}"
    return r


def printer(counts,keydict):
    print(texturedef(keydict))
    for i in counts:
        print(imagedef(i))


def kset():
    keydict = {
    "thumb" : input("input your thumb note: "),
    "index" : input("input your index note: "),
    "middle" : input("input your middle note: "),
    "ring" : input("input your ring note: "),
    "pinky" : input("input your pinky note: ")
    }
    # keyboard definitions
    k1 = ["thumb"]
    k2 = ["index","index"]
    k3 = ["index","thumb","index"]
    k4 = ["middle","index","index","middle"]
    k5 = ["middle","index","thumb","index","middle"]
    k6 = ["ring","middle","index","index","middle","ring"]
    k7 = ["ring","middle","index","thumb","index","middle","ring"]
    k8 = ["ring","middle","index","thumb","thumb","index","middle","ring"]
    k9 = ["pinky","ring","middle","index","thumb","index","middle","ring","pinky"]
    k10 = ["pinky","ring","middle","index","thumb","thumb","index","middle","ring","pinky"]
    k18 = ["pinky","ring","middle","index","pinky","ring","middle","index","thumb","thumb","index","middle","ring","pinky","index","middle","ring","pinky"]
    counts = [k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k18]

    printer(counts,keydict)
    

def bset():
    keydict = {
    "scratch" : input("input your scratch note: "),
    "white" : input("input your white note: "),
    "blue" : input("input your blue note: ")
    }
    # beatmania definitions
    b5 = ["scratch","white","blue","white","blue","white"]
    b7 = ["scratch","white","blue","white","blue","white","blue","white"]
    b10 = ["scratch","white","blue","white","blue","white","white","blue","white","blue","white","scratch"]
    b14 = ["scratch","white","blue","white","blue","white","blue","white","white","blue","white","blue","white","blue","white","scratch"]
    counts = [b5,b7,b10,b14]

    printer(counts,keydict)


def eset():
    keydict = {
    "scratch" : input("input your scratch note: "),
    "white" : input("input your white note: "),
    "blue" : input("input your blue note: "),
    "red" : input("input your red note: "),
    "foot" : input("input your foot note: ")
    }
    # ez2dj definitions
    e5 = ["scratch","white","blue","white","blue","white","foot"]
    e7 = ["scratch","white","blue","white","blue","white","foot","red","red"]
    e10 = ["scratch","white","blue","white","blue","white","foot","white","blue","white","blue","white","scratch"]
    e14 = ["scratch","white","blue","white","blue","white","red","red","red","red","white","blue","white","blue","white","scratch"]
    e16 = ["scratch","white","blue","white","blue","white","foot","red","red","red","red","foot","white","blue","white","blue","white","scratch"]
    counts = [e5,e7,e10,e14,e16]

    printer(counts,keydict)

while True:
    start()








# insert other definitions here maybe idk

