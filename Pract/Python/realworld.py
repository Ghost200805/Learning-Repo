# Q1

def analyse(orders):
    revenue = {}
    product_count = {}
    all_statuses = {}
    
    for order in orders:
        cust = order['customer']
        status = order['status']
        
        if cust not in all_statuses:
            all_statuses[cust] = set()
        all_statuses[cust].add(status)
        
        if status != 'CANCELLED':
            items = order['items']
            for item in items:
                item_name = item[0]
                qty = item[1]
                price = item[2]
                
                if cust not in revenue:
                    revenue[cust] = 0.0
                revenue[cust] = revenue[cust] + (qty * price)
                
                if item_name not in product_count:
                    product_count[item_name] = 0
                product_count[item_name] = product_count[item_name] + qty

    product_list = []
    for name, qty in product_count.items():
        product_list.append([-qty, name])
    product_list.sort()
    
    top_products = []
    for i in range(min(2, len(product_list))):
        qty = -product_list[i][0]
        name = product_list[i][1]
        top_products.append((name, qty))

    fully_delivered = []
    for cust in all_statuses:
        statuses = all_statuses[cust]
        if len(statuses) == 1 and 'DELIVERED' in statuses:
            fully_delivered.append(cust)
    fully_delivered.sort()

    ans = {
        'revenue': revenue,
        'top_products': top_products,
        'fully_delivered': fully_delivered
    }
    return ans

orders = [
    {'id': 101, 'customer': 'Asha', 'status': 'DELIVERED', 'items': [('keyboard', 2, 1499.0), ('mouse', 1, 599.0)]},
    {'id': 102, 'customer': 'Ravi', 'status': 'CANCELLED', 'items': [('monitor', 1, 10999.0)]},
    {'id': 103, 'customer': 'Asha', 'status': 'DELIVERED', 'items': [('cable', 5, 199.0)]},
    {'id': 104, 'customer': 'Meera', 'status': 'SHIPPED', 'items': [('keyboard', 1, 1499.0), ('monitor', 1, 10999.0)]},
    {'id': 105, 'customer': 'Ravi', 'status': 'DELIVERED', 'items': [('mouse', 3, 599.0)]}
]

result = analyse(orders)
print(result)



# Q2
def clean_customer(raw):
    fields = raw.split(';')
    if len(fields) != 4:
        return None
        
    name = fields[0].strip().title()
    email = fields[1].strip().lower()
    phone = fields[2].replace(' ', '').replace('-', '')
    city = fields[3].strip().title()
    
    if name == "":
        return None
    words = name.split(' ')
    for w in words:
        if not w.isalpha():
            return None

    if city == "":
        return None
        
    at_count = 0
    for char in email:
        if char == '@':
            at_count += 1
    if at_count != 1:
        return None
        
    email_parts = email.split('@')
    if email_parts[0] == "":
        return None
        
    domain = email_parts[1]
    if '.' not in domain:
        return None
    if domain[0] == '.' or domain[-1] == '.':
        return None
        
    if phone.startswith('+91'):
        phone = phone[3:]
    elif len(phone) == 12 and phone.startswith('91'):
        phone = phone[2:]
        
    if len(phone) != 10:
        return None
        
    for char in phone:
        if char < '0' or char > '9':
            return None
            
    if phone[0] not in ['6', '7', '8', '9']:
        return None
        
    return {
        'name': name,
        'email': email,
        'phone': phone,
        'city': city
    }


lines = [
    'asha VERMA; ASHA.V@Example.COM; +91 98765-43210;pune',
    'ravi kumar;ravi@@corp.in;9123456780;Mumbai',
    'meera;meera@mail;9123456780;Delhi',
    'john doe; john@x.org; 12345; Goa',
    'Neha Rao;neha.rao@firm.co.in; 919876501234;nashik',
    'amit amit@site.com;9876543210'
]

rejected_count = 0

for line in lines:
    cleaned = clean_customer(line)
    if cleaned != None:
        print(cleaned)
    else:
        rejected_count += 1

print("Rejected:", rejected_count)