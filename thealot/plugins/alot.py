from .plugin import Plugin
import re


class AlotPlugin(Plugin):

    URL = 'http://hyperboleandahalf.blogspot.co.uk/2010/04/alot-is-better-than-you-at-everything.html'

    help = {
    }

    def hook(self):
        self.bot.hookEvent("pubmsg", self.on_message)

    def unhook(self):
        self.bot.unhookEvent("pubmsg", self.on_message)

    def on_message(self, source=None, target=None, args=None):
        msg = args.lower()
        if msg == 'alot' or msg[:5] == 'alot ' or msg[-5:] == ' alot' \
                or re.search(r'\Walot\W', msg):
            self.message(target, "{}: {}".format(source.nick, AlotPlugin.URL))
