from flask import Flask, request, redirect, url_for, jsonify
import pandas as pd
import itertools as it
from ast import literal_eval

app = Flask(__name__)


# c = it.combinations(range(1,interval+1),n_column)

@app.route('/')
def index():
    return "<h1>Sistema de combinações</h1>"
@app.route('/listar',methods=['GET', 'POST'] )
def listar():
    f = literal_eval(request.args.get('f', None))
    start = literal_eval(request.args.get('start', None))
    end =  literal_eval(request.args.get('end', None))
    n_column = 15
    interval = 25
    if (f != None):
        rg = len(f)
        filtered = jsonify(list(it.filterfalse(lambda x: x[0:rg] != f, it.combinations(range(1,interval+1),n_column))))
        return filtered
    else:
        return jsonify (list(it.islice(it.combinations(range(1,interval+1),n_column), start, end)))

if __name__ =="__main__":
    app.run()