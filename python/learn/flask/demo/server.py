#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route('/')
def demo():
    print(request.path)
    print(request.full_path)
    print(request.args.__str__())
    r = request.args.get('user', 'dong')
    return r


@app.route('/register', methods=['POST', 'GET'])
def register():
    print(request.headers)
    # print(request.stream.read())
    print(request.form)
    print(request.form['name'])
    print(request.form.get('name'))
    print(request.form.getlist('name'))
    print(request.form.get('nickname', default='little apple'))
    return 'welcome'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8822, debug=True)
