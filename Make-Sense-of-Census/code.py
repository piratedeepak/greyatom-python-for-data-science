# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')
# Step 1: In this first task, we will load the data to a numpy array and add a new record to it.

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

# Display Data
print("\nData: \n\n", data)

# Append the new_record in data
census = np.concatenate((new_record, data))
# print(census.shape)

# Step 2: We often associate the potential of a country based on the age distribution of the people residing there. We too want to do a simple analysis of the age distribution

age = np.array(census[:,0]) # Selecting Age column from census
max_age = max(age) # finding the max age
print(max_age)  
min_age = min(age) # finding the min age
print(min_age)
age_mean = np.mean(age) # finding the mean of age 
age_mean = np.round(age_mean,2)
print(age_mean)
age_std = round(np.std(age),2) # finding the standard derviation of age
print(age_std)

# STEP 3 : finding the race and minorities

race = np.array(census[:,2]) # filtering the races
# print(race)

# creating races separate data according to each race like 0,1,2,3,4 respectively
race_0 = census[census[:,2] == 0]
race_1 = census[census[:,2] == 1]
race_2 = census[census[:,2] == 2]
race_3 = census[census[:,2] == 3]
race_4 = census[census[:,2] == 4]

# finding the quantity of particular race
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

# comparing which race is in minority
if len_0 < len_1 and len_0 < len_2 and len_0 < len_3 and len_0 < len_4:
    minority_race = 0
elif len_1 < len_0 and len_1 < len_2 and len_1 < len_3 and len_1 < len_4:
    minority_race = 1
elif len_2 < len_0 and len_2 < len_1 and len_2 < len_3 and len_2 < len_4:
    minority_race = 2
elif len_3 < len_0 and len_3 < len_1 and len_3 < len_2 and len_3 < len_4:
    minority_race = 3
else:
    minority_race = 4
print(minority_race)

# Step 4: As per the new govt. policy, all citizens above age 60 should not be made to 
# work more than 25 hours per week. Let us look at the data and see if that policy is followed

senior_citizens = census[census[:,0] > 60] # creating array of people who aged above 60.
working_hours_sum = senior_citizens.sum(axis=0)[6] # sum the total working hours of above 60 aged people.
senior_citizens_len = len(senior_citizens) # Total no. of people aged above 60.
avg_working_hours = np.round(working_hours_sum / senior_citizens_len, 2) # average working finding
print(working_hours_sum)
print(avg_working_hours)

# Step 5: Our parents have repeatedly told us that we need to study well 
# in order to get a good(read: higher-paying) job. Let's see 
# whether the higher educated people have better pay in general.

# creating array of people have high or low education on respective criteria
high = census[census[:,1] > 10] 
low = census[census[:,1] <= 10]
# finding average salary pay to higher education people
avg_pay_high = np.round(high.mean(axis = 0)[7],2)
avg_pay_low = np.round(low.mean(axis = 0)[7],2)
print(avg_pay_high,avg_pay_low,sep="\n")





