# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
#bank.head()

categorical_var = bank.select_dtypes(include = 'object')

#print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')

print(numerical_var)






# code ends here


# --------------
# code starts here
banks = bank.drop(columns = 'Loan_ID')

#banks.head()

print(banks.isnull().sum())

bank_mode = banks.mode()

#bank_mode.head()

banks.fillna(bank_mode.iloc[0], inplace = True)

banks.head()



#code ends here


# --------------
# Code starts here
import pandas as pd
import numpy as np

avg_loan_amount = banks.pivot_table(index = ['Gender','Married', 'Self_Employed'],values = 'LoanAmount', aggfunc='mean')



# code ends here



# --------------
# code starts here
import pandas as pd
mask1 = banks['Self_Employed'] == 'Yes'
mask2 = banks['Loan_Status'] == 'Y'
loan_approved_se = len(banks[mask1 & mask2])

mask3 = banks['Self_Employed'] == 'No'
loan_approved_nse = len(banks[mask2 & mask3])



percentage_se = loan_approved_se/614 * 100
percentage_nse = loan_approved_nse/614 * 100



#loan_approved_se = banks[banks['Self_Employed'] == 'Yes' & banks['Loan_Status'] == 'Y'].value_counts()

#highest_legendary = df[df['Legendary'] == True]['Type 1'].value_counts().idxmax()
# code ends here


# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)

big_loan_term = banks.loc[loan_term>=25].shape[0]

# code ends here


# --------------
# code ends here
loan_groupby = banks.groupby(['Loan_Status'])['ApplicantIncome', 'Credit_History'] 

mean_values = loan_groupby.mean()


# code ends here


