#!/usr/bin/env python3

from paramiko import SSHClient, AutoAddPolicy

client = SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy())
client.connect("158.193.152.116", port=22, username="admin", password="class", look_for_keys=False, allow_agent=False, timeout=60)

# Cisco
# stdin, stdout, stderr = client.exec_command("sh ip int brief")
# for riadok in stdout:
#     zoznam = riadok.strip("\n").strip("\r").split(" ")
#     for prvok in zoznam:
#         if prvok == "":
#             zoznam.remove(prvok)
#     print(zoznam)

# stdin, stdout, stderr = client.exec_command("sh version")
# for riadok in stdout:
#     print(riadok.strip("\n"))

# Mikrotik RouterOS
stdin, stdout, stderr = client.exec_command("ip address print terse")
for riadok in stdout:
    print(riadok.strip("\n").split(" "))

stdin, stdout, stderr = client.exec_command("interface print terse")
for riadok in stdout:
    print(riadok.strip("\n").split(" "))

stdin, stdout, stderr = client.exec_command("interface bridge add name=lo0")
for riadok in stdout:
    print(riadok.strip("\n").split(" "))

stdin, stdout, stderr = client.exec_command("interface print terse")
for riadok in stdout:
    print(riadok.strip("\n").split(" "))

client.close()