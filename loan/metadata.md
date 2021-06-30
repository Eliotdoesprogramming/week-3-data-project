data cleaning steps:
1. Replaced NA values for Credit history to 0's because it will represent that we dont have data on their credit history.
2. Replaced NA values for Self_Employed to No because we dont know if they are self employed
3. Replaced NA values for Loan Amount to mean in order to minimize changes in distribution
4. Replaced NA values for Loan Term to mean in order to minimize changes in distribution
5. Replace NA values for Gender to mode because of lack of data on NA genders
6. Replace NA values for Married to mode due to there only being 3 rows of NA
7. Encode Target of Loan Status to 1 and 0 for Yes and No
8. Encode property area with get_dummies to Rural, Urban, Semiurban
9. Encode gender to 0 or 1 for female or male
10. Convert Dependents to integer values, 3+ becomes 3
11. Encode education to 0 being non graduate, 1 being graudate
12. Encode Married to 0 for not Married, 1 for Married
13. Encode Self Employed to 0 for no, 1 for yes
