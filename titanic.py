'''
rapha_jacobson_titanic_file_io.py

Description: Analyzes the titanic data set and writes information to new files

Features: calculates price of package, calculates the distance a package will go

Log: 1.0

Bugs: 
'''

def load_and_display(file):
  '''
    display first 10 rows, column names, and total number of passengers                                                                 
    Args:
        file - Titanic data
    Returns:
        a list of 10 rows, column names, and total num of passengers
    '''
  try:
    with open('loadanddisplay.csv', 'w') as output:                                             #Create a new file and write into it (maker recognizable by "output")
      ten_count = 0
      for line in file:
        output.write(line)
        ten_count+=1
        if ten_count == 11:
          break
      file.seek(1)                                                                              #bring pointer back to line 1
      pass_count = 0
      for line in file:
        if len(line) > 1:
          pass_count += 1
      output.write(f"There are {pass_count - 1} passengers")                                    #Write to the loadanddisplay file the amount of passengers on the titanic
  except FileNotFoundError:
    print(f"Error {'loadanddisplay.csv'} not found")


def survival_rate(file):
  '''
    find the survival rate of all passengers                                                                 
    Args:
        file - Titanic data
    Returns:
        The survival rate of all passengers
    '''
  try: 
    with open('survivalrate.csv', 'w') as output:                                    #Create a new file and write into it (maker recognizable by "output")
      survive = 0
      for line in file:
        data = line.strip().split(',')                                               #Create variable "data" which creates a list out of each line in the titanic data set (makes it easy to find a specific data point through index)
        if len(data) > 1:
          if data[1] == "1":
            survive += 1
      output.write (f"{survive / 891 * 100} %")                                      #write to the survivalrate.csv file the survivval rate of all passengers
  except FileNotFoundError:
    print(f"Error {'loadanddisplay.csv'} not found")

def survival_by_gender(file):
  '''
    Finds the survival rate by gender
    Args:
      file - Titanic data
    Returns:
      Percentage of males and females who survived
      If a male of female is more likely to survive
    '''
  with open('survivalbygender.csv', 'w') as output:                         #Create a new file and write into it (maker recognizable by "output")
    try:
      m_survive = 0
      f_survive = 0
      for line in file:
        data = line.strip().split(',')                                      #Create variable "data" which creates a list out of each line in the titanic data set (makes it easy to find a specific data point through index)
        if data[1] == "1" and data[5] == "male":
          m_survive += 1
        if data[1] == "1" and data[5] == "female":
          f_survive += 1
      m_surv_rate = m_survive / 577 * 100                                   #calculate percentage of male survival rate
      f_surv_rate = f_survive / 314 * 100                                   #calculate percentage of female survival rate
      output.write (f"The female survival rate is {f_surv_rate}%\n")        #write to survivalbygender.csv
      output.write (f"The male survival rate is {m_surv_rate}%\n")          #write to survivalbygender.csv
      if m_surv_rate > f_surv_rate:
        output.write("Therefore the male survival rate is higher")          #write to survivalbygender.csv
      elif f_surv_rate > m_surv_rate:
        output.write("Therefore the female survival rate is higher")        #write to survivalbygender.csv
    except FileNotFoundError:
      print(f"Error {'loadanddisplay.csv'} not found")

def age_analysis(file):
  '''
    Analysis of the ages of all passengers
    Args:
        file - Titanic data
    Returns:
      The oldest passenger
      The youngest passenger
      The average age of passengers
      The average age of survivors vs. non-survivors
    '''
  with open('ageanalysis.csv', 'w') as output:                               #Create a new file and write into it (maker recognizable by "output")
      try:
        age_list = []
        for line in file:
            data = line.strip().split(',')                                   #Create variable "data" which creates a list out of each line in the titanic data set (makes it easy to find a specific data point through index)
            try:
                age_list.append(float(data[6]))                              #add index 6 of every line in the titanic data set to the list named "age_list"
            except:
                continue
        all_ages = sum(age_list)
        avg_age = round(all_ages/(len(age_list)))
        output.write(f"The average age is: {avg_age}\n")                     #write to the ageanalysis.csv file
        file.seek(1)                                                         #bring pointer back to line 1
        surv_age = []
        died_age = []
        for line in file:
            data = line.strip().split(',')
            if data[1] == "1":
                try:
                    surv_age.append(float(data[6]))                         #add data at index 6 to the surv_age list
                except:
                    continue
            else:
                try:
                    died_age.append(float(data[6]))                         #add data at index 6 to the died_age list
                except:
                    continue
        all_surv_ages = sum(surv_age)
        all_died_ages = sum(died_age)
        oldest_pass = max(age_list)
        youngest_pass = min(age_list)
        avg_surv_age = round(all_surv_ages/(len(surv_age)))
        avg_died_age = round(all_died_ages/(len(died_age)))
        output.write(f"The average age of all survivors of the titanic is: {avg_surv_age}\n")
        output.write(f"The average age of all the non-survivors of the titanic is: {avg_died_age}\n")
        output.write(f"The youngest passenger is {youngest_pass} years old\n")
        output.write(f"The oldest passenger is {oldest_pass} years old\n")
      except FileExistsError:
        print(f"Error {'ageanalysis'} not found")

