import subprocess
import sys
import os
import config

def quote(s):
    return "\""+s+"\""

def send(fname,target_dir):
    fname_wout_path = fname.split("\\")[-1]
    target_fname = os.path.join(target_dir,fname_wout_path)
    os.chdir(config.LOCAL_PUTTY_DIR)
    pscp_exe = quote(os.path.join(config.LOCAL_PUTTY_DIR,"pscp.exe"))
    copy_to_sandbox_cmd = [
        pscp_exe,
        "-P",
        "22",
        "-pw", 
        config.SANDBOX_PASSWORD, 
        quote(fname), 
        quote(config.SANDBOX_USERNAME)+"@"+config.SANDBOX_IP+":"+quote(target_fname)
    ]
    print("\n")
    print(" ".join(copy_to_sandbox_cmd))
    result = subprocess.check_output(" ".join(copy_to_sandbox_cmd), shell=True)
    return target_fname, result

if __name__ == "__main__":
    fname = sys.argv[1]
    target_dir = sys.argv[2]
    send(fname, target_dir)
