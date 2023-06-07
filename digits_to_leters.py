''' the program takes in a numerical digit from 0-999,999,999 nd return it in words. '''


class DigitToLetter():

    def_digit_dict={
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        10:'ten',
        11:'eleven',
        12:'twelve',
        13:'thirteen',
        14:'fourteen',
        15:'fifteen',
        16:'sixteen',
        17:'seventeen',
        18:'eighteen',
        19:'nineteen'
        }
    place_value={
        2:'tens',
        3:'hundred',
        4:'thousand',
        5:'thousand',
        6:'thousand',
        7:'million',
        8:'million',
        9:'million',
        10:'bllion'
    }
    tens_place={
        2:'twenty',
        3:'thirty',
        4:'forty',
        5:'fifty',
        6:'sixty',
        7:'seventy',
        8:'eighty',
        9:'ninety'
    }
    
    def in_default(self,digit): #checks dictionary for values
        try:
           word = self.def_digit_dict[digit]
           return word
        except:
            return False
    def split_digit(self,digit):
        dig= str(digit)
        dig_list=[int(i) for i in dig ]
        return dig_list
    
    def split_hundred(self,digit):
        dgt=str(digit)
        overflow=len(dgt)%3
        
        lst=[]

        if not overflow == 0:
            lst.append(dgt[:overflow])
        rng= int((len(dgt)-overflow)/3)
       
        start=overflow
        end=overflow+3
        for _ in range(rng):
            lst.append(dgt[start:end])
            start+=3
            end+=3
        
        return lst

    def tens_word(self,digit): # checks for the tens that are not in the dictionary
    
        in_default=self.in_default(digit)
        if in_default:
            return in_default
        
        dig_list=self.split_digit(digit)
       
        tens_place=self.tens_place[dig_list[0]]
        if dig_list[1]==0:
            word = f'{tens_place}'
        else:

            unit=self.def_digit_dict[dig_list[1]]
            word=f'{tens_place} {unit}'
        return word
    
    def hundred(self,dgt):
        digit=int(dgt)
       
        if digit==000:
            return None
        
        dig_list=self.split_digit(digit)
        if dgt[0]=='0':
            word =f'{self.tens_word(digit)}'

        else:
            tens=f'{dig_list[1]}'+f'{dig_list[2]}'
            word=f'{self.def_digit_dict[dig_list[0]]} hundred and {self.tens_word(tens)}'

        return word
    
    #10,234,567
    def others(self,digit):
        length=len(str(digit))
        place_value=self.place_value[length]
        
        splt=self.split_hundred(digit)
        lst=[]
        start=0
        if len(splt[0])<=2:
            lst.append(self.tens_word(int(splt[0])))
            start=1


        for i in splt[start:]:
            lst.append(self.hundred(i))
         


        word=f'{lst[0]} {place_value}'
        new_lst=lst
        new_lst.remove(new_lst[0])
        plc=[]
        new_spt=splt.copy()
        new_spt.pop(0)

        length=length-len(str(splt[0]))

        for i in new_spt:
           

            print(length,'len')
           

            plce=self.place_value[length]
           
            plc.append(plce)
            length=length-len(i)


        for i in range(len(new_lst)):
            if new_lst[i] == None:
                continue
          
            plce=plc[i]

            if plce=='hundred':
                word+=f' {new_lst[i]}'

            else:
                word+=f' {new_lst[i]} {plce}'
  
        return word

    
    
    def word(self,digit):
   
        
        lenght=len(str(digit))
        place_value=self.place_value[lenght]

        if place_value=='tens':
            
            return self.tens_word(digit)
        elif place_value=='hundred':
            return self.hundred(digit)
        return self.others(digit)

obj=DigitToLetter()



print(obj.word(456888))
