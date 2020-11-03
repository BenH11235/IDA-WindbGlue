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
    remote_path, scp_output = sandbox.send(input_path,config.SANDBOX_DEBUGGING_FOLDER)
    print(scp_output)
    return remote_path


def remote_debug():
    remote_path = send_cur_file_to_sandbox()
    if remote_path != None:
        print("Remote path: ", remote_path)
        ida_dbg.start_process(remote_path,"",config.SANDBOX_DEBUGGING_FOLDER)

def remote_debug_dll():
    input_path = get_input_file_path()
    if not input_path.endswith(".dll"):
        print("Input file name does not end with dll!")
        print("This will cause rundll to silently fail to load it.")
        print("Please rename the input file, set the new path in Debugger->Process options and try again.") 
    remote_path = send_cur_file_to_sandbox()
    ida_dbg.start_process(config.SANDBOX_RUNDLL_PATH,remote_path+" #1",config.SANDBOX_DEBUGGING_FOLDER)
    
    
