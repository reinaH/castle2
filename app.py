import sqlite3
from flask import g
import os
import boto3
import requests
from flask import Flask, render_template, request, send_file

app = Flask(__name__)
DATABASE = 'stuff.db'


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = []
    lastid = 0

    if request.method == "POST":

        if ( len(str((request.form['key1'])).strip()) > 0 ) and ( len(str((request.form['key2'])).strip()) > 0 ):

            try:

                ec2 = boto3.client('ec2', aws_access_key_id=request.form['key1'],
                aws_secret_access_key=request.form['key2'])
                res = ec2.describe_instances()

                with sqlite3.connect("stuff.db") as con:
                    cur = con.cursor()
                    print("made connection")

                    cur.execute("INSERT INTO USER (ACCESSKEY) VALUES (?)", (str(request.form['key1']),))
                    this = cur.execute("select last_insert_rowid()") #returned as sqlite3.cursor obj
                    lastid = this.fetchone()[0] #string representation of var


                    con.commit()
                    print("user added")

                for el in res['Reservations']:
                    var = (el['Instances'])
                    for ek in var:
                        one = ek['InstanceId']
                        two = ek['PublicDnsName']
                        three = ek['State']['Name']

                        results.append({'Instance Information': [one,two,three]})
                        cur.execute("INSERT INTO INST (INSTUSER, AWSINSTANCEID, PUBLICDNSNAME, INSTANCESTATE) VALUES (?,?,?,?)", (str(lastid), str(one), str(two), str(three),))
                        con.commit()
                        print("instance added")

            except Exception as e:
                print (e)
                errors.append(e)

    return render_template('index.html', errors=errors, results=results)
    con.close()




if __name__ == '__main__':
    app.run()
