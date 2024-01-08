from werkzeug.wrappers import Request, Response
from flask import Flask,request
from datetime import datetime
from os import path
import jpype
import jaydebeapi
import os
import logging

app=Flask(__name__)
app.config['SECRET_KEY']='you-will-never-guess'
app.config['SERVER_NAME']='host_name:port'

logtimestamp=datetime.now()
logtimestamp=logtimestamp.strftime("%m%d%Y").upper()

logging.basicConfig(filename='log_file_name'+logtimestamp+'.log',level=logging.DEBUG)


class UpdateForm():
    BUSINESS_UNIT='Parameter1'
    ACCOUNTS='Parameter2'
    INDIVIDUAL_SEGMENTS='Parameter3'
    JOURNAL_ST_DT='Parameter4'
    JOURNAL_ED_DT='Parameter5'
    REQ_NO='Parameter6'
    USER_NAME='Parameter7'


@app.route("/" ,methods=['GET','POST'])
def update():

    logtimestamp=datetime.now()
    logtimestamp=logtimestamp.strftime("%m%d%Y").upper()
    logging.basicConfig(filename='log_file_name'+logtimestamp+'.log',level=logging.DEBUG)

    form=UpdateForm()
    form.BUSINESS_UNIT=request.args.get('BUSINESS_UNIT')
    form.ACCOUNTS = request.args.get('ACCOUNTS')
    form.INDIVIDUAL_SEGMENTS = request.args.get('INDIVIDUAL_SEGMENTS')
    form.REQ_NO = request.args.get('REQ_NO')
    form.USER_NAME = request.args.get('USER_NAME')

    form.JOURNAL_ST_DT = request.args.get('JOURNAL_ST_DT')
    date_time_obj=datetime.strptime(form.JOURNAL_ST_DT,'%m/%d/%Y')
    form.JOURNAL_ST_DT=date_time_obj.strftime("%Y-%m-%d")


    form.JOURNAL_ED_DT = request.args.get('JOURNAL_ED_DT')
    date_time_obj=datetime.strptime(form.JOURNAL_ED_DT,'%m/%d/%Y')
    form.JOURNAL_ED_DT=date_time_obj.strftime("%Y-%m-%d")

    jar=os.getcwd()+'\ojdbc8.jar'
    args='-Djava.class.path=%s' %jar
    jvm_path=jpype.getDefaultJVMPath()
    print(jvm_path)
    if not jpype.isJVMStarted():
        jpype.startJVM(jvm_path,args)
