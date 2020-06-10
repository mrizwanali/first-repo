''' Discription: Number guessing game
    auther:Syed M.Faisal
'''

import random
import re
import winsound
import googletrans
from googletrans import Translator


#Generate a random four-digit non-repeating number to be guessed by the player 
thou = hndr = tnth = unit = 0
def generate_num():
    while True:
        unit = random.randint(0,7) + 1
        tnth = random.randint(0,7) + 1
        hndr = random.randint(0,7) + 1
        thou = random.randint(0,7) + 1
        if (thou != hndr and thou != tnth and thou != unit) and (hndr != tnth and hndr != unit) and (tnth != unit):
            break
    return thou*1000 + hndr*100 + tnth*10 + unit
 
target_num = [int(d) for d in str(generate_num())]
pattern1 = r'\b[09][09][09][09]\b'
pattern2 = r'\b[1-8][1-8][1-8][1-8]\b'
print(target_num)

#Using googletrans Translator class to translate output in urdu
translator = Translator()

print("|===============================================GUESS MASTER============================================================|")
print("|GOAL: Match a hidden four digit non-repeating number for e.g 1234, 2345 or 8765 etc. in maximum ten attempts.          |")
print("|INSTRUCTIONS: Your 4-digit input should contain only numbers between 1 to 8. No 0's or 9's or any repeating digit.     |")
print("|Hints 'D/P'will be given at each attempt.                                                                              |")
print("|'D' indicates valid number of digits matches , 'P' indicates number of digits correct position                         |")
print("|=======================================================================================================================|")
		
print('\t \t \t \t'+  ' ==========================='+ '            ' + '================================')
print()
print('\t \t \t \t'+  ' ATTEMPTS' + ' |' + '  INPUT | '+ 'D'+ '/'+ 'P' + '                ***********CAUTIONS*************')
print('\t \t \t \t'+  ' ==========================='+ '            ' + '================================')

#Function to check if user input has any adjacent repeating elements
def isrepeat(num):    
   st= str(num)
   for i in range(len(st)-1):
      if st[i] == st[i+1]:
         return True
   return False

#Loop to give user 10 attempts to guess the target number
for attempt in range(10):
    
    while True:
        #This outer try block will check for exception raised in case of non-numeric element
        try:
            urdutrans1 = translator.translate('Enter a 4-digit number', dest='ur')
            print(urdutrans1.text)
            num = int(input('Enter a 4-digit number: '))
            #Check if the input digts are less or more than 4 digits, also check there are no repeating digits
            if len(str(num))!=4 or isrepeat(num)== True or len(str(num))!= len(set([char for char in str(num)])):
                print("\t\t\t\t\t\t\t\t\tCaution: Enter four digit non-repeating numbers, no 0's or 9's ", dest ='ur')
                urdutrans2 = translator.translate("Caution: Only Enter four digit non-repeating numbers, There should not be 0's or 9's ", dest='ur')
                print('\t\t\t\t\t\t\t\t\t',urdutrans2.text)
                winsound.PlaySound('Windows Ding.wav', winsound.SND_ASYNC)
                continue
            #Check if there is any 0's, 9's or spaces
            elif re.search(pattern1, str(num)) != None or re.search(pattern2,str(num)) == None:
                print("\t\t\t\t\t\t\t\t\tCaution: There should not be any Zeros or Nines! or any spaces or non-numeric character")
                urdutrans3 = translator.translate('Caution: No Zeros or Nines! No spaces or non-numeric character ', dest='ur')
                print('\t\t\t\t\t\t\t\t\t',urdutrans3.text)
                winsound.PlaySound('Windows Ding.wav', winsound.SND_ASYNC)
                continue
            break
        except:
            print('\t\t\t\t\t\t\t\t\tCaution: Enter numbers only! No spaces or non-numeric characters')
            urdutrans4 = translator.translate('Caution: Enter numbers only! There should not be any spaces or non-numeric characters ', dest='ur')
            print('\t\t\t\t\t\t\t\t\t',urdutrans4.text)
            winsound.PlaySound('Windows Ding.wav', winsound.SND_ASYNC)
           
    #user_input will be parsed as individual elements of the list
    user_input = []
    user_input.append(num//1000)
    user_input.append((num%1000)//100)
    user_input.append((num%100)//10)
    user_input.append(num%10)
    
#Function to compare each elements of user_input with the system generated four digit number contained in target_num list 
    def compare_lists(list1,list2):
        matched_digits = 0
        matched_positions = 0        
        if len(list1) == len(list2):
            for i in range(len(list1)):
                for j in range(len(list2)):
                    if list1[i] == list2[j]:
                        matched_digits = matched_digits + 1
                        if i == j:
                            matched_positions = matched_positions + 1
                            continue
            result = [matched_digits, matched_positions]                               
        return result
    
    result_list = compare_lists(target_num, user_input)
    print('\t \t \t\t   {:>2}     |  {}  | {}/{}'.format(attempt+1,num,str(result_list[0]),str(result_list[1])))
    print('\t \t \t\t'+  ' ___________________________')
    if result_list[1] == 4 and result_list[0] == 4 and attempt < 3:
        print('Bingo! You are damn lucky!')
        urdutrans5 = translator.translate('Great! You are very lucky! ', dest='ur')
        print(urdutrans5.text)
        break
    elif result_list[1] == 4 and result_list[0] == 4 and attempt < 6:
        print('Bravo! You are a genious!')
        urdutrans6 = translator.translate('Excellent! you seem to be very intelligent', dest='ur')
        print(urdutrans6.text)
        break
    elif result_list[1] == 4 and result_list[0] == 4 and attempt >= 6:
        print('Bravo! You won!')
        urdutrans7 = translator.translate('Great! You won', dest='ur')
        print(urdutrans7.text)
        break      
    if attempt == 9 and result_list[1] != 4:
        print('\n              Try again! Target number was:  ', end='')
        for i in target_num:
            print(i, end='')
        urdutrans8 = translator.translate('!Try again', dest='ur')
        print("              ", urdutrans8.text)    
