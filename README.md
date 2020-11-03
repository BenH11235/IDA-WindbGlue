Contributed by Check Point Software Technologies, 2018.

# IDA-WindbGlue

These are "glue" scripts, meant to automate the task of copying the currently analyzed executable to a remote VM and starting a debugging session using the remote Windbg debugging server (`dbgsrv.exe`).
These scripts are updated for the overhauled IDA 7.0 API.

## Installation

Simply copy the scripts in this repository to a local directory.

For this script to work requires a fairly extensive set-up of the environment and the configuration in `config.py`. Detailed information of how to properly set up the environment is available [here](https://research.checkpoint.com/2018/scriptable-remote-debugging-windbg-ida-pro/).

## Usage

First, set up the full environment including the remote debugging host, as explained in the link above.

In IDA Pro, choose "run script" (`alt+F7`) and choose the script `windbg_remote.py`.

In the Python console, run: `remote_debug()`. If all goes well, a debugging session should start.

## Contributing

I think this is a useful little script for a decent disassembly / debugging setup. If you have any idea of how to improve it please feel free to email me, send pull requests, etc.

## History

2020-11-03: Added link to blog post (which has existed for ages, really), updated to support IDA 7.0 API
2018-04-01: Initial upload 
