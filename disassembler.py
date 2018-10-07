#Group 13: Jessica, Jonathan, Francis
#-----------------------------------------------------------

print("ECE366 Fall 2018 Group 13's ISA Design:")
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

input_file = open("ISA_machine_code.txt", "r")
output_file = open("ISA_assembly.txt","w")

disassembled = [None] * 3
for line in input_file:
    if (line == "\n"):              # empty lines ignored
        continue

    line = line.replace("\n","")    # remove 'endline' character
    print("Instr: ", line)          # show the binary instruction to screen
    line = line.replace(" ","")     # remove spaces anywhere in line


    if(line[1:3] == "10"):                # init: 10
        #Splitting the line to: P|1 0| I I I I I
        binaryInput = [line[0], line[1:3], line[3:8]]

        #Disassembling it to: init imm
        disassembled[0]  = "init "
        if(binaryInput[2][0] == '1'):
            binaryInput[2] = -32 + int(format(int(binaryInput[2], 2)))
            imm = str(int(binaryInput[2]))
        else:
            imm = str(int(format(int(binaryInput[2], 2))))
        disassembled[1] = imm + "\n"
       
        print(disassembled[0] + disassembled[1])
        output_file.write(disassembled[0] + disassembled[1])
    
    elif(line[1:3] == '11'):                # bez: 11
        # Splitting the line to: P|1 0| I I I I I
        binaryInput = [line[0], line[1:3], line[3:8]]

        # Disassembling it to: bez imm
        disassembled[0] = "bez "
        if(binaryInput[2][0] == '1'):
            binaryInput[2] = -32 + int(format(int(binaryInput[2], 2)))
            imm = str(int(binaryInput[2]))
        else:
            imm = str(int(format(int(binaryInput[2], 2))))
        disassembled[1] = imm + "\n"

        print(disassembled[0] + disassembled[1])
        output_file.write(disassembled[0] + disassembled[1])

    elif(line[1:5] == '0000'):                # add: 0000
        # Splitting the line to: P|0 0 0 0|Rx|Ry Ry
        binaryInput = [line[0], line[1:5], line[5], line[6:8]]

        # Disassembling it to: add rx, ry
        disassembled[0] = "add "
        rx = str(int(format(int(binaryInput[1], 2))))
        ry = str(int(format(int(binaryInput[2], 2))))
        disassembled[1] = "$" + rx + ", "
        disassembled[2] = "$" + ry + "\n"

        print(disassembled[0] + disassembled[1] + disassembled[2])
        output_file.write(disassembled[0] + disassembled[1] + disassembled[2])

    elif (line[1:5] == '0001'):  # slt: 0001
        # Splitting the line to: P|0 0 0 1|Rx|Ry Ry
        binaryInput = [line[0], line[1:5], line[5], line[6:8]]

        # Disassembling it to: slt rx, ry
        disassembled[0] = "slt "
        rx = str(int(format(int(binaryInput[1], 2))))
        ry = str(int(format(int(binaryInput[2], 2))))
        disassembled[1] = "$" + rx + ", "
        disassembled[2] = "$" + ry + "\n"

        print(disassembled[0] + disassembled[1] + disassembled[2])
        output_file.write(disassembled[0] + disassembled[1] + disassembled[2])

    elif (line[1:5] == '0011'):  # lw: 0011
        # Splitting the line to: P|0 0 1 1|I I I
        binaryInput = [line[0], line[1:5], line[5:8]]

        # Disassembling it to: lw imm (unsigned)
        disassembled[0] = "lw "
        imm = str(int(format(int(binaryInput[2], 2))))
        disassembled[1] = imm + "\n"

        print(disassembled[0] + disassembled[1])
        output_file.write(disassembled[0] + disassembled[1])

    elif (line[1:5] == '0010'):  # lw: 0010
        # Splitting the line to: P|0 0 1 0|I I I
        binaryInput = [line[0], line[1:5], line[5:8]]

        # Disassembling it to: sw imm (unsigned)
        disassembled[0] = "sw "
        imm = str(int(format(int(binaryInput[2], 2))))
        disassembled[1] = imm + "\n"

        print(disassembled[0] + disassembled[1])
        output_file.write(disassembled[0] + disassembled[1])

    elif (line[1:5] == '0100'):  # xor: 0100
        # Splitting the line to: P|0 1 0 0|Rx|Ry Ry
        binaryInput = [line[0], line[1:5], line[5], line[6:8]]

        # Disassembling it to: xor rx, ry
        disassembled[0] = "xor "
        rx = str(int(format(int(binaryInput[1], 2))))
        ry = str(int(format(int(binaryInput[2], 2))))
        disassembled[1] = "$" + rx + ", "
        disassembled[2] = "$" + ry + "\n"

        print(disassembled[0] + disassembled[1] + disassembled[2])
        output_file.write(disassembled[0] + disassembled[1] + disassembled[2])

    elif (line[1:5] == '0101'):  # and: 0101
        # Splitting the line to: P|0 1 0 1|Rx|Ry Ry
        binaryInput = [line[0], line[1:5], line[5], line[6:8]]

        # Disassembling it to: and rx, ry
        disassembled[0] = "and "
        rx = str(int(format(int(binaryInput[1], 2))))
        ry = str(int(format(int(binaryInput[2], 2))))
        disassembled[1] = "$" + rx + ", "
        disassembled[2] = "$" + ry + "\n"

        print(disassembled[0] + disassembled[1] + disassembled[2])
        output_file.write(disassembled[0] + disassembled[1] + disassembled[2])

    elif (line[1:4] == '0111'):  # srl: 0111
        # Splitting the line to: P|0 1 1 1|Rx Rx Rx
        binaryInput = [line[0:0], line[1:4],line[5:7]]

        # Disassembling it to: and rx, ry
        disassembled[0] = "srl "
        rx = str(int(format(int(binaryInput[1], 2))))
        ry = str(int(format(int(binaryInput[2], 2))))
        disassembled[1] = "$" + rx + ", "
        print(disassembled[0] + disassembled[1])
        output_file.write(disassembled[0] + disassembled[1])

    elif (line[1:5] == '0110'):  # halt: 0110
        # Splitting the line to: P|0 1 1 1|X X X
        binaryInput = [line[0], line[1:5],line[5:8]]

        # Disassembling it to: and rx, ry
        disassembled[0] = "halt\n"
        print(disassembled[0])
        output_file.write(disassembled[0])

    else:
        print("Unknown instruction:"+line)

input_file.close()
output_file.close()

