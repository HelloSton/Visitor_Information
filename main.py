#oject Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: <Wong Jia Le>
#Class: <PL2004Y>
#Date: <20-Aug-2021>
#Version: <1.0>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import matplotlib for piechart
import matplotlib.pyplot as plt
#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

  #print number of rows in dataframe
  print("There are " + str(len(df)) + " data rows read. \n")

  df = df.replace(to_replace =[" na ", "na"],value ="0")

  #display dataframe (rows and columns)
  print("The following dataframe are read as follows: \n")
  print(df)

  print("\nThe following data for South-East Asia region from 1988 to 1998 are shown below : \n")

  SortedSEA = (df[['Year', 'Month', ' Brunei Darussalam ', ' Indonesia ', ' Malaysia ', ' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ']][120:252])
  print(SortedSEA)
  
  
  #remove year & month
  NewSEA = SortedSEA.drop(columns=["Year", "Month"])

  #convert to int
  NewSEA = NewSEA.astype(str).astype(int)
  #print(NewSEA.columns)
  
  #Total sum
  TotalSEA=NewSEA.sum()

  #Sort in order
  SortednewSEA = TotalSEA.sort_values(ascending=False)

  #back to object
  SortednewSEA = SortednewSEA.reset_index()

  #adding columns
  SortednewSEA.columns = ['Countries', 'Visitor']

  #Display of all the countries
  print("\nThe numbers visitor from the SEA region are as follow(Please close the piechart to proceed):\n")
  print(SortednewSEA)
  print("\n")
  topthree = (SortednewSEA.head(3))
  print(topthree)

  #piechart
  visitorss = [3164529, 1902547, 646889]
  Countries = ['Indonesia','Malaysia','Thailand']
  plt.pie(visitorss,labels= Countries,autopct='%1.1f%%')
  plt.title('TopThree')
  plt.axis('equal')
  plt.legend(loc="lower right")
  plt.show()
  
  return
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

  #read csv File
  df = pd.read_csv('MonthyVisitors.csv')

  #Replacing the Value of na to 0
  df = df.replace(to_replace =[" na ", "na"],value ="0")

  #Sorting for Afria region
  SortedAF1=(df[['Year','Month',' Africa ']][120:252])
  NewAF1 = SortedAF1.drop(columns=["Year", "Month"])
  NewAF1 = NewAF1.astype(str).astype(int) 
  TotalAF1=NewAF1.sum()
  SortednewAF1 = TotalAF1.sort_values(ascending=False)
  SortednewAF1 = SortednewAF1.reset_index()
  SortednewAF1.columns = ['Countries', 'Visitor']

  #Sorting Australia region
  SortedAU1=(df[['Year','Month',' Australia ',' New Zealand ']][120:252])
  NewAU1 = SortedAU1.drop(columns=["Year", "Month"])
  NewAU1 = NewAU1.astype(str).astype(int) 
  TotalAU1=NewAU1.sum()
  SortednewAU1 = TotalAU1.sort_values(ascending=False)
  SortednewAU1 = SortednewAU1.reset_index()
  SortednewAU1.columns = ['Countries', 'Visitor']

  #Sorting NorthAmerica region
  SortedNA1=(df[['Year','Month',' USA ',' Canada ']][120:252])
  NewNA1 = SortedNA1.drop(columns=["Year", "Month"])
  NewNA1 = NewNA1.astype(str).astype(int) 
  TotalNA1=NewNA1.sum()
  SortednewNA1 = TotalNA1.sort_values(ascending=False)
  SortednewNA1 = SortednewNA1.reset_index()
  SortednewNA1.columns = ['Countries', 'Visitor']
  
  #Sorting Europe
  SortedEU1=(df[['Year','Month',' United Kingdom ',' Germany ',' France ',' Italy ',' Netherlands ',' Greece ',' Belgium & Luxembourg ',' Switzerland ',' Austria ',' Scandinavia ',' CIS & Eastern Europe ']][120:252])
  NewEU1 = SortedEU1.drop(columns=["Year", "Month"])
  NewEU1 = NewEU1.astype(str).astype(int) 
  TotalEU1=NewEU1.sum()
  SortednewEU1 = TotalEU1.sort_values(ascending=False)
  SortednewEU1 = SortednewEU1.reset_index()
  SortednewEU1.columns = ['Countries', 'Visitor']

  #Sorting Middle East region
  SortedME1=(df[['Year','Month',' Saudi Arabia ',' Kuwait ',' UAE ']][120:252])
  NewME1 = SortedME1.drop(columns=["Year", "Month"])
  NewME1 = NewME1.astype(str).astype(int) 
  TotalME1=NewME1.sum()
  SortednewME1 = TotalME1.sort_values(ascending=False)
  SortednewME1 = SortednewME1.reset_index()
  SortednewME1.columns = ['Countries', 'Visitor']

  #Sorting South-Asia Pacific region
  SortedSA1=(df[['Year','Month',' India ',' Pakistan ',' Sri Lanka ']][120:252])
  NewSA1 = SortedSA1.drop(columns=["Year", "Month"])
  NewSA1 = NewSA1.astype(str).astype(int) 
  TotalSA1=NewSA1.sum()
  SortednewSA1 = TotalSA1.sort_values(ascending=False)
  SortednewSA1 = SortednewSA1.reset_index()
  SortednewSA1.columns = ['Countries', 'Visitor']

  #Sorting Asia Pacific region
  SortedAP1=(df[['Year','Month',' Japan ',' Hong Kong ',' China ',' Taiwan ',' Korea, Republic Of ']][120:252])
  NewAP1 = SortedAP1.drop(columns=["Year", "Month"])
  NewAP1 = NewAP1.astype(str).astype(int) 
  TotalAP1=NewAP1.sum()
  SortednewAP1 = TotalAP1.sort_values(ascending=False)
  SortednewAP1 = SortednewAP1.reset_index()
  SortednewAP1.columns = ['Countries', 'Visitor']

  #Region and Countries
  SEA1 = df.columns[2] + "," + df.columns[3] + ","+ df.columns[4] + "," + df.columns[5] + "," + df.columns[6] + "," + df.columns[7] + ","+ df.columns[8]
  AP1 = df.columns[9] + "," + df.columns[10] + "," + df.columns[11] + "," + df.columns[12] + "," + df.columns[13] 
  SAP1 = df.columns[14] + "," + df.columns[15] + "," + df.columns[16]
  ME1 = df.columns[17] + "," + df.columns[18] + "," + df.columns[19]
  EU1 = df.columns[20] + "," + df.columns[21] + "," + df.columns[22] + "," + df.columns[23] + "," + df.columns[24] + "," + df.columns[25] + "," + df.columns[26] + "," + df.columns[27]  + "," + df.columns[28] + "," + df.columns[29] + "," + df.columns[30]
  NA1 = df.columns[31] + "," + df.columns[32]
  AU1 = df.columns[33] + "," + df.columns[34]
  AF1 = df.columns[35]  

  #Display Region and countries
  print("\nAsiaPacific Region :" + AP1)
  print("\nSouthAsiaPacific Region :" + SAP1)
  print("\nMiddleEast Region :" + ME1)
  print("\nEurope Region :"+EU1)
  print("\nNorthAmerica Region :"+NA1)
  print("\nAustria Region :" +AU1)
  print("\nAfrica Region :"+AF1) 




  #Iteration & String handling
  while True:
    print("\nKey in the same excat value as shown above(Do not include 'Region')")
    region = input("Enter the region that you picked(Key in A/a to quit): ")
    if region.isalpha() is False:
      print("Only Text are allowed!")
    else :
      print("\nYou have picked "+region)
      if region == "Africa" :
        print("\n")
        print(SortedAF1)
        print(SortednewAF1)
        break
      elif region == "Australia" :
        print("\n")
        print(SortedAU1)
        print(SortednewAU1)
        break
      elif region == "NorthAmerica" :
        print("\n")
        print(SortedNA1)
        print(SortednewNA1)
        break
      elif region == "Europe" :
        print("\n")
        print(SortedEU1)
        print(SortednewEU1)
        break
      elif region == "MiddleEast" :
        print("\n")
        print(SortedME1)
        print(SortednewME1)
        break
      elif region == "SouthAsiaPacific" :
        print("\n")
        print(SortedSA1)
        print(SortednewSA1)
        break
      elif region == "AsiaPacfic" :
        print("\n")
        print(SortedAP1)
        print(SortednewAP1)
        break
      elif region == "A" or region == "a" :
        print("STOP")
        break
      else:
        print("Since you have gave a invalid region,please look at the given region again.")

      


  

#########################################################################
#Main Branch: End of Code
#########################################################################