from lists import UnorderedList


# Create List
L = UnorderedList()

for i in range(5):
    L.add(i)

# Check if List is empty
print "Empty: %s" % L.isEmpty()

# Check the size of the list
print "Size of List: %s" % L.size()

# Search the list
for i in range(2, 7):
    print "%s in list: %s" % (i, L.search(i))
print "\n\n---\n\n"

# Remove item from list
L.lprint()
print "removing 3 from the list"
L.remove(3)
L.lprint()
print "\n\n---\n\n"

# Append item to list
L.lprint()
print "appending 3 to the list"
L.append(3)
L.lprint()
print "\n\n---\n\n"

# Insert item into list
L.lprint()
print "insert 10 at index 0"
L.insert(0, 10)
L.lprint()
print "\n\n---\n\n"
print "insert 15 at index 4"
L.insert(4, 15)
L.lprint()
print "\n\n---\n\n"

# return index of item
print "index of 15 is %s" % L.index(15)
print "\n\n---\n\n"

# pop item
L.lprint()
print "Popping last item: %s" % L.pop()
L.lprint()
print "Popping item at index 4: %s" % L.pop(4)
L.lprint()
