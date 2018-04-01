from idaapi import *
import idc
import subprocess
import sandbox
import config

def send_cur_file_to_sandbox() :
    input_path = get_input_file_path()
    if input_path == None:
        print("ERROR: No input file path. Please set the path in Debugger->Process Options.")
        return None
    return sandbox.send(input_path,config.SANDBOX_DEBUGGING_FOLDER)

def remote_debug():
    remote_path = send_cur_file_to_sandbox()
    if remote_path != None:
        print("Remote path: ", remote_path)
        idc.StartDebugger(remote_path,"",config.SANDBOX_DEBUGGING_FOLDER)
    
    
