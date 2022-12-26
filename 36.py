'''Write a Python program to check multiple keys exists in a dictionary '''

Adict = {"Mon":3, "Tue":11,"Wed":6,"Thu":9}
check_keys={"Tue","Thu"}

# Use comaprision
if(Adict.keys()) >= check_keys:
   print("All keys are present")
else:
   print("All keys are not present")
   
# Check for new keys
check_keys={"Mon","Fri"}
if(Adict.keys()) >= check_keys:
   print("All keys are present")
else:
   print("All keys are not present")
