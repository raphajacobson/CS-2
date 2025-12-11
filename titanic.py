
       
def load_and_display(file):
  try:
    with open('loadanddisplay.csv', 'w') as output:
      ten_count = 0
      for line in file:
        output.write(line)
        ten_count+=1
        if ten_count == 11:
          break
      file.seek(1)
      pass_count = 0
      for line in file:
        if len(line) > 1:
          pass_count += 1
      output.write(f"There are {pass_count - 1} passengers")
  except FileNotFoundError:
    print(f"Error {'loadanddisplay.csv'} not found")


def survival_rate(file):
  try: 
    with open('survivalrate.csv', 'w') as output:
      survive = 0
      for line in file:
        data = line.strip().split(',')
        if len(data) > 1:
          if data[1] == "1":
            survive += 1
      output.write (f"{survive / 891 * 100} %")
  except FileNotFoundError:
    print(f"Error {'loadanddisplay.csv'} not found")

def survival_by_gender(file):
  with open('survivalbygender.csv', 'w') as output:
    try:
      m_survive = 0
      f_survive = 0
      for line in file:
        data = line.strip().split(',')
        if data[1] == "1" and data[5] == "male":
          m_survive += 1
        if data[1] == "1" and data[5] == "female":
          f_survive += 1
      m_surv_rate = m_survive / 577 * 100
      f_surv_rate = f_survive / 314 * 100
      output.write (f"The female survival rate is {f_surv_rate}%\n")
      output.write (f"The male survival rate is {m_surv_rate}%\n")
      if m_surv_rate > f_surv_rate:
        output.write("Therefore the male survival rate is higher")
      elif f_surv_rate > m_surv_rate:
        output.write("Therefore the female survival rate is higher")
    except FileNotFoundError:
      print(f"Error {'loadanddisplay.csv'} not found")

def age_analysis(file):
  with open('ageanalysis.csv', 'w') as output:
      try:
        age_list = []
        for line in file:
            data = line.strip().split(',')
            try:
                age_list.append(float(data[6]))
            except:
                continue
        all_ages = sum(age_list)
        avg_age = round(all_ages/(len(age_list)))
        output.write(f"The average age is: {avg_age}\n")
        file.seek(1)
        surv_age = []
        died_age = []
        for line in file:
            data = line.strip().split(',')
            if data[1] == "1":
                try:
                    surv_age.append(float(data[6]))
                except:
                    continue
            else:
                try:
                    died_age.append(float(data[6]))
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
   
  try: 
    with open('classbasedanalysis.csv', 'w') as output:
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
        data = line.strip().split(',')
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
  try: 
    with open('familysurvivalpatterns.csv', 'w') as output:
      if_alone = 0
      if_wfam = 0
      alone_surv = []
      family_surv = []
      next(file)
      for line in file:
        data = line.strip().split(',')
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


#family size = sibsp + parch + 1
#if family size 
#

def main():
  try:
    with open('titanic.csv', 'r') as file:
      #header = file.readline().strip().split(',')  # Read the header row
      #name_index = header.index('Name')  # Find the index of 'Name' column
      data = open("titanic.csv")

      load_and_display(file)
      file.seek(1)
      survival_rate(file)
      file.seek(1)
      survival_by_gender(file)
      file.seek(1)
      age_analysis(file)
      file.seek(1)
      class_based_analysis(file)
      file.seek(1)
      family_survival_patterns(file)


  except FileNotFoundError:
    print("Error: 'titanic.csv' file not found.")  
  

main()
