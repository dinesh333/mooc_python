# Write your solution here

def add_to_dict(dict, base, start, end):
    for i in range(start, end+1):
        dict[i] = dict[base] + '-' + dict[i%base]

def dict_of_numbers():
    dict = {}
    dict[0]  = 'zero'
    dict[1]  = 'one'
    dict[2]  = 'two'
    dict[3]  = 'three'
    dict[4]  = 'four'
    dict[5]  = 'five'
    dict[6]  = 'six'
    dict[7]  = 'seven'
    dict[8]  = 'eight'
    dict[9]  = 'nine'
    dict[10] = 'ten'
    dict[11] = 'eleven'
    dict[12] = 'twelve'
    dict[13] = 'thirteen'
    dict[14] = 'fourteen'
    dict[15] = 'fifteen'
    dict[16] = 'sixteen'
    dict[17] = 'seventeen'
    dict[18] = 'eighteen'
    dict[19] = 'nineteen'
    dict[20] = 'twenty'
    dict[30] = 'thirty'
    dict[40] = 'forty'
    dict[50] = 'fifty'
    dict[60] = 'sixty'
    dict[70] = 'seventy'
    dict[80] = 'eighty'
    dict[90] = 'ninety'

    for i in range(2, 10):
        base = i * 10
        add_to_dict(dict, base, base+1, base+9)
    
    return dict