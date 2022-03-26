import snap7.client as c
from snap7.util import *
from snap7.types import *
import time
from datetime import datetime

def ReadMemory(plc,byte,bit,datatype):
    result = plc.read_area(Areas.MK,0,int(byte),int(datatype))
    if datatype==S7WLBit:
        return get_bool(result,0,bit)
    elif datatype==S7WLByte or datatype==S7WLWord:
        return get_int(result,0)
    elif datatype==S7WLReal:
        return get_real(result,0)
    elif datatype==S7WLDWord:
        return get_dword(result,0)
    else:
        return None

def WriteMemory(plc,byte,bit,datatype,value):
    result = plc.read_area(Areas.MK,0,byte,datatype)
    if datatype==S7WLBit:
        set_bool(result,0,bit,value)
    elif datatype==S7WLByte or datatype==S7WLWord:
        set_int(result,0,value)
    elif datatype==S7WLReal:
        set_real(result,0,value)
    elif datatype==S7WLDWord:
        set_dword(result,0,value)
    plc.write_area(Areas.MK,0,byte,result)

if __name__=="__main__":
    plc = c.Client()
    plc.connect('192.168.0.11',0,1,102)
    # print(plc.get_connected())
    while(True):
        a = ReadMemory(plc,0,0,S7WLBit)
        b = ReadMemory(plc,0,1,S7WLBit)
        c = ReadMemory(plc,0,2,S7WLBit)
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        print(date_time," - Liga :", a, " - Desliga: ", b, " - Motor: ", c)
        time.sleep(1)
    # WriteMemory(plc,420,0,S7WLReal,3.141592)
    # print (ReadMemory(plc,420,0,S7WLReal))