def class_based_analysis(file):
  '''
  Analyzes data based off of class (1, 2, or 3)
  Args:
      file - Titanic data
  Returns:
      The survival rate of 1st, 2nd, and 3rd class
      The average fare paid for 1st, 2nd, and 3rd class
      A statement saying which class was most likely to survive
  '''
  try: 
    with open('classbasedanalysis.csv', 'w') as output:                                                   #Create a new file and write into it (maker recognizable by "output")
      next(file)
      firstc_surv = 0
      secondc_surv = 0
      thirdc_surv = 0
      fare_fc = []
      fare_sc = []
      fare_tc = []
      c1 = 0
      c2 = 0
      c3 = 0
      for line in file:
        data = line.strip().split(',')                                                                    #Create variable "data" which creates a list out of each line in the titanic data set (makes it easy to find a specific data point through index)
        if data[2] == "1":
          c1 += 1
          if data[1] == "1":
            firstc_surv += 1
          fare_fc.append(float(data[10]))
        elif data[2] == "2":
          c2 += 1
          if data[1] == "1":
            secondc_surv += 1
          fare_sc.append(float(data[10]))
        elif data[2] == "3":
          c3 += 1
          if data[1] == "1":
            thirdc_surv += 1
          fare_tc.append(float(data[10]))
      first_sr = round((firstc_surv/c1)*100)
      second_sr = round((secondc_surv/c2)*100)
      third_sr = round((thirdc_surv/c3)*100)
      avg_fare1 = round(((sum(fare_fc)/len(fare_fc))))
      avg_fare2 = round(((sum(fare_sc)/len(fare_sc))))
      avg_fare3 = round(((sum(fare_tc)/len(fare_tc))))
      output.write(f"The average fare of the first class is ${avg_fare1}\n")
      output.write(f"The average fare of the second class is ${avg_fare2}\n")
      output.write(f"The average fare of the third class is ${avg_fare3}\n")
      output.write(f"The average survival rate of the first class is {first_sr}%\n")
      output.write(f"The average survival rate of the second class is {second_sr}%\n")
      output.write(f"The average survival rate of the third class is {third_sr}%\n")
      if first_sr > second_sr and first_sr > third_sr:
        output.write("The first class has the highest survival rate")
      elif second_sr > first_sr and second_sr > third_sr:
        output.write("The second class has the highest survival rate")
      elif third_sr > first_sr and third_sr > second_sr:
        output.write("The third class has the highest survival rate")
  except FileExistsError:
    print(f"Error {'classbasedanalysis.csv'} not found")

def family_survival_patterns(file):
  '''
    Analyze survival based off of family
    Args:
        file - Titanic data
    Returns:
      Survival rate if you were travelling alone
      Survival rate if you were travelling with a family
      A statement saying if your survival chances were better when travelling alone or with a family
    '''
  try: 
    with open('familysurvivalpatterns.csv', 'w') as output:                                  #Create a new file and write into it (maker recognizable by "output")
      if_alone = 0
      if_wfam = 0
      alone_surv = []
      family_surv = []
      next(file)
      for line in file:
        data = line.strip().split(',')                                                      #Create variable "data" which creates a list out of each line in the titanic data set (makes it easy to find a specific data point through index)
        family_size = int(data[7]) + int(data[8]) + 1
        if family_size == 1:
          if_alone += 1
          if data[1] == "1":
            alone_surv.append(data[1])
        elif family_size > 1:
          if_wfam += 1
          if data[1] == "1":
            family_surv.append(data[1])
      alone_sr = round((len(alone_surv)/if_alone)*100)
      family_sr = round((len(family_surv)/if_wfam)*100)
      output.write(f"The survival rate of travelers alone on the titanic is {alone_sr}%\n")
      output.write(f"The survival rate of travelers with family on the titanic is {family_sr}%\n")
      if alone_sr > family_sr:
        output.write("If you were travelling alone, you were more likely to survive than if you wer traveling with a family")
      elif family_sr > alone_sr:
        output.write("If you were travelling with a family, you were more likely to survive than if you were travelling alone")
  except FileExistsError:
    print(f"Error {'familysurvivalpatterns.csv'} not found")



def main():
  try:
    with open('titanic.csv', 'r') as file:
      #header = file.readline().strip().split(',')  # Read the header row
      #name_index = header.index('Name')  # Find the index of 'Name' column
      data = open("titanic.csv")
      
      
      while True:
        inp = input("This code analzes the titanic data set. What would you like do do?\n" \
        "1. Show the first 10 rows, the headers, and display the number of passengers\n" \
        "2. Display the survival rate of all passengers\n" \
        "3. Display the survival rate for males and females, and which is more likely to survive\n" \
        "4. Display the average age of all passengers, the oldest and youngest pasengers, and the average age of all survivors vs. non-survivors\n" \
        "5. Display the survival rate and average fare paid based off class(1st, 2nd, or 3rd)\n" \
        "6. Display the survival rates based off of family size and display whether traveling alone increased or decreased you chances of survival\n" \
        "7. Display bar charts comparing survival rates by gender, a histogram showing age distribution, and a bar chart showing survival rate by class\n" \
        #"8. A complete analysis report of the passengers on the titanic\n"
        ": ")
        if inp == "1":
          load_and_display(file)
          file.seek(1)                                                              #bring pointer back to line 1
        elif inp == "2":
          survival_rate(file)
          file.seek(1)
        elif inp == "3":
          survival_by_gender(file)
          file.seek(1)
        elif inp == "4":
          age_analysis(file)
          file.seek(1)
        elif inp == "5":
          class_based_analysis(file)
          file.seek(1)
        elif inp == "6":
          family_survival_patterns(file)
          file.seek(1)
        ##elif inp == "8":
          ##comprehensive_report(file)
        else:
          print("Invalid response - Please try again")

  except FileNotFoundError:
    print("Error: 'titanic.csv' file not found.")  
  
main()
