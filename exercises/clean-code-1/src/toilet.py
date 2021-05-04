# Shitty code describing a toilet.
# Get it?

# TODO: Make this code as bad as possible while it still does what it should
# - functions that perform multiple things at the same time
# - functions that are very long
# - bad naming (camel case and underscores together, names giving the wrong idea)
# - repeat the same code multiple times
# - "if var == True:"
# - hardcode

class Toilet:
    def __init__(self):
        self.lid = 0  # BAD: treated as integer while actually boolean or enum, name should be lid_status
        self.waterlevel = 0  # BAD: never used
        self.content = 0
        self.brush_needed = 0  # BAD: treated as integer while actually boolean

    def change_lid_status(self, lid):  # BAD: trivial setter, better: open_lid() and close_lid()
        self.lid = lid
    
    def check_content(self):
        return self.content

    def perform_peepoo(self, pee, poo):
        self.content = self.content + pee + poo
        if poo > 0:
            self.brush_needed = True
        else:
            self.brush_needed = False  # BAD: This function now works like a cleaning function...

    def flush(self):
        self.content = self.content - 10  # BAD: hardcoded 10
        if self.content < 0:  # BAD: better: content = max(content-10 , 0)
            self.content = 0

    def check_if_BrushNecessary(self):  # BAD: mixed camel & underscore
        if self.brush_needed == True:  # BAD: unnecessary if else, just return brush_needed
            return True
        else:
            return False

    def useBrush(self):
        self.brush_needed = False

# BAD: All of this should actually be in another file (main)
# you just moved into a new apartment and need to install a toilet
myToilet = Toilet()
print("Toilet installed!")
print("lid=" + str(myToilet.lid) + ", waterlevel=" + str(myToilet.waterlevel) + ", content=" + str(myToilet.content) + ", brush_needed=" + str(myToilet.brush_needed))
# BAD: printing this multiple times, add a function for this and/or add print within respective functions

# you use the toilet for the first time:

# open lid
myToilet.change_lid_status(1)
print("Lid opened!")
print("lid=" + str(myToilet.lid) + ", waterlevel=" + str(myToilet.waterlevel) + ", content=" + str(myToilet.content) + ", brush_needed=" + str(myToilet.brush_needed))

# check if full
full = myToilet.check_content()
print("Checked content!")
print("lid=" + str(myToilet.lid) + ", waterlevel=" + str(myToilet.waterlevel) + ", content=" + str(myToilet.content) + ", brush_needed=" + str(myToilet.brush_needed))
if full > 0:  # BAD: just do if myToilet.check_content(), full is not needed anymore after this
    while full > 0:
        print("Toilet is full!")
        myToilet.flush()
        full = myToilet.check_content()
        print("Toilet flushed!")
        print("lid=" + str(myToilet.lid) + ", waterlevel=" + str(myToilet.waterlevel) + ", content=" + str(myToilet.content) + ", brush_needed=" + str(myToilet.brush_needed))

# perform peepeepoopoo
myToilet.perform_peepoo(pee=1,poo=12)
print("Performed peepoo!")
print("lid=" + str(myToilet.lid) + ", waterlevel=" + str(myToilet.waterlevel) + ", content=" + str(myToilet.content) + ", brush_needed=" + str(myToilet.brush_needed))

# flush
myToilet.flush()
print("Toilet flushed!")
print("lid=" + str(myToilet.lid) + ", waterlevel=" + str(myToilet.waterlevel) + ", content=" + str(myToilet.content) + ", brush_needed=" + str(myToilet.brush_needed))

# check if worked (redo if not)
full = myToilet.check_content()
print("Checked content!")
print("lid=" + str(myToilet.lid) + ", waterlevel=" + str(myToilet.waterlevel) + ", content=" + str(myToilet.content) + ", brush_needed=" + str(myToilet.brush_needed))
if full > 0:  # BAD: just do if myToilet.check_content(), full is not needed anymore after this
    while full > 0:  # BAD: if-condition before was unneccessary if we're going into while loop anyways
        print("Toilet is full!")
        myToilet.flush()
        full = myToilet.check_content()
        print("Toilet flushed!")
        print("lid=" + str(myToilet.lid) + ", waterlevel=" + str(myToilet.waterlevel) + ", content=" + str(myToilet.content) + ", brush_needed=" + str(myToilet.brush_needed))

# check if brush necessary
brush_needed = myToilet.check_if_BrushNecessary()  # BAD: did not assign to myToilet.brush_needed
print("Checked if brush necessary!")
print("lid=" + str(myToilet.lid) + ", waterlevel=" + str(myToilet.waterlevel) + ", content=" + str(myToilet.content) + ", brush_needed=" + str(myToilet.brush_needed))
if brush_needed == True:
    print("Brush is necessary!")
    myToilet.useBrush()
    print("Used brush!")
    print("lid=" + str(myToilet.lid) + ", waterlevel=" + str(myToilet.waterlevel) + ", content=" + str(myToilet.content) + ", brush_needed=" + str(myToilet.brush_needed))

# close lid
myToilet.change_lid_status(0)
print("Lid closed!")
print("lid=" + str(myToilet.lid) + ", waterlevel=" + str(myToilet.waterlevel) + ", content=" + str(myToilet.content) + ", brush_needed=" + str(myToilet.brush_needed))
