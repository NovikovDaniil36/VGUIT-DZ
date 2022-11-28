# -*- coding: utf-8 -*-

import requests
import json
from tkinter import *


def request_repo():
  repo = 'https://api.github.com/repos/NixOS/nixpkgs'
  data = requests.get(repo).json()
  data = dict((key, data[key]) for key in ['company', 'created_at', 'email', 'id', 'name', 'url'] if key in data)
  with open('repo.json', 'w') as file:
    json.dump(data, file)


tk = Tk()
tk.minsize(400, 150)
tk.title('Novikov Daniil')
Button(tk, text='Get repo', command=request_repo).pack()
tk.mainloop()
