# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data=np.genfromtxt(path,delimiter=",",skip_header=1)

census=np.concatenate((data,new_record))
print(census)


# --------------
#Code starts here
from statistics import stdev 
from statistics import mean
import math
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier
age=census[:,0]
print(age)
max_age=max(age)
min_age=min(age)
age_mean=mean(age)
age_std=round_down(stdev(age),2)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)


# --------------
#Code starts here
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
len_final=[len_0,len_1,len_2,len_3,len_4]
minority_race=len_final.index(min(len_final))

print(len_final)
print(minority_race)


# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
#print(senior_citizens)
working_hours_sum=sum(senior_citizens[:,6])
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
avg_working_hours=round(working_hours_sum/senior_citizens_len,2)
print(senior_citizens_len)
print(avg_working_hours)



# --------------
#Code starts here
from statistics import mean
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=mean(high[:,7])
avg_pay_low=mean(low[:,7])
if (avg_pay_high>avg_pay_low):
    print('Higher education leads to better pay')
else:
    print('Higher education does not matter')


