access_logs = [
    '2019-01-01T00:00:01, 12.21.1.101, GET, /assets/js/loader2.js, 102, 0',
    '2019-01-01T00:00:02, 12.21.1.109, GET, /assets/js/loader3.js, 102, 0',
    '2019-01-01T00:00:01, 12.21.1.101, GET, /assets/js/loader.js, 102, 0',
    '2019-01-01T00:00:02, 12.21.2.102, GET, /assets/img/hero_100.jpg, 157121, 0',
    '2019-01-01T01:00:01, 12.21.1.102, GET, /assets/js/loader.js, 102, 1',
    '2019-01-01T01:00:03, 12.21.1.108, GET, /assets/js/loader.js, 102, 1',
    '2019-01-01T00:00:04, 12.21.1.107, GET, /assets/js/loader.js, 102, 0',
    '2019-01-01T00:00:05, 12.21.2.108, GET, /assets/img/hero_100.jpg, 157121, 0',
    '2019-01-01T01:00:06, 12.21.1.102, GET, /assets/js/loader.js, 102, 1',
    '2019-01-01T01:00:07, 12.21.1.104, GET, /assets/js/loader.js, 102, 1',
    '2019-01-01T00:00:08, 12.21.2.105, GET, /assets/img/hero_100.jpg, 157121, 0',
    '2019-01-01T01:00:09, 12.21.1.103, GET, /assets/js/loader.js, 102, 1',
    '2019-01-01T00:00:10, 12.21.2.102, GET, /assets/img/hero_100.jpg, 157121, 0',
    '2019-01-01T01:00:11, 12.21.1.101, GET, /assets/js/loader.js, 102, 1',
]

'''
Part 3
Generate a report showing the bytes transferred  to each destination.
Bytes Transferred to destination
IPs, Bytes Transferred
'12.21.1.107': 102,
'12.21.1.104': 157121
'''
def display_access_report3(access_logs):
    # Implementation starts here
    ips=[]
    bytes=[]
    for row_log in access_logs:
        row_log_list=row_log.split(',')
        ips.append(str(row_log_list[1]))
        bytes.append(int(row_log_list[4]))
    zip_data=list(zip(ips,bytes))
    
    print(zip_data)
    
    dict_bytes_transfer={}
    for dest_ip in set(ips):
        dest_ip_list=filter(lambda pair:pair[0]==dest_ip,zip_data)
        
        print("dest_ip_list",dest_ip_list)
        print(len(dest_ip_list))
        dest_ip_list_arr=[dest_ip_list[l][1] for l  in range(len(dest_ip_list))]
        print("dest_ip_list_arr",dest_ip_list_arr)
        dict_bytes_transfer[dest_ip]= sum(dest_ip_list_arr)
    print("Problem # 3: Bytes Transferred to destination")
    print("IPs, Bytes Transferred")
    for k,v in dict_bytes_transfer.items():
      print('{} {}'.format(k,v))

display_access_report3(access_logs)




import re
def extract_phone(input):
  phone_regex=re.compile(r'\d{3} \d{3}-\d{3}$')
  match=phone_regex.search(input)
  if match:
    return match.group()
  return None  

print(extract_phone("my phone is 123 456-833"))