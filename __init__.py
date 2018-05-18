
"""
Number to word converter
"""
 
__author__ = 'Oluwafemi <fems.david@hotmail.com>'
__version__ = '1.0'
import json
import math
import random
import re

int_to_word={
            "0":"Zero",
            "1":"One",
            "2":"Two",
            "3":"Three",
            "4":"Four",
            "5":"Five",
            "6":"Six",
            "7":"Seven",
            "8":"Eight",
            "9":"Nine",
            "10":"Ten",
            "11":"Eleven",
            "12":"Twelve",
            "13":"Thirteen",
            "14":"Fourteen",
            "15":"Fifteen",
            "16":"Sixteen",
            "17":"Seventeen",
            "18":"Eighteen",
            "19":"Nineteen",
            "20":"Twenty",
            "30":"Thirty",
            "40":"Forty",
            "50":"Fifty",
            "60":"Sixty",
            "70":"Seventy",
            "80":"Eighty",
            "90":"Ninety",
    }

large_numbers=["",
            "Thousand",
            "Million",
            "Billion",
            "Trillion",
            "Quantillion",
            "Sex-tillion",
            "Septillion",
            "Octillion",
            "Nonillion",
            "Decillion",
            "Undecillion",
            "Duodecillion",
            "Tredecillion",
            "Quattuordecillion",
            "Quindecillion",
            "Sexdecillion",
            "Septendecillion",
            "Octodecillion",
            "Novemdecillion",
            "Vigintillion",
            "Centillion",
        ]

 
"""
    Method to pad number string
"""
def pad_string(int_str):
    int_str_length=len(int_str)     #length of the string
    """
    get the number of padding needed so that string can be in muliple of 3
    e.g if int_str is 1234, it requires to be padded twice so that
    int_str can become 001234
    """
    number_of_padding=3*math.ceil(int_str_length/3)-int_str_length #number of string to pad

    #pad with 0
    new_int_str=("0"*abs(number_of_padding))+int_str
    return new_int_str

"""
    Method to validate number string e.g 2344r567 is not a valid number string
"""
def clean_number_string(int_str):
    
    pattern="(^\d+)(\.\d+)?$"
    match = re.match(pattern,int_str)
    
    if match:
        #print(int_str.split("."))
        return int_str
    else:
        raise ValueError("Error: %s is not a valid Number"%int_str)


"""
Method to convert number string to word e.g 1234 to One Thousand, two hundred and thirty four
"""
def num2word(number_string,add_comma=True):
  
    cleaned_number_string=clean_number_string(number_string)

    parts=cleaned_number_string.split(".")
    fractional_part=""
    integer_part=parts[0]
    integer_part_in_word=_num2word(integer_part)
    fractional_part_in_word=""
    if len(parts)>1:
        fractional_part=parts[1]
        fractional_part_in_word=" point"
        for w in fractional_part:
            fractional_part_in_word=fractional_part_in_word+" "+int_to_word[w]

    return "%s%s"%(integer_part_in_word,fractional_part_in_word)
    
def _num2word(cleaned_number_string,add_comma=True):
    padded_number_string=pad_string(cleaned_number_string)
    comma=","
    if not add_comma:
        comma=""
    number2word_list=[] #container for group of 3 characters

    #break  number string into group of 3 characters e.g 453, 278, 001
    sub_number_string_list=[]
    for i in range(int(len(padded_number_string)/3)):
        from_index=3*i
        to_index=(3*i)+3
        #extract 3 characters
        three_character_string=padded_number_string[from_index:to_index]
        in_word=_convert_numbertoword(three_character_string)
        if len(in_word.strip())==0:
            continue
        number2word_list.append(in_word)
        sub_number_string_list.append(three_character_string)

    size=len(number2word_list)
    word=""
    counter=1
    last_entry=number2word_list.pop(-1)
    number2word_list.append("")
    #print(list)
    #print("Size: %s"%int_wrd_dict)
    for hundreds in number2word_list:
        if hundreds=='000':
            counter+=1
            continue
        word+=hundreds+" %s "%large_numbers[size-counter]
        counter+=1
        if size>counter:
            word=word.strip()+"%s "%comma
        else:
            word=word.strip()+" "


    if word.strip()=="":
        word=last_entry
    else:
        if int(sub_number_string_list.pop(-1))<100:
            word+="and "+last_entry
        else:
            word=word.strip()+"%s %s"%(comma,last_entry)

    return word.lower().capitalize()

   

"""
Helper method to convert 3 character number string  to word
"""
def _convert_numbertoword(three_character_number_string):
    
    hundred=three_character_number_string[0]
    tens=three_character_number_string[1]
    unit=three_character_number_string[2]

    if three_character_number_string=='000':
        return three_character_number_string


    wrd=""
    if int(hundred)!=0:
        wrd=int_to_word[hundred]+" Hundred "
        if int(tens)==0:
            if int(unit)==0:
                pass
            else:
                wrd+="and %s"%int_to_word[unit]
        else:
             #add tens and unit
            tens_and_unit_sum=10*int(tens)+int(unit)
            str_tens_and_unit_sum=int_to_word.get(str(tens_and_unit_sum),"")
            if len(str_tens_and_unit_sum)!=0:
                wrd+= "and %s"%str_tens_and_unit_sum
            else:
                str_x_tens=int_to_word.get(str(int(tens)*10),"")
                str_x_unit=int_to_word.get(str(unit),"")
                wrd+="and %s %s"%(str_x_tens,str_x_unit)
    else:
            tens_and_unit_sum=10*int(tens)+int(unit)
            str_tens_and_unit_sum=int_to_word.get(str(tens_and_unit_sum),"")
            if len(str_tens_and_unit_sum)!=0:
                wrd+= "%s"%str_tens_and_unit_sum
            else:
                str_x_tens=int_to_word.get(str(10*int(tens)),"")
                str_x_unit=int_to_word.get(str(unit),"")
                wrd+="%s %s"%(str_x_tens,str_x_unit)
          
    return wrd.strip()


