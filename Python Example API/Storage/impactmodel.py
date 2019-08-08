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
    csvfile = codecs.open("F:\\FlaskEndpoints\\ImpactModel\\Dependencies\\ImpactModelData2.csv",'r','utf-8')

    affected_servers =[]
    affected_appcodes = []

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
            affected_servers.append(server)
            affected_appcodes.append(appcode)
            for app in hostlst:
                affected_appcodes.append(app)

        if input == devicename:
            affected_servers.append(server)
            affected_appcodes.append(appcode)
            for app in hostlst:
                affected_appcodes.append(app)

        if input == virtualhost:
            affected_servers.append(server)
            affected_appcodes.append(appcode)
            for app in hostlst:
                affected_appcodes.append(app)

        if input == cluster:
            affected_servers.append(server)
            affected_appcodes.append(appcode)
            for app in hostlst:
                affected_appcodes.append(app)

        if input == datacenter:
            affected_servers.append(server)
            affected_appcodes.append(appcode)
            for app in hostlst:
                affected_appcodes.append(app)

    csvfile.close()

    try:
        affected_servers.remove('N/A')
        affected_appcodes.remove('N/A')
    except:
        pass

    affected_servers = list(set(affected_servers))
    affected_appcodes =  list(set(affected_appcodes))

    dic = {}
    dic['appcodes'] = affected_appcodes
    dic['servers'] = affected_servers
    return(dic)



