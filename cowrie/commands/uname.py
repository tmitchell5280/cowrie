#

from __future__ import division, absolute_import

from cowrie.shell.honeypot import HoneyPotCommand

commands = {}

class command_uname(HoneyPotCommand):
    def call(self):
        if len(self.args) and self.args[0].strip() in ('-a', '--all'):
            self.write(
                'Linux %s 4.4.0-31-generic #50~14.04.1-Ubuntu SMP Wed Jul 13 01:07:32 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux\n' % \
                self.protocol.hostname)
        elif len(self.args) and self.args[0].strip() in ('-r', '--kernel-release'):
            self.write( '4.4.0-31-generic\n' )
        elif len(self.args) and self.args[0].strip() in ('-m', '--machine'):
            self.write( 'x86_64\n' )
        else:
            self.write('Linux\n')

commands['/bin/uname'] = command_uname
