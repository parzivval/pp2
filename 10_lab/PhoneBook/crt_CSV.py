# Creating CSV file 

import csv

new_contacts = [
    ['id', 'name', 'email', 'number', 'company'],
    [6, 'contact 6', 'contact6@gmail.com', '87078622896', 'Company 6'],
    [7, 'contact 7', 'contact7@gmail.com', '87078622897', 'Company 7'],
    [8, 'contact 8', 'contact8@gmail.com', '87078622898', 'Company 8'],
    [9, 'contact 9', 'contact9@gmail.com', '87078622899', 'Company 9'],
    [10, 'contact 10', 'contact10@gmail.com', '87078622810', 'Company 10'],
    [11, 'contact 11', 'contact11@gmail.com', '87078622811', 'Company 11'],
    [12, 'contact 12', 'contact12@gmail.com', '87078622812', 'Company 12'],
    [13, 'contact 13', 'contact13@gmail.com', '87078622813', 'Company 13'],
    [14, 'contact 14', 'contact14@gmail.com', '87078622814', 'Company 14'],
    [15, 'contact 15', 'contact15@gmail.com', '87078622815', 'Company 15'],

]
with open('new_contacts.csv', 'w') as f:
    csv.writer(f).writerows(new_contacts)