#Group 13: Jessica, Jonathan, Francis
#-----------------------------------------------------------

print("ECE366 Fall 2018 Group 13's ISA Design, FJSquared:")
print("init imm")
print("bez imm")
print("add rx ry")
print("slt rx ry")
print("lw imm")
print("sw imm")
print("xor rx ry")
print("and rx ry")
print("srl rx ry")
print("halt")

print("___________")

input_file = open("project2_group_13_p2_bin.txt", "r")
output_file = open("project2_group_13_p2_asm.txt","w")

disassembled = [""] * 5
for line in input_file:
    if (line == "\n"):              # empty lines ignored
        continue

    line = line.replace("\n","")    # remove 'endline' character
    print("Instr: ", line)          # show the binary instruction to screen
    splitLine = line.split("#")
    if(len(splitLine) == 2):
        line = splitLine[0].replace(" ","") + "#" + splitLine[1]     # remove spaces anywhere in line[0:8]
    else:
        line = splitLine[0].replace(" ","")

    if(line[1:3] == "10"):                # init: 10
        #Splitting the line to: P|1 0|I I|Rx| I I
        binaryInput = [line[0], line[1:3], line[3:5], line[5], line[6:8]]

        #Disassembling it to: init imm
        disassembled[0] = "init "
        disassembled[1] = "$r" + str(int(binaryInput[3])) + ", "
        immediate = str(binaryInput[2])+str(binaryInput[4])
        if(immediate[0] == '1'):
            imm = -16 + int(format(int(immediate, 2)))
            imm = str(int(imm))
        else:
            imm = str(int(format(int(immediate, 2)))) + "\t"
        disassembled[2] = imm + "\t"
        if(len(line)>8):
            if(line[8] == "#"):
                disassembled[3] = " " + line[8:len(line)]
            disassembled[3] = disassembled[3] + "\n"
        else:
            disassembled[3] = "\n"
        print(disassembled[0] + disassembled[1] + disassembled[2] + disassembled[3])
        output_file.write(disassembled[0] + disassembled[1] + disassembled[2] + disassembled[3])

    elif(line[1:3] == '11'):                # bez: 11
        # Splitting the line to: P|1 0|X X|Rx|X X
        binaryInput = [line[0], line[1:3], line[3:5], line[5], line[6:8]]

        # Disassembling it to: bez imm
        disassembled[0] = "bez "
        disassembled[1] = "$r" + binaryInput[3]+ "\t\t\t"
        if(len(line)>8):
            if(line[8] == "#"):
                disassembled[2] = " " + line[8:len(line)]
            disassembled[2] = disassembled[2] + "\n"
        else:
            disassembled[2] = "\n"
        print(disassembled[0] + disassembled[1] + disassembled[2])
        output_file.write(disassembled[0] + disassembled[1] + disassembled[2])

    elif(line[1:5] == '0000'):                # add: 0000
        # Splitting the line to: P|0 0 0 0|Rx|Ry Ry
        binaryInput = [line[0], line[1:5], line[5], line[6:8]]

        # Disassembling it to: add rx, ry
        disassembled[0] = "add "
        rx = str(int(format(int(binaryInput[2], 2))))
        ry = str(int(format(int(binaryInput[3], 2))))
        disassembled[1] = "$r" + rx + ", "
        disassembled[2] = "$r" + ry + "\t"
        if(len(line)>8):
            if(line[8] == "#"):
                disassembled[3] = " " + line[8:len(line)]
            disassembled[3] = disassembled[3] + "\n"
        else:
            disassembled[3] = "\n"

        print(disassembled[0] + disassembled[1] + disassembled[2] + disassembled[3])
        output_file.write(disassembled[0] + disassembled[1] + disassembled[2] + disassembled[3])

    elif (line[1:5] == '0001'):  # slt: 0001
        # Splitting the line to: P|0 0 0 1|Rx|Ry Ry
        binaryInput = [line[0], line[1:5], line[5], line[6:8]]

        # Disassembling it to: slt rx, ry
        disassembled[0] = "slt "
        rx = str(int(format(int(binaryInput[1], 2))))
        ry = str(int(format(int(binaryInput[2], 2))))
        disassembled[1] = "$r" + rx + ", "
        disassembled[2] = "$r" + ry+ "\t"
        if (len(line) > 8):
            if (line[8] == "#"):
                disassembled[3] = " " + line[8:len(line)]
            disassembled[3] = disassembled[3] +  "\n"
        else:
            disassembled[3] = "\n"

        print(disassembled[0] + disassembled[1] + disassembled[2] + disassembled[3])
        output_file.write(disassembled[0] + disassembled[1] + disassembled[2] + disassembled[3])

    elif (line[1:5] == '0011'):  # lw: 0011
        # Splitting the line to: P|0 0 1 1|Rx|Ry Ry
        binaryInput = [line[0], line[1:5], line[5], line[6:8]]

        # Disassembling it to: lw imm (unsigned)
        disassembled[0] = "lw "
        disassembled[1] = "$r" + str(int(format(int(binaryInput[2], 2)))) + ", "
        disassembled[2] = "$r" + str(int(format(int(binaryInput[3], 2))))+ "\t\t"
        if (len(line) > 8):
            if (line[8] == "#"):
                disassembled[3] = " " + line[8:len(line)]
            disassembled[3] = disassembled[3] + "\n"
        else:
            disassembled[3] = "\n"

        print(disassembled[0] + disassembled[1] + disassembled[2] + disassembled[3])
        output_file.write(disassembled[0] + disassembled[1] + disassembled[2] + disassembled[3])

    elif (line[1:5] == '0010'):  # sw: 0010
        # Splitting the line to: P|0 0 1 0|Rx|Ry Ry
        binaryInput = [line[0], line[1:5], line[5], line[6:8]]

        # Disassembling it to: sw imm (unsigned)
        disassembled[0] = "sw "
        disassembled[1] = "$r" + str(int(format(int(binaryInput[2], 2)))) + ", "
        disassembled[2] = "$r" + str(int(format(int(binaryInput[3], 2)))) + "\t\t"
        if (len(line) > 8):
            if (line[8] == "#"):
                disassembled[3] = " " + line[8:len(line)]
            disassembled[3] = disassembled[3] +  "\n"
        else:
            disassembled[3] = "\n"

        print(disassembled[0] + disassembled[1] + disassembled[2] + disassembled[3])
        output_file.write(disassembled[0] + disassembled[1] + disassembled[2] + disassembled[3])

    elif (line[1:5] == '0100'):  # xor: 0100
        # Splitting the line to: P|0 1 0 0|Rx|Ry Ry
        binaryInput = [line[0], line[1:5], line[5], line[6:8]]

        # Disassembling it to: xor rx, ry
        disassembled[0] = "xor "
        rx = str(int(format(int(binaryInput[2], 2))))
        ry = str(int(format(int(binaryInput[3], 2))))
        disassembled[1] = "$r" + rx + ", "
        disassembled[2] = "$r" + ry + "\t"
        if (len(line) > 8):
            if (line[8] == "#"):
                disassembled[3] = " " + line[8:len(line)]
            disassembled[3] = disassembled[3] +  "\n"
        else:
            disassembled[3] = "\n"

        print(disassembled[0] + disassembled[1] + disassembled[2] + disassembled[3])
        output_file.write(disassembled[0] + disassembled[1] + disassembled[2] + disassembled[3])

    elif (line[1:5] == '0101'):  # and: 0101
        # Splitting the line to: P|0 1 0 1|Rx|Ry Ry
        binaryInput = [line[0], line[1:5], line[5], line[6:8], line[8:]]

        # Disassembling it to: and rx, ry
        disassembled[0] = "and "
        rx = str(int(format(int(binaryInput[2], 2))))
        ry = str(int(format(int(binaryInput[3], 2))))
        disassembled[1] = "$r" + rx + ", "
        disassembled[2] = "$r" + ry +  "\t"

        if (len(line) > 8):
            if (line[8] == "#"):
                disassembled[3] = " " + line[8:len(line)]
            disassembled[3] = disassembled[3] +  "\n"
        else:
            disassembled[3] = "\n"

        print(disassembled[0] + disassembled[1] + disassembled[2] + disassembled[3])
        output_file.write(disassembled[0] + disassembled[1] + disassembled[2] + disassembled[3])

    elif (line[1:5] == '0111'):  # srl: 0111
        # Splitting the line to: P|0 1 1 1|X| Rx Rx
        binaryInput = [line[0:0], line[1:5], line[5], line[6:7]]

        # Disassembling it to: srl rx
        disassembled[0] = "srl "
        disassembled[1] = "$r" + str(int(format(int(binaryInput[3], 2)))) + "\t"
        if (len(line) > 8):
            if (line[8] == "#"):
                disassembled[2] = " " + line[8:len(line)]
            disassembled[2] = disassembled[2] + "\n"
        else:
            disassembled[2] = "\n"

        print(disassembled[0] + disassembled[1] + disassembled[2])
        output_file.write(disassembled[0] + disassembled[1] + disassembled[2])

    elif (line[1:5] == '0110'):  # sub: 0110
        # Splitting the line to: P|0 1 1 1|Rx|Ry|Rz
        binaryInput = [line[0], line[1:5], line[5], line[6], line[7]]

        # Disassembling it to: sub rx, ry, rz
        disassembled[0] = "sub "
        disassembled[1] = "$r" + str(binaryInput[2]) + ","
        disassembled[2] = "$r" + str(binaryInput[3]) + ","
        disassembled[3] = "$" + str(binaryInput[4]) + "\t"
        if (len(line) > 8):
            if (line[8] == "#"):
                disassembled[4] = " " + line[8:len(line)]
            disassembled[4] = disassembled[4] + "\n"
        else:
            disassembled[4] = "\n"

        print(disassembled[0] + disassembled[1] + disassembled[2] + disassembled[3] + disassembled[4])
        output_file.write(disassembled[0] + disassembled[1] + disassembled[2] + disassembled[3] + disassembled[4])

    else:
        print("Unknown instruction:"+line)

input_file.close()
output_file.close()

