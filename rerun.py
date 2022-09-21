import requests
import asyncio
import json
import base64
import os

rtoken = os.getenv("RTOKEN")
header = {"Authorization": "Bearer {}".format(rtoken)}
link="https://api.github.com/repos/noname201012345/VoiceCamp/contents/"

def rerun():
  await asyncio.sleep(100)
  with open("rerun.json", "r") as f:
      rerun = json.load(f)
  if rerun["id"]==1:
      rerun["id"]=0
  elif rerun["id"]==0:
      rerun["id"]=1
  r = requests.get(link+"rerun.json",headers=header)
  sh=r.json()["sha"]
  base64S= base64.b64encode(bytes(json.dumps(rerun), "utf-8"))
  rjson = {"message":"cf", "content":base64S.decode("utf-8"),"sha":sh}
  response = requests.put(link+"rerun.json", data=json.dumps(rjson), headers=header)
