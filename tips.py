def suma(dataset, bill_index, tip_index, sex_index, smoker_index, day_index, time_index):
    total_bill = 0
    total_tips = 0
    sex_freq = {}
    smoker_freq = {}
    day_freq = {}
    time_freq = {}

    for row in dataset:
        bill = float(row[bill_index])
        tip = float(row[tip_index])
        total_bill += bill
        total_tips += tip
    print(f'Total bill {total_bill} and Total tip {total_tips}')

    for row in dataset:
        sex = row[sex_index]
        if sex in sex_freq:
            sex_freq[sex] += 1
        else:
            sex_freq[sex] = 1
    print(f'Sex Frequency is {sex_freq}')
    
    for row in dataset:
        smoker = row[smoker_index]
        if smoker in smoker_freq:
            smoker_freq[smoker] += 1
        else:
            smoker_freq[smoker] = 1
    print(f'Smoker Frequency is {smoker_freq}')

    for row in dataset:
        day = row[day_index]
        if day in day_freq:
            day_freq[day] += 1
        else:
            day_freq[day] = 1
    print(f'Day Frequency is {day_freq}')
        
    for row in dataset:
        time = row[time_index]
        if time in time_freq:
            time_freq[time] += 1
        else:
            time_freq[time] = 1
    print(f'Time Frequency is {time_freq}')


calling = suma(dataset=tips_list, bill_index =0 , tip_index = 1,sex_index= 2,smoker_index= 3,day_index= 4,time_index= 5)
