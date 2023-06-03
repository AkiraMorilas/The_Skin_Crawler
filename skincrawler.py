
# keycount definitions
# stored as ["name", [assignment], [input names]]
keyboardcounts = {
    "1key" : ["thumb"],
    "2key" : ["index","index"],
    "3key" : ["index","thumb","index"],
    "4key" : ["middle","index","index","middle"],
    "5key" : ["middle","index","thumb","index","middle"],
    "6key" : ["ring","middle","index","index","middle","ring"],
    "7key" : ["ring","middle","index","thumb","index","middle","ring"],
    "8key" : ["ring","middle","index","thumb","thumb","index","middle","ring"],
    "9key" : ["pinky","ring","middle","index","thumb","index","middle","ring","pinky"],
    "10key" : ["pinky","ring","middle","index","thumb","thumb","index","middle","ring","pinky"],
    "18key" : ["pinky","ring","middle","index","pinky","ring","middle","index","thumb","thumb","index","middle","ring","pinky","index","middle","ring","pinky"]
    }

beatcounts = {
    "5key1scratch" : ["scratch","white","blue","white","blue","white"],
    "7key1scratch" : ["scratch","white","blue","white","blue","white", "blue","white"],
    "10key2scratch" : ["scratch","white","blue","white","blue","white","white","blue","white","blue","white","scratch"],
    "14key2scratch" : ["scratch","white","blue","white","blue","white","blue","white","white","blue","white","blue","white","blue","white","scratch"]
    }

firstfewlines = 'local NoteSkinVsrg = require("sphere.models.NoteSkinModel.NoteSkinVsrg")' + "\n" + 'local BasePlayfield = require("sphere.models.NoteSkinModel.BasePlayfield")'
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
def imagedef(title,count):
    r = title + " = {\n"
    for i in count:
        r += '"' + i + '", ' + "\n"
    r += "},\n"
    return r

def shortnotedef(count):
    r = "noteskin:setShortNote({\n"
    r += imagedef("image",count)
    r += "h=48,\n})"
    return r

def longnotedef(count):
    r = "noteskin:setLongNote({\n"
    r += imagedef("head",count)
    r += imagedef("body",count)
    r += imagedef("tail",count)
    r += "h=48,\n})"
    return r    

# creates noteskin:setColumns()
def sizedef(size,count):
    r = "noteskin:setColumns({\noffset = 0,\n" + 'align = "center",' + "\nwidth = {"
    for i in count:
        r += size + ", "
    r += "},\nspace = {"
    for i in count:
        r += "0, "
    r += "0},\n})"
    return r

# assigns filename to finger(or key color in beat skins)
def notename(notes):
    r = {}
    for i in notes:
        r[i] = str(input("input the filename of your " + i + " note: "))
    return r

def skindata(name,count,hitposition):
    return "local noteskin = NoteSkinVsrg:new({\npath = ...,\n" + 'name = "' + name + '",' + "\ninputMode = " + '"' + count + '",' + "\nrange = {-1, 1},\nunit = 480,\nhitposition = " + hitposition + ",\n})"

def measuredef(measureline):
    return "noteskin:addMeasureLine({\nh = " + measureline + ",\ncolor = {1, 1, 1, 0.5},\nimage = " + '"pixel"' + "\n})"

#I'm just copypasting this bit from the default, I'll work out what it actually does later
def addbga():
    return "noteskin:addBga({\nx = 0,\ny = 0,\nw = 1,\nh = 1,\ncolor = {0.25, 0.25, 0.25, 1}\n})"

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
+ the requires
+ noteskin = NoteSkinVsrg:new
+ noteskin:setInput()
+ noteskin:setColumns()
+ noteskin:setTextures()
+ noteskin:setImagesAuto()
+ noteskin:setShortNote()
+ noteskin:setLongNote()
- noteskin:setShortNote() <- ???
+ noteskin:addMeasureLine()
+ noteskin:addBga()
+ playfield = BasePlayfield:new
+ playfield:addBga()
+ playfield:enableCamera()
+ playfield:addNotes()
- playfield:addKeyImages()
+ playfield:disableCamera()
+ playfield:addBaseElements()
- playfield:addDeltaTimeJudgement()
+ return noteskin
'''
# the actual thing that writes files(or will in the future)
def printer(counts,keydict):
    size = input("what is your note width? ")
    name = input("what is the name of the skin? ")
    hitposition = input("what is your hitposition? ")
    measureline = input("how thick do you want your measure line(0 for none)? ")
    for key, value in counts.items():
        f = open(key + ".skin.lua","w")
        skin = firstfewlines + "\n\n"
        skin += skindata(name,key,hitposition) + "\n\n"
        skin += inputdef(key) + "\n\n"
        skin += sizedef(size,value) + "\n\n"
        skin += texturedef(keydict) + "\n\n"
        skin += "noteskin:setImagesAuto()\n\n"
        skin += shortnotedef(value) + "\n\n"
        skin += longnotedef(value) + "\n\n"
        skin += measuredef(measureline) + "\n\n"
        skin += addbga() + "\n\n"
        skin += "local playfield = BasePlayfield:new({\nnoteskin = noteskin\n})"
        skin += "playfield:enableCamera()" + "\n\n"
        skin += "playfield:addNotes()" + "\n\n"
        skin += "playfield:disableCamera()" + "\n\n"
        skin += "playfield:addBaseElements()" + "\n\n"
        skin += "return noteskin"
        f.write(skin)

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
