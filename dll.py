import datetime

# Colors
billet='\u001b['

Fore=dict(
    list(
        zip(
            ['black',
            'red',
            'green',
            'yellow',
            'blue',
            'purple',
            'cyan',
            'white'
            ],
            list(range(30, 38))
        )
    )
)
Style=dict(
    list(
        zip(
            [
            'bold',
            'faded',
            'italics',
            'underlined',
            'flashing',
            'striketrough'
            ],
            list(range(1,10))
        )
    )
)
Background=dict(
    list(
        zip(
            [
            'black',
            'red',
            'green',
            'yellow',
            'blue',
            'purple',
            'cyan',
            'white'
            ],
            list(range(40, 48))
        )
    )
)

class ANSIError(Exception): ...
class SetColor(ANSIError):
    def Fore(color, skip_error=False):
        ANSImode()
        if skip_error == False:
            if color not in Fore:
                raise ANSIError(f'Not Found Color -> {color}')
            else:
                return billet+str(Fore[color])+'m'
    def Style(type, skip_error=False):
        ANSImode()
        if skip_error == False:
            if type not in Style:
                raise ANSIError(f'Not Found Color -> {type}')
            else:
                return billet+str(Style[type])+'m'
    def BackGround(color, skip_error=False):
        ANSImode()
        if skip_error == False:
            if color not in Fore:
                raise ANSIError(f'Not Found Color -> {color}')
            else:
                return billet+str(Background[color])+'m'
    def Clear():
        ANSImode()
        return billet+str(0)+'m'
def ANSImode():
    import ctypes, os
    if os.sys.platform == "win32":
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    else:
        pass

# LOGer
Root = 'root'

Text = str

View_dict = {
    'View':{
        'txt':  [
                'text', 'txt', 'log', 'TXT', 'LOG'
                ],
        'str':  [
                'str', 'STR', 'out'
                ]
    }
}

def _main_debug_(_TEXT_, _NickName, _Sender, _TypeMSG):
    if _Sender == False or _Sender == None:
        _Send = False
    else:
        _Send = True
    if _TypeMSG == False or _TypeMSG == None:
        msg = False
    else:
        msg = True
    if _Send == True:
        if msg == True:
            return f'[ {_NickName} ] - [ DEBUG {_TEXT_} ] --- {_Sender} <--- {_TypeMSG} '
        else:
            return f'[ {_NickName} ] - [ DEBUG {_TEXT_} ] --- {_Sender} '
    else:
        if msg == True:
            return f'[ {_NickName} ] - [ DEBUG {_TEXT_} ] <--- {_TypeMSG} '
        else:
            return f'[ {_NickName} ] - [ DEBUG {_TEXT_} ]'
def _main_info_(_TEXT_, _NickName):
    return f'[ {_NickName} ] - [ INFO {_TEXT_} ] '
def _main_error_(_TEXT_, _NickName, _Sender, _TypeError, _TypeMSG):
    if _Sender == False or _Sender == None:
        _Send = False
    else:
        _Send = True
    if _TypeError == False or _TypeError == None:
        _TE = False
    else:
        _TE = True
    if _TypeMSG == False or _TypeMSG == None:
        msg = False
    else:
        msg = True
    if _Send == True:
        if _TE == True:
            if msg == True:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] --- {_TypeError} --- {_Sender} <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] --- {_TypeError} --- {_Sender} '
        else:
            if msg == True:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] --- {_Sender} <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] --- {_Sender}'
    else:
        if _TE == True:
            if msg == True:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] --- {_TypeError} <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] --- {_TypeError} '
        else:
            if msg == True:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ]'
def _main_warning_(_TEXT_, _NickName, _TypeMSG):
    if _TypeMSG == False or _TypeMSG == None:
        msg = False
    else:
        msg = True
    if msg == True:
        return f'[ {_NickName} ] - [ WARNING {_TEXT_} ] <--- {_TypeMSG} '
    else:
        return f'[ {_NickName} ] - [ WARNING {_TEXT_} ]'

