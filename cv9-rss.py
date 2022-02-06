#!/usr/bin/env python3

from tkinter.constants import DISABLED, NORMAL
import urllib.request as URL_Req
import xml.etree.ElementTree as XML_Tree

import tkinter as tk
import ssl

def parsujRSS(paURL):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    otvorene_rss = URL_Req.urlopen(paURL, context=ctx)
    stranka = otvorene_rss.read()

    koren = XML_Tree.fromstring(stranka)
    retazec = ""
    for channel in koren:
        for item in channel:
            # ak nie som v item tagu, tak nic nerob
            if item.tag != "item":
                continue

            title = ""
            desc = ""
            link = ""
            date = ""
            for polozka in item:
                if polozka.tag == "title":
                    title = polozka.text
                elif polozka.tag == "description":
                    desc = polozka.text
                elif polozka.tag == "link":
                    link = polozka.text
                elif polozka.tag == "pubDate":
                    date = polozka.text
            retazec += "Nadpis: {} - {}, URL: {}, {}\n\n".format(
                title, desc, link, date
            )
    return retazec

def vykonajTlacidlo(urlPole, vystupPole):
    vystupPole.config(state=NORMAL)
    vystupPole.delete(1.0, tk.END)
    url = urlPole.get()
    retazec = parsujRSS(url)
    vystupPole.insert(tk.END, retazec)
    vystupPole.config(state=DISABLED)

if __name__ == "__main__":
    url = "http://www.dsl.sk/export/rss_articles.php"
    # sprava = parsujRSS(url)
    # print(sprava)

    root = tk.Tk()
    root.title("RSS Reader v0.1")
    root.geometry("670x470+300+200")
    root.resizable(False,False)

    label = tk.Label(root, text="URL")
    label.grid(row=0, column=0, padx=10)

    urlPole = tk.Entry(root)
    urlPole.grid(row=0, column=1, pady=10, ipadx=180)
    urlPole.insert(0, url)

    vystupPole = tk.Text(root)
    vystupPole.grid(row=1, column=0, columnspan=3, padx=10)

    parsujTlacidlo = tk.Button(root, text="Parsuj", command=lambda: vykonajTlacidlo(urlPole, vystupPole))
    parsujTlacidlo.grid(row=0, column=2, padx=10)

    root.mainloop()