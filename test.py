import csv
users = []
cusers = 0
invoices = []
cinvoices = 0


with open('C:\\Users\\Noga\\Downloads\\users.csv',newline='',encoding='utf8') as fuser :
    ruser = csv.reader(fuser, delimiter=';' )
    for user in ruser :
        users += user[0].split()
        cusers += 1
print('users: ',cusers, users)

with open('C:\\Users\\Noga\\Downloads\\invoices.csv',newline='',encoding='utf8') as finvoice :
    rinvoice = csv.reader(finvoice, delimiter=';' )
    for invoice in rinvoice :
        invoices += invoice[5].split()
        cinvoices += 1
print('invoices: ',cinvoices, invoices)

Not_matching = list(set(invoices).difference(users))
Matching = list(set(invoices).intersection(users))
count_not_match = len(Not_matching)
count_match = len(Matching)

print('Not matching users are:', count_not_match, ':', Not_matching)
print('Matching users are: ', count_match, ':', Matching)
