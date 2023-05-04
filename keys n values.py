def dictionairy():    
 key_value ={}   
 
 key_value[2] = 56      
 key_value[1] = 59
 key_value[4] = 23
 key_value[5] = 75
 key_value[6] = 34     
 key_value[3] = 76
 
 print ("Task 1:-\n")
 print ("Keys are")
  
 for i in sorted (key_value.keys()) :
     print(i, end = " ")
 
def main():
    dictionairy()            
     
if __name__=="__main__":     
    main()
