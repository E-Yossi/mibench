f = open("input_large.dat")
p = open
i=0

for line in f:
    line = line.split()
    print "array[{0:4}].x, {1:15} ;".format(i,line[0]);
    print "array[{0:4}].y, {1:15} ;".format(i,line[1]);
    print "array[{0:4}].z, {1:15} ;".format(i,line[2]);
    i+=1

f.close()