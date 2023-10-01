Account_Balance = 10000
Point_Value = 0.00001
Pip_Value =  0.0001
Risk_Percentage = 1
Risk_Float = Risk_Percentage/100
ATR_Value = 0.0010
Stop_Loss_Pips = (ATR_Value*1.5)/Point_Value
Lots = (Account_Balance * Risk_Float)/(Stop_Loss_Pips*Pip_Value)
print(round(Lots,2))
