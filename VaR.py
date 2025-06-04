import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import os.path

def ReadData(): 
    file = str(input("Please input filepath for dataset (.xlsx/.csv): ")).strip() 
    base1 , ext1 = os.path.splitext(file)

    while ext1.lower() not in (".csv",".xlsx"): #dont use != because cannot compare string to tuple and also this checks if it is excel or csv file
        print("Please input a correct filetype (.xlsx/.csv)")
        file = input("Try Again: ").strip()
        base1, ext1 = os.path.splitext(file)

    if ext1 == ".csv":
        data = pd.read_csv(file)
    if ext1 == ".xlsx":
        data = pd.read_excel(file)

    data = data.dropna(subset=["Open","Date"]) #NAN HANDLING

    data["Open"] = data["Open"].astype(float) # ENSURE ALL RETURNS ARE FLOAT

    data["Returns"] = data["Open"].pct_change()*100  #PCT CHANGE (RETURNS)

    data['LgReturns'] = np.log(data["Open"]/data["Open"].shift(1)) #Log-Normal returns

    data = data.dropna(subset= ['LgReturns','Returns']) #Check if in case have NaN 

    return(data)


def VaR (data):
    sorted_returns = np.sort(data["Returns"].dropna())
    worst_case_loss = -sorted_returns.min() #worst case loss
    bins = np.log(2*len(sorted_returns)+1) #use sturges rule to calculate bins
    plt.hist(-data["Returns"].dropna(), bins=bins,edgecolor= 'black') #Tail risk in black
    plt.title("Loss Distribution")
    plt.xlabel("Loss(%)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

def range_of_VaR(data):
    if "Returns" not in data.columns:
        raise ValueError("DataFrame must contain a 'Returns' Column")
    
    confidence_levels =  np.linspace(0.90,0.999,10)
    VaRs = [-data["Returns"].quantile(1-cl) for cl in confidence_levels]

    for cl, var in zip(confidence_levels,VaRs):
        print(f"VaR at {int(cl*100)}% confidence: {var:.4f}")


