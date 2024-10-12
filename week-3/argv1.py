import sys
print(sys.argv)

what_to_do = sys.argv[1]
print(f'I will {what_to_do}, just wait...')

if what_to_do == 'start':
  print('System online')
elif what_to_do == 'stop':
  print('System offline')
else:
  print('Ok')
