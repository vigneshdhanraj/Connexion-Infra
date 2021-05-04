# Import gettext module
import gettext

def getmessage(message, lang="en"):
    # Set the local directory
    localedir = './locales'

    # Set up your magic function
    translate = gettext.translation('ppl-doordash-skip', localedir, fallback=True, languages=[lang])
    _ = translate.gettext
    return _(message)
