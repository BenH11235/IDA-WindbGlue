Contributed by Check Point Software Technologies, 2018.

# IDA-WindbGlue

These are "glue" scripts, meant to automate the task of copying the currently analyzed executable to a remote VM and starting a debugging session using the remote Windbg debugging server (`dbgsrv.exe`).

## Installation

Simply copy the scripts in this repository to a local directory.

For this script to work requires a fairly extensive set-up of the environment and the configuration in `config.py`. Detailed information of how to properly set up the environment is forthcoming, so stay tuned. 

## Usage

In IDA Pro, choose "run script" (`alt+F7`) and choose the script `windbg_remote.py`.

In the Python console, run: `remote_debug()`. If all goes well, a debugging session should start.

## Contributing

I think this is a useful little script for a decent disassembly / debugging setup. If you have any idea of how to improve it please feel free to email me, send pull requests, etc.

## History

2018-04-01: Initial upload 