def _debug_(View, TEXT=Text, NickName=Root, Sender=None, TypeMSG=None, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View =='str':
        if WriteTime == True:
            print(
                _main_debug_(
                            _TEXT_=TEXT,
                            _NickName=NickName, 
                            _Sender=Sender, 
                            _TypeMSG=TypeMSG
                            ) + str(datetime.datetime.now())
            )
        else:
            print(
                _main_debug_(
                            _TEXT_=TEXT,
                            _NickName=NickName, 
                            _Sender=Sender, 
                            _TypeMSG=TypeMSG
                            )
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_debug_(
                                _TEXT_=TEXT, 
                                _NickName=NickName, 
                                _Sender=Sender, 
                                _TypeMSG=TypeMSG
                                ) + str(datetime.datetime.now())
        else:
            return _main_debug_(
                                _TEXT_=TEXT, 
                                _NickName=NickName, 
                                _Sender=Sender, 
                                _TypeMSG=TypeMSG
                                )
def _info_(View, TEXT=Text, NickName=Root, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View == 'str':
        if WriteTime == True:
            print(
                _main_info_(
                            _TEXT_=TEXT,
                            _NickName=NickName
                ) + str(datetime.datetime.now())
            )
        else:
            print(
                _main_info_(
                            _TEXT_=TEXT,
                            _NickName=NickName
                ) 
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_info_(
                            _TEXT_=TEXT,
                            _NickName=NickName
                ) + str(datetime.datetime.now())
        else:
            return _main_info_(
                            _TEXT_=TEXT,
                            _NickName=NickName
                )
def _error_(View, TEXT=Text, NickName=Root, Sender=None, TypeError=None, TypeMSG=None, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View == 'str':
        if WriteTime == True:
            print(
                _main_error_(
                            _TEXT_=TEXT,
                            _NickName=NickName,
                            _Sender=Sender,
                            _TypeError=TypeError,
                            _TypeMSG=TypeMSG
                ) + str(datetime.datetime.now()))
        else:
            print(
                _main_error_(
                            _TEXT_=TEXT,
                            _NickName=NickName,
                            _Sender=Sender,
                            _TypeError=TypeError,
                            _TypeMSG=TypeMSG
                )
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_error_(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _Sender=Sender,
                                _TypeError=TypeError,
                                _TypeMSG=TypeMSG
                ) + str(datetime.datetime.now())
        else:
            return _main_error_(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _Sender=Sender,
                                _TypeError=TypeError,
                                _TypeMSG=TypeMSG
                )

def _warning_(View, TEXT=Text, NickName=Root, TypeMSG=None, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View == 'str':
        if WriteTime == True:
            print(
                _main_warning_(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _TypeMSG=TypeMSG
                                ) + str(datetime.datetime.now())
            )
        else:
            print(
                _main_warning_(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _TypeMSG=TypeMSG
                                )
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_warning_(
                                    _TEXT_=TEXT,
                                    _NickName=NickName,
                                    _TypeMSG=TypeMSG
            ) + str(datetime.datetime.now())
        else:
            return _main_warning_(
                                    _TEXT_=TEXT,
                                    _NickName=NickName,
                                    _TypeMSG=TypeMSG
            )

def _main_debug_color(_TEXT_, _NickName, _Sender, _TypeMSG):
    if _Sender == False or _Sender == None:
        _Send = False
    else:
        _Send = True
    if _TypeMSG == False or _TypeMSG == None:
        msg = False
    else:
        msg = True
    if _Send == True:
        if msg == True:
            return f'[ {_NickName} ] - [ {SetColor.Fore(color="green")}{SetColor.Style(type="bold")}{SetColor.Style(type="underlined")}DEBUG{SetColor.Clear()} {_TEXT_} ] --- {_Sender} <--- {_TypeMSG} '
        else:
            return f'[ {_NickName} ] - [ {SetColor.Fore(color="green")}{SetColor.Style(type="bold")}{SetColor.Style(type="underlined")}DEBUG{SetColor.Clear()} {_TEXT_} ] --- {_Sender} '
    else:
        if msg == True:
            return f'[ {_NickName} ] - [ {SetColor.Fore(color="green")}{SetColor.Style(type="bold")}{SetColor.Style(type="underlined")}DEBUG{SetColor.Clear()} {_TEXT_} ] <--- {_TypeMSG} '
        else:
            return f'[ {_NickName} ] - [ {SetColor.Fore(color="green")}{SetColor.Style(type="bold")}{SetColor.Style(type="underlined")}DEBUG{SetColor.Clear()} {_TEXT_} ]'
def _main_info_color(_TEXT_, _NickName):
    return f'[ {_NickName} ] - [ {SetColor.Fore(color="green")}{SetColor.Style(type="bold")}INFO{SetColor.Clear()} {_TEXT_} ] '
def _main_error_color(_TEXT_, _NickName, _Sender, _TypeError, _TypeMSG):
    if _Sender == False or _Sender == None:
        _Send = False
    else:
        _Send = True
    if _TypeError == False or _TypeError == None:
        _TE = False
    else:
        _TE = True
    if _TypeMSG == False or _TypeMSG == None:
        msg = False
    else:
        msg = True
    if _Send == True:
        if _TE == True:
            if msg == True:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] --- {_TypeError} --- {_Sender} <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] --- {_TypeError} --- {_Sender} '
        else:
            if msg == True:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] --- {_Sender} <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] --- {_Sender}'
    else:
        if _TE == True:
            if msg == True:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] --- {_TypeError} <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] --- {_TypeError} '
        else:
            if msg == True:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ]'
def _main_warning_color(_TEXT_, _NickName, _TypeMSG):
    if _TypeMSG == False or _TypeMSG == None:
        msg = False
    else:
        msg = True
    if msg == True:
        return f'[ {_NickName} ] - [ {SetColor.Fore(color="yellow")}{SetColor.Style(type="bold")}WARNING{SetColor.Clear()} {_TEXT_} ] <--- {_TypeMSG} '
    else:
        return f'[ {_NickName} ] - [ {SetColor.Fore(color="yellow")}{SetColor.Style(type="bold")}WARNING{SetColor.Clear()} {_TEXT_} ]'

def _debug_color_(View, TEXT=Text, NickName=Root, Sender=None, TypeMSG=None, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View =='str':
        if WriteTime == True:
            print(
                _main_debug_color(
                            _TEXT_=TEXT,
                            _NickName=NickName, 
                            _Sender=Sender, 
                            _TypeMSG=TypeMSG
                            ) + str(datetime.datetime.now())
            )
        else:
            print(
                _main_debug_color(
                            _TEXT_=TEXT,
                            _NickName=NickName, 
                            _Sender=Sender, 
                            _TypeMSG=TypeMSG
                            )
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_debug_color(
                                _TEXT_=TEXT, 
                                _NickName=NickName, 
                                _Sender=Sender, 
                                _TypeMSG=TypeMSG
                                ) + str(datetime.datetime.now())
        else:
            return _main_debug_color(
                                _TEXT_=TEXT, 
                                _NickName=NickName, 
                                _Sender=Sender, 
                                _TypeMSG=TypeMSG
                                )
def _info_color(View, TEXT=Text, NickName=Root, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View == 'str':
        if WriteTime == True:
            print(
                _main_info_color(
                            _TEXT_=TEXT,
                            _NickName=NickName
                ) + str(datetime.datetime.now())
            )
        else:
            print(
                _main_info_color(
                            _TEXT_=TEXT,
                            _NickName=NickName
                ) 
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_info_color(
                            _TEXT_=TEXT,
                            _NickName=NickName
                ) + str(datetime.datetime.now())
        else:
            return _main_info_color(
                            _TEXT_=TEXT,
                            _NickName=NickName
            )
def _error_color(View, TEXT=Text, NickName=Root, Sender=None, TypeError=None, TypeMSG=None, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View == 'str':
        if WriteTime == True:
            print(
                _main_error_color(
                            _TEXT_=TEXT,
                            _NickName=NickName,
                            _Sender=Sender,
                            _TypeError=TypeError,
                            _TypeMSG=TypeMSG
                ) + str(datetime.datetime.now()))
        else:
            print(
                _main_error_color(
                            _TEXT_=TEXT,
                            _NickName=NickName,
                            _Sender=Sender,
                            _TypeError=TypeError,
                            _TypeMSG=TypeMSG
                )
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_error_color(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _Sender=Sender,
                                _TypeError=TypeError,
                                _TypeMSG=TypeMSG
                ) + str(datetime.datetime.now())
        else:
            return _main_error_color(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _Sender=Sender,
                                _TypeError=TypeError,
                                _TypeMSG=TypeMSG
                )
def _warning_color(View, TEXT=Text, NickName=Root, TypeMSG=None, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View == 'str':
        if WriteTime == True:
            print(
                _main_warning_color(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _TypeMSG=TypeMSG
                                ) + str(datetime.datetime.now())
            )
        else:
            print(
                _main_warning_color(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _TypeMSG=TypeMSG
                                )
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_warning_color(
                                    _TEXT_=TEXT,
                                    _NickName=NickName,
                                    _TypeMSG=TypeMSG
            ) + str(datetime.datetime.now())
        else:
            return _main_warning_color(
                                    _TEXT_=TEXT,
                                    _NickName=NickName,
                                    _TypeMSG=TypeMSG
            )

typeloglist = {
            "Type":{
                "error": ['error', 'ERROR', 'Error'],
                "debug": ['debug', 'DEBUG', 'Debug'],
                "warning": ['warning', 'WARNING', 'Warning', 'Warn'],
                "info": ['info', 'INFO', 'Info']
            }
        }

class autolog:
    def __init__(self, typelog, text, typemsg=None, wayerror=bytes, waydebug=bytes, waywarn=bytes, wayinfo=bytes, waygeneral=bytes, nick=Root, without_out_console=True | False):
        for k, v in typeloglist["Type"].items():
            if typelog in v:
                typelog=k
        if typelog == 'error':
            if without_out_console == True:
                with open(wayerror, 'a') as error_log:
                    error_log.write(_error_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                try:
                    with open(waygeneral) as general_log:
                        general_log.write(_error_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
            elif without_out_console == False:
                with open(wayerror, 'a') as error_log:
                    error_log.write(_error_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                _error_(View='str', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=False)
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_error_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) +'\n')
                except TypeError:
                    pass
        elif typelog == 'debug':
            if without_out_console == True:
                with open(waydebug, 'a') as debug_log:
                    debug_log.write(_debug_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_debug_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
            elif without_out_console == False:
                with open(waydebug, 'a') as debug_log:
                    debug_log.write(_debug_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                _debug_(View='str', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=False)
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_debug_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
        elif typelog == 'warning':
            if without_out_console == True:
                with open(waywarn, 'a') as warn_log:
                    warn_log.write(_warning_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_warning_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
            elif without_out_console == False:
                with open(waywarn, 'a') as warn_log:
                    warn_log.write(_warning_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                _warning_(View='str', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=False)
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_warning_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
        elif typelog == 'info':
            if without_out_console == True:
                with open(wayinfo, 'a') as info_log:
                    info_log.write(_info_(View='txt', TEXT=text, NickName=nick, WriteTime=True) + '\n')
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_info_(View='txt', TEXT=text, NickName=nick, WriteTime=True) + '\n')
                except TypeError:
                    pass
            elif without_out_console == False:
                with open(wayinfo, 'a') as info_log:
                    info_log.write(_info_(View='txt', TEXT=text, NickName=nick, WriteTime=True) + '\n')
                _info_(View='str', TEXT=text, NickName=nick, WriteTime=False)
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_info_(View='txt', TEXT=text, NickName=nick, WriteTime=True) + '\n')
                except TypeError:
                    pass
class autolog_color:
    def __init__(self, typelog, text, typemsg=None, wayerror=bytes, waydebug=bytes, waywarn=bytes, wayinfo=bytes, waygeneral=bytes, nick=Root, without_out_console=True | False):
        for k, v in typeloglist["Type"].items():
            if typelog in v:
                typelog=k
        if typelog == 'error':
            if without_out_console == True:
                with open(wayerror, 'a') as error_log:
                    error_log.write(_error_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                try:
                    with open(waygeneral) as general_log:
                        general_log.write(_error_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
            elif without_out_console == False:
                with open(wayerror, 'a') as error_log:
                    error_log.write(_error_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                _error_color(View='str', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=False)
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_error_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) +'\n')
                except TypeError:
                    pass
        elif typelog == 'debug':
            if without_out_console == True:
                with open(waydebug, 'a') as debug_log:
                    debug_log.write(_debug_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_debug_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
            elif without_out_console == False:
                with open(waydebug, 'a') as debug_log:
                    debug_log.write(_debug_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                _debug_color_(View='str', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=False)
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_debug_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
        elif typelog == 'warning':
            if without_out_console == True:
                with open(waywarn, 'a') as warn_log:
                    warn_log.write(_warning_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_warning_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
            elif without_out_console == False:
                with open(waywarn, 'a') as warn_log:
                    warn_log.write(_warning_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                _warning_color(View='str', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=False)
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_warning_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
        elif typelog == 'info':
            if without_out_console == True:
                with open(wayinfo, 'a') as info_log:
                    info_log.write(_info_(View='txt', TEXT=text, NickName=nick, WriteTime=True) + '\n')
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_info_(View='txt', TEXT=text, NickName=nick, WriteTime=True) + '\n')
                except TypeError:
                    pass
            elif without_out_console == False:
                with open(wayinfo, 'a') as info_log:
                    info_log.write(_info_(View='txt', TEXT=text, NickName=nick, WriteTime=True) + '\n')
                _info_color(View='str', TEXT=text, NickName=nick, WriteTime=False)
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_info_(View='txt', TEXT=text, NickName=nick, WriteTime=True) + '\n')
                except TypeError:
                    pass

class Handlers:
    class Type:
        class DataError(BaseException): ...
        class ParametersError(BaseException): ...
        class RequestsError(BaseException): ...
        import json
        def __init__(self, debug=True):
            self.debug=debug
        def __text__(self, name, *info, _answer):
            if name == "break_ip":
                try:
                    datatextip = f"""
    Continent        :::{info[0]}:::
    Country          :::{info[1]}:::
    Region           :::{info[2]}:::
    City             :::{info[3]}:::
    Lat              :::{info[4]}:::
    Lon              :::{info[5]}:::
    ISP              :::{info[6]}:::
    ORG              :::{info[7]}:::
    AS               :::{info[8]}:::
    ASName           :::{info[9]}:::
    Reverse          :::{info[10]}:::
    MobileConnection :::{info[11]}:::
    ProxyConnection  :::{info[12]}:::
    Hosting          :::{info[13]}:::"""
                    data_frametextip = f"""
    :::{info[0]}:::
    :::{info[1]}:::
    :::{info[2]}:::
    :::{info[3]}:::
    :::{info[4]}:::
    :::{info[5]}:::
    :::{info[6]}:::
    :::{info[7]}:::
    :::{info[8]}:::
    :::{info[9]}:::
    :::{info[10]}:::
    :::{info[11]}:::
    :::{info[12]}:::
    :::{info[13]}:::"""
                except: raise self.DataError("Error work with data")
                finally:
                    if _answer == "text": 
                        return data_frametextip
                    if _answer == "all": 
                        return datatextip
                    else : raise self.ParametersError(f"Not found parameters -> {_answer}")
            if name == "break_number":
                try:
                    datatextnumber = f"""
    Operator    :::{info[0]}:::
    MNC         :::{info[1]}:::
    Brand       :::{info[2]}:::
    INN         :::{info[3]}:::
    Work_Mobile :::{info[4]}:::
    Name        :::{info[5]}:::
    """
                    data_frametextnumber = f"""
    :::{info[0]}:::
    :::{info[1]}:::
    :::{info[2]}:::
    :::{info[3]}:::
    :::{info[4]}:::
    :::{info[5]}:::
    """
                except: raise self.DataError("Error work with data")
                finally:
                    if _answer == "text": 
                        return data_frametextnumber
                    if _answer == "all": 
                        return datatextnumber
                    else : raise self.ParametersError(f"Not found parameters -> {_answer}")
            if name == "break_mac":
                try:
                    data = f"""
    Company   :::{info[0]}:::
    Address   :::{info[1]}:::
    BlockSize :::{info[3]}:::
    """
                    data_frame = f"""
    :::{info[0]}:::
    :::{info[1]}:::
    :::{info[3]}:::
    """
                except: raise self.DataError("Error work with data")
                finally:
                    if _answer == "text": 
                        return data_frame
                    if _answer == "all": 
                        return data
                    else : raise self.ParametersError(f"Not found parameters -> {_answer}")
        def __json__(self, name, *info, path):
            if name == "break_ip":
                try:
                    data_framejsonip = {
                        "Continent":f"{info[0]}",
                        "Country":f"{info[1]}",
                        "Region":f"{info[2]}",
                        "City":f"{info[3]}",
                        "Lat":f"{info[4]}",
                        "Lon":f"{info[5]}",
                        "ISP":f"{info[6]}",
                        "ORG":f"{info[7]}",
                        "AS":f"{info[8]}",
                        "ASName":f"{info[9]}",
                        "Reverse":f"{info[10]}",
                        "MobileConnection":f"{info[11]}",
                        "ProxyConnection":f"{info[12]}",
                        "Hosting":f"{info[13]}"
                    }
                except: raise self.DataError("Error work with data")
                finally:
                    with open(path, 'w', encoding='utf-8') as file : self.json.dump(data_framejsonip, file)
                    if self.debug == True : print(data_framejsonip), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                    if self.debug == False : pass
            if name == "break_number":
                try:
                    data_framejsonnumber = {
                        "Operator":f"{info[0]}",
                        "MNC":f"{info[1]}",
                        "Brand":f"{info[2]}",
                        "INN":f"{info[3]}",
                        "Work_Mobile":f"{info[4]}",
                        "Name":f"{info[5]}"
                    }
                except: raise self.DataError("Error work with data")
                finally:
                    with open(path, 'w', encoding='utf-8') as file : self.json.dump(data_framejsonnumber, file)
                    match self.debug:
                        case True : print(data_framejsonnumber), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                        case False : pass
            if name == "break_mac":
                try:
                    data_framejsonmac = {
                        "Company":f"{info[0]}",
                        "Address":f"{info[1]}",
                        "BlockSize":f"{info[2]}"
                    }
                except: raise self.DataError("Error work with data")
                finally:
                    with open(path, 'w', encoding='utf-8') as file : self.json.dump(data_framejsonmac, file)
                    if self.debug == True : print(data_framejsonmac), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                    if self.debug == False : pass
        def __file__(self, name, *info, path, view="ini", _mode="w"):
            if name == "break_ip":
                if view == "ini":
                    try:
                        datainiip = f"""
    [IP]
    Continent={info[0]}
    Country={info[1]}
    Region={info[2]}
    City={info[3]}
    Lat={info[4]}
    Lon={info[5]}
    ISP={info[6]}
    ORG={info[7]}
    AS={info[8]}
    ASName={info[9]}
    Reverse={info[10]}
    MobileConnection={info[11]}
    ProxyConnection={info[12]}
    Hosting={info[13]}"""
                    except: raise self.DataError("Error work with data")
                    finally:
                        with open(path, mode=_mode, encoding='utf-8') as file : file.write(datainiip)
                        if self.debug == True : print(datainiip), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                        if self.debug == False : pass
                if view == "txt":
                    try:
                        datatxtip = f"""
    {info[0]}
    {info[1]}
    {info[2]}
    {info[3]}
    {info[4]}
    {info[5]}
    {info[6]}
    {info[7]}
    {info[8]}
    {info[9]}
    {info[10]}
    {info[11]}
    {info[12]}
    {info[13]}"""
                        print(datatxtip)
                    except: raise self.DataError("Error work with data")
                    finally:
                        with open(path, mode=_mode, encoding='utf-8') as file : file.write(datatxtip)
                        if self.debug == True : print(datatxtip), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                        if self.debug == False : pass
                else: self.ParametersError(f"Not found parameters -> {view}")
            if name == "break_number":
                if view == "ini":
                    try:
                        dataininumber = f"""
    [NumberPhone]
    Operator={info[0]}
    MNC={info[1]}
    Brand={info[2]}
    INN={info[3]}
    Work_Mobile={info[4]}
    Name={info[5]}
    """
                    except: raise self.DataError("Error work with data")
                    finally:
                        with open(path, mode=_mode, encoding='utf-8') as file : file.write(dataininumber)
                        if self.debug == True : print(dataininumber), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                        if self.debug == False : pass
                if view == "txt":
                    try:
                        datatxtnumber = f"""
    {info[0]}
    {info[1]}
    {info[2]}
    {info[3]}
    {info[4]}
    {info[5]}
    """
                    except: raise self.DataError("Error work with data")
                    finally:
                        with open(path, mode=_mode, encoding='utf-8') as file : file.write(datatxtnumber)
                        if self.debug == True : print(datatxtnumber), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                        if self.debug == False : pass
                else : raise self.ParametersError(f"Not found parameters -> {view}")
            if name == "break_mac":
                if view == "ini":
                    try:
                        datainimac = f"""
    [MAC]
    Company={info[0]}
    Address={info[1]}
    BlockSize={info[3]}
    """
                    except: raise self.DataError("Error work with data")
                    finally:
                        with open(path, mode=_mode, encoding='utf-8') as file : file.write(datainimac)
                        match self.debug:
                            case True : print(datainimac), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                            case False : pass
                if view == "txt":
                    try:
                        datatxtmac = f"""
    {info[0]}
    {info[1]}
    {info[3]}
    """
                    except: raise self.DataError("Error work with data")
                    finally:
                        with open(path, mode=_mode, encoding='utf-8') as file : file.write(datatxtmac)
                        if self.debug == True : print(datatxtmac), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                        if self.debug == False : pass
                else : raise self.ParametersError(f"Not found parameters -> {view}")
        def __html__(self, name, *info, path):
            if name == "break_ip":
                try:
                    datahtmlip = f"""<!DOCTYPE html>
    <head>
        <title>TWSEConsoleFUP 0.3</title>
        <meta charset="utf-8">
    </head>
    <body>
        <div class="Continent">{info[0]}
        </div>
        <div class="Country">{info[1]}
        </div>
        <div class="RegionName">{info[2]}
        </div>
        <div class="City">{info[3]}
        </div>
        <div class="Lat">{info[4]}
        </div>
        <div class="Lon">{info[5]}
        </div>
        <div class="ISP">{info[6]}
        </div>
        <div class="ORG">{info[7]}
        </div>
        <div class="AS">{info[8]}
        </div>
        <div class="ASName">{info[9]}
        </div>
        <div class="Reverse">{info[10]}
        </div>
        <div class="MobileConnection">{info[11]}
        </div>
        <div class="ProxyConnection">{info[12]}
        </div>
        <div class="Hosting">{info[13]}
        </div>
    </body>
    """
                except: raise self.DataError("Error work with data")
                finally:
                    with open(path, mode='w', encoding='utf-8') as file : file.write(datahtmlip)
                    if self.debug == True : print(datahtmlip), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                    if self.debug == False : pass
            if name == "break_number":
                try:
                    datahtmlnumber = f"""<!DOCTYPE html>
    <head>
        <title>TWSEConsoleFUP 0.3</title>
        <meta charset="utf-8">
    </head>
    <body>
        <div class="OperName">{info[0]}
        </div>
        <div class="MNC">{info[1]}
        </div>
        <div class="Brand">{info[2]}
        </div>
        <div class="INN">{info[3]}
        </div>
        <div class="Work_Mobile">{info[4]}
        </div>
        <div class="Name">{info[5]}
        </div>
    </body>
    """
                except: raise self.DataError("Error work with data")
                finally:
                    with open(path, mode='w', encoding='utf-8') as file : file.write(datahtmlnumber)
                    if self.debug == True : print(datahtmlnumber), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                    if self.debug == False : pass
            if name == "break_mac":
                try:
                    datahtmlmac = f"""<!DOCTYPE html>
    <head>
        <title>TWSEConsoleFUP 0.3</title>
        <meta charset="utf-8">
    </head>
    <body>
        <div class="Company">{info[0]}
        </div>
        <div class="Address">{info[1]}
        </div>
        <div class="BlockSize">{info[2]}
        </div>
    </body>
    """
                except: raise self.DataError("Error work with data")
                finally:
                    with open(path, mode='w', encoding='utf-8') as file : file.write(datahtmlmac)
                    if self.debug == True : print(datahtmlmac), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                    if self.debug == False : pass

class api:
    class break_ip:
        class BreakIPAddress(Handlers):
            my_name = 'break_ip'
            from requests import exceptions, get
            from bs4 import BeautifulSoup
            from json import loads
            def __init__(self, mode, ip, way=None, autoprint=True or False, debug=True, proxy=None):
                self.mode=mode
                self.ip=ip
                self.autoprint=autoprint
                self.debug=debug
                self.way=way
                self.proxy=proxy
            def __checkproxy__(self):
                bad = 0
                true = 0
                try:
                    send_request = self.get("http://ip-api.com/json")
                    answer = send_request
                    soup_json = self.BeautifulSoup(answer.text, "html.parser").text.strip()
                    site_json = self.loads(soup_json)
                    Handler = site_json
                    user_ip = Handler["query"]
                    try:
                        send_request_proxy = self.get("http://ip-api.com/json", proxies=self.proxy)
                    except self.exceptions.ConnectionError:
                        raise super().Type.RequestsError("Not Found connection to internet")
                    answer_proxy = send_request_proxy
                    soup_json_proxy = self.BeautifulSoup(answer_proxy.text, "html.parser").text.strip()
                    site_json_proxy = self.loads(soup_json_proxy)
                    Handler_proxy = site_json_proxy
                    user_ip_proxy = Handler_proxy["query"]
                    if self.debug == True : print(f'[ TWSE_FUP ] - [ user -> {user_ip}, proxy_user -> {user_ip_proxy} ]')
                    if self.debug == False : pass
                    if user_ip == user_ip_proxy:
                        bad = bad + 1
                    else:
                        true = true + 1
                except:
                    raise super().Type.DataError("Error work with data. Maybe not found connection to internet")
                finally:
                    if bad == 1:
                        return False
                    elif true == 1:
                        return True
            def __sendrequest__(self):
                try:
                    if self.proxy is not None:
                        if self.__checkproxy__() == True : pass
                        else:
                            raise super().Type.RequestsError("Proxy not working")
                    if self.proxy is not None:
                        send_requests = self.get(f'http://ip-api.com/json/{self.ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting', proxies=self.proxy)
                    else:
                        send_requests = self.get(f'http://ip-api.com/json/{self.ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting')
                    answer = send_requests
                    soup_json = self.BeautifulSoup(answer.text, 'html.parser').text.strip()
                    site_json = self.loads(soup_json)
                    Handler = site_json
                except:
                    raise super().Type.DataError("Error work with data. Maybe not found connection to internet")
                finally:
                    return Handler
            def main(self, _answer="all", view="ini", _mode="w"):
                if self.mode == "HTML":
                    Handler = self.__sendrequest__()
                    super().Type(self.debug).__html__(self.my_name, Handler["continent"], Handler["country"], Handler["regionName"], Handler["city"], Handler["lat"], Handler["lon"], Handler["isp"], Handler["org"], Handler["as"], Handler["asname"], Handler["reverse"], Handler["mobile"], Handler["proxy"], Handler["hosting"], path=self.way)
                if self.mode == "OnlyText":
                        Handler = self.__sendrequest__()
                        if self.autoprint == True:
                            print(super().Type(self.debug).__text__(self.my_name, Handler["continent"], Handler["country"], Handler["regionName"], Handler["city"], Handler["lat"], Handler["lon"], Handler["isp"], Handler["org"], Handler["as"], Handler["asname"], Handler["reverse"], Handler["mobile"], Handler["proxy"], Handler["hosting"], _answer=_answer))
                        if self.autoprint == False:
                            super().Type(self.debug).__text__(self.my_name, Handler["continent"], Handler["country"], Handler["regionName"], Handler["city"], Handler["lat"], Handler["lon"], Handler["isp"], Handler["org"], Handler["as"], Handler["asname"], Handler["reverse"], Handler["mobile"], Handler["proxy"], Handler["hosting"], _answer=_answer)
                if self.mode == "JSON":
                    Handler = self.__sendrequest__()
                    super().Type(self.debug).__json__(self.my_name, Handler["continent"], Handler["country"], Handler["regionName"], Handler["city"], Handler["lat"], Handler["lon"], Handler["isp"], Handler["org"], Handler["as"], Handler["asname"], Handler["reverse"], Handler["mobile"], Handler["proxy"], Handler["hosting"], path=self.way)
                if self.mode == "FileAnswer":
                    Handler = self.__sendrequest__()
                    super().Type(self.debug).__file__(self.my_name, Handler["continent"], Handler["country"], Handler["regionName"], Handler["city"], Handler["lat"], Handler["lon"], Handler["isp"], Handler["org"], Handler["as"], Handler["asname"], Handler["reverse"], Handler["mobile"], Handler["proxy"], Handler["hosting"], path=self.way, view=view, _mode=_mode)
                else:
                    raise super().Type.ParametersError(f"Not found parameters -> {self.mode}. [\"HTML\", \"OnlyText\", \"JSON\", \"FileAnswer\"]")
    class break_mac:
        class BreakMACAddress(Handlers):
            my_name = 'break_mac'
            from requests import exceptions, get
            from bs4 import BeautifulSoup
            from json import loads
            def __init__(self, mode, mac, way=None, autoprint=True or False, debug=True, proxy=None):
                self.mode=mode
                self.mac=mac
                self.autoprint=autoprint
                self.debug=debug
                self.way=way
                self.proxy=proxy
            def __checkproxy__(self):
                bad = 0
                true = 0
                try:
                    send_request = self.get("http://ip-api.com/json")
                    answer = send_request
                    soup_json = self.BeautifulSoup(answer.text, "html.parser").text.strip()
                    site_json = self.loads(soup_json)
                    Handler = site_json
                    user_ip = Handler["query"]
                    try:
                        send_request_proxy = self.get("http://ip-api.com/json", proxies=self.proxy)
                    except self.exceptions.ConnectionError:
                        raise super().Type.RequestsError("Not Found connection to internet")
                    answer_proxy = send_request_proxy
                    soup_json_proxy = self.BeautifulSoup(answer_proxy.text, "html.parser").text.strip()
                    site_json_proxy = self.loads(soup_json_proxy)
                    Handler_proxy = site_json_proxy
                    user_ip_proxy = Handler_proxy["query"]
                    if self.debug == True : print(f'[ TWSE_FUP ] - [ user -> {user_ip}, proxy_user -> {user_ip_proxy} ]')
                    if self.debug == False : pass
                    if user_ip == user_ip_proxy:
                        bad = bad + 1
                    else:
                        true = true + 1
                except:
                    raise super().Type.DataError("Error work with data. Maybe not found connection to internet")
                finally:
                    if bad == 1:
                        return False
                    elif true == 1:
                        return True
            def __sendrequest__(self):
                try:
                    if self.proxy is not None:
                        if self.__checkproxy__() == True : pass
                        else:
                            raise super().Type.RequestsError("Proxy not working")
                    if self.proxy is not None:
                        send_requests = self.get(f'https://api.2ip.ua/mac.json?mac={self.mac}', proxies=self.proxy)
                    else:
                        send_requests = self.get(f'https://api.2ip.ua/mac.json?mac={self.mac}')
                    answer = send_requests
                    soup_json = self.BeautifulSoup(answer.text, 'html.parser').text.strip()
                    site_json = self.loads(soup_json)
                    Handler = site_json
                except:
                    raise super().Type.DataError("Error work with data. Maybe not found connection to internet")
                finally:
                    return Handler
            def main(self, _answer="all", view="ini", _mode="w"):
                if self.mode == "HTML":
                    Handler = self.__sendrequest__()
                    super().Type(self.debug).__html__(self.my_name, Handler["company"], Handler["address"], Handler["block_size"], path=self.way)
                if self.mode == "OnlyText":
                    Handler = self.__sendrequest__()
                    if self.autoprint == True:
                        print(super().Type(self.debug).__text__(self.my_name, Handler["company"], Handler["address"], Handler["block_size"], _answer=_answer))
                    if self.autoprint == False:
                        super().Type(self.debug).__text__(self.my_name, Handler["company"], Handler["address"], Handler["block_size"], _answer=_answer)
                if self.mode == "JSON":
                    Handler = self.__sendrequest__()
                    super().Type(self.debug).__json__(self.my_name, Handler["company"], Handler["address"], Handler["block_size"], path=self.way)
                if self.mode == "FileAnswer":
                    Handler = self.__sendrequest__()
                    super().Type(self.debug).__file__(self.my_name, Handler["company"], Handler["address"], Handler["block_size"], path=self.way, view=view, _mode=_mode)
                else:
                    raise super().Type.ParametersError(f"Not found parameters -> {self.mode}. [\"HTML\", \"OnlyText\", \"JSON\", \"FileAnswer\"]")
    class break_number:
        class BreakNumberPhone(Handlers):
            my_name = 'break_number'
            from requests import exceptions, get
            from bs4 import BeautifulSoup
            from json import loads
            def __init__(self, mode, number, way=None, autoprint=True or False, debug=True, proxy=None):
                self.mode=mode
                self.number=number
                self.autoprint=autoprint
                self.debug=debug
                self.way=way
                self.proxy=proxy
            def __checkproxy__(self):
                bad = 0
                true = 0
                try:
                    send_request = self.get("http://ip-api.com/json")
                    answer = send_request
                    soup_json = self.BeautifulSoup(answer.text, "html.parser").text.strip()
                    site_json = self.loads(soup_json)
                    Handler = site_json
                    user_ip = Handler["query"]
                    try:
                        send_request_proxy = self.get("http://ip-api.com/json", proxies=self.proxy)
                    except self.exceptions.ConnectionError:
                        raise super().Type.RequestsError("Not Found connection to internet")
                    answer_proxy = send_request_proxy
                    soup_json_proxy = self.BeautifulSoup(answer_proxy.text, "html.parser").text.strip()
                    site_json_proxy = self.loads(soup_json_proxy)
                    Handler_proxy = site_json_proxy
                    user_ip_proxy = Handler_proxy["query"]
                    if self.debug == True : print(f'[ TWSE_FUP ] - [ user -> {user_ip}, proxy_user -> {user_ip_proxy} ]')
                    if self.debug == False : pass
                    if user_ip == user_ip_proxy:
                        bad = bad + 1
                    else:
                        true = true + 1
                except:
                    raise super().Type.DataError("Error work with data. Maybe not found connection to internet")
                finally:
                    if bad == 1:
                        return False
                    elif true == 1:
                        return True
            def __sendrequest__(self):
                try:
                    if self.proxy is not None:
                        if self.__checkproxy__() == True : pass
                        else:
                            raise super().Type.RequestsError("Proxy not working")
                    if self.proxy is not None:
                        send_requests = self.get(f'https://htmlweb.ru/json/mnp/phone/{self.number}', proxies=self.proxy)
                    else:
                        send_requests = self.get(f'https://htmlweb.ru/json/mnp/phone/{self.number}')
                    answer = send_requests
                    soup_json = self.BeautifulSoup(answer.text, 'html.parser').text.strip()
                    site_json = self.loads(soup_json)
                    Handler = site_json
                except:
                    raise super().Type.DataError("Error work with data. Maybe not found connection to internet")
                finally:
                    return Handler
            def main(self, _answer="all", view="ini", _mode="w"):
                if self.mode =="HTML":
                    Handler = self.__sendrequest__()
                    super().Type(self.debug).__html__(self.my_name, Handler["oper"]["name"], Handler["oper"]["mnc"], Handler["oper"]["brand"], Handler["oper"]["inn"], Handler["mobile"], Handler["region"]["name"], path=self.way)
                if self.mode == "OnlyText":
                    Handler = self.__sendrequest__()
                    if self.autoprint == True:
                        print(super().Type(self.debug).__text__(self.my_name, Handler["oper"]["name"], Handler["oper"]["mnc"], Handler["oper"]["brand"], Handler["oper"]["inn"], Handler["mobile"], Handler["region"]["name"], _answer=_answer))
                    if self.autoprint == False:
                        super().Type(self.debug).__text__(self.my_name, Handler["oper"]["name"], Handler["oper"]["mnc"], Handler["oper"]["brand"], Handler["oper"]["inn"], Handler["mobile"], Handler["region"]["name"], _answer=_answer)
                if self.mode == "JSON":
                    Handler = self.__sendrequest__()
                    super().Type(self.debug).__json__(self.my_name, Handler["oper"]["name"], Handler["oper"]["mnc"], Handler["oper"]["brand"], Handler["oper"]["inn"], Handler["mobile"], Handler["region"]["name"], path=self.way)
                if self.mode == "FileAnswer":
                    Handler = self.__sendrequest__()
                    super().Type(self.debug).__file__(self.my_name, Handler["oper"]["name"], Handler["oper"]["mnc"], Handler["oper"]["brand"], Handler["oper"]["inn"], Handler["mobile"], Handler["region"]["name"], path=self.way, view=view, _mode=_mode)
                else:
                    raise super().Type.ParametersError(f"Not found parameters -> {self.mode}. [\"HTML\", \"OnlyText\", \"JSON\", \"FileAnswer\"]")
