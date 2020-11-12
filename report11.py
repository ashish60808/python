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

def display_access_report(access_logs):
    # Implementation starts here
    list_assets=[]
    for row_log in access_logs:
        row_log_list=row_log.split(',')
        list_assets.append(row_log_list[3])      # Extracting the URI Path
    dict_assets={uri: list_assets.count(uri) for uri in list_assets}          #Dictionary comprehension
    sorted_d = sorted(dict_assets.items(), key=lambda x: x[1],reverse=True)
    print(sorted_d)
    print("Problem # 1: Assets count for each URI ")
    print("Asset, Count")
    for k,v in sorted_d:
        print('{} {}'.format(k,v))


#Call a functions
display_access_report(access_logs)