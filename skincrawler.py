
# keycount definitions
# stored as ["name", [assignment], [input names]]
keyboardcounts = [
["1key", ["thumb"]],
["2key", ["index","index"]],
["3key", ["index","thumb","index"]],
["4key", ["middle","index","index","middle"]],
["5key", ["middle","index","thumb","index","middle"]],
["6key", ["ring","middle","index","index","middle","ring"]],
["7key", ["ring","middle","index","thumb","index","middle","ring"]],
["8key", ["ring","middle","index","thumb","thumb","index","middle","ring"]],
["9key", ["pinky","ring","middle","index","thumb","index","middle","ring","pinky"]],
["10key", ["pinky","ring","middle","index","thumb","thumb","index","middle","ring","pinky"]],
["18key", ["pinky","ring","middle","index","pinky","ring","middle","index","thumb","thumb","index","middle","ring","pinky","index","middle","ring","pinky"]]
]
beatcounts = [
["5key1scratch", ["scratch","white","blue","white","blue","white"]],
["7key1scratch", ["scratch","white","blue","white","blue","white", "blue","white"]],
["10key2scratch", ["scratch","white","blue","white","blue","white","white","blue","white","blue","white","scratch"]],
["14key2scratch", ["scratch","white","blue","white","blue","white","blue","white","white","blue","white","blue","white","blue","white","scratch"]]
]

# generate input names from keycount name
def inputdef(count):
    knum = count.find("k")
    k = count[:knum]
    snum = count.find("s")
    if snum == -1:
        s = 0
    else:
        s = (count[-8])
    r = "noteskin:setInput({\n"
    if int(s) > 0:
        r += '"scratch1",'+"\n"
    for i in range(int(k)):
        r += '"key'+str(i+1)+'",'+"\n"
    if int(s) > 1:
        r += '"scratch2"'+"\n"
    r += "})"
    return r

# creates noteskin:setTextures() code
def texturedef(keydict):
    r = "noteskin:setTextures({\n"
    for i in keydict:
        r += "{" + i + ' = "' + keydict[i] + '"}, ' + "\n"
    r += "})"
    return r

# creates image lists for noteskin:setShortNote() and noteskin:setLongNote()
def imagedef(count):
    r = "image = {\n"
    for i in count[1]:
        r += '"' + i + '", ' + "\n"
    r += "}"
    return r

# creates noteskin:setColumns()
def sizedef(size,count):
    r = "noteskin:setColumns({offset = 0, " + 'align = "center", ' + "width = {"
    for i in count:
        r += size + ", "
    r += "}, space = {"
    for i in count:
        r += "0, "
    r += "},})"
    return r

# assigns filename to finger(or key color in beat skins)
def notename(notes):
    r = {}
    for i in notes:
        r[i] = str(input("input the filename of your " + i + " note: "))
    return r

# for keyboard keycounts
def kset():
    notes = ["thumb", "index", "middle", "ring", "pinky"]
    printer(keyboardcounts,notename(notes))
    
# for bms keycounts
def bset():
    notes = ["scratch", "white", "blue"]
    printer(beatcounts,notename(notes))


'''
in order:
- the requires
- noteskin = NoteSkinVsrg:new
+ noteskin:setInput()
- noteskin:setColumns()
+ noteskin:setTextures()
- noteskin:setImagesAuto() <- figure out what's up with that
+ noteskin:setShortNote()
- noteskin:setLongNote()
- noteskin:setShortNote() <- ???
- noteskin:addMeasureLine()
- noteskin:addBga()
- playfield = BasePlayfield:new
- playfield:addBga()
- playfield:enableCamera()
- playfield:addNotes()
- playfield:addKeyImages()
- playfield:disableCamera()
- playfield:addBaseElements()
- playfield:addDeltaTimeJudgement()
- return noteskin
'''
# the actual thing that writes files(or will in the future)
def printer(counts,keydict):
    print(texturedef(keydict))
    for i in counts:
        print(i[0])
        print(imagedef(i))
        print(inputdef(i[0]))

# it might be a more common to call this main?
def start():
    choice = input("Do you want to set (k)eyboard keymodes, (b)ms keymodes, or (q)uit?")
    if choice.lower() == "k":
        kset()
    elif choice.lower() == "b":
        bset()
    elif choice.lower() == "q":
        exit()
    else:
        print("try again")

while True:
    start()

'''
here lies some old unused code because EZ2DJ-like keymode files don't seem to be actually available anywhere 
despite youtube videos with them being not that difficult to find. 
Also, while "5key1pedal1scratch", and "7key1pedal1scratch" exist in the default skin, none of the EZ doubles modes do.

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
'''

