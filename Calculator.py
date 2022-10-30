# Calculations
# the flat rate is 20%
flat_tax_rate = .20
# Standard decduction is $10,00
standard_deduction= 10000 
# Dependant deduction based per person
dependent_deduction= 3000 


# The user inputs  gross income 

gross_input = float(input(" Enter the gross input "))

# The user input number of dependendents

num_dependants = int(input("Enter the number of dependants "))

# Calculations
sum_dependent = (dependent_deduction * num_dependants)
sum_deduction = sum_dependent + standard_deduction

tax_cal= (gross_input - sum_deduction ) * (flat_tax_rate)
#output
print (f'Gross input: {gross_input}')
print (f'Number of dependant: {num_dependants}')
print (f'The income tax is: {tax_cal}')