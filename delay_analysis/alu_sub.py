import os
import subprocess

fp3 = open("sub_output.txt", 'w')
fp3.close()

command = "ngspice sub_dest.ckt"

for j in range(0, 8):
    if j < 4:
        s1 = "A" + str(j)
    else:
        s1 = "B" + str(j - 4)

    for i in range(0, 4):
        s2 = "YS" + str(i)

        if j < 4:
            fp1 = open("alu_sub1.cir", 'r')
            mode1 = "RISE"
            mode2 = "RISE"
            mode3 = "FALL"
            mode4 = "FALL"
        else:
            fp1 = open("alu_sub2.cir", 'r')
            mode1 = "RISE"
            mode2 = "FALL"
            mode3 = "FALL"
            mode4 = "RISE"

        fp2 = open("sub_dest.ckt", 'w')
        fp3 = open("sub_output.txt", 'a')

        data = fp1.read()

        search_text = "*target text"
        replace_text = f'''
.measure tran trise 
+ TRIG v({s1}) VAL = 'SUPPLY/2' {mode1} =1
+ TARG v({s2}) VAL = 'SUPPLY/2' {mode2} =1 

.measure tran tfall 
+ TRIG v({s1}) VAL = 'SUPPLY/2' {mode3} =1 
+ TARG v({s2}) VAL = 'SUPPLY/2' {mode4}=1

.measure tran tpd param = '(trise + tfall)/2' goal = 0
        '''

        data = data.replace(search_text, replace_text)
        fp2.write(data)
        fp1.close()
        fp2.close()

        completed_process = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if completed_process.returncode == 0:
            output = completed_process.stdout
        else:
            output = ("Command execution failed. at", str(i), str(j))

        output = output.split('\n')
        output = output[-4]
        additional_text = f" input = {s1} output = {s2}\n"

        fp3.write(output + additional_text)

fp3.close()
