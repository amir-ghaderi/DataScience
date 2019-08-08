#Impact Model
import codecs
import json

#input = "anroosf1"
#input = "SE125177"
##input = "SEW20033V"
##input = "SINGEQX-CLU-PROD-01"
##input = "GCC"
#input = "SE106619"
#input = input.lower()

#array = JSON.dumps(json)
#jsn = JSON.loads(array)


def impact(input):
    #array = json.dumps(input)
    #jsn = json.loads(array)
    input = input['affectedci']
    input = input.lower()
    #Read Knowledge Base
    csvfile = codecs.open("F:\\Flask Stack\\ImpactModel\\Dependencies\\ImpactModelData2.csv",'r','utf-8')

    affected_items = []

    #Data Strucutre
    # Server, Appcode,Device, Device Type, VirtualHost, Cluster, DataCenter, Hostedapp

    for item in csvfile:
        tmp = item.lower().replace('\r','').replace('\n','').split('`')
        server = tmp[0]
        appcode = tmp[1]
        devicename = tmp[2]
        devicetype = tmp[3]
        virtualhost = tmp[4]
        cluster = tmp[5]
        datacenter = tmp[6]
        hostedapp = tmp[7]
        hostlst = hostedapp.split(',')
    
        if input == server:
            group = {}
            group[server] = [appcode]
            for app in hostlst:
                group[server].append(app)
            group[server] = list(set(group[server]))
            affected_items.append(group)

        if input == devicename:
            group = {}
            group[server] = [appcode]
            for app in hostlst:
                group[server].append(app)
            group[server] = list(set(group[server]))
            affected_items.append(group)

        if input == virtualhost:
            group = {}
            group[server] = [appcode]
            for app in hostlst:
                group[server].append(app)
            group[server] = list(set(group[server]))
            affected_items.append(group)

        if input == cluster:
            group = {}
            group[server] = [appcode]
            for app in hostlst:
                group[server].append(app)
            group[server] = list(set(group[server]))
            affected_items.append(group)

        if input == datacenter:
            group = {}
            group[server] = [appcode]
            for app in hostlst:
                group[server].append(app)
            group[server] = list(set(group[server]))
            affected_items.append(group)

    csvfile.close()

    dic = {'data':affected_items}

    return(dic)



