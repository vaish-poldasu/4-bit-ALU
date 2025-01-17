# import os
# import subprocess

# # This clears the output file
# fp3 = open("comp_output.txt", 'w')
# fp3.close()

# # This is the command that helps to choose which file to run
# command = "ngspice comp_dest.ckt"

# # Start of script
# for j in range(0, 8):
#     if j < 4:
#         s1 = "A" + str(j)
#     else:
#         s1 = "B" + str(j - 4)

#     s2 = "AequalB"


#     # fp1 is src file since you can't modify it, you open it in read mode
#     if j < 4:
#         fp1 = open("alu_comp2.cir", 'r')  # Adjust the file name accordingly
#     else:
#         fp1 = open("alu_comp3.cir", 'r')  # Adjust the file name accordingly

#     fp2 = open("comp_dest.ckt", 'w')  # Destination file for running
#     fp3 = open("comp_output.txt", 'a')  # Final output file
#     mode1 = "RISE"
#     mode2 = "FALL"
#     mode3 = "FALL"
#     mode4 = "RISE"

#     data = fp1.read()  # Reading data from the file to a string

#     search_text = "*target text"
#     replace_text = f'''
# .measure tran trise 
# + TRIG v({s1}) VAL = 'SUPPLY/2' {mode1} =1
# + TARG v({s2}) VAL = 'SUPPLY/2' {mode2} =1 

# .measure tran tfall 
# + TRIG v({s1}) VAL = 'SUPPLY/2' {mode3} =1 
# + TARG v({s2}) VAL = 'SUPPLY/2' {mode4}=1

# .measure tran tpd param = '(trise + tfall)/2' goal = 0
#     '''

#     # Now we replace search text with replace text in the file
#     data = data.replace(search_text, replace_text)
#     fp2.write(data)  # This writes the modified text into a new file called temp2.ckt
#     fp1.close()
#     fp2.close()

#     # Just use this block as it is so that your command is run in the terminal and output is stored into the string named as output
#     completed_process = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     if completed_process.returncode == 0:
#         # Capture the standard output into a string
#         output = completed_process.stdout
#     else:
#         output = ("Command execution failed. at", str(j))

#     output = output.split('\n')  # Helps to separate the string based on the new line characters
#     output = output[-4]
#     additional_text = f" input = {s1} output = {s2}\n"

#     fp3.write(output + additional_text)

# # Close the file after writing
# fp3.close()


import os
import subprocess

# This clears the output file
fp3 = open("comp_output.txt", 'w')
fp3.close()

# This is the command that helps to choose which file to run
command = "ngspice comp_dest.ckt"

# Start of script
for j in range(0, 8):
    if j < 4:
        s1 = "A" + str(j)
    else:
        s1 = "B" + str(j - 4)

    s2 = "AequalB"
    

    # fp1 is src file since you can't modify it, you open it in read mode
    if j < 4:
        fp1 = open("alu_comp2.cir", 'r')  # Adjust the file name accordingly
        s3 = "AB"
    else:
        fp1 = open("alu_comp3.cir", 'r')  # Adjust the file name accordingly
        s3 = "BA"

    fp2 = open("comp_dest.ckt", 'w')  # Destination file for running
    fp3 = open("comp_output.txt", 'a')  # Final output file
    mode1 = "RISE"
    mode2 = "FALL"
    mode3 = "FALL"
    mode4 = "RISE"

    data = fp1.read()  # Reading data from the file to a string

    search_text = "*target text"
    replace_text = f'''
.measure tran trise 
+ TRIG v({s1}) VAL = 'SUPPLY/2' {mode1} =1
+ TARG v({s2}) VAL = 'SUPPLY/2' {mode2} =1 

.measure tran tfall 
+ TRIG v({s1}) VAL = 'SUPPLY/2' {mode3} =1 
+ TARG v({s2}) VAL = 'SUPPLY/2' {mode4}=1

.measure tran tpd param = '(trise + tfall)/2' goal = 0

.measure tran trise1 
+ TRIG v({s1}) VAL = 'SUPPLY/2' {mode1} =1
+ TARG v({s3}) VAL = 'SUPPLY/2' {mode4} =1 

.measure tran tfall1 
+ TRIG v({s1}) VAL = 'SUPPLY/2' {mode2} =1 
+ TARG v({s3}) VAL = 'SUPPLY/2' {mode3}=1

.measure tran tpd param = '(trise1 + tfall1)/2' goal = 0
    '''

    # Now we replace search text with replace text in the file
    data = data.replace(search_text, replace_text)
    fp2.write(data)  # This writes the modified text into a new file called temp2.ckt
    fp1.close()
    fp2.close()

    # Just use this block as it is so that your command is run in the terminal and output is stored into the string named as output
    completed_process = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if completed_process.returncode == 0:
        # Capture the standard output into a string
        output = completed_process.stdout
    else:
        output = ("Command execution failed. at", str(j))

    output = output.split('\n')  # Helps to separate the string based on the new line characters
    
    output2 = output[-4]
    additional_text2 = f" input = {s1} output = {s3}\n"
    fp3.write(output2 + additional_text2)

    output = output[-7]
    additional_text = f" input = {s1} output = {s2}\n"
    fp3.write(output+ additional_text)
# Close the file after writing
fp3.close()
