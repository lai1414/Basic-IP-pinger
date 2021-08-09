import os

ip = input('Enter ip : ')
os.system(f'ping {ip}')
print('----------------------')
print(f'Successfully pinged {ip}.')