# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 17:31:45 2015

@author: Venkata Jagannath
"""
import numpy as np
import pandas as pd
import matplotlib


Prudential=pd.read_csv('Prudential.csv')


Prudential_category=Prudential[['Id','Product_Info_1','Product_Info_2','Product_Info_3','Product_Info_5','Product_Info_6',
                            'Product_Info_7', 'Employment_Info_2', 'Employment_Info_3', 'Employment_Info_5',
                            'InsuredInfo_1', 'InsuredInfo_2', 'InsuredInfo_3', 'InsuredInfo_4', 'InsuredInfo_5',
                            'InsuredInfo_6', 'InsuredInfo_7','Insurance_History_1', 'Insurance_History_2',
                            'Insurance_History_3','Insurance_History_4','Insurance_History_7','Insurance_History_8',
                            'Insurance_History_9','Family_Hist_1','Medical_History_2','Medical_History_3',
                            'Medical_History_4','Medical_History_5','Medical_History_6','Medical_History_7',
                            'Medical_History_8','Medical_History_9','Medical_History_10','Medical_History_11',
                            'Medical_History_12','Medical_History_13','Medical_History_14','Medical_History_16',
                            'Medical_History_17','Medical_History_18','Medical_History_19','Medical_History_20',
                            'Medical_History_21', 'Medical_History_22','Medical_History_23','Medical_History_25',
                            'Medical_History_26','Medical_History_27','Medical_History_28', 'Medical_History_29',
                            'Medical_History_30','Medical_History_31', 'Medical_History_33','Medical_History_34',
                            'Medical_History_35','Medical_History_36','Medical_History_37','Medical_History_38',
                            'Medical_History_39','Medical_History_40','Medical_History_41']]
    
Prudential_cont=Prudential[['Id','Product_Info_4', 'Ins_Age', 'Ht', 'Wt', 'BMI', 'Employment_Info_1', 'Employment_Info_4',
                            'Employment_Info_6', 'Insurance_History_5', 'Family_Hist_2', 'Family_Hist_3', 'Family_Hist_4',
                            'Family_Hist_5']]                 

def column_modify():
    for column in Prudential_category:
        Prudential_category[column] = Prudential_category[column].astype('category')
        Prudential_category['Id']=Prudential_category['Id'].astype('float64')
    
column_modify()

Prudential_final=pd.concat([Prudential_category,Prudential_cont])

Prudential_final=pd.DataFrame(Prudential_final)

del(Prudential_category,Prudential_cont)

def correlation():
    Correlation=pd.DataFrame(Prudential_final.corr())
    x=float(input("Please enter the correlation value between 0 and 1"))
    for i in Correlation:
        for j in Correlation:
            if(x<Correlation[i][j]<1):
                {
                    print("There is a high degree of correlation between",i,"and",j)
                }

def visualize_the_data():
    Prudential_final.plot(x='Ht',y='BMI',kind='Hist',color='Orange')
    Prudential_final.plot(x='Insurance_History_5',y='Employment_Info_1')
    Prudential_final.plot(x='Insurance_History_5',y='Family_Hist_2')
    Prudential_final.plot(x='Insurance_History_5',y='Family_Hist_3')
    Prudential_final.plot(x='Insurance_History_5',y='Family_Hist_4')
    Prudential_final.plot(x='Insurance_History_5',y='Family_Hist_5')
    Prudential_final.plot(x='Employment_Info_1',y='Family_Hist_2')
    Prudential_final.plot(x='Ins_Age',y='Wt',kind='barh', stacked=True,color='Blue')
    






    

    
    

