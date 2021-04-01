from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import uvicorn
import io
import requests
import json
import time

app = FastAPI()
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get("/下載網路檔案/")
def 下載網路檔案(檔案網址="https://cameo.tw/mot/mot_sample.csv"):
    os.popen(f"wget").read()
    return {"輸出": 輸出}


@app.get("/")
def read_root():
    return {"fastapi": "yuyu"}


class CameoPost(BaseModel):
    str_project_id: str
    str_data_path: str
    str_csv: str


@app.post("/cameo_post/")
def cameo_post(cameo_post_obj: CameoPost):
    print("str_project_id:"+cameo_post_obj.str_project_id)
    print("str_data_path:"+cameo_post_obj.str_data_path)
    print("str_csv:"+cameo_post_obj.str_csv)
    return cameo_post_obj


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="8123")
