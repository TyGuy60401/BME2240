import sys

def main(argv):
    fin = argv[1]
    fout = argv[2]
    num = float(argv[3])

    my_file = open(fin, "r")

    file_list = my_file.readlines()

    fout = open(fout, "w")
    for line in file_list:
        x_val = float(line.split(' ')[0])
        x_val += num
        newString = "%f %s" % (x_val, line.split(' ')[1])
        fout.write(newString)

if __name__ == '__main__':
    main(sys.argv)
