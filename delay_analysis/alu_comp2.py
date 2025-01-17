import os
import subprocess

command = "ngspice comp_dest_combined.ckt"

for j in range(0, 4):
    
    s1 = "A" + str(j)
    
    s2 = "B" + str(j )

    s3 = "AB"
    s4 = "BA"
    
    fp1 = open("alu_comp1.cir")

    fp2 = open("comp_dest_combined.ckt", 'w')  # Destination file 
    fp3 = open("comp_output.txt", 'a')  #output file
    mode1 = "RISE"
    mode2 = "FALL"
    mode3 = "FALL"
    mode4 = "RISE"

    data = fp1.read()  

    search_text = "*target text"
    replace_text = f'''
.measure tran trise 
+ TRIG v({s1}) VAL = 'SUPPLY/2' {mode1} =1
+ TARG v({s4}) VAL = 'SUPPLY/2' {mode2} =1 

.measure tran tfall 
+ TRIG v({s1}) VAL = 'SUPPLY/2' {mode3} =1 
+ TARG v({s4}) VAL = 'SUPPLY/2' {mode4}=1

.measure tran tpd param = '(trise + tfall)/2' goal = 0

.measure tran trise1 
+ TRIG v({s2}) VAL = 'SUPPLY/2' {mode1} =1
+ TARG v({s3}) VAL = 'SUPPLY/2' {mode2} =1 

.measure tran tfall1 
+ TRIG v({s2}) VAL = 'SUPPLY/2' {mode3} =1 
+ TARG v({s3}) VAL = 'SUPPLY/2' {mode4}=1

.measure tran tpd param = '(trise1 + tfall1)/2' goal = 0
    '''

    data = data.replace(search_text, replace_text)
    fp2.write(data) 
    fp1.close()
    fp2.close()

    completed_process = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if completed_process.returncode == 0:
        # Capture the standard output into a string
        output = completed_process.stdout
    else:
        output = ("Command execution failed. at", str(j))

    output = output.split('\n')  
    output2 = output[-4]
    additional_text2 = f" input = {s2} output = {s3}\n"
    fp3.write(output2 + additional_text2)

    output = output[-7]
    additional_text = f" input = {s1} output = {s4}\n"
    fp3.write(output+ additional_text)

fp3.close()
