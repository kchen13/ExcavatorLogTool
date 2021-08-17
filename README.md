# ExcavatorLogTool
Tool to quickly get stats from console output of Excavator from NiceHash

**What this script does**

 - Create another log file(filename_clean.log) in same directory with
   only stats, accepted and rejected  
 - Print out in console averages
 - Example of print out

> Select log file
> C:/Users/kchen/Desktop/excavttor log.txt 
> C:/Users/kchen/Desktop/excavttor log_clean.log has been created.  
> Avg Speed:  108.48  MH/s
> Avg Power:  275.12  W 
> Avg> Efficiency: 394.35 kH/J 
> Avg Ping:  137 ms 
> Total Rejected:  1

**How to run**

 1. Select and copy all text from console window
 2. Create new text file, paste contents, save
 3. Run this python script
 4. Select log file from step 2
 5. Profit

**Requirements:**
Excavator 1.16.11f
Python 3.9
