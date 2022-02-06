#!/usr/bin/env python3

from netmiko import ConnectHandler

# cisco = {
#     "device_type": "cisco_ios",
#     "host": "158.193.152.122",
#     "username": "admin",
#     "password": "class",
#     "port": 22 
# }

# client = ConnectHandler(**cisco)

# # vystup = client.send_command("sh version")
# # print(vystup)

# vystup = client.send_command("sh ip int brief")
# print(vystup)

# loop = [
#     "int lo100",
#     "ip add 1.2.3.4 255.255.255.255",
#     "no shut"
# ]
# vystup = client.send_config_set(loop)
# print(vystup)

# vystup = client.send_command("sh ip int brief")
# print(vystup)



mikrotik = {
    "device_type": "mikrotik_routeros",
    "host": "158.193.152.116",
    "username": "admin",
    "password": "class",
    "port": 22 
}

client = ConnectHandler(**mikrotik)

vystup = client.send_command("ip add print")
print(vystup)