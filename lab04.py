# Part A: Leap Year

def leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False

year = int(input("Year: "))

print(leap_year(year))


#Part B: Rotate (Optional Challenge is Done)

def rotate(s,n):
    if len(s) == 1 or len(s) == 0:
        return s
    elif len(s) >= n:
        temp_f = s[(len(s)-n):]
        temp_l = s[:(len(s)-n)]
        new_s = temp_f + temp_l
        return new_s
    elif len(s) <= n:
        m = n % len(s)
        temp_f = s[(len(s)-m):]
        temp_l = s[:(len(s)-m)]
        new_s = temp_f + temp_l
        return new_s

s = input("S: ")
n = int(input('N: ')) 

print(rotate(s,n))


#Part C: Digit Count

def digit_count(num):
    num_str = str(num)
    i=0
    c_even = 0
    c_odd = 0
    c_zero = 0
    for i in range(len(num_str)):
        
        if int(num_str[i]) == 0:
            c_zero += 1
        elif int(num_str[i]) % 2 ==0:
            c_even += 1
        else: 
            c_odd += 1
    
    return c_even, c_odd, c_zero

num = int(input("Write the num:"))
print(digit_count(num))


#Part D: Float Check

def float_check(s):
    s = s.replace(".","",1)
    return s.isdigit()

txt = input("Str: ")
print(float_check(txt))
