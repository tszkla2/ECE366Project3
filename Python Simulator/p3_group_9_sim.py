input_file = open("p3_group_9_p1_mc.txt","r")

print("ECE366 Fall 2018 - Project 3 - Group 9 Python Simulator")
print()

def simulate(I,NSteps):
    PC = 0
    DIC = 0
    Reg = [0,0,0,0]
    Memory = [0 for i in range(10)]

    print("###### Start of Simulation ######")

    finished = False
    while(not(finished)):
        fetch = I[PC]
        DIC += 1
        print(fetch)
        if (fetch[1:8] == "1111100"):
            result = Reg[2] ^ Reg[1]    #XorR2R1: R2 = R2 XOR R1
            Reg[2] = result
            PC += 1

        elif (fetch[1:8] == "1111101"):
            result = Reg[3] & 1     #AndR3: R3 = R3 AND 1
            Reg[3] = result
            PC += 1

        elif (fetch[1:8] == "1111001"):
            Reg[2] >> 1     #ShiftR: R2 >>
            PC += 1

        elif (fetch[1:8] == "1111000"):
            Reg[2] << 1     #ShiftL: R2 <<
            PC += 1

        elif (fetch[1:5] == "1110"):
            Rx = int(fetch[5:7],2)
            imm = int(fetch[7],2)
            Reg[Rx] = imm       #Init: Rx = imm
            PC += 1

        elif (fetch[1:4] == "110"):
            Rx = int(fetch[4:6],2)
            Ry = int(fetch[6:8],2)
            if(Reg[Rx] < Reg[Ry]):
                Reg[1] = 1      #SltR1: if Rx < Ry, R1 = 1
                PC += 1
            else:
                PC +=1

        elif (fetch[1:4] == "011"):
            Rx = int(fetch[4:6],2)
            Ry = int(fetch[6:8],2)
            Memory[Reg[Ry]] = Reg[Rx]   #Store: M[Ry] <- Rx
            PC += 1

        elif (fetch[1:4] == "010"):
            Rx = int(fetch[4:6], 2)
            Ry = int(fetch[6:8], 2)
            Reg[Rx] = Memory[Reg[Ry]]  # Load: M[Ry] -> Rx
            PC += 1

        elif (fetch[1:4] == "001"):  # Rx = Rx - Ry
            Rx = int(fetch[3:4], 2)
            Ry = int(fetch[5:6], 2)
            Reg[Rx] = Reg[Rx] - Reg[Ry]
            PC += 1

        elif (fetch[1:4] == "000"):  # Rx = Rx + Ry
            Rx = int(fetch[3:4], 2)
            Ry = int(fetch[5:6], 2)
            Reg[Rx] = Reg[Rx] + Reg[Ry]
            PC += 1

        elif (fetch[1:6] == "10000"):  # PC -= Rx
            Rx = int(fetch[5:7], 2)
            PC = PC - Reg[Rx]

        elif (fetch[1:6] == "10100"):  # If R1==0, PC += Rx
            Rx = int(fetch[5:7], 2)
            if (Reg[1] == 0):
                PC = PC + Reg[Rx]
            else:
                PC += 1