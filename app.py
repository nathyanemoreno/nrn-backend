from flask import Flask, request, redirect, url_for, jsonify
import pandas as pd
import itertools as it
from ast import literal_eval

app = Flask(__name__)

n_column = 15
interval = 25
@app.route('/')
def index():
    return "<h1>Sistema de combinações</h1>"
@app.route('/listar',methods=['GET', 'POST'] )
def listar():
    f = literal_eval(request.args.get('f', None))
    
    rg = len(f)
    c = it.combinations(range(1,interval+1),n_column)
    filtered = jsonify(list(it.filterfalse(lambda x: x[0:rg] != f, c)))
    return filtered


if __name__ =="__main__":
    app.run(debug=True)