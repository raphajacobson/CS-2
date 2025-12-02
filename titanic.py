
       
def read_titanic_data(file):
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
      output.write (f"The female survival rate is {f_surv_rate}%")
      output.write (f"The male survival rate is {m_surv_rate}%")
      if m_surv_rate > f_surv_rate:
        output.write("Therefore the male survival rate is higher")
      elif f_surv_rate > m_surv_rate:
        output.write("Therefore the female survival rate is higher")
    except FileNotFoundError:
      print(f"Error {'loadanddisplay.csv'} not found")

def age_analysis(file):
    for line in file
        data = line.strip().split(',')
        age = data[6]
        avg_age = (age / len(file))
        print (avg_age)



        


def main():
  try:
    with open('titanic.csv', 'r') as file:
      #header = file.readline().strip().split(',')  # Read the header row
      #name_index = header.index('Name')  # Find the index of 'Name' column
      data = open("titanic.csv")

      read_titanic_data(file)
      file.seek(1)
      survival_rate(file)
      file.seek(1)
      survival_by_gender(file)
      file.seek(1)
      age_analysis(file)
      file.seek(1)


  except FileNotFoundError:
    print("Error: 'titanic.csv' file not found.")  
  

main()

## for line in file:
 ##           row = line.strip().split(',')
  ##          #print(row[name_index])
    ##with open('howmanygirls.csv', 'w') as file:
      ##  girl_count = 0
        ##or row in 'ffile':
           ## if row[5] == "female":
          ##      girl_count += 1
            ##    girl_count += 1
        ##howmanygirls.write("males", "females")
