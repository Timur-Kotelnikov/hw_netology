#quest 1 (mortgage)
base_rate = 10
region = input('Where is customer from? ')
amount_of_children = int(input('How many children do customer have? '))
salary = input('Is customer already our client? (yes or no) ')
insurance = input('Will customer buy our insurance? (yes or no) ')
if region in ['Amur', 'Vladivostok', 'Kamchatka', 'Sakhalin', 'Magadan', 'Chukotka']:
  final_rate = 2
elif amount_of_children > 3 and salary == 'yes' and insurance == 'yes':
  final_rate = base_rate-3
elif amount_of_children > 3 and salary == 'yes' and insurance == 'no':
  final_rate = base_rate-1.5
elif amount_of_children > 3 and salary == 'no' and insurance == 'yes':
  final_rate = base_rate-2.5
elif amount_of_children <= 3 and salary == 'yes' and insurance == 'yes':
  final_rate = base_rate-2
elif amount_of_children <= 3 and salary == 'no' and insurance == 'yes':
  final_rate = base_rate-1.5
elif amount_of_children <= 3 and salary == 'yes' and insurance == 'no':
  final_rate = base_rate-0.5
elif amount_of_children > 3 and salary == 'no' and insurance == 'no':
  final_rate = base_rate-1
else:
    final_rate = base_rate
print (f'Final rate = {final_rate} %')