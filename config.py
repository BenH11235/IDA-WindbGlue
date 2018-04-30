#Path to the local installtion of PuTTY SSH client. This should be a full installation that includes the pscp.exe binary.
LOCAL_PUTTY_DIR = "C:\\Path_to\\PuTTy\\"

#IP address of the sandbox machine.
SANDBOX_IP = "ip.addr.of.sandbox"

#The script requires a working SSH account set up at the sandbox. The username and password of the account go here.
SANDBOX_USERNAME = "username_of_sandbox_account"
SANDBOX_PASSWORD = "password_of_sandbox_account"

#The script requires a pre-existing directory at the sandbox to transfer binary files to.
#Create this directory at the sandbox and set this variable to equal the directory's path.
SANDBOX_DEBUGGING_FOLDER = "C:\directory_that_exists_on_sandbox"
