
import logging
log = logging.getLogger("Thug")

def ShellExecute(self, *args):
    cmdLine = ''
    for arg in args:
        if not arg or len(arg) == 0:
            continue

        cmdLine += str(arg)

    log.ThugLogging.add_behavior_warn('[Shell.Application ActiveX] ShellExecute command: ' + cmdLine)

