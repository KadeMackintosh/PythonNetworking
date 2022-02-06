#!/usr/bin/env python3

from flask import Flask, render_template, request
import requests

IP = "158.193.152.116"
PORT = 443
USER = "admin"
PASS = "class"

def dajRozhrania(paIP, paPort, paUser, paPass):
    odpoved = requests.get("https://{}:{}/rest/interface".format(paIP, paPort), auth=(paUser,paPass), verify=False)
    if odpoved.status_code == 200:
        vystup = list()
        for polozka in odpoved.json():
            vystup.append(dict(name=polozka["name"]))
        return vystup
    else:
        print(odpoved.status_code)
        print(odpoved.json())
        return None

def dajIP(paIP, paPort, paUser, paPass):
    odpoved = requests.get("https://{}:{}/rest/ip/address".format(paIP, paPort), auth=(paUser,paPass), verify=False)
    if odpoved.status_code == 200:
        return odpoved.json()
    else:
        print(odpoved.status_code)
        print(odpoved.json())
        return None

def nastavIP(paIP, paPort, paUser, paPass, paAdresa, paRozhranie):
    ip = {"address": paAdresa, "interface": paRozhranie}
    odpoved = requests.put("https://{}:{}/rest/ip/address".format(paIP, paPort), auth=(paUser,paPass), verify=False, json=ip)
    if odpoved.status_code == 201:
        return odpoved.json()
    else:
        print(odpoved.status_code)
        print(odpoved.json())
        return None

def vytvorLoop(paIP, paPort, paUser, paPass, paRozhranie):
    ip = {"name": paRozhranie}
    odpoved = requests.put("https://{}:{}/rest/interface/bridge".format(paIP, paPort), auth=(paUser,paPass), verify=False, json=ip)
    if odpoved.status_code == 201:
        return odpoved.json()
    else:
        print(odpoved.status_code)
        print(odpoved.json())
        return None

def dajRozhraniaIP():
    rozhrania = dajRozhrania(IP,PORT,USER,PASS)
    ip = dajIP(IP,PORT,USER,PASS)
    vystup = list()
    for rozhranie in rozhrania:
        address = ""
        for i in ip:
            if rozhranie["name"] == i["interface"]:
                address += i["address"] + " "
        vystup.append(dict(name=rozhranie["name"], address=address))
    return vystup

app = Flask(__name__)

@app.route("/")
def index():
    rozhrania = dajRozhraniaIP()
    # vystup = "<table>"
    # vystup += "<tr><th>Rozhranie</th><th>IP</th></tr>"
    # for rozhranie in rozhrania:
    #     vystup += "<tr><td>{}</td><td>{}</td></tr>".format(rozhranie["name"], rozhranie["address"])
    # vystup += "</table>"
    # return vystup
    return render_template("index.html", data=rozhrania)

@app.route("/loop", methods=("GET", "POST"))
def loop():
    if request.method == "GET":
        return render_template("loop.html")
    else:
        rozhranie = request.form["name"]
        if vytvorLoop(IP,PORT,USER,PASS,rozhranie) == None:
            return render_template("vystup.html",sprava="Chyba")
        else:
            text = "Loopback {} bol uspesne vytvoreny.".format(rozhranie)
            return render_template("vystup.html",sprava=text)

@app.route("/ip", methods=("GET", "POST"))
def ip():
    if request.method == "GET":
        return render_template("ip.html")
    else:
        rozhranie = request.form["interface"]
        adresa = request.form["address"]
        if nastavIP(IP,PORT,USER,PASS,adresa,rozhranie) == None:
            return render_template("vystup.html",sprava="Chyba")
        else:
            text = "Adresa {} bola uspesne nastavena na rozhranie {}.".format(adresa, rozhranie)
            return render_template("vystup.html",sprava=text)

if __name__ == "__main__":
    # vystup = vytvorLoop(IP,PORT,USER,PASS,"lo111")
    # print(vystup)
    app.run("0.0.0.0", 8888)