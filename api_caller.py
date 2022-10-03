import requests
from requests.auth import HTTPBasicAuth
import json
import re

srv : str = "http://192.168.178.42:8080"
thing : str = "/rest/things?summary=false"
thing_by_uid : str = "/rest/things/"
link : str = "/rest/links/"
username : str = "admin"
password : str = "Wiggles12"

def get_knx_device_uid():
    filtered_thing = None
    r= requests.get(
        srv + thing, 
        auth=(username, password))

    if r.status_code == 200:   
        res = json.loads(r.text)
        for c in res:
            for key, value in c.items():
                if key == "UID" and "knx:device" in value:
                    filtered_thing = c

        if filtered_thing:
            return filtered_thing
        else:
            raise ValueError("Kein KNX Device gefunden")
    else:
        raise r.raise_for_status()

def get_thing_by_uid(uid:str)-> dict:
    r= requests.get(
        srv + thing_by_uid + uid["UID"], 
        auth=HTTPBasicAuth(username,password))
   
    if r.status_code == 200:
        return json.loads(r.text)
    else:
        r.raise_for_status()

def delete_link(itemname:str,channeluid:str):
    r= requests.get(
        srv + link + itemname + "/" + channeluid, 
        auth=HTTPBasicAuth(username,password))
   
    if r.status_code == 200:
        return json.loads(r.text)

def change_thing(uid, channel_config):

        r= requests.put(
        srv + thing_by_uid + uid["UID"], 
        headers={"Content-Type": "application/json"},
        auth=HTTPBasicAuth(username, password),
        data=channel_config)

        if r.status_code == 200:
            return True
        else:
            raise ValueError(str(r.status_code) + " " + r.text)

def delete_channels(uid, channel_config : str):

    d = json.loads(channel_config)
    d["channels"] = []
    dump =json.dumps(d)
    r= requests.put(
        srv + thing_by_uid + uid["UID"], 
        headers={"Content-Type": "application/json"},
        auth=HTTPBasicAuth(username, password),
        data=dump)


    if r.status_code == 200:
        r.close()
        return True
    else:
        raise ValueError(str(r.status_code) + " " + r.text)
    
    

def get_uid_hex_value(uid : dict):
    if "UID" in uid:
        uid_value = uid["UID"]
        val : list[str]= uid_value.split(":")
        if val.__len__() != 4:
            raise ValueError("ungültiger split, Erwartung ist das 4 Elemente enthalten sind")
        return val[2] + ":" + val[3]
    else:
        raise ValueError("ungültiger Übergabeparameter, UID nicht gesetzt.")