
import pandas as pd
import openpyxl
import json
import numpy as np
from sentence_transformers import SentenceTransformer, util



def read_excel_file():
    snippet_list=[]
    file_path = 'Dataset 1.xlsx'  # Replace with your file path

    df = pd.read_excel(file_path, header=[0, 1])
    print(df)
    
    #total participants
    total_sample_number = df.iat[2, 1] 
    total_sample_percent=df.iat[3, 1]
    total_male_number=df.iat[4, 1]
    total_male_percent=df.iat[5, 1]
    total_female_number=df.iat[6, 1]
    total_female_percent=df.iat[7, 1]

    # print(f"total participants : {total_sample_number}")
    # print(f"Male participants : {total_male_number}")
    # print(f"Female participants : {total_female_number}")

    #region data ----noth east
    north_east_total_number=df.iat[12, 1]
    north_east_total_percent=df.iat[13, 1]
    north_east_male_number=df.iat[12, 3]
    north_east_male_percent=df.iat[13, 3]
    north_east_female_number=df.iat[12, 4]
    north_east_female_percent=df.iat[13, 4]
        
    # print(f"North East Total participants : {north_east_total_number}")
    # print(f"North East Total Male participants : {north_east_male_percent}")
    # print(f"North East Total Female participants : {north_east_female_percent}")


    #region data ----noth west
    north_west_total_number=df.iat[14, 1]
    north_west_total_percent=df.iat[15, 1]
    north_west_male_number=df.iat[14, 3]
    north_west_male_percent=df.iat[15, 3]
    north_west_female_number=df.iat[14, 4]
    north_west_female_percent=df.iat[15, 4]
        
    # print(f"North West Total participants : {north_west_total_number}")
    # print(f"North West Total Male participants : {north_west_male_number}")
    # print(f"North West Total Female participants : {north_west_female_number}")


    #region data Yorkshire & The Humber

    yorkshire_total_number=df.iat[16, 1]
    yorkshire_total_percent=df.iat[17, 1]
    yorkshire_male_number=df.iat[16, 3]
    yorkshire_male_percent=df.iat[17, 3]
    yorkshire_female_number=df.iat[16, 4]
    yorkshire_female_percent=df.iat[17, 4]


    #region data East Midlands

    east_midlands_total_number=df.iat[18, 1]
    east_midlands_total_percent=df.iat[19, 1]
    east_midlands_male_number=df.iat[18, 3]
    east_midlands_male_percent=df.iat[19, 3]
    east_midlands_female_number=df.iat[18, 4]
    east_midlands_female_percent=df.iat[19, 4]


    #region data West Midlands

    west_midlands_total_number=df.iat[20, 1]
    west_midlands_total_percent=df.iat[21, 1]
    west_midlands_male_number=df.iat[20, 3]
    west_midlands_male_percent=df.iat[21, 3]
    west_midlands_female_number=df.iat[20, 4]
    west_midlands_female_percent=df.iat[21, 4]


    #region data  East of England

    east_england_total_number=df.iat[22, 1]
    east_england_total_percent=df.iat[23, 1]
    east_england_male_number=df.iat[22, 3]
    east_england_male_percent=df.iat[23, 3]
    east_england_female_number=df.iat[22, 4]
    east_england_female_percent=df.iat[23 , 4]
    
    #region data  London

    
    london_total_number=df.iat[24, 1]
    london_total_percent=df.iat[25, 1]
    london_male_number=df.iat[24, 3]
    london_male_percent=df.iat[25, 3]
    london_female_number=df.iat[24, 4]
    london_female_percent=df.iat[25 , 4]
   

    #region data  South East

    south_east_total_number=df.iat[26, 1]
    south_east_total_percent=df.iat[27, 1]
    south_east_male_number=df.iat[26, 3]
    south_east_male_percent=df.iat[27, 3]
    south_east_female_number=df.iat[26, 4]
    south_east_female_percent=df.iat[27 , 4]
   

    #region data  South West
    south_west_total_number=df.iat[28, 1]
    south_west_total_percent=df.iat[29, 1]
    south_west_male_number=df.iat[28, 3]
    south_west_male_percent=df.iat[29, 3]
    south_west_female_number=df.iat[28, 4]
    south_west_female_percent=df.iat[29 , 4]
   

    #region data  Wales
    wales_total_number=df.iat[30, 1]
    wales_total_percent=df.iat[31, 1]
    wales_male_number=df.iat[30, 3]
    wales_male_percent=df.iat[31, 3]
    wales_female_number=df.iat[30, 4]
    wales_female_percent=df.iat[31 , 4]
   
    
    #region data  Scotland

    scotland_total_number=df.iat[32, 1]
    scotland_total_percent=df.iat[33, 1]
    scotland_male_number=df.iat[32, 3]
    scotland_male_percent=df.iat[33, 3]
    scotland_female_number=df.iat[32, 4]
    scotland_female_percent=df.iat[33 , 4]
   
    #region data  Northern Ireland

    nothern_ireland_total_number=df.iat[34, 1]
    nothern_ireland_total_percent=df.iat[35, 1]
    nothern_ireland_male_number=df.iat[34, 3]
    nothern_ireland_male_percent=df.iat[35, 3]
    nothern_ireland_female_number=df.iat[34, 4]
    nothern_ireland_female_percent=df.iat[35 , 4]
   
    #Age 18-24
    eighteen_twentyfour_total_number=df.iat[40, 1]
    eighteen_twentyfour_total_percent=df.iat[41, 1]
    eighteen_twentyfour_male_number=df.iat[40, 3]
    eighteen_twentyfour_male_percent=df.iat[41, 3]
    eighteen_twentyfour_female_number=df.iat[40, 4]
    eighteen_twentyfour_female_percent=df.iat[41 , 4]

    #Age 25-34
    twenty_thirty_total_number=df.iat[42, 1]
    twenty_thirty_total_percent=df.iat[43, 1]
    twenty_thirty_male_number=df.iat[42, 3]
    twenty_thirty_male_percent=df.iat[43, 3]
    twenty_thirty_female_number=df.iat[42, 4]
    twenty_thirty_female_percent=df.iat[43 , 4]


        #Age 35-44
    thirty_forty_total_number=df.iat[44, 1]
    thirty_forty_total_percent=df.iat[45, 1]
    thirty_forty_male_number=df.iat[44, 3]
    thirty_forty_male_percent=df.iat[45, 3]
    thirty_forty_female_number=df.iat[44, 4]
    thirty_forty_female_percent=df.iat[45 , 4]


            #Age 45-54
    forty_fifty_total_number=df.iat[46, 1]
    forty_fifty_total_percent=df.iat[47, 1]
    forty_fifty_male_number=df.iat[46, 3]
    forty_fifty_male_percent=df.iat[47, 3]
    forty_fifty_female_number=df.iat[46, 4]
    forty_fifty_female_percent=df.iat[47 , 4]


    #Age 55-64
    fifty_sixty_total_number=df.iat[48, 1]
    fifty_sixty_total_percent=df.iat[49, 1]
    fifty_sixty_male_number=df.iat[48, 3]
    fifty_sixty_male_percent=df.iat[49, 3]
    fifty_sixty_female_number=df.iat[48, 4]
    fifty_sixty_female_percent=df.iat[49 , 4]

    #Questions data

    question1=df.iat[53,0]
    total_participants_question1=df.iat[54,1]
    male_participants_question1=df.iat[54,3]
    female_participants_question1=df.iat[54,4]

    crime_total_participants=df.iat[56,1]
    crime_male_participants=df.iat[56,3]
    crime_female_participants=df.iat[56,4]
    crime_north_east=df.iat[56,6]
    crime_north_west=df.iat[56,7]
    crime_yorkshire_the_humber=df.iat[56,8]
    crime_east_Midlands=df.iat[56,9]
    crime_west_midlands=df.iat[56,10]
    crime_east_of_england=df.iat[56,11]
    crime_london=df.iat[56,12]
    crime_south_east=df.iat[56,13]
    crime_south_west=df.iat[56,14]
    crime_wales=df.iat[56,15]
    crime_scotland=df.iat[56,16]
    crime_northern_ireland=df.iat[56,17]
    crime_age_18_24=df.iat[56,19]
    crime_age_25_34=df.iat[56,20]
    crime_age_35_44=df.iat[56,21]
    crime_age_45_54=df.iat[56,22]
    crime_age_55_64=df.iat[56,23]

    cost_of_living_total_participants=df.iat[58,1]
    cost_of_living_male_participants=df.iat[58,3]
    cost_of_living_female_participants=df.iat[58,4]
    cost_of_living_north_east=df.iat[58,6]
    cost_of_living_north_west=df.iat[58,7]
    cost_of_living_yorkshire_the_humber=df.iat[58,8]
    cost_of_living_east_Midlands=df.iat[58,9]
    cost_of_living_west_midlands=df.iat[58,10]
    cost_of_living_east_of_england=df.iat[58,11]
    cost_of_living_london=df.iat[58,12]
    cost_of_living_south_east=df.iat[58,13]
    cost_of_living_south_west=df.iat[58,14]
    cost_of_living_wales=df.iat[58,15]
    cost_of_living_scotland=df.iat[58,16]
    cost_of_living_northern_ireland=df.iat[58,17]
    cost_of_living_age_18_24=df.iat[58,19]
    cost_of_living_age_25_34=df.iat[58,20]
    cost_of_living_age_35_44=df.iat[58,21]
    cost_of_living_age_45_54=df.iat[58,22]
    cost_of_living_age_55_64=df.iat[58,23]

    education_total_participants=df.iat[60,1]
    education_male_participants=df.iat[60,3]
    education_female_participants=df.iat[60,4]
    education_north_east=df.iat[60,6]
    education_north_west=df.iat[60,7]
    education_yorkshire_the_humber=df.iat[60,8]
    education_east_Midlands=df.iat[60,9]
    education_west_midlands=df.iat[60,10]
    education_east_of_england=df.iat[60,11]
    education_london=df.iat[60,12]
    education_south_east=df.iat[60,13]
    education_south_west=df.iat[60,14]
    education_wales=df.iat[60,15]
    education_scotland=df.iat[60,16]
    education_northern_ireland=df.iat[60,17]
    education_age_18_24=df.iat[60,19]
    education_age_25_34=df.iat[60,20]
    education_age_35_44=df.iat[60,21]
    education_age_45_54=df.iat[60,22]
    education_age_55_64=df.iat[60,23]

    housing_total_participants=df.iat[62,1]
    housing_male_participants=df.iat[62,3]
    housing_female_participants=df.iat[62,4]
    housing_north_east=df.iat[62,6]
    housing_north_west=df.iat[62,7]
    housing_yorkshire_the_humber=df.iat[62,8]
    housing_east_Midlands=df.iat[62,9]
    housing_west_midlands=df.iat[62,10]
    housing_east_of_england=df.iat[62,11]
    housing_london=df.iat[62,12]
    housing_south_east=df.iat[62,13]
    housing_south_west=df.iat[62,14]
    housing_wales=df.iat[62,15]
    housing_scotland=df.iat[62,16]
    housing_northern_ireland=df.iat[62,17]
    housing_age_18_24=df.iat[62,19]
    housing_age_25_34=df.iat[62,20]
    housing_age_35_44=df.iat[62,21]
    housing_age_45_54=df.iat[62,22]
    housing_age_55_64=df.iat[62,23]


    international_conflict_total_participants=df.iat[64,1]
    international_conflict_male_participants=df.iat[64,3]
    international_conflict_female_participants=df.iat[64,4]
    international_conflict_north_east=df.iat[64,6]
    international_conflict_north_west=df.iat[64,7]
    international_conflict_yorkshire_the_humber=df.iat[64,8]
    international_conflict_east_Midlands=df.iat[64,9]
    international_conflict_west_midlands=df.iat[64,10]
    international_conflict_east_of_england=df.iat[64,11]
    international_conflict_london=df.iat[64,12]
    international_conflict_south_east=df.iat[64,13]
    international_conflict_south_west=df.iat[64,14]
    international_conflict_wales=df.iat[64,15]
    international_conflict_scotland=df.iat[64,16]
    international_conflict_northern_ireland=df.iat[64,17]
    international_conflict_age_18_24=df.iat[64,19]
    international_conflict_age_25_34=df.iat[64,20]
    international_conflict_age_35_44=df.iat[64,21]
    international_conflict_age_45_54=df.iat[64,22]
    international_conflict_age_55_64=df.iat[64,23]


    mortgage_interest_rates_total_participants=df.iat[66,1]
    mortgage_interest_rates_male_participants=df.iat[66,3]
    mortgage_interest_rates_female_participants=df.iat[66,4]
    mortgage_interest_rates_north_east=df.iat[66,6]
    mortgage_interest_rates_north_west=df.iat[66,7]
    mortgage_interest_rates_yorkshire_the_humber=df.iat[66,8]
    mortgage_interest_rates_east_Midlands=df.iat[66,9]
    mortgage_interest_rates_west_midlands=df.iat[66,10]
    mortgage_interest_rates_east_of_england=df.iat[66,11]
    mortgage_interest_rates_london=df.iat[66,12]
    mortgage_interest_rates_south_east=df.iat[66,13]
    mortgage_interest_rates_south_west=df.iat[66,14]
    mortgage_interest_rates_wales=df.iat[66,15]
    mortgage_interest_rates_scotland=df.iat[66,16]
    mortgage_interest_rates_northern_ireland=df.iat[66,17]
    mortgage_interest_rates_age_18_24=df.iat[66,19]
    mortgage_interest_rates_age_25_34=df.iat[66,20]
    mortgage_interest_rates_age_35_44=df.iat[66,21]
    mortgage_interest_rates_age_45_54=df.iat[66,22]
    mortgage_interest_rates_age_55_64=df.iat[66,23]

    
    the_economy_total_participants=df.iat[68,1]
    the_economy_male_participants=df.iat[68,3]
    the_economy_female_participants=df.iat[68,4]
    the_economy_north_east=df.iat[68,6]
    the_economy_north_west=df.iat[68,7]
    the_economy_yorkshire_the_humber=df.iat[68,8]
    the_economy_east_Midlands=df.iat[68,9]
    the_economy_west_midlands=df.iat[68,10]
    the_economy_east_of_england=df.iat[68,11]
    the_economy_london=df.iat[68,12]
    the_economy_south_east=df.iat[68,13]
    the_economy_south_west=df.iat[68,14]
    the_economy_wales=df.iat[68,15]
    the_economy_scotland=df.iat[68,16]
    the_economy_northern_ireland=df.iat[68,17]
    the_economy_age_18_24=df.iat[68,19]
    the_economy_age_25_34=df.iat[68,20]
    the_economy_age_35_44=df.iat[68,21]
    the_economy_age_45_54=df.iat[68,22]
    the_economy_age_55_64=df.iat[68,23]


    the_environment_and_climate_change_total_participants=df.iat[70,1]
    the_environment_and_climate_change_male_participants=df.iat[70,3]
    the_environment_and_climate_change_female_participants=df.iat[70,4]
    the_environment_and_climate_change_north_east=df.iat[70,6]
    the_environment_and_climate_change_north_west=df.iat[70,7]
    the_environment_and_climate_change_yorkshire_the_humber=df.iat[70,8]
    the_environment_and_climate_change_east_Midlands=df.iat[70,9]
    the_environment_and_climate_change_west_midlands=df.iat[70,10]
    the_environment_and_climate_change_east_of_england=df.iat[70,11]
    the_environment_and_climate_change_london=df.iat[70,12]
    the_environment_and_climate_change_south_east=df.iat[70,13]
    the_environment_and_climate_change_south_west=df.iat[70,14]
    the_environment_and_climate_change_wales=df.iat[70,15]
    the_environment_and_climate_change_scotland=df.iat[70,16]
    the_environment_and_climate_change_northern_ireland=df.iat[70,17]
    the_environment_and_climate_change_age_18_24=df.iat[70,19]
    the_environment_and_climate_change_age_25_34=df.iat[70,20]
    the_environment_and_climate_change_age_35_44=df.iat[70,21]
    the_environment_and_climate_change_age_45_54=df.iat[70,22]
    the_environment_and_climate_change_age_55_64=df.iat[70,23]


    the_nhs_total_participants=df.iat[72,1]
    the_nhs_male_participants=df.iat[72,3]
    the_nhs_female_participants=df.iat[72,4]
    the_nhs_north_east=df.iat[72,6]
    the_nhs_north_west=df.iat[72,7]
    the_nhs_yorkshire_the_humber=df.iat[72,8]
    the_nhs_east_Midlands=df.iat[72,9]
    the_nhs_west_midlands=df.iat[72,10]
    the_nhs_east_of_england=df.iat[72,11]
    the_nhs_london=df.iat[72,12]
    the_nhs_south_east=df.iat[72,13]
    the_nhs_south_west=df.iat[72,14]
    the_nhs_wales=df.iat[72,15]
    the_nhs_scotland=df.iat[72,16]
    the_nhs_northern_ireland=df.iat[72,17]
    the_nhs_age_18_24=df.iat[72,19]
    the_nhs_age_25_34=df.iat[72,20]
    the_nhs_age_35_44=df.iat[72,21]
    the_nhs_age_45_54=df.iat[72,22]
    the_nhs_age_55_64=df.iat[72,23]


    unemployment_total_participants=df.iat[74,1]
    unemployment_male_participants=df.iat[74,3]
    unemployment_female_participants=df.iat[74,4]
    unemployment_north_east=df.iat[74,6]
    unemployment_north_west=df.iat[74,7]
    unemployment_yorkshire_the_humber=df.iat[74,8]
    unemployment_east_Midlands=df.iat[74,9]
    unemployment_west_midlands=df.iat[74,10]
    unemployment_east_of_england=df.iat[74,11]
    unemployment_london=df.iat[74,12]
    unemployment_south_east=df.iat[74,13]
    unemployment_south_west=df.iat[74,14]
    unemployment_wales=df.iat[74,15]
    unemployment_scotland=df.iat[74,16]
    unemployment_northern_ireland=df.iat[74,17]
    unemployment_age_18_24=df.iat[74,19]
    unemployment_age_25_34=df.iat[74,20]
    unemployment_age_35_44=df.iat[74,21]
    unemployment_age_45_54=df.iat[74,22]
    unemployment_age_55_64=df.iat[74,23]

    #Question 2
    question2=df.iat[77,0]
    total_participants_question2=df.iat[78,1]
    male_participants_question2=df.iat[78,3]
    female_participants_question2=df.iat[78,4]

    vegetarian_total_participants=df.iat[80,1]
    vegetarian_male_participants=df.iat[80,3]
    vegetarian_female_participants=df.iat[80,4]   
    vegetarian_north_east=df.iat[80,6]
    vegetarian_north_west=df.iat[80,7]
    vegetarian_yorkshire_the_humber=df.iat[80,8]
    vegetarian_east_Midlands=df.iat[80,9]
    vegetarian_west_midlands=df.iat[80,10]
    vegetarian_east_of_england=df.iat[80,11]
    vegetarian_london=df.iat[80,12]
    vegetarian_south_east=df.iat[80,13]
    vegetarian_south_west=df.iat[80,14]
    vegetarian_wales=df.iat[80,15]
    vegetarian_scotland=df.iat[80,16]
    vegetarian_northern_ireland=df.iat[80,17]
    vegetarian_age_18_24=df.iat[80,19]
    vegetarian_age_25_34=df.iat[80,20]
    vegetarian_age_35_44=df.iat[80,21]
    vegetarian_age_45_54=df.iat[80,22]
    vegetarian_age_55_64=df.iat[80,23]

    vegan_total_participants=df.iat[82,1]
    vegan_male_participants=df.iat[82,3]
    vegan_female_participants=df.iat[82,4]   
    vegan_north_east=df.iat[82,6]
    vegan_north_west=df.iat[82,7]
    vegan_yorkshire_the_humber=df.iat[82,8]
    vegan_east_Midlands=df.iat[82,9]
    vegan_west_midlands=df.iat[82,10]
    vegan_east_of_england=df.iat[82,11]
    vegan_london=df.iat[82,12]
    vegan_south_east=df.iat[82,13]
    vegan_south_west=df.iat[82,14]
    vegan_wales=df.iat[82,15]
    vegan_scotland=df.iat[82,16]
    vegan_northern_ireland=df.iat[82,17]
    vegan_age_18_24=df.iat[82,19]
    vegan_age_25_34=df.iat[82,20]
    vegan_age_35_44=df.iat[82,21]
    vegan_age_45_54=df.iat[82,22]
    vegan_age_55_64=df.iat[82,23]

    
    pescatarian_total_participants=df.iat[84,1]
    pescatarian_male_participants=df.iat[84,3]
    pescatarian_female_participants=df.iat[84,4]   
    pescatarian_north_east=df.iat[84,6]
    pescatarian_north_west=df.iat[84,7]
    pescatarian_yorkshire_the_humber=df.iat[84,8]
    pescatarian_east_Midlands=df.iat[84,9]
    pescatarian_west_midlands=df.iat[84,10]
    pescatarian_east_of_england=df.iat[84,11]
    pescatarian_london=df.iat[84,12]
    pescatarian_south_east=df.iat[84,13]
    pescatarian_south_west=df.iat[84,14]
    pescatarian_wales=df.iat[84,15]
    pescatarian_scotland=df.iat[84,16]
    pescatarian_northern_ireland=df.iat[84,17]
    pescatarian_age_18_24=df.iat[84,19]
    pescatarian_age_25_34=df.iat[84,20]
    pescatarian_age_35_44=df.iat[84,21]
    pescatarian_age_45_54=df.iat[84,22]
    pescatarian_age_55_64=df.iat[84,23]

    halal_total_participants=df.iat[86,1]
    halal_male_participants=df.iat[86,3]
    halal_female_participants=df.iat[86,4]   
    halal_north_east=df.iat[86,6]
    halal_north_west=df.iat[86,7]
    halal_yorkshire_the_humber=df.iat[86,8]
    halal_east_Midlands=df.iat[86,9]
    halal_west_midlands=df.iat[86,10]
    halal_east_of_england=df.iat[86,11]
    halal_london=df.iat[86,12]
    halal_south_east=df.iat[86,13]
    halal_south_west=df.iat[86,14]
    halal_wales=df.iat[86,15]
    halal_scotland=df.iat[86,16]
    halal_northern_ireland=df.iat[86,17]
    halal_age_18_24=df.iat[86,19]
    halal_age_25_34=df.iat[86,20]
    halal_age_35_44=df.iat[86,21]
    halal_age_45_54=df.iat[86,22]
    halal_age_55_64=df.iat[86,23]

    halal_chunk={
    'Question 2':question2,    
    'halal_total_participants': halal_total_participants,
    'halal_male_participants':halal_male_participants,
    'halal_female_participants':halal_female_participants,   
    'halal_north_east':halal_north_east,
    'halal_north_west':halal_north_west,
    'halal_yorkshire_the_humber':halal_yorkshire_the_humber,
    'halal_east_Midlands':halal_east_Midlands,
    'halal_west_midlands':halal_west_midlands,
    'halal_east_of_england':halal_east_of_england,
    'halal_london':halal_london,
    'halal_south_east':halal_south_east,
    'halal_south_west':halal_south_west,
    'halal_wales':halal_wales,
    'halal_scotland':halal_scotland,
    'halal_northern_ireland':halal_northern_ireland,
    'halal_age_18_24':halal_age_18_24,
    'halal_age_25_34':halal_age_25_34,
    'halal_age_35_44':halal_age_35_44,
    'halal_age_45_54':halal_age_45_54,
    'halal_age_55_64':halal_age_55_64,
}

    kosher_total_participants=df.iat[88,1]
    kosher_male_participants=df.iat[88,3]
    kosher_female_participants=df.iat[88,4]   
    kosher_north_east=df.iat[88,6]
    kosher_north_west=df.iat[88,7]
    kosher_yorkshire_the_humber=df.iat[88,8]
    kosher_east_Midlands=df.iat[88,9]
    kosher_west_midlands=df.iat[88,10]
    kosher_east_of_england=df.iat[88,11]
    kosher_london=df.iat[88,12]
    kosher_south_east=df.iat[88,13]
    kosher_south_west=df.iat[88,14]
    kosher_wales=df.iat[88,15]
    kosher_scotland=df.iat[88,16]
    kosher_northern_ireland=df.iat[88,17]
    kosher_age_18_24=df.iat[88,19]
    kosher_age_25_34=df.iat[88,20]
    kosher_age_35_44=df.iat[88,21]
    kosher_age_45_54=df.iat[88,22]
    kosher_age_55_64=df.iat[88,23]

    chunk_kosher={
    'Question 2':question2,
    'kosher_total_participants':kosher_total_participants,
    'kosher_male_participants':kosher_male_participants,
    'kosher_female_participants':    kosher_female_participants,
    'kosher_north_east':    kosher_north_east,
    'kosher_north_west':    kosher_north_west,
    'kosher_yorkshire_the_humber':    kosher_yorkshire_the_humber,
    'kosher_east_Midlands':    kosher_east_Midlands,
    'kosher_west_midlands':    kosher_west_midlands,
    'kosher_east_of_england':    kosher_east_of_england,
    'kosher_london':    kosher_london,
    'kosher_south_east':    kosher_south_east,
    'kosher_south_west':    kosher_south_west,
    'kosher_wales':    kosher_wales,
    'kosher_scotland':    kosher_scotland,
    'kosher_northern_ireland':    kosher_northern_ireland,
    'kosher_age_18_24':    kosher_age_18_24,
    'kosher_age_25_34':    kosher_age_25_34,
    'kosher_age_35_44':    kosher_age_35_44,
    'kosher_age_45_54':    kosher_age_45_54,
    'kosher_age_55_64':    kosher_age_55_64,

    }

    none_of_the_above_total_participants=df.iat[90,1]
    none_of_the_above_male_participants=df.iat[90,3]
    none_of_the_above_female_participants=df.iat[90,4]   
    none_of_the_above_north_east=df.iat[90,6]
    none_of_the_above_north_west=df.iat[90,7]
    none_of_the_above_yorkshire_the_humber=df.iat[90,8]
    none_of_the_above_east_Midlands=df.iat[90,9]
    none_of_the_above_west_midlands=df.iat[90,10]
    none_of_the_above_east_of_england=df.iat[90,11]
    none_of_the_above_london=df.iat[90,12]
    none_of_the_above_south_east=df.iat[90,13]
    none_of_the_above_south_west=df.iat[90,14]
    none_of_the_above_wales=df.iat[90,15]
    none_of_the_above_scotland=df.iat[90,16]
    none_of_the_above_northern_ireland=df.iat[90,17]
    none_of_the_above_age_18_24=df.iat[90,19]
    none_of_the_above_age_25_34=df.iat[90,20]
    none_of_the_above_age_35_44=df.iat[90,21]
    none_of_the_above_age_45_54=df.iat[90,22]
    none_of_the_above_age_55_64=df.iat[90,23]

    chunk_none_of_the_above={
    'Question 2':question2,
    'none_of_the_above_total_participants':    none_of_the_above_total_participants,
    'none_of_the_above_male_participants':    none_of_the_above_male_participants,
    'none_of_the_above_female_participants':    none_of_the_above_female_participants,
    'none_of_the_above_north_east':    none_of_the_above_north_east,
    'none_of_the_above_north_west':    none_of_the_above_north_west,
    'none_of_the_above_yorkshire_the_humber':    none_of_the_above_yorkshire_the_humber,
    'none_of_the_above_east_Midlands':    none_of_the_above_east_Midlands,
    'none_of_the_above_west_midlands':    none_of_the_above_west_midlands,
    'none_of_the_above_east_of_england':    none_of_the_above_east_of_england,
    'none_of_the_above_london':    none_of_the_above_london,
    'none_of_the_above_south_east':    none_of_the_above_south_east,
    'none_of_the_above_south_west':    none_of_the_above_south_west,
    'none_of_the_above_wales':    none_of_the_above_wales,
    'none_of_the_above_scotland':    none_of_the_above_scotland,
    'none_of_the_above_northern_ireland':    none_of_the_above_northern_ireland,
    'none_of_the_above_age_18_24':    none_of_the_above_age_18_24,
    'none_of_the_above_age_25_34':    none_of_the_above_age_25_34,
    'none_of_the_above_age_35_44':    none_of_the_above_age_35_44,
    'none_of_the_above_age_45_54':    none_of_the_above_age_45_54,
    'none_of_the_above_age_55_64':    none_of_the_above_age_55_64,

    }

    # Question 3

    question3=df.iat[93,0]
    total_participants_question3=df.iat[94,1]
    male_participants_question3=df.iat[94,3]
    female_participants_question3=df.iat[94,4]

    always_total_participants=df.iat[96,1]
    always_male_participants=df.iat[96,3]
    always_female_participants=df.iat[96,4]   
    always_north_east=df.iat[96,6]
    always_north_west=df.iat[96,7]
    always_yorkshire_the_humber=df.iat[96,8]
    always_east_Midlands=df.iat[96,9]
    always_west_midlands=df.iat[96,10]
    always_east_of_england=df.iat[96,11]
    always_london=df.iat[96,12]
    always_south_east=df.iat[96,13]
    always_south_west=df.iat[96,14]
    always_wales=df.iat[96,15]
    always_scotland=df.iat[96,16]
    always_northern_ireland=df.iat[96,17]
    always_age_18_24=df.iat[96,19]
    always_age_25_34=df.iat[96,20]
    always_age_35_44=df.iat[96,21]
    always_age_45_54=df.iat[96,22]
    always_age_55_64=df.iat[96,23]


    sometimes_total_participants=df.iat[100,1]
    sometimes_male_participants=df.iat[100,3]
    sometimes_female_participants=df.iat[100,4]   
    sometimes_north_east=df.iat[100,6]
    sometimes_north_west=df.iat[100,7]
    sometimes_yorkshire_the_humber=df.iat[100,8]
    sometimes_yorkshire_the_humber=df.iat[100,8]
    sometimes_east_Midlands=df.iat[100,9]
    sometimes_west_midlands=df.iat[100,10]
    sometimes_west_midlands=df.iat[100,10]
    sometimes_east_of_england=df.iat[100,11]
    sometimes_london=df.iat[100,12]
    sometimes_south_east=df.iat[100,13]
    sometimes_south_west=df.iat[100,14]
    sometimes_wales=df.iat[100,15]
    sometimes_scotland=df.iat[100,16]
    sometimes_northern_ireland=df.iat[100,17]
    sometimes_age_18_24=df.iat[100,19]
    sometimes_age_25_34=df.iat[100,20]
    sometimes_age_35_44=df.iat[100,21]
    sometimes_age_45_54=df.iat[100,22]
    sometimes_age_55_64=df.iat[100,23]


    rarely_total_participants=df.iat[102,1]
    rarely_male_participants=df.iat[102,3]
    rarely_female_participants=df.iat[102,4]   
    rarely_north_east=df.iat[102,6]
    rarely_north_west=df.iat[102,7]
    rarely_yorkshire_the_humber=df.iat[102,8]
    rarely_yorkshire_the_humber=df.iat[102,8]
    rarely_east_Midlands=df.iat[102,9]
    rarely_west_midlands=df.iat[102,10]
    rarely_west_midlands=df.iat[102,10]
    rarely_east_of_england=df.iat[102,11]
    rarely_london=df.iat[102,12]
    rarely_south_east=df.iat[102,13]
    rarely_south_west=df.iat[102,14]
    rarely_wales=df.iat[102,15]
    rarely_scotland=df.iat[102,16]
    rarely_northern_ireland=df.iat[102,17]
    rarely_age_18_24=df.iat[102,19]
    rarely_age_25_34=df.iat[102,20]
    rarely_age_35_44=df.iat[102,21]
    rarely_age_45_54=df.iat[102,22]
    rarely_age_55_64=df.iat[102,23]


    
    never_total_participants=df.iat[104,1]
    never_male_participants=df.iat[104,3]
    never_female_participants=df.iat[104,4]   
    never_north_east=df.iat[104,6]
    never_north_west=df.iat[104,7]
    never_yorkshire_the_humber=df.iat[104,8]
    never_yorkshire_the_humber=df.iat[104,8]
    never_east_Midlands=df.iat[104,9]
    never_west_midlands=df.iat[104,10]
    never_west_midlands=df.iat[104,10]
    never_east_of_england=df.iat[104,11]
    never_london=df.iat[104,12]
    never_south_east=df.iat[104,13]
    never_south_west=df.iat[104,14]
    never_wales=df.iat[104,15]
    never_scotland=df.iat[104,16]
    never_northern_ireland=df.iat[104,17]
    never_age_18_24=df.iat[104,19]
    never_age_25_34=df.iat[104,20]
    never_age_35_44=df.iat[104,21]
    never_age_45_54=df.iat[104,22]
    never_age_55_64=df.iat[104,23]



    # Question 4
    question4=df.iat[107,0]
    total_participants_question4=df.iat[108,1]
    male_participants_question4=df.iat[108,3]
    female_participants_question4=df.iat[108,4]

    very_important_total_participants=df.iat[110,1]
    very_important_male_participants=df.iat[110,3]
    very_important_female_participants=df.iat[110,4]   
    very_important_north_east=df.iat[110,6]
    very_important_north_west=df.iat[110,7]
    very_important_yorkshire_the_humber=df.iat[110,8]
    very_important_east_Midlands=df.iat[110,9]
    very_important_west_midlands=df.iat[110,10]
    very_important_east_of_england=df.iat[110,11]
    very_important_london=df.iat[110,12]
    very_important_south_east=df.iat[110,13]
    very_important_south_west=df.iat[110,14]
    very_important_wales=df.iat[110,15]
    very_important_scotland=df.iat[110,16]
    very_important_northern_ireland=df.iat[110,17]
    very_important_age_18_24=df.iat[110,19]
    very_important_age_25_34=df.iat[110,20]
    very_important_age_35_44=df.iat[110,21]
    very_important_age_45_54=df.iat[110,22]
    very_important_age_55_64=df.iat[110,23]

    fairly_important_total_participants=df.iat[112,1]
    fairly_important_male_participants=df.iat[112,3]
    fairly_important_female_participants=df.iat[112,4]   
    fairly_important_north_east=df.iat[112,6]
    fairly_important_north_west=df.iat[112,7]
    fairly_important_yorkshire_the_humber=df.iat[112,8]
    fairly_important_east_Midlands=df.iat[112,9]
    fairly_important_west_midlands=df.iat[112,10]
    fairly_important_east_of_england=df.iat[112,11]
    fairly_important_london=df.iat[112,12]
    fairly_important_south_east=df.iat[112,13]
    fairly_important_south_west=df.iat[112,14]
    fairly_important_wales=df.iat[112,15]
    fairly_important_scotland=df.iat[112,16]
    fairly_important_northern_ireland=df.iat[112,17]
    fairly_important_age_18_24=df.iat[112,19]
    fairly_important_age_25_34=df.iat[112,20]
    fairly_important_age_35_44=df.iat[112,21]
    fairly_important_age_45_54=df.iat[112,22]
    fairly_important_age_55_64=df.iat[112,23]

    neither_total_participants=df.iat[114,1]
    neither_important_male_participants=df.iat[114,3]
    neither_important_female_participants=df.iat[114,4]   
    neither_important_north_east=df.iat[114,6]
    neither_important_north_west=df.iat[114,7]
    neither_important_yorkshire_the_humber=df.iat[114,8]
    neither_important_east_Midlands=df.iat[114,9]
    neither_important_west_midlands=df.iat[114,10]
    neither_important_east_of_england=df.iat[114,11]
    neither_important_london=df.iat[114,12]
    neither_important_south_east=df.iat[114,13]
    neither_important_south_west=df.iat[114,14]
    neither_important_wales=df.iat[114,15]
    neither_important_scotland=df.iat[114,16]
    neither_important_northern_ireland=df.iat[114,17]
    neither_important_age_18_24=df.iat[114,19]
    neither_important_age_25_34=df.iat[114,20]
    neither_important_age_35_44=df.iat[114,21]
    neither_important_age_45_54=df.iat[114,22]
    neither_important_age_55_64=df.iat[114,23]

    fairly_unimportant_total_participants=df.iat[116,1]
    fairly_unimportant_male_participants=df.iat[116,3]
    fairly_unimportant_female_participants=df.iat[116,4]   
    fairly_unimportant_north_east=df.iat[116,6]
    fairly_unimportant_north_west=df.iat[116,7]
    fairly_unimportant_yorkshire_the_humber=df.iat[116,8]
    fairly_unimportant_east_Midlands=df.iat[116,9]
    fairly_unimportant_west_midlands=df.iat[116,10]
    fairly_unimportant_east_of_england=df.iat[116,11]
    fairly_unimportant_london=df.iat[116,12]
    fairly_unimportant_south_east=df.iat[116,13]
    fairly_unimportant_south_west=df.iat[116,14]
    fairly_unimportant_wales=df.iat[116,15]
    fairly_unimportant_scotland=df.iat[116,16]
    fairly_unimportant_northern_ireland=df.iat[116,17]
    fairly_unimportant_age_18_24=df.iat[116,19]
    fairly_unimportant_age_25_34=df.iat[116,20]
    fairly_unimportant_age_35_44=df.iat[116,21]
    fairly_unimportant_age_45_54=df.iat[116,22]
    fairly_unimportant_age_55_64=df.iat[116,23]

    very_unimportant_total_participants=df.iat[118,1]
    very_unimportant_male_participants=df.iat[118,3]
    very_unimportant_female_participants=df.iat[118,4]   
    very_unimportant_north_east=df.iat[118,6]
    very_unimportant_north_west=df.iat[118,7]
    very_unimportant_yorkshire_the_humber=df.iat[118,8]
    very_unimportant_east_Midlands=df.iat[118,9]
    very_unimportant_west_midlands=df.iat[118,10]
    very_unimportant_east_of_england=df.iat[118,11]
    very_unimportant_london=df.iat[118,12]
    very_unimportant_south_east=df.iat[118,13]
    very_unimportant_south_west=df.iat[118,14]
    very_unimportant_wales=df.iat[118,15]
    very_unimportant_scotland=df.iat[118,16]
    very_unimportant_northern_ireland=df.iat[118,17]
    very_unimportant_age_18_24=df.iat[118,19]
    very_unimportant_age_25_34=df.iat[118,20]
    very_unimportant_age_35_44=df.iat[118,21]
    very_unimportant_age_45_54=df.iat[118,22]
    very_unimportant_age_55_64=df.iat[118,23]

    #Question 5

    question5=df.iat[121,0]
    total_participants_question5=df.iat[122,1]
    male_participants_question5=df.iat[122,3]
    female_participants_question5=df.iat[122,4]

    environmentally_friendly_total_participants=df.iat[124,1]
    environmentally_friendly_male_participants=df.iat[124,3]
    environmentally_friendly_female_participants=df.iat[124,4]   
    environmentally_friendly_north_east=df.iat[124,6]
    environmentally_friendly_north_west=df.iat[124,7]
    environmentally_friendly_yorkshire_the_humber=df.iat[124,8]
    environmentally_friendly_east_Midlands=df.iat[124,9]
    environmentally_friendly_west_midlands=df.iat[124,10]
    environmentally_friendly_east_of_england=df.iat[124,11]
    environmentally_friendly_london=df.iat[124,12]
    environmentally_friendly_south_east=df.iat[124,13]
    environmentally_friendly_south_west=df.iat[124,14]
    environmentally_friendly_wales=df.iat[124,15]
    environmentally_friendly_scotland=df.iat[124,16]
    environmentally_friendly_northern_ireland=df.iat[124,17]
    environmentally_friendly_age_18_24=df.iat[124,19]
    environmentally_friendly_age_25_34=df.iat[124,20]
    environmentally_friendly_age_35_44=df.iat[124,21]
    environmentally_friendly_age_45_54=df.iat[124,22]
    environmentally_friendly_age_55_64=df.iat[124,23]


    good_for_the_planet_total_participants=df.iat[126,1]
    good_for_the_planet_male_participants=df.iat[126,3]
    good_for_the_planet_female_participants=df.iat[126,4]   
    good_for_the_planet_north_east=df.iat[126,6]
    good_for_the_planet_north_west=df.iat[126,7]
    good_for_the_planet_yorkshire_the_humber=df.iat[126,8]
    good_for_the_planet_east_Midlands=df.iat[126,9]
    good_for_the_planet_west_midlands=df.iat[126,10]
    good_for_the_planet_east_of_england=df.iat[126,11]
    good_for_the_planet_london=df.iat[126,12]
    good_for_the_planet_south_east=df.iat[126,13]
    good_for_the_planet_south_west=df.iat[126,14]
    good_for_the_planet_wales=df.iat[126,15]
    good_for_the_planet_scotland=df.iat[126,16]
    good_for_the_planet_northern_ireland=df.iat[126,17]
    good_for_the_planet_age_18_24=df.iat[126,19]
    good_for_the_planet_age_25_34=df.iat[126,20]
    good_for_the_planet_age_35_44=df.iat[126,21]
    good_for_the_planet_age_45_54=df.iat[126,22]
    good_for_the_planet_age_55_64=df.iat[126,23]

    less_waste_total_participants=df.iat[128,1]
    less_waste_male_participants=df.iat[128,3]
    less_waste_female_participants=df.iat[128,4]   
    less_waste_north_east=df.iat[128,6]
    less_waste_north_west=df.iat[128,7]
    less_waste_yorkshire_the_humber=df.iat[128,8]
    less_waste_east_Midlands=df.iat[128,9]
    less_waste_west_midlands=df.iat[128,10]
    less_waste_east_of_england=df.iat[128,11]
    less_waste_london=df.iat[128,12]
    less_waste_south_east=df.iat[128,13]
    less_waste_south_west=df.iat[128,14]
    less_waste_wales=df.iat[128,15]
    less_waste_scotland=df.iat[128,16]
    less_waste_northern_ireland=df.iat[128,17]
    less_waste_age_18_24=df.iat[128,19]
    less_waste_age_25_34=df.iat[128,20]
    less_waste_age_35_44=df.iat[128,21]
    less_waste_age_45_54=df.iat[128,22]
    less_waste_age_55_64=df.iat[128,23]


    local_total_participants=df.iat[130,1]
    local_male_participants=df.iat[130,3]
    local_female_participants=df.iat[130,4]   
    local_north_east=df.iat[130,6]
    local_north_west=df.iat[130,7]
    local_yorkshire_the_humber=df.iat[130,8]
    local_east_Midlands=df.iat[130,9]
    local_west_midlands=df.iat[130,10]
    local_east_of_england=df.iat[130,11]
    local_london=df.iat[130,12]
    local_south_east=df.iat[130,13]
    local_south_west=df.iat[130,14]
    local_wales=df.iat[130,15]
    local_scotland=df.iat[130,16]
    local_northern_ireland=df.iat[130,17]
    local_age_18_24=df.iat[130,19]
    local_age_25_34=df.iat[130,20]
    local_age_35_44=df.iat[130,21]
    local_age_45_54=df.iat[130,22]
    local_age_55_64=df.iat[130,23]

    
    ethical_total_participants=df.iat[132,1]
    ethical_male_participants=df.iat[132,3]
    ethical_female_participants=df.iat[132,4]   
    ethical_north_east=df.iat[132,6]
    ethical_north_west=df.iat[132,7]
    ethical_yorkshire_the_humber=df.iat[132,8]
    ethical_east_Midlands=df.iat[132,9]
    ethical_west_midlands=df.iat[132,10]
    ethical_east_of_england=df.iat[132,11]
    ethical_london=df.iat[132,12]
    ethical_south_east=df.iat[132,13]
    ethical_south_west=df.iat[132,14]
    ethical_wales=df.iat[132,15]
    ethical_scotland=df.iat[132,16]
    ethical_northern_ireland=df.iat[132,17]
    ethical_age_18_24=df.iat[132,19]
    ethical_age_25_34=df.iat[132,20]
    ethical_age_35_44=df.iat[132,21]
    ethical_age_45_54=df.iat[132,22]
    ethical_age_55_64=df.iat[132,23]

    dont_know_total_participants=df.iat[134,1]
    dont_know_male_participants=df.iat[134,3]
    dont_know_female_participants=df.iat[134,4]   
    dont_know_north_east=df.iat[134,6]
    dont_know_north_west=df.iat[134,7]
    dont_know_yorkshire_the_humber=df.iat[134,8]
    dont_know_east_Midlands=df.iat[134,9]
    dont_know_west_midlands=df.iat[134,10]
    dont_know_east_of_england=df.iat[134,11]
    dont_know_london=df.iat[134,12]
    dont_know_south_east=df.iat[134,13]
    dont_know_south_west=df.iat[134,14]
    dont_know_wales=df.iat[134,15]
    dont_know_scotland=df.iat[134,16]
    dont_know_northern_ireland=df.iat[134,17]
    dont_know_age_18_24=df.iat[134,19]
    dont_know_age_25_34=df.iat[134,20]
    dont_know_age_35_44=df.iat[134,21]
    dont_know_age_45_54=df.iat[134,22]
    dont_know_age_55_64=df.iat[134,23]

    longer_lasting_total_participants=df.iat[136,1]
    longer_lasting_male_participants=df.iat[136,3]
    longer_lasting_female_participants=df.iat[136,4]   
    longer_lasting_north_east=df.iat[136,6]
    longer_lasting_north_west=df.iat[136,7]
    longer_lasting_yorkshire_the_humber=df.iat[136,8]
    longer_lasting_east_Midlands=df.iat[136,9]
    longer_lasting_west_midlands=df.iat[136,10]
    longer_lasting_east_of_england=df.iat[136,11]
    longer_lasting_london=df.iat[136,12]
    longer_lasting_south_east=df.iat[136,13]
    longer_lasting_south_west=df.iat[136,14]
    longer_lasting_wales=df.iat[136,15]
    longer_lasting_scotland=df.iat[136,16]
    longer_lasting_northern_ireland=df.iat[136,17]
    longer_lasting_age_18_24=df.iat[136,19]
    longer_lasting_age_25_34=df.iat[136,20]
    longer_lasting_age_35_44=df.iat[136,21]
    longer_lasting_age_45_54=df.iat[136,22]
    longer_lasting_age_55_64=df.iat[136,23]

    no_natural_resource_depletion_total_participants=df.iat[138,1]
    no_natural_resource_depletion_male_participants=df.iat[138,3]
    no_natural_resource_depletion_female_participants=df.iat[138,4]   
    no_natural_resource_depletion_north_east=df.iat[138,6]
    no_natural_resource_depletion_north_west=df.iat[138,7]
    no_natural_resource_depletion_yorkshire_the_humber=df.iat[138,8]
    no_natural_resource_depletion_east_Midlands=df.iat[138,9]
    no_natural_resource_depletion_west_midlands=df.iat[138,10]
    no_natural_resource_depletion_east_of_england=df.iat[138,11]
    no_natural_resource_depletion_london=df.iat[138,12]
    no_natural_resource_depletion_south_east=df.iat[138,13]
    no_natural_resource_depletion_south_west=df.iat[138,14]
    no_natural_resource_depletion_wales=df.iat[138,15]
    no_natural_resource_depletion_scotland=df.iat[138,16]
    no_natural_resource_depletion_northern_ireland=df.iat[138,17]
    no_natural_resource_depletion_age_18_24=df.iat[138,19]
    no_natural_resource_depletion_age_25_34=df.iat[138,20]
    no_natural_resource_depletion_age_35_44=df.iat[138,21]
    no_natural_resource_depletion_age_45_54=df.iat[138,22]
    no_natural_resource_depletion_age_55_64=df.iat[138,23]


    recyclable_total_participants=df.iat[140,1]
    recyclable_male_participants=df.iat[140,3]
    recyclable_female_participants=df.iat[140,4]   
    recyclable_north_east=df.iat[140,6]
    recyclable_north_west=df.iat[140,7]
    recyclable_yorkshire_the_humber=df.iat[140,8]
    recyclable_east_Midlands=df.iat[140,9]
    recyclable_west_midlands=df.iat[140,10]
    recyclable_east_of_england=df.iat[140,11]
    recyclable_london=df.iat[140,12]
    recyclable_south_east=df.iat[140,13]
    recyclable_south_west=df.iat[140,14]
    recyclable_wales=df.iat[140,15]
    recyclable_scotland=df.iat[140,16]
    recyclable_northern_ireland=df.iat[140,17]
    recyclable_age_18_24=df.iat[140,19]
    recyclable_age_25_34=df.iat[140,20]
    recyclable_age_35_44=df.iat[140,21]
    recyclable_age_45_54=df.iat[140,22]
    recyclable_age_55_64=df.iat[140,23]

    locally_sourced_total_participants=df.iat[142,1]
    locally_sourced_male_participants=df.iat[142,3]
    locally_sourced_female_participants=df.iat[142,4]   
    locally_sourced_north_east=df.iat[142,6]
    locally_sourced_north_west=df.iat[142,7]
    locally_sourced_yorkshire_the_humber=df.iat[142,8]
    locally_sourced_east_Midlands=df.iat[142,9]
    locally_sourced_west_midlands=df.iat[142,10]
    locally_sourced_east_of_england=df.iat[142,11]
    locally_sourced_london=df.iat[142,12]
    locally_sourced_south_east=df.iat[142,13]
    locally_sourced_south_west=df.iat[142,14]
    locally_sourced_wales=df.iat[142,15]
    locally_sourced_scotland=df.iat[142,16]
    locally_sourced_northern_ireland=df.iat[142,17]
    locally_sourced_age_18_24=df.iat[142,19]
    locally_sourced_age_25_34=df.iat[142,20]
    locally_sourced_age_35_44=df.iat[142,21]
    locally_sourced_age_45_54=df.iat[142,22]
    locally_sourced_age_55_64=df.iat[142,23]

    
    zero_carbon_total_participants=df.iat[144,1]
    zero_carbon_male_participants=df.iat[144,3]
    zero_carbon_female_participants=df.iat[144,4]   
    zero_carbon_north_east=df.iat[144,6]
    zero_carbon_north_west=df.iat[144,7]
    zero_carbon_yorkshire_the_humber=df.iat[144,8]
    zero_carbon_east_Midlands=df.iat[144,9]
    zero_carbon_west_midlands=df.iat[144,10]
    zero_carbon_east_of_england=df.iat[144,11]
    zero_carbon_london=df.iat[144,12]
    zero_carbon_south_east=df.iat[144,13]
    zero_carbon_south_west=df.iat[144,14]
    zero_carbon_wales=df.iat[144,15]
    zero_carbon_scotland=df.iat[144,16]
    zero_carbon_northern_ireland=df.iat[144,17]
    zero_carbon_age_18_24=df.iat[144,19]
    zero_carbon_age_25_34=df.iat[144,20]
    zero_carbon_age_35_44=df.iat[144,21]
    zero_carbon_age_45_54=df.iat[144,22]
    zero_carbon_age_55_64=df.iat[144,23]


    
    reuse_or_repurpose_total_participants=df.iat[146,1]
    reuse_or_repurpose_male_participants=df.iat[146,3]
    reuse_or_repurpose_female_participants=df.iat[146,4]   
    reuse_or_repurpose_north_east=df.iat[146,6]
    reuse_or_repurpose_north_west=df.iat[146,7]
    reuse_or_repurpose_yorkshire_the_humber=df.iat[146,8]
    reuse_or_repurpose_east_Midlands=df.iat[146,9]
    reuse_or_repurpose_west_midlands=df.iat[146,10]
    reuse_or_repurpose_east_of_england=df.iat[146,11]
    reuse_or_repurpose_london=df.iat[146,12]
    reuse_or_repurpose_south_east=df.iat[146,13]
    reuse_or_repurpose_south_west=df.iat[146,14]
    reuse_or_repurpose_wales=df.iat[146,15]
    reuse_or_repurpose_scotland=df.iat[146,16]
    reuse_or_repurpose_northern_ireland=df.iat[146,17]
    reuse_or_repurpose_age_18_24=df.iat[146,19]
    reuse_or_repurpose_age_25_34=df.iat[146,20]
    reuse_or_repurpose_age_35_44=df.iat[146,21]
    reuse_or_repurpose_age_45_54=df.iat[146,22]
    reuse_or_repurpose_age_55_64=df.iat[146,23]
    

    no_group_total_participants=df.iat[148,1]
    no_group_male_participants=df.iat[148,3]
    no_group_female_participants=df.iat[148,4]   
    no_group_north_east=df.iat[148,6]
    no_group_north_west=df.iat[148,7]
    no_group_yorkshire_the_humber=df.iat[148,8]
    no_group_east_Midlands=df.iat[148,9]
    no_group_west_midlands=df.iat[148,10]
    no_group_east_of_england=df.iat[148,11]
    no_group_london=df.iat[148,12]
    no_group_south_east=df.iat[148,13]
    no_group_south_west=df.iat[148,14]
    no_group_wales=df.iat[148,15]
    no_group_scotland=df.iat[148,16]
    no_group_northern_ireland=df.iat[148,17]
    no_group_age_18_24=df.iat[148,19]
    no_group_age_25_34=df.iat[148,20]
    no_group_age_35_44=df.iat[148,21]
    no_group_age_45_54=df.iat[148,22]
    no_group_age_55_64=df.iat[148,23]

    #region Question 6
    question6=df.iat[151,0]
    total_participants_question6=df.iat[152,1]
    male_participants_question6=df.iat[152,3]
    female_participants_question6=df.iat[152,4]
    
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_total_participants=df.iat[154,1]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_male_participants=df.iat[154,3]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_female_participants=df.iat[154,4]   
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_north_east=df.iat[154,6]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_north_west=df.iat[154,7]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_yorkshire_the_humber=df.iat[154,8]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_east_Midlands=df.iat[154,9]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_west_midlands=df.iat[154,10]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_east_of_england=df.iat[154,11]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_london=df.iat[154,12]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_south_east=df.iat[154,13]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_south_west=df.iat[154,14]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_wales=df.iat[154,15]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_scotland=df.iat[154,16]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_northern_ireland=df.iat[154,17]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_age_18_24=df.iat[154,19]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_age_25_34=df.iat[154,20]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_age_35_44=df.iat[154,21]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_age_45_54=df.iat[154,22]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_always_age_55_64=df.iat[154,23]


    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_total_participants=df.iat[156,1]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_male_participants=df.iat[156,3]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_female_participants=df.iat[156,4]   
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_north_east=df.iat[156,6]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_north_west=df.iat[156,7]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_yorkshire_the_humber=df.iat[156,8]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_east_Midlands=df.iat[156,9]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_west_midlands=df.iat[156,10]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_east_of_england=df.iat[156,11]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_london=df.iat[156,12]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_south_east=df.iat[156,13]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_south_west=df.iat[156,14]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_wales=df.iat[156,15]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_scotland=df.iat[156,16]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_northern_ireland=df.iat[156,17]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_age_18_24=df.iat[156,19]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_age_25_34=df.iat[156,20]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_age_35_44=df.iat[156,21]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_age_45_54=df.iat[156,22]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_often_age_55_64=df.iat[156,23]


    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_total_participants=df.iat[158,1]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_male_participants=df.iat[158,3]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_female_participants=df.iat[158,4]   
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_north_east=df.iat[158,6]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_north_west=df.iat[158,7]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_yorkshire_the_humber=df.iat[158,8]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_east_Midlands=df.iat[158,9]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_west_midlands=df.iat[158,10]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_east_of_england=df.iat[158,11]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_london=df.iat[158,12]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_south_east=df.iat[158,13]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_south_west=df.iat[158,14]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_wales=df.iat[158,15]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_scotland=df.iat[158,16]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_northern_ireland=df.iat[158,17]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_age_18_24=df.iat[158,19]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_age_25_34=df.iat[158,20]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_age_35_44=df.iat[158,21]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_age_45_54=df.iat[158,22]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_rarely_age_55_64=df.iat[158,23]
	

    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_total_participants=df.iat[160,1]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_male_participants=df.iat[160,3]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_female_participants=df.iat[160,4]   
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_north_east=df.iat[160,6]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_north_west=df.iat[160,7]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_yorkshire_the_humber=df.iat[160,8]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_east_Midlands=df.iat[160,9]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_west_midlands=df.iat[160,10]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_east_of_england=df.iat[160,11]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_london=df.iat[160,12]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_south_east=df.iat[160,13]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_south_west=df.iat[160,14]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_wales=df.iat[160,15]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_scotland=df.iat[160,16]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_northern_ireland=df.iat[160,17]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_age_18_24=df.iat[160,19]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_age_25_34=df.iat[160,20]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_age_35_44=df.iat[160,21]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_age_45_54=df.iat[160,22]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_sometimes_age_55_64=df.iat[160,23]

    
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_total_participants=df.iat[162,1]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_male_participants=df.iat[162,3]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_female_participants=df.iat[162,4]   
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_north_east=df.iat[162,6]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_north_west=df.iat[162,7]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_yorkshire_the_humber=df.iat[162,8]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_east_Midlands=df.iat[162,9]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_west_midlands=df.iat[162,10]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_east_of_england=df.iat[162,11]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_london=df.iat[162,12]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_south_east=df.iat[162,13]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_south_west=df.iat[162,14]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_wales=df.iat[162,15]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_scotland=df.iat[162,16]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_northern_ireland=df.iat[162,17]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_age_18_24=df.iat[162,19]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_age_25_34=df.iat[162,20]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_age_35_44=df.iat[162,21]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_age_45_54=df.iat[162,22]
    check_if_products_are_made_from_recyclable_or_biodegradable_materials_never_age_55_64=df.iat[162,23]

    
    limit_my_use_of_single_use_plastics_always_total_participants=df.iat[164,1]
    limit_my_use_of_single_use_plastics_always_male_participants=df.iat[164,3]
    limit_my_use_of_single_use_plastics_always_female_participants=df.iat[164,4]   
    limit_my_use_of_single_use_plastics_always_north_east=df.iat[164,6]
    limit_my_use_of_single_use_plastics_always_north_west=df.iat[164,7]
    limit_my_use_of_single_use_plastics_always_yorkshire_the_humber=df.iat[164,8]
    limit_my_use_of_single_use_plastics_always_east_Midlands=df.iat[164,9]
    limit_my_use_of_single_use_plastics_always_west_midlands=df.iat[164,10]
    limit_my_use_of_single_use_plastics_always_east_of_england=df.iat[164,11]
    limit_my_use_of_single_use_plastics_always_london=df.iat[164,12]
    limit_my_use_of_single_use_plastics_always_south_east=df.iat[164,13]
    limit_my_use_of_single_use_plastics_always_south_west=df.iat[164,14]
    limit_my_use_of_single_use_plastics_always_wales=df.iat[164,15]
    limit_my_use_of_single_use_plastics_always_scotland=df.iat[164,16]
    limit_my_use_of_single_use_plastics_always_northern_ireland=df.iat[164,17]
    limit_my_use_of_single_use_plastics_always_age_18_24=df.iat[164,19]
    limit_my_use_of_single_use_plastics_always_age_25_34=df.iat[164,20]
    limit_my_use_of_single_use_plastics_always_age_35_44=df.iat[164,21]
    limit_my_use_of_single_use_plastics_always_age_45_54=df.iat[164,22]
    limit_my_use_of_single_use_plastics_always_age_55_64=df.iat[164,23]


    
    
    limit_my_use_of_single_use_plastics_often_always_total_participants=df.iat[166,1]
    limit_my_use_of_single_use_plastics_often_male_participants=df.iat[166,3]
    limit_my_use_of_single_use_plastics_often_female_participants=df.iat[166,4]   
    limit_my_use_of_single_use_plastics_often_north_east=df.iat[166,6]
    limit_my_use_of_single_use_plastics_often_north_west=df.iat[166,7]
    limit_my_use_of_single_use_plastics_often_yorkshire_the_humber=df.iat[166,8]
    limit_my_use_of_single_use_plastics_often_east_Midlands=df.iat[166,9]
    limit_my_use_of_single_use_plastics_often_west_midlands=df.iat[166,10]
    limit_my_use_of_single_use_plastics_often_east_of_england=df.iat[166,11]
    limit_my_use_of_single_use_plastics_often_london=df.iat[166,12]
    limit_my_use_of_single_use_plastics_often_south_east=df.iat[166,13]
    limit_my_use_of_single_use_plastics_often_south_west=df.iat[166,14]
    limit_my_use_of_single_use_plastics_often_wales=df.iat[166,15]
    limit_my_use_of_single_use_plastics_often_scotland=df.iat[166,16]
    limit_my_use_of_single_use_plastics_often_northern_ireland=df.iat[166,17]
    limit_my_use_of_single_use_plastics_often_age_18_24=df.iat[166,19]
    limit_my_use_of_single_use_plastics_often_age_25_34=df.iat[166,20]
    limit_my_use_of_single_use_plastics_often_age_35_44=df.iat[166,21]
    limit_my_use_of_single_use_plastics_often_age_45_54=df.iat[166,22]
    limit_my_use_of_single_use_plastics_often_age_55_64=df.iat[166,23]
    
    
    
    limit_my_use_of_single_use_plastics_rarely_total_participants=df.iat[168,1]
    limit_my_use_of_single_use_plastics_rarely_male_participants=df.iat[168,3]
    limit_my_use_of_single_use_plastics_rarely_female_participants=df.iat[168,4]   
    limit_my_use_of_single_use_plastics_rarely_north_east=df.iat[168,6]
    limit_my_use_of_single_use_plastics_rarely_north_west=df.iat[168,7]
    limit_my_use_of_single_use_plastics_rarely_yorkshire_the_humber=df.iat[168,8]
    limit_my_use_of_single_use_plastics_rarely_east_Midlands=df.iat[168,9]
    limit_my_use_of_single_use_plastics_rarely_west_midlands=df.iat[168,10]
    limit_my_use_of_single_use_plastics_rarely_east_of_england=df.iat[168,11]
    limit_my_use_of_single_use_plastics_rarely_london=df.iat[168,12]
    limit_my_use_of_single_use_plastics_rarely_south_east=df.iat[168,13]
    limit_my_use_of_single_use_plastics_rarely_south_west=df.iat[168,14]
    limit_my_use_of_single_use_plastics_rarely_wales=df.iat[168,15]
    limit_my_use_of_single_use_plastics_rarely_scotland=df.iat[168,16]
    limit_my_use_of_single_use_plastics_rarely_northern_ireland=df.iat[168,17]
    limit_my_use_of_single_use_plastics_rarely_age_18_24=df.iat[168,19]
    limit_my_use_of_single_use_plastics_rarely_age_25_34=df.iat[168,20]
    limit_my_use_of_single_use_plastics_rarely_age_35_44=df.iat[168,21]
    limit_my_use_of_single_use_plastics_rarely_age_45_54=df.iat[168,22]
    limit_my_use_of_single_use_plastics_rarely_age_55_64=df.iat[168,23]


    
    limit_my_use_of_single_use_plastics_sometimes_total_participants=df.iat[170,1]
    limit_my_use_of_single_use_plastics_sometimes_male_participants=df.iat[170,3]
    limit_my_use_of_single_use_plastics_sometimes_female_participants=df.iat[170,4]   
    limit_my_use_of_single_use_plastics_sometimes_north_east=df.iat[170,6]
    limit_my_use_of_single_use_plastics_sometimes_north_west=df.iat[170,7]
    limit_my_use_of_single_use_plastics_sometimes_yorkshire_the_humber=df.iat[170,8]
    limit_my_use_of_single_use_plastics_sometimes_east_Midlands=df.iat[170,9]
    limit_my_use_of_single_use_plastics_sometimes_west_midlands=df.iat[170,10]
    limit_my_use_of_single_use_plastics_sometimes_east_of_england=df.iat[170,11]
    limit_my_use_of_single_use_plastics_sometimes_london=df.iat[170,12]
    limit_my_use_of_single_use_plastics_sometimes_south_east=df.iat[170,13]
    limit_my_use_of_single_use_plastics_sometimes_south_west=df.iat[170,14]
    limit_my_use_of_single_use_plastics_sometimes_wales=df.iat[170,15]
    limit_my_use_of_single_use_plastics_sometimes_scotland=df.iat[170,16]
    limit_my_use_of_single_use_plastics_sometimes_northern_ireland=df.iat[170,17]
    limit_my_use_of_single_use_plastics_sometimes_age_18_24=df.iat[170,19]
    limit_my_use_of_single_use_plastics_sometimes_age_25_34=df.iat[170,20]
    limit_my_use_of_single_use_plastics_sometimes_age_35_44=df.iat[170,21]
    limit_my_use_of_single_use_plastics_sometimes_age_45_54=df.iat[170,22]
    limit_my_use_of_single_use_plastics_sometimes_age_55_64=df.iat[170,23]

        
    limit_my_use_of_single_use_plastics_never_total_participants=df.iat[172,1]
    Limit_my_use_of_single_use_plastics_never_male_participants=df.iat[172,3]
    Limit_my_use_of_single_use_plastics_never_female_participants=df.iat[172,4]   
    Limit_my_use_of_single_use_plastics_never_north_east=df.iat[172,6]
    Limit_my_use_of_single_use_plastics_never_north_west=df.iat[172,7]
    Limit_my_use_of_single_use_plastics_never_yorkshire_the_humber=df.iat[172,8]
    Limit_my_use_of_single_use_plastics_never_east_Midlands=df.iat[172,9]
    Limit_my_use_of_single_use_plastics_never_west_midlands=df.iat[172,10]
    Limit_my_use_of_single_use_plastics_never_east_of_england=df.iat[172,11]
    Limit_my_use_of_single_use_plastics_never_london=df.iat[172,12]
    Limit_my_use_of_single_use_plastics_never_south_east=df.iat[172,13]
    Limit_my_use_of_single_use_plastics_never_south_west=df.iat[172,14]
    Limit_my_use_of_single_use_plastics_never_wales=df.iat[172,15]
    Limit_my_use_of_single_use_plastics_never_scotland=df.iat[172,16]
    Limit_my_use_of_single_use_plastics_never_northern_ireland=df.iat[172,17]
    Limit_my_use_of_single_use_plastics_never_age_18_24=df.iat[172,19]
    Limit_my_use_of_single_use_plastics_never_age_25_34=df.iat[172,20]
    Limit_my_use_of_single_use_plastics_never_age_35_44=df.iat[172,21]
    Limit_my_use_of_single_use_plastics_never_age_45_54=df.iat[172,22]
    Limit_my_use_of_single_use_plastics_never_age_55_64=df.iat[172,23]

    pay_more_for_more_durable_longer_lasting_items_always_total_participants=df.iat[174,1]
    pay_more_for_more_durable_longer_lasting_items_always_male_participants=df.iat[174,3]
    pay_more_for_more_durable_longer_lasting_items_always_female_participants=df.iat[174,4]   
    pay_more_for_more_durable_longer_lasting_items_always_north_east=df.iat[174,6]
    pay_more_for_more_durable_longer_lasting_items_always_north_west=df.iat[174,7]
    pay_more_for_more_durable_longer_lasting_items_always_yorkshire_the_humber=df.iat[174,8]
    pay_more_for_more_durable_longer_lasting_items_always_east_Midlands=df.iat[174,9]
    pay_more_for_more_durable_longer_lasting_items_always_west_midlands=df.iat[174,10]
    pay_more_for_more_durable_longer_lasting_items_always_east_of_england=df.iat[174,11]
    pay_more_for_more_durable_longer_lasting_items_always_london=df.iat[174,12]
    pay_more_for_more_durable_longer_lasting_items_always_south_east=df.iat[174,13]
    pay_more_for_more_durable_longer_lasting_items_always_south_west=df.iat[174,14]
    pay_more_for_more_durable_longer_lasting_items_always_wales=df.iat[174,15]
    pay_more_for_more_durable_longer_lasting_items_always_scotland=df.iat[174,16]
    pay_more_for_more_durable_longer_lasting_items_always_northern_ireland=df.iat[174,17]
    pay_more_for_more_durable_longer_lasting_items_always_age_18_24=df.iat[174,19]
    pay_more_for_more_durable_longer_lasting_items_always_age_25_34=df.iat[174,20]
    pay_more_for_more_durable_longer_lasting_items_always_age_35_44=df.iat[174,21]
    pay_more_for_more_durable_longer_lasting_items_always_age_45_54=df.iat[174,22]
    pay_more_for_more_durable_longer_lasting_items_always_age_55_64=df.iat[174,23]

        
    pay_more_for_a_more_durable_longer_lasting_items_often_total_participants=df.iat[176,1]
    pay_more_for_a_more_durable_longer_lasting_items_often_male_participants=df.iat[176,3]
    pay_more_for_a_more_durable_longer_lasting_items_often_female_participants=df.iat[176,4]   
    pay_more_for_a_more_durable_longer_lasting_items_often_north_east=df.iat[176,6]
    pay_more_for_a_more_durable_longer_lasting_items_often_north_west=df.iat[176,7]
    pay_more_for_a_more_durable_longer_lasting_items_often_yorkshire_the_humber=df.iat[176,8]
    pay_more_for_a_more_durable_longer_lasting_items_often_east_Midlands=df.iat[176,9]
    pay_more_for_a_more_durable_longer_lasting_items_often_west_midlands=df.iat[176,10]
    pay_more_for_a_more_durable_longer_lasting_items_often_east_of_england=df.iat[176,11]
    pay_more_for_a_more_durable_longer_lasting_items_often_london=df.iat[176,12]
    pay_more_for_a_more_durable_longer_lasting_items_often_south_east=df.iat[176,13]
    pay_more_for_a_more_durable_longer_lasting_items_often_south_west=df.iat[176,14]
    pay_more_for_a_more_durable_longer_lasting_items_often_wales=df.iat[176,15]
    pay_more_for_a_more_durable_longer_lasting_items_often_scotland=df.iat[176,16]
    pay_more_for_a_more_durable_longer_lasting_items_often_northern_ireland=df.iat[176,17]
    pay_more_for_a_more_durable_longer_lasting_items_often_age_18_24=df.iat[176,19]
    pay_more_for_a_more_durable_longer_lasting_items_often_age_25_34=df.iat[176,20]
    pay_more_for_a_more_durable_longer_lasting_items_often_age_35_44=df.iat[176,21]
    pay_more_for_a_more_durable_longer_lasting_items_often_age_45_54=df.iat[176,22]
    pay_more_for_a_more_durable_longer_lasting_items_often_age_55_64=df.iat[176,23]


        
    pay_more_for_a_more_durable_longer_lasting_items_rarely_total_participants=df.iat[178,1]
    pay_more_for_a_more_durable_longer_lasting_items_rarely_male_participants=df.iat[178,3]
    pay_more_for_a_more_durable_longer_lasting_items_rarely_female_participants=df.iat[178,4]   
    pay_more_for_a_more_durable_longer_lasting_items_rarely_north_east=df.iat[178,6]
    pay_more_for_a_more_durable_longer_lasting_items_rarely_north_west=df.iat[178,7]
    pay_more_for_a_more_durable_longer_lasting_items_rarely_yorkshire_the_humber=df.iat[178,8]
    pay_more_for_a_more_durable_longer_lasting_items_rarely_east_Midlands=df.iat[178,9]
    pay_more_for_a_more_durable_longer_lasting_items_rarely_west_midlands=df.iat[178,10]
    pay_more_for_a_more_durable_longer_lasting_items_rarely_east_of_england=df.iat[178,11]
    pay_more_for_a_more_durable_longer_lasting_items_rarely_london=df.iat[178,12]
    pay_more_for_a_more_durable_longer_lasting_items_rarely_south_east=df.iat[178,13]
    pay_more_for_a_more_durable_longer_lasting_items_rarely_south_west=df.iat[178,14]
    pay_more_for_a_more_durable_longer_lasting_items_rarely_wales=df.iat[178,15]
    pay_more_for_a_more_durable_longer_lasting_items_rarely_scotland=df.iat[178,16]
    pay_more_for_a_more_durable_longer_lasting_items_rarely_northern_ireland=df.iat[178,17]
    pay_more_for_a_more_durable_longer_lasting_items_rarely_age_18_24=df.iat[178,19]
    pay_more_for_a_more_durable_longer_lasting_items_rarely_age_25_34=df.iat[178,20]
    pay_more_for_a_more_durable_longer_lasting_items_rarely_age_35_44=df.iat[178,21]
    pay_more_for_a_more_durable_longer_lasting_items_rarely_age_45_54=df.iat[178,22]
    pay_more_for_a_more_durable_longer_lasting_items_rarely_age_55_64=df.iat[178,23]


  
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_total_participants=df.iat[180,1]
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_male_participants=df.iat[180,3]
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_female_participants=df.iat[180,4]   
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_north_east=df.iat[180,6]
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_north_west=df.iat[180,7]
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_yorkshire_the_humber=df.iat[180,8]
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_east_Midlands=df.iat[180,9]
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_west_midlands=df.iat[180,10]
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_east_of_england=df.iat[180,11]
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_london=df.iat[180,12]
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_south_east=df.iat[180,13]
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_south_west=df.iat[180,14]
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_wales=df.iat[180,15]
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_scotland=df.iat[180,16]
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_northern_ireland=df.iat[180,17]
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_age_18_24=df.iat[180,19]
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_age_25_34=df.iat[180,20]
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_age_35_44=df.iat[180,21]
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_age_45_54=df.iat[180,22]
    pay_more_for_a_more_durable_longer_lasting_items_sometimes_age_55_64=df.iat[180,23]

        
    pay_more_for_a_more_durable_longer_lasting_items_never_total_participants=df.iat[182,1]
    pay_more_for_a_more_durable_longer_lasting_items_never_male_participants=df.iat[182,3]
    pay_more_for_a_more_durable_longer_lasting_items_never_female_participants=df.iat[182,4]   
    pay_more_for_a_more_durable_longer_lasting_items_never_north_east=df.iat[182,6]
    pay_more_for_a_more_durable_longer_lasting_items_never_north_west=df.iat[182,7]
    pay_more_for_a_more_durable_longer_lasting_items_never_yorkshire_the_humber=df.iat[182,8]
    pay_more_for_a_more_durable_longer_lasting_items_never_east_Midlands=df.iat[182,9]
    pay_more_for_a_more_durable_longer_lasting_items_never_west_midlands=df.iat[182,10]
    pay_more_for_a_more_durable_longer_lasting_items_never_east_of_england=df.iat[182,11]
    pay_more_for_a_more_durable_longer_lasting_items_never_london=df.iat[182,12]
    pay_more_for_a_more_durable_longer_lasting_items_never_south_east=df.iat[182,13]
    pay_more_for_a_more_durable_longer_lasting_items_never_south_west=df.iat[182,14]
    pay_more_for_a_more_durable_longer_lasting_items_never_wales=df.iat[182,15]
    pay_more_for_a_more_durable_longer_lasting_items_never_scotland=df.iat[182,16]
    pay_more_for_a_more_durable_longer_lasting_items_never_northern_ireland=df.iat[182,17]
    pay_more_for_a_more_durable_longer_lasting_items_never_age_18_24=df.iat[182,19]
    pay_more_for_a_more_durable_longer_lasting_items_never_age_25_34=df.iat[182,20]
    pay_more_for_a_more_durable_longer_lasting_items_never_age_35_44=df.iat[182,21]
    pay_more_for_a_more_durable_longer_lasting_items_never_age_45_54=df.iat[182,22]
    pay_more_for_a_more_durable_longer_lasting_items_never_age_55_64=df.iat[182,23]

    purchase_fewer_plastics_always_total_participants=df.iat[184,1]
    purchase_fewer_plastics_always_male_participants=df.iat[184,3]
    purchase_fewer_plastics_always_female_participants=df.iat[184,4]   
    purchase_fewer_plastics_always_north_east=df.iat[184,6]
    purchase_fewer_plastics_always_north_west=df.iat[184,7]
    purchase_fewer_plastics_always_yorkshire_the_humber=df.iat[184,8]
    purchase_fewer_plastics_always_east_Midlands=df.iat[184,9]
    purchase_fewer_plastics_always_west_midlands=df.iat[184,10]
    purchase_fewer_plastics_always_east_of_england=df.iat[184,11]
    purchase_fewer_plastics_always_london=df.iat[184,12]
    purchase_fewer_plastics_always_south_east=df.iat[184,13]
    purchase_fewer_plastics_always_south_west=df.iat[184,14]
    purchase_fewer_plastics_always_wales=df.iat[184,15]
    purchase_fewer_plastics_always_scotland=df.iat[184,16]
    purchase_fewer_plastics_always_northern_ireland=df.iat[184,17]
    purchase_fewer_plastics_always_age_18_24=df.iat[184,19]
    purchase_fewer_plastics_always_age_25_34=df.iat[184,20]
    purchase_fewer_plastics_always_age_35_44=df.iat[184,21]
    purchase_fewer_plastics_always_age_45_54=df.iat[184,22]
    purchase_fewer_plastics_always_age_55_64=df.iat[184,23]


    purchase_fewer_plastics_often_total_participants=df.iat[186,1]
    purchase_fewer_plastics_often_male_participants=df.iat[186,3]
    purchase_fewer_plastics_often_female_participants=df.iat[186,4]   
    purchase_fewer_plastics_often_north_east=df.iat[186,6]
    purchase_fewer_plastics_often_north_west=df.iat[186,7]
    purchase_fewer_plastics_often_yorkshire_the_humber=df.iat[186,8]
    purchase_fewer_plastics_often_east_Midlands=df.iat[186,9]
    purchase_fewer_plastics_often_west_midlands=df.iat[186,10]
    purchase_fewer_plastics_often_east_of_england=df.iat[186,11]
    purchase_fewer_plastics_often_london=df.iat[186,12]
    purchase_fewer_plastics_often_south_east=df.iat[186,13]
    purchase_fewer_plastics_often_south_west=df.iat[186,14]
    purchase_fewer_plastics_often_wales=df.iat[186,15]
    purchase_fewer_plastics_often_scotland=df.iat[186,16]
    purchase_fewer_plastics_often_northern_ireland=df.iat[186,17]
    purchase_fewer_plastics_often_age_18_24=df.iat[186,19]
    purchase_fewer_plastics_often_age_25_34=df.iat[186,20]
    purchase_fewer_plastics_often_age_35_44=df.iat[186,21]
    purchase_fewer_plastics_often_age_45_54=df.iat[186,22]
    purchase_fewer_plastics_often_age_55_64=df.iat[186,23]


    purchase_fewer_plastics_rarely_total_participants=df.iat[188,1]
    purchase_fewer_plastics_rarely_male_participants=df.iat[188,3]
    purchase_fewer_plastics_rarely_female_participants=df.iat[188,4]   
    purchase_fewer_plastics_rarely_north_east=df.iat[188,6]
    purchase_fewer_plastics_rarely_north_west=df.iat[188,7]
    purchase_fewer_plastics_rarely_yorkshire_the_humber=df.iat[188,8]
    purchase_fewer_plastics_rarely_east_Midlands=df.iat[188,9]
    purchase_fewer_plastics_rarely_west_midlands=df.iat[188,10]
    purchase_fewer_plastics_rarely_east_of_england=df.iat[188,11]
    purchase_fewer_plastics_rarely_london=df.iat[188,12]
    purchase_fewer_plastics_rarely_south_east=df.iat[188,13]
    purchase_fewer_plastics_rarely_south_west=df.iat[188,14]
    purchase_fewer_plastics_rarely_wales=df.iat[188,15]
    purchase_fewer_plastics_rarely_scotland=df.iat[188,16]
    purchase_fewer_plastics_rarely_northern_ireland=df.iat[188,17]
    purchase_fewer_plastics_rarely_age_18_24=df.iat[188,19]
    purchase_fewer_plastics_rarely_age_25_34=df.iat[188,20]
    purchase_fewer_plastics_rarely_age_35_44=df.iat[188,21]
    purchase_fewer_plastics_rarely_age_45_54=df.iat[188,22]
    purchase_fewer_plastics_rarely_age_55_64=df.iat[188,23]


    purchase_fewer_plastics_sometimes_total_participants=df.iat[190,1]
    purchase_fewer_plastics_sometimes_male_participants=df.iat[190,3]
    purchase_fewer_plastics_sometimes_female_participants=df.iat[190,4]   
    purchase_fewer_plastics_sometimes_north_east=df.iat[190,6]
    purchase_fewer_plastics_sometimes_north_west=df.iat[190,7]
    purchase_fewer_plastics_sometimes_yorkshire_the_humber=df.iat[190,8]
    purchase_fewer_plastics_sometimes_east_Midlands=df.iat[190,9]
    purchase_fewer_plastics_sometimes_west_midlands=df.iat[190,10]
    purchase_fewer_plastics_sometimes_east_of_england=df.iat[190,11]
    purchase_fewer_plastics_sometimes_london=df.iat[190,12]
    purchase_fewer_plastics_sometimes_south_east=df.iat[190,13]
    purchase_fewer_plastics_sometimes_south_west=df.iat[190,14]
    purchase_fewer_plastics_sometimes_wales=df.iat[190,15]
    purchase_fewer_plastics_sometimes_scotland=df.iat[190,16]
    purchase_fewer_plastics_sometimes_northern_ireland=df.iat[190,17]
    purchase_fewer_plastics_sometimes_age_18_24=df.iat[190,19]
    purchase_fewer_plastics_sometimes_age_25_34=df.iat[190,20]
    purchase_fewer_plastics_sometimes_age_35_44=df.iat[190,21]
    purchase_fewer_plastics_sometimes_age_45_54=df.iat[190,22]
    purchase_fewer_plastics_sometimes_age_55_64=df.iat[190,23]


    purchase_fewer_plastics_never_total_participants=df.iat[192,1]
    purchase_fewer_plastics_never_male_participants=df.iat[192,3]
    purchase_fewer_plastics_never_female_participants=df.iat[192,4]   
    purchase_fewer_plastics_never_north_east=df.iat[192,6]
    purchase_fewer_plastics_never_north_west=df.iat[192,7]
    purchase_fewer_plastics_never_yorkshire_the_humber=df.iat[192,8]
    purchase_fewer_plastics_never_east_Midlands=df.iat[192,9]
    purchase_fewer_plastics_never_west_midlands=df.iat[192,10]
    purchase_fewer_plastics_never_east_of_england=df.iat[192,11]
    purchase_fewer_plastics_never_london=df.iat[192,12]
    purchase_fewer_plastics_never_south_east=df.iat[192,13]
    purchase_fewer_plastics_never_south_west=df.iat[192,14]
    purchase_fewer_plastics_never_wales=df.iat[192,15]
    purchase_fewer_plastics_never_scotland=df.iat[192,16]
    purchase_fewer_plastics_never_northern_ireland=df.iat[192,17]
    purchase_fewer_plastics_never_age_18_24=df.iat[192,19]
    purchase_fewer_plastics_never_age_25_34=df.iat[192,20]
    purchase_fewer_plastics_never_age_35_44=df.iat[192,21]
    purchase_fewer_plastics_never_age_45_54=df.iat[192,22]
    purchase_fewer_plastics_never_age_55_64=df.iat[192,23]

    ####### read till purchase_fewer_plastics_never --  missing fro 194 to 222
    #endregion
    
    #Question 7
    question7=df.iat[225,0]
    total_participants_question7=df.iat[226,1]
    male_participants_question7=df.iat[226,3]
    female_participants_question7=df.iat[226,4]
    
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_total_participants=df.iat[228,1]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_male_participants=df.iat[228,3]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_female_participants=df.iat[228,4]   
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_north_east=df.iat[228,6]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_north_west=df.iat[228,7]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_yorkshire_the_humber=df.iat[228,8]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_east_Midlands=df.iat[228,9]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_west_midlands=df.iat[228,10]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_east_of_england=df.iat[228,11]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_london=df.iat[228,12]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_south_east=df.iat[228,13]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_south_west=df.iat[228,14]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_wales=df.iat[228,15]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_scotland=df.iat[228,16]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_northern_ireland=df.iat[228,17]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_age_18_24=df.iat[228,19]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_age_25_34=df.iat[228,20]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_age_35_44=df.iat[228,21]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_age_45_54=df.iat[228,22]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_always_age_55_64=df.iat[228,23]



    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_total_participants=df.iat[230,1]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_male_participants=df.iat[230,3]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_female_participants=df.iat[230,4]   
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_north_east=df.iat[230,6]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_north_west=df.iat[230,7]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_yorkshire_the_humber=df.iat[230,8]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_east_Midlands=df.iat[230,9]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_west_midlands=df.iat[230,10]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_east_of_england=df.iat[230,11]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_london=df.iat[230,12]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_south_east=df.iat[230,13]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_south_west=df.iat[230,14]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_wales=df.iat[230,15]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_scotland=df.iat[230,16]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_northern_ireland=df.iat[230,17]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_age_18_24=df.iat[230,19]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_age_25_34=df.iat[230,20]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_age_35_44=df.iat[230,21]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_age_45_54=df.iat[230,22]
    purchase_brands_that_promote_environmentally_sustainable_practices_values_often_age_55_64=df.iat[230,23]


    # read till row 233...
  
    

    survery1_dataset =[
    {
    'info_id':1,    
    'chunk':f"total participants in dataset 1 {total_sample_number} total participants percentage in dataset 1 {total_sample_percent}"
         
    },
    {
    'info_id':2,    
    'chunk':f"total male_participants {total_male_number} total_male_participants_percentage {total_male_percent} total_female_participants {total_female_number} total_female_participants_percent {total_female_percent}"        
    },
    {
    'info_id':3,   
    'chunk':f"region_north_east_total_participants {north_east_total_number} region_north_east_total_participants_percentage {north_east_total_percent} region_north_east_male_participants {north_east_male_number} region_north_east_male_participants_percent {north_east_male_percent} region_north_east_female_participants {north_east_female_number} region_north_east_female_participants_percent {north_east_female_percent} region_north_west_total_participants {north_west_total_number} region_north_west_total_participants_percentage {north_west_total_percent} region_north_west_male_participants {north_west_male_number} region_north_west_male_participants_percentage {north_west_male_percent} region_north_west_female_participants {north_west_female_number} region_north_west_female_participants_percentage {north_west_female_percent}"
        
    },
    {
    'info_id':4,    
    'chunk':f"male age group 18-24: {eighteen_twentyfour_male_number} male age group 25-34: {twenty_thirty_male_number} male age group 35-44: {thirty_forty_male_number} male age group 45-54:{forty_fifty_male_number} male age group 55-64 :{fifty_sixty_male_number}"     
    },
    {
    'info_id':5, 
    'chunk':f"female age group 18-24: {eighteen_twentyfour_female_percent} female age group 25-34: {twenty_thirty_female_number} female age group 35-44: {thirty_forty_female_number} female age group 45-54 {forty_fifty_female_number} female age group 55-64 :{fifty_sixty_female_number}"
      
    },
    {
    'info_id':6, 
    'chunk':f":Question 1 {question1} total_participants_question1  {total_participants_question1} male_participants_question1: {male_participants_question1} female_participants_question1: {female_participants_question1}"
      
    }    
    ,
    {
    'info_id':7, 
    'chunk':f":Question 1 {question1} crime_total_participants: {crime_total_participants} crime_male_participants: {crime_male_participants} crime_female_participants: {crime_female_participants} crime_north_east: {crime_north_east} crime_north_west: {crime_north_west} crime_yorkshire_the_humber:{crime_yorkshire_the_humber} crime_east_Midlands: {crime_east_Midlands} crime_west_midlands: {crime_west_midlands} crime_east_of_england: {crime_east_of_england} crime_london: {crime_london} crime_south_east:{crime_south_east} crime_south_west:{crime_south_west} crime_wales: {crime_wales} crime_scotland: {crime_scotland} crime_northern_ireland: {crime_northern_ireland} crime_age_18_24: {crime_age_18_24} crime_age_25_34:{crime_age_25_34} crime_age_35_44:{crime_age_35_44} crime_age_45_54:{crime_age_45_54} crime_age_55_64:{crime_age_55_64}"
      
    }, 

    {
    'info_id':8, 
    'chunk':f":Question 1 {question1} cost_of_living_total_participants: {cost_of_living_total_participants} cost_of_living_male_participants: {cost_of_living_male_participants} cost_of_living_female_participants: {cost_of_living_female_participants} cost_of_living_north_east: {cost_of_living_north_east} cost_of_living_north_west: {cost_of_living_north_west} cost_of_living_yorkshire_the_humber:{cost_of_living_yorkshire_the_humber} cost_of_living_east_Midlands: {cost_of_living_east_Midlands} cost_of_living_west_midlands: {cost_of_living_west_midlands} cost_of_living_east_of_england: {cost_of_living_east_of_england} cost_of_living_london: {cost_of_living_london} cost_of_living_south_east:{cost_of_living_south_east} cost_of_living_south_west:{cost_of_living_south_west} cost_of_living_wales: {cost_of_living_wales} cost_of_living_scotland: {cost_of_living_scotland} cost_of_living_northern_ireland: {cost_of_living_northern_ireland} cost_of_living_age_18_24: {cost_of_living_age_18_24} cost_of_living_age_25_34:{cost_of_living_age_25_34} cost_of_living_age_35_44:{cost_of_living_age_35_44} cost_of_living_age_45_54:{cost_of_living_age_45_54} cost_of_living_age_55_64:{cost_of_living_age_55_64}"
      
    },

    {
    'info_id':9, 
    'chunk':f":Question 1 {question1} education_total_participants: {education_total_participants} education_male_participants: {education_male_participants} education_female_participants: {education_female_participants} education_north_east: {education_north_east} education_north_west: {education_north_west} education_yorkshire_the_humber:{education_yorkshire_the_humber} education_east_Midlands: {education_east_Midlands} education_west_midlands: {education_west_midlands} education_east_of_england: {education_east_of_england} education_london: {education_london} education_south_east:{education_south_east} education_south_west:{education_south_west} education_wales: {education_wales} education_scotland: {education_scotland} education_northern_ireland: {education_northern_ireland} education_age_18_24: {education_age_18_24} education_age_25_34:{education_age_25_34} education_age_35_44:{education_age_35_44} education_age_45_54:{education_age_45_54} education_age_55_64:{education_age_55_64}"
      
    },

    {
    'info_id':10, 
    'chunk':f":Question 1 {question1} housing_total_participants: {housing_total_participants} housing_male_participants: {housing_male_participants} housing_female_participants: {housing_female_participants} housing_north_east: {housing_north_east} housing_north_west: {housing_north_west} housing_yorkshire_the_humber:{housing_yorkshire_the_humber} housing_east_Midlands: {housing_east_Midlands} housing_west_midlands: {housing_west_midlands} housing_east_of_england: {housing_east_of_england} housing_london: {housing_london} housing_south_east:{housing_south_east} housing_south_west:{housing_south_west} housing_wales: {housing_wales} housing_scotland: {housing_scotland} housing_northern_ireland: {housing_northern_ireland} housing_age_18_24: {housing_age_18_24} housing_age_25_34:{housing_age_25_34} housing_age_35_44:{housing_age_35_44} housing_age_45_54:{housing_age_45_54} housing_age_55_64:{housing_age_55_64}"
      
    } 
    ,

    {
    'info_id':11, 
    'chunk':f":Question 1 {question1} international_conflict_total_participants: {international_conflict_total_participants} international_conflict_male_participants: {international_conflict_male_participants} international_conflict_female_participants: {international_conflict_female_participants} international_conflict_north_east: {international_conflict_north_east} international_conflict_north_west: {international_conflict_north_west} international_conflict_yorkshire_the_humber:{international_conflict_yorkshire_the_humber} international_conflict_east_Midlands: {international_conflict_east_Midlands} international_conflict_west_midlands: {international_conflict_west_midlands} international_conflict_east_of_england: {international_conflict_east_of_england} international_conflict_london: {international_conflict_london} international_conflict_south_east:{international_conflict_south_east} international_conflict_south_west:{international_conflict_south_west} international_conflict_wales: {international_conflict_wales} international_conflict_scotland: {international_conflict_scotland} international_conflict_northern_ireland: {international_conflict_northern_ireland} international_conflict_age_18_24: {international_conflict_age_18_24} international_conflict_age_25_34:{international_conflict_age_25_34} international_conflict_age_35_44:{international_conflict_age_35_44} international_conflict_age_45_54:{international_conflict_age_45_54} international_conflict_age_55_64:{international_conflict_age_55_64}"
      
    },
    {
    'info_id':12, 
    'chunk':f":Question 1 {question1} mortgage_interest_rates_total_participants: {mortgage_interest_rates_total_participants} mortgage_interest_rates_male_participants: {mortgage_interest_rates_male_participants} mortgage_interest_rates_female_participants: {mortgage_interest_rates_female_participants} mortgage_interest_rates_north_east: {mortgage_interest_rates_north_east} mortgage_interest_rates_north_west: {mortgage_interest_rates_north_west} mortgage_interest_rates_yorkshire_the_humber:{mortgage_interest_rates_yorkshire_the_humber} mortgage_interest_rates_east_Midlands: {mortgage_interest_rates_east_Midlands} mortgage_interest_rates_west_midlands: {mortgage_interest_rates_west_midlands} mortgage_interest_rates_east_of_england: {mortgage_interest_rates_east_of_england} mortgage_interest_rates_london: {mortgage_interest_rates_london} mortgage_interest_rates_south_east:{mortgage_interest_rates_south_east} mortgage_interest_rates_south_west:{mortgage_interest_rates_south_west} mortgage_interest_rates_wales: {mortgage_interest_rates_wales} mortgage_interest_rates_scotland: {mortgage_interest_rates_scotland} mortgage_interest_rates_northern_ireland: {mortgage_interest_rates_northern_ireland} mortgage_interest_rates_age_18_24: {mortgage_interest_rates_age_18_24} mortgage_interest_rates_age_25_34:{mortgage_interest_rates_age_25_34} mortgage_interest_rates_age_35_44:{mortgage_interest_rates_age_35_44} mortgage_interest_rates_age_45_54:{mortgage_interest_rates_age_45_54} mortgage_interest_rates_age_55_64:{mortgage_interest_rates_age_55_64}"
      
    },
     {
    'info_id':13, 
    'chunk':f":Question 1 {question1} the_economy_total_participants: {the_economy_total_participants} the_economy_male_participants: {the_economy_male_participants} the_economy_female_participants: {the_economy_female_participants} the_economy_north_east: {the_economy_north_east} the_economy_north_west: {the_economy_north_west} the_economy_yorkshire_the_humber:{the_economy_yorkshire_the_humber} the_economy_east_Midlands: {the_economy_east_Midlands} the_economy_west_midlands: {the_economy_west_midlands} the_economy_east_of_england: {the_economy_east_of_england} the_economy_london: {the_economy_london} the_economy_south_east:{the_economy_south_east} the_economy_south_west:{the_economy_south_west} the_economy_wales: {the_economy_wales} the_economy_scotland: {the_economy_scotland} the_economy_northern_ireland: {the_economy_northern_ireland} the_economy_age_18_24: {the_economy_age_18_24} the_economy_age_25_34:{the_economy_age_25_34} the_economy_age_35_44:{the_economy_age_35_44} the_economy_age_45_54:{the_economy_age_45_54} the_economy_age_55_64:{the_economy_age_55_64}"
      
    },
    {
    'info_id':14, 
    'chunk':f":Question 1 {question1} the_environment_and_climate_change_total_participants: {the_environment_and_climate_change_total_participants} the_environment_and_climate_change_male_participants: {the_environment_and_climate_change_male_participants} the_environment_and_climate_change_female_participants: {the_environment_and_climate_change_female_participants} the_environment_and_climate_change_north_east: {the_environment_and_climate_change_north_east} the_environment_and_climate_change_north_west: {the_environment_and_climate_change_north_west} the_environment_and_climate_change_yorkshire_the_humber:{the_environment_and_climate_change_yorkshire_the_humber} the_environment_and_climate_change_east_Midlands: {the_environment_and_climate_change_east_Midlands} the_environment_and_climate_change_west_midlands: {the_environment_and_climate_change_west_midlands} the_environment_and_climate_change_east_of_england: {the_environment_and_climate_change_east_of_england} the_environment_and_climate_change_london: {the_environment_and_climate_change_london} the_environment_and_climate_change_south_east:{the_environment_and_climate_change_south_east} the_environment_and_climate_change_south_west:{the_environment_and_climate_change_south_west} the_environment_and_climate_change_wales: {the_environment_and_climate_change_wales} the_environment_and_climate_change_scotland: {the_environment_and_climate_change_scotland} the_environment_and_climate_change_northern_ireland: {the_environment_and_climate_change_northern_ireland} the_environment_and_climate_change_age_18_24: {the_environment_and_climate_change_age_18_24} the_environment_and_climate_change_age_25_34:{the_environment_and_climate_change_age_25_34} the_environment_and_climate_change_age_35_44:{the_environment_and_climate_change_age_35_44} the_environment_and_climate_change_age_45_54:{the_environment_and_climate_change_age_45_54} the_environment_and_climate_change_age_55_64:{the_environment_and_climate_change_age_55_64}"
      
    },
    {
    'info_id':15, 
    'chunk':f":Question 1 {question1} the_nhs_total_participants: {the_nhs_total_participants} the_nhs_male_participants: {the_nhs_male_participants} the_nhs_female_participants: {the_nhs_female_participants} the_nhs_north_east: {the_nhs_north_east} the_nhs_north_west: {the_nhs_north_west} the_nhs_yorkshire_the_humber:{the_nhs_yorkshire_the_humber} the_nhs_east_Midlands: {the_nhs_east_Midlands} the_nhs_west_midlands: {the_nhs_west_midlands} the_nhs_east_of_england: {the_nhs_east_of_england} the_nhs_london: {the_nhs_london} the_nhs_south_east:{the_nhs_south_east} the_nhs_south_west:{the_nhs_south_west} the_nhs_wales: {the_nhs_wales} the_nhs_scotland: {the_nhs_scotland} the_nhs_northern_ireland: {the_nhs_northern_ireland} the_nhs_age_18_24: {the_nhs_age_18_24} the_nhs_age_25_34:{the_nhs_age_25_34} the_nhs_age_35_44:{the_nhs_age_35_44} the_nhs_age_45_54:{the_nhs_age_45_54} the_nhs_age_55_64:{the_nhs_age_55_64}"
      
    },
    {
    'info_id':16, 
    'chunk':f":Question 1 {question1} unemployment_total_participants: {unemployment_total_participants} unemployment_male_participants: {unemployment_male_participants} unemployment_female_participants: {unemployment_female_participants} unemployment_north_east: {unemployment_north_east} unemployment_north_west: {unemployment_north_west} unemployment_yorkshire_the_humber:{unemployment_yorkshire_the_humber} unemployment_east_Midlands: {unemployment_east_Midlands} unemployment_west_midlands: {unemployment_west_midlands} unemployment_east_of_england: {unemployment_east_of_england} unemployment_london: {unemployment_london} unemployment_south_east:{unemployment_south_east} unemployment_south_west:{unemployment_south_west} unemployment_wales: {unemployment_wales} unemployment_scotland: {unemployment_scotland} unemployment_northern_ireland: {unemployment_northern_ireland} unemployment_age_18_24: {unemployment_age_18_24} unemployment_age_25_34:{unemployment_age_25_34} unemployment_age_35_44:{unemployment_age_35_44} unemployment_age_45_54:{unemployment_age_45_54} unemployment_age_55_64:{unemployment_age_55_64}"
      
    },

    {
    'info_id':17, 
    'chunk':f":Question 2 {question2} total_participants_question2: {total_participants_question2} male_participants_question2: {male_participants_question2} female_participants_question2: {female_participants_question2} "
      
    },
    {
    'info_id':18, 
    'chunk':f":Question 2 {question2} vegetarian_total_participants: {vegetarian_total_participants} vegetarian_male_participants: {vegetarian_male_participants} vegetarian_female_participants: {vegetarian_female_participants} vegetarian_north_east: {vegetarian_north_east} vegetarian_north_west: {vegetarian_north_west} vegetarian_yorkshire_the_humber:{vegetarian_yorkshire_the_humber} vegetarian_east_Midlands: {vegetarian_east_Midlands} vegetarian_east_Midlands: {vegetarian_east_Midlands} vegetarian_east_of_england: {vegetarian_east_of_england} vegetarian_london: {vegetarian_london} vegetarian_south_east:{vegetarian_south_east} vegetarian_south_west:{vegetarian_south_west} vegetarian_wales: {vegetarian_wales} vegetarian_scotland: {vegetarian_scotland} vegetarian_northern_ireland: {vegetarian_northern_ireland} vegetarian_age_18_24: {vegetarian_age_18_24} vegetarian_age_25_34:{vegetarian_age_25_34} vegetarian_age_35_44:{vegetarian_age_35_44} vegetarian_age_45_54:{vegetarian_age_45_54} vegetarian_age_55_64:{vegetarian_age_55_64}"
      
    },
    {
    'info_id':19,   
    'chunk':f":Question 2 {question2} vegan_total_participants: {vegan_total_participants} vegan_male_participants: {vegan_male_participants} vegan_female_participants: {vegan_female_participants} vegan_north_east: {vegan_north_east} vegan_north_west: {vegan_north_west} vegan_yorkshire_the_humber:{vegan_yorkshire_the_humber} vegan_east_Midlands: {vegan_east_Midlands} vegan_west_midlands: {vegan_west_midlands} vegan_east_of_england: {vegan_east_of_england} vegan_london: {vegan_london} vegan_south_east:{vegan_south_east} vegan_south_west:{vegan_south_west} vegan_wales: {vegan_wales} vegan_scotland: {vegan_scotland} vegan_northern_ireland: {vegan_northern_ireland} vegan_age_18_24: {vegan_age_18_24} vegan_age_25_34:{vegan_age_25_34} vegan_age_35_44:{vegan_age_35_44} vegan_age_45_54:{vegan_age_45_54} vegan_age_55_64:{vegan_age_55_64}"
      
    },
    {
    'info_id':20,   
    'chunk':f":Question 2 {question2} pescatarian_total_participants: {pescatarian_total_participants} pescatarian_male_participants: {pescatarian_male_participants} vegan_female_participants: {pescatarian_female_participants} pescatarian_north_east: {pescatarian_north_east} pescatarian_north_west: {pescatarian_north_west} pescatarian_yorkshire_the_humber:{pescatarian_yorkshire_the_humber} pescatarian_east_Midlands: {pescatarian_east_Midlands} pescatarian_west_midlands: {pescatarian_west_midlands} pescatarian_east_of_england: {pescatarian_east_of_england} pescatarian_london: {pescatarian_london} pescatarian_south_east:{pescatarian_south_east} pescatarian_south_west:{pescatarian_south_west} pescatarian_wales: {pescatarian_wales} pescatarian_scotland: {pescatarian_scotland} pescatarian_northern_ireland: {pescatarian_northern_ireland} pescatarian_age_18_24: {pescatarian_age_18_24} pescatarian_age_25_34:{pescatarian_age_25_34} pescatarian_age_35_44:{pescatarian_age_35_44} pescatarian_age_45_54:{pescatarian_age_45_54} pescatarian_age_55_64:{pescatarian_age_55_64}"
      
    },
    {
    'info_id':21,   
    'chunk':halal_chunk   
    },
    {
    'info_id':22,   
    'chunk':chunk_kosher   
    },
    {
    'info_id':23,   
    'chunk':chunk_none_of_the_above   
    }
    
    ]


    json_data = json.dumps(survery1_dataset)
    chunks_info=json.loads(json_data)
    return chunks_info


def create_embeddings(temp_texts,sentence_encoder_model):
    #with torch.no_grad(): 
    embeddings_bert_model = sentence_encoder_model.encode(temp_texts, normalize_embeddings=True)
    return embeddings_bert_model


sentence_encoder_model = SentenceTransformer('BAAI/bge-small-en',device='cpu')
dataset=read_excel_file()
chunks_list=[]
embeddings_list=[]
for chunk in dataset:
    chunks_list.append(chunk['chunk'])

data_embeddings=create_embeddings(chunks_list,sentence_encoder_model)
for n in range(len(dataset)):
    embeddings_list.append({'info_id':str(dataset[n]['info_id']),'embedding': np.array(data_embeddings[n]).tolist()})
embedding_filename = 'embedding_file.txt'
chunks_filename='chunks_file.txt'

#save embedding file
with open(embedding_filename, 'w') as file:
    json.dump(embeddings_list, file, indent=4)  


#save chunks file
with open(chunks_filename, 'w') as file:
    json.dump(dataset, file, indent=4)  


print("Chunks and embeddings created for dataset 1...")    


    