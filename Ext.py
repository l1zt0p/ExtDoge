#ExtDoge v6.0 by L1zt0p
#Ебём говноедов с 17.01.18
import vk_requests, time, random, socket, requests, os, colorama, logging, threading, winsound, glob, configparser, asyncio
from clint.textui import progress
ver = 601
vertxt = 'v6.0'
codename = 'Fable'
hostname = socket.gethostname()
colorama.init()
logfl = time.strftime('log/%Y-%m-%d-%H.%M.%S.log')

#Trying read or create configuration file
def createcfg():
    config = configparser.ConfigParser()
    config.add_section("ExtDoge Settings")
    config.set("ExtDoge Settings", "audioenabled", "True")
    with open('config.ini', "w") as config_file:
        config.write(config_file)
if not os.path.exists('config.ini'):
    createcfg()
config = configparser.ConfigParser()
config.read('config.ini')
config = config.get("ExtDoge Settings", "audioenabled")

#SoundEngine
def sound(data):
    global config
    if (config == 'True'):
        winsound.PlaySound(('data\\' + str(data)), winsound.SND_ASYNC)
        logger.info('Playing: ' + data)
    else:
        logger.warning("Don't playing: " + data)

#Starting Logging
logf = '[%(asctime)s (%(name)s) %(levelname)s]: %(message)s'
logging.basicConfig(format = logf, level = logging.INFO, filename = logfl)
logger = logging.getLogger('Root')
loggerext = logging.getLogger('Ext')
loggerstatus = logging.getLogger('Status')
loggerdog = logging.getLogger('Doggy')
print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Starting ExtDoge ' + vertxt + ' on ' + hostname + '..')
print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + '<c> HappyDropper, L1zt0p, Dropper Project, 2018-2021.')
logger.info('Starting ExtDoge ' + vertxt + ' on ' + hostname + '..')
logger.info('Codename: ' + codename)
logger.info('<c> HappyDropper, L1zt0p, Dropper Project, 2018-2021.')
sound('auth.wav')




#Whitelist
head = {'User-Agent': 'ExtDoge'}
try:
    security = requests.get('https://api.dropproj.ru/ban/ExtDoge/Whitelist.txt', headers=head, timeout=3).content.decode('UTF-8')
    security = security.split("\n")
except:
    print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Whitelist not downloaded!')
    security = ''


#FuckCM
cm = open('data/anticm.ext', 'r', encoding="utf-8").read()
cm = cm.split("\n")
logger.info('Loaded FuckCM text')
#UserGen
wmsg = open('data/warning.ext', 'r', encoding="utf-8").read()
wmsg = wmsg.split("\n")
logger.info('Loaded Warnings')

#En/Dis Dialogue
def dialog(name):
    dg = False
    while (dg == False):
        try:
            dg_st = int(input(str(name) + '? (0/1): '))
        except:
            print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Enter INT 0 or 1!')
        if (dg_st == 0):
            logger.info(str(name) + ' Disabled.')
            dg = True
            return False
        elif (dg_st == 1):
            logger.info(str(name) + ' Enabled.')
            dg = True
            return True
        elif (dg_st == 1337):
            print('\x1b[95mЛиза\x1b[94m топчик\x1b[91m :3\x1b[0m')
        elif (dg_st == 17012018):
            print('         ▄              ▄')
            print('        ▌▒█           ▄▀▒▌      /$$$$$$$$             /$$     /$$$$$$$')
            print('        ▌▒▒▀▄       ▄▀▒▒▒▐     | $$_____/            | $$    | $$__  $$')
            print('       ▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐     | $$       /$$   /$$ /$$$$$$  | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$')
            print('     ▄▄▀▒▒▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐     | $$$$$   |  $$ /$$/|_  $$_/  | $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$')
            print('   ▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀██▀▒▌     | $$__/    \  $$$$/   | $$    | $$  | $$| $$  \ $$| $$  \ $$| $$$$$$$$')
            print('  ▐▒▒▒▄▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄▒▒▌    | $$        >$$  $$   | $$ /$$| $$  | $$| $$  | $$| $$  | $$| $$_____/')
            print('  ▌▒▒▐▄█▀▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐    | $$$$$$$$ /$$/\  $$  |  $$$$/| $$$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$')
            print(' ▐▒▒▒▒▒▒▒▒▒▒▒▌██▀▒▒▒▒▒▒▒▒▀▄    |________/|__/  \__/   \___/  |_______/  \______/  \____  $$ \_______/')
            print(' ▌▒▀▄██▄▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▌                                                      /$$  \ $$')
            print(' ▌▀▐▄█▄█▌▄▒▀▒▒▒▒▒▒░░░░░░▒▒▒▐                                                      |  $$$$$$/')
            print('▐▒▀▐▀▐▀▒▒▄▄▒▄▒▒▒▒▒░░░░░░▒▒▒▒▌                                                      \______/')
            print('▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒░░░░░░▒▒▒▐')
            print(' ▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒▒▒░░░░▒▒▒▒▌                   Nice hack')
            print(' ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐                                   WOW! Such DDoS!')
            print('  ▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▌')
            print('    ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀')
            print('   ▐▀▒▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀  by HappyDropper (v1.0 - v3.6) and L1zt0p (v4.0 - 6.0) 17.01.2018 - 13.09.2021')
        else:
            print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Enter 0 or 1!')

def sel_dialog():
    dg = False
    while (dg == False):
        try:
            dg_st = int(input('Select Chat/User/AutoChat/InvLink (0/3): '))
        except:
            print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Enter INT 0/1/2/3!')
        if (dg_st == 0):
            logger.warning('Chat Mode.')
            dg = True
            return 0
        if (dg_st == 1):
            logger.warning('User Mode.')
            dg = True
            return 1
        if (dg_st == 2):
            logger.warning('Auto-Chat Mode.')
            dg = True
            return 2
        if (dg_st == 3):
            logger.warning('Invite Mode.')
            dg = True
            return 3
        else:
            print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Enter 0/1/2/3!')

#Select account file
print('Accounts:')
afile = glob.glob('acc*.txt')
if (len(afile) == 0):
    print('Not found!')
    print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + "Are you seriously try to start w/o accounts?)")
    logger.critical("0 accounts.")
    input('Press ENTER to close ExtDoge!')
    os._exit(5)
elif (len(afile) != 1):
    for load in range(0, len(afile)):
        print(str(load) + ' - ' + afile[load])
    try:
        load = int(input('Select Accounts File (0-' + str(len(afile)-1) + '): '))
    except:
        print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Enter 0 or 1!')
    print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Loaded file: ' + afile[load])
    logger.info('Loaded file: ' + afile[load])
    afile = afile[load]
    load = ''
else:
    afile = ('acc.txt')
    print('0 - acc.txt')
    print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Loaded file: acc.txt')
    logger.info('Loaded file: acc.txt')

#Auth
n = 0
api = []
uid = []
name = []
for load in open(afile, 'r').readlines():
    load = load.replace("\n", "")
    load = str(load).split(':')
    try:
        print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Authorization.. ' + '[' + str(n) + ']')
        logger.info('Authorization.. ' + '[' + str(n) + ']')
        load = vk_requests.create_api(app_id=2274003, login = load[0], password = load[1], client_secret='hHbZxrka2uZ6jB1inYsH', interactive = False, scope=['messages', 'account', 'friends', 'users', 'status', 'offline'])
        api.append(load)
        uid.append(api[n].users.get(fields = 'id')[0]['id'])
        name.append(api[n].users.get(fields = 'first_name')[0]['first_name'])
        n += 1
        time.sleep(0.5)
    except:
        print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Oops, Invalid error, may be empty string, skipping account...')
        logger.warning('Oops, Invalid error, may be empty string, skipping account...')
print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: Loaded ') + str(n) + ' account(s)')
logger.info('Loaded ' + str(n) + ' account(s)')
logger.debug('Cleaning up..')
rmb = load = 0

if (n == 0):
    print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + "Are you seriously try to start w/o accounts?)")
    logger.critical("0 accounts.")
    input('Press ENTER to close ExtDoge!')
    os._exit(5)
print(time.strftime('[%X\x1b[32m OK\x1b[0m]: ') + 'Authorized.')
logger.info('Authorized.')

#Adding friends
if (dialog('Add accounts to friends') == True):
    try:
        print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Getting friends..')
        fget = api[0].friends.get(order='id', offset=0, user_id=uid[0])['items']
        for over in range(1, n):
            try:
                if (uid[over] not in fget):
                    print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Adding user: ' + str(uid[over]), end='.')
                    api[over].friends.add(user_id=uid[0])
                    print('.', end='')
                    time.sleep(0.2)
                    api[0].friends.add(user_id=uid[over], follow=0)
                    print('.OK!')
                    logger.info('Added user: ' + str(uid[over]))
                    time.sleep(0.3)
                else:
                    print(time.strftime('[%X\x1b[32m OK\x1b[0m]: ') + 'User: ' + str(uid[over]) + ' already in friends.')
            except:
                print('')
                print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Error while adding user: ' + str(uid[over]))
                logger.error('Error while adding user: ' + str(uid[over]))
                time.sleep(0.2)
        fget = 0
    except:
        print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Getting friends failed.')
        fget = 0

#Status cleaning
if (dialog('Clean Status') == True):
    for chicken in range(0, n):
        try:
            print(time.strftime('[%X\x1b[32m OK\x1b[0m]: ') + 'Cleaning Status ['+str(chicken)+']', end=' ')
            api[chicken].status.set(text='')
            print('OK!')
            logger.info('Cleaning Status..OK  ['+str(chicken)+']')
        except:
            print('FAIL!')
            logger.error('Cleaning Status..FAIL  ['+str(chicken)+']')

def CheckWhite(id):
    global security
    ban = 0
    for lox in range(0, len(security)):
        if (str(security[lox]) == str(id)):
            print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + "You can't attack this people :)")
            ban = 1
    return ban

def char_set():
    dg = False
    while (dg == False):
        try:
            dg_st = int(input('Enter the multiplier of characters (x100) (E.g. 160): '))
            if (dg_st == 0):
                print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Setting default 100 chars..')
                dg_st = 1
            dg_st = (dg_st)
            dg = True
            logger.info('Char: ' + str(dg_st * 100))
            return dg_st
        except:
            print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Enter INT Value!')

def spd_set():
    dg = False
    while (dg == False):
        try:
            dg_st = float(input('Enter the speed value (sleep in secs) (E.g. 0.5): '))
            dg = True
            logger.info('Speed: ' + str(dg_st))
            return dg_st
        except:
            print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Enter FLOAT Value!')

#Mode select
chat = []
peer = []
mok = []
mof = []
temp_acc = []
temp_uid = []
fus = False
logger.info('Pre-initializied Chat-Vars')
sel = sel_dialog()
if (sel == 0):
    bak = dialog("Enable 'Сливной Бачок'")
    fcm = dialog("Enable 'FuckCM'")
    dog = dialog("Enable 'Спидозная собака'")
    state = dialog("Enable 'Status Translation'")
    char = char_set()
    spd = spd_set()
    sound('plant.wav')
    for pidr in range(0, n):
        inv = False
        while (inv == False):
            try:
                chat.append(int(input('Enter ChatID ' + str(pidr) + ' [' + str(name[pidr]) + ']: ')))
                logger.info('ChatID ' + str(pidr) + ' [' + str(uid[pidr]) + ']: ' + str(chat[pidr]))
                peer.append(2000000000 + int(chat[pidr]))
                mok.append(0)
                mof.append(0)
                inv = True
            except:
                print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Enter INT value!')
elif (sel == 1):
    try:
        pidoras = input('Enter UserID or Domain Name: ')
        if (pidoras.isdigit() == False):
            pidoras = api[0].users.get(user_ids=pidoras, name_case = 'Nom')[0]['id']
        sound('plant.wav')
        bak = dialog("Enable 'Сливной Бачок'")
        fcm = dialog("Enable 'FuckCM'")
        if (fcm == False):
            fus = dialog("Enable 'FuckUser'")
        state = dialog("Enable 'Status Translation'")
        char = char_set()
        spd = spd_set()
        if (CheckWhite(pidoras) == 0):
            logger.info('UserID: ' + str(pidoras))
            for inv in range(0, n):
                peer.append(pidoras)
                mok.append(0)
                mof.append(0)
        else:
            sound('alarm.wav')
            logger.critical("WL User.")
            input('Press ENTER to close ExtDoge!')
            os._exit(5)
    except:
        print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Enter INT value!')
elif (sel == 2):
    bak = dialog("Enable 'Сливной Бачок'")
    fcm = dialog("Enable 'FuckCM'")
    dog = dialog("Enable 'Спидозная собака'")
    state = dialog("Enable 'Status Translation'")
    char = char_set()
    spd = spd_set()
    add = False
    if (n > 1):
        add = dialog('Add accounts to Chat')
    chng = dialog('Change to random name')
    try:
        chat.append(int(input('Enter ChatID 0 ' + '[' + str(name[0]) + ']: ')))
        logger.info('ChatID 0 ' + ' [' + str(uid[0]) + ']: ' + str(chat[0]))
        peer.append(2000000000 + int(chat[0]))
        print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Getting Name', end='.')
        lox = api[0].messages.getChat(chat_id=chat[0])['title']
        print('.OK')
        logger.info('Getting name: OK')
        temp_acc.append(api[0])
        temp_uid.append(uid[0])
        mok.append(0)
        mof.append(0)
        sound('plant.wav')
        if (chng == True):
            try:
                print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Backing up name..')
                logger.info('Backing up name..')
                b_lox = lox
                lox = ('EXT-' + str(random.randint(100000, 500001)))
                print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Changing name..')
                logger.info('Changing name..')
                api[0].messages.editChat(chat_id=chat[0], title=lox)
            except:
                print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: Not INT value or this chat secured! Continue w/o it..'))
                lox = b_lox
                logger.error('Not INT value or this chat secured!')
        if (add == True):
            for lizaveta in range(1, n):
                try:
                    print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Adding user: ' + str(uid[lizaveta]), end='.')
                    try:
                        api[0].messages.addChatUser(chat_id=chat[0], user_id = str(uid[lizaveta]))
                        peer.append(api[lizaveta].messages.searchConversations(q=lox, count=1)['items'][0]['peer']['id'])
                        print('.', end='')
                        print('.OK ' + 'ID: ' + str(chat[lizaveta]) + ' [' + str(lizaveta) + ']')
                        logger.info('User: ' + str(uid[lizaveta]) + ' ID: ' + str(chat[lizaveta]) + ' [' + str(lizaveta) + '] Added!')
                        temp_acc.append(api[lizaveta])
                        temp_uid.append(uid[lizaveta])
                        mok.append(0)
                        mof.append(0)
                    except:
                        try:
                            print('ERROR, may be added, trying search ID.', end='.')
                            peer.append(api[lizaveta].messages.searchConversations(q=lox, count=1)['items'][0]['peer']['id'])
                            print('OK ' + 'ID: ' + str(chat[lizaveta]) + ' [' + str(lizaveta) + ']')
                            logger.info('User: ' + str(uid[lizaveta]) + ' ID: ' + str(chat[lizaveta]) + ' [' + str(lizaveta) + '] found!')
                            temp_acc.append(api[lizaveta])
                            temp_uid.append(uid[lizaveta])
                            mok.append(0)
                            mof.append(0)
                        except:
                            print('ERROR')
                            logger.error('Error while adding user: ' + str(uid[lizaveta]) + ' [' + str(lizaveta) + ']')
                except:
                    print('ERROR')
                    logger.error('Error while adding user: ' + str(uid[lizaveta]) + ' [' + str(lizaveta) + ']')
        elif (add == False):
            for gubin in range(1, n):
                try:
                    peer.append(api[gubin].messages.searchConversations(q=lox, count=1)['items'][0]['peer']['id'])
                    logger.info('Writing ID.. ' + str(peer[gubin]) + ' ['+str(gubin)+']' + ' [' + str(uid[gubin]) + ']')
                    print(time.strftime('[%X\x1b[32m OK\x1b[0m]: Writing ID.. ' + str(peer[gubin]) + ' ['+str(gubin)+']' + ' [' + str(uid[gubin]) + ']'))
                    temp_acc.append(api[gubin])
                    temp_uid.append(uid[gubin])
                    mok.append(0)
                    mof.append(0)
                except:
                    print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Writing ID failed.. ['+str(gubin)+']' + ' [' + str(uid[gubin]) + ']')
                    logger.warning('Writing ID failed.. ['+str(gubin)+']' + ' [' + str(uid[gubin]) + ']')
        if (chng == True):
            try:
                logger.info('Restoring name..')
                api[0].messages.editChat(chat_id=chat[0], title=b_lox)
                print(time.strftime('[%X\x1b[32m OK\x1b[0m]: ') + 'Restoring name..')
            except:
                print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Restoring failed!')
                logger.error('Restoring failed!')
        print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Preparing ' + str(len(temp_acc)) + ' accounts out of ' + str(n) + ' to start..')
        logger.info('Preparing ' + str(len(temp_acc)) + ' accounts out of ' + str(n) + ' to start..')
        api = temp_acc[:]
        uid = temp_uid[:]
        n = len(api)
        sel = 0
    except:
        print('FAILED')
        logger.error('Getting Name: Failed!')
elif (sel == 3):
    bak = dialog("Enable 'Сливной Бачок'")
    fcm = dialog("Enable 'FuckCM'")
    dog = dialog("Enable 'Спидозная собака'")
    state = dialog("Enable 'Status Translation'")
    char = char_set()
    spd = spd_set()
    lnk = str(input('Invite Link: '))
    logger.info('Invite Link: ' + lnk)
    sound('plant.wav')
    for dropper in range(0, n):
        try:
            print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Trying join.. ' + '[' + str(dropper) + ']')
            logger.info('Trying join.. ' + '[' + str(dropper) + ']')
            chat.append(api[dropper].messages.joinChatByInviteLink(link=lnk)['chat_id'])
            peer.append(2000000000 + int(chat[dropper]))
            temp_acc.append(api[dropper])
            temp_uid.append(uid[dropper])
            mok.append(0)
            mof.append(0)
            print(time.strftime('[%X\x1b[32m OK\x1b[0m]: ') + 'ChatID ' + str(dropper) + ' [' + str(uid[dropper]) + ']: ' + str(chat[dropper]))
            logger.info('ChatID ' + str(dropper) + ' [' + str(uid[dropper]) + ']: ' + str(chat[dropper]))
        except:
            print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Joining failed! ' + '[' + str(dropper) + ']')
            logger.warning('Joining failed! ' + '[' + str(dropper) + ']')
    print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Preparing ' + str(len(temp_acc)) + ' accounts out of ' + str(n) + ' to start..')
    logger.info('Preparing ' + str(len(temp_acc)) + ' accounts out of ' + str(n) + ' to start..')
    api = temp_acc[:]
    uid = temp_uid[:]
    n = len(api)
    sel = 0
logger.info('Cleaning up trash vars..')
pidr = inv = pidoras = lizaveta = gubin = add = chng = temp_acc = temp_uid = dropper = 0
time.sleep(0.3)

if (n == 0):
    print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Error on all accounts.')
    logger.critical("0 accounts.")
    input('Press ENTER to close ExtDoge!')
    os._exit(5)


#ATTENTION
at = ['photo-84463287_456239227', 'photo-84463287_456239228', 'photo-84463287_456239182', 'photo-84463287_456239520', 'photo-84463287_456239507', 'photo-84463287_456239503', 'photo-84463287_456239456', 'photo-84463287_456239405', 'photo-84463287_457240257', 'photo-84463287_457240258', 'photo-84463287_457240259', 'photo-84463287_457240260', 'photo-84463287_457240261', 'photo-84463287_457240262', 'photo-84463287_457240263', 'photo-84463287_457240264', 'photo-84463287_457240265', 'photo-84463287_457240266', 'photo-84463287_457240267', 'photo-84463287_457240268', 'photo-84463287_457240269', 'photo-84463287_457240270', 'photo-84463287_457240271', 'photo-84463287_457240741']
print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Sending WARNING message from main account.. ')
logger.info('Sending WARNING message from main account..')
try:
    api[0].messages.send(peer_id=peer[0], message=('ExtDoge ' + vertxt + ' запущен.. ' + wmsg[random.randint(0, (len(wmsg)-1))]), attachment=at[random.randint(0, (len(at)-1))], random_id=(random.randint(0, 65535)))
    print(time.strftime('[%X\x1b[32m OK\x1b[0m]: ') + 'WARNING message has been sent!')
    logger.info('WARNING message has been sent!')
except Exception:
    print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Error when sending.')
    logger.error('Error while sending.')

#DDoS
sound('start.wav')
msg = ''
doge = ''
smsg0 = [128506, 128000, 127902, 127744]
smsg1 = [128591, 128142, 127984, 127777]
ok = 0
fail = 0
db = 0
async def SmileGen():
    global char, msg
    for l1zt0p in range(0, 50):
        rnd0 = (random.randint(0, 3))
        rnd1 = (random.randint(0, 3))
        rmsg0 = (random.randint(smsg0[rnd0], smsg1[rnd0]))
        rmsg1 = (random.randint(smsg0[rnd1], smsg1[rnd1]))
        msg = (msg + '&#' + str(rmsg0) + ';')
        msg = (msg + '&#' + str(rmsg1) + ';')
    msg = (str(msg) * char)
    return msg

async def SmileGenDoge():
    global char, doge
    for happydropper in range(0, 50):
        rn0 = (random.randint(0, 3))
        rn1 = (random.randint(0, 3))
        dmsg0 = (random.randint(smsg0[rn0], smsg1[rn0]))
        dmsg1 = (random.randint(smsg0[rn1], smsg1[rn1]))
        doge = (doge + '&#' + str(dmsg0) + ';')
        doge = (doge + '&#' + str(dmsg1) + ';')
    doge = (str(doge) * char)
    return doge

def Bak():
    global db, smile, ok, fail, mok, mof
    if (sel == 0):
        print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Ярiк блять, тiкаем отсюда..')
        loggerext.warning('Activating Slivnoy Bachok..')
        for anuspsa in range(0, n):
            try:
                api[anuspsa].messages.removeChatUser(chat_id=chat[anuspsa], user_id=uid[anuspsa])
            except Exception:
                print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Ярiк блять, бачок потiк..  ['+str(anuspsa)+']')
                loggerext.warning('Bachok Error..  ['+str(anuspsa)+']')
    print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Sleeping 30min..')
    print(time.strftime('[%X\x1b[34;1m STATUS\x1b[0m]: ') + 'OK: ' + str(ok) + ' Fail: ' + str(fail) + ' Via 1 account ~ ' + str(round(int(ok)/int(n))))
    loggerext.warning('Sleeping 30min..')
    loggerext.info('OK: ' + str(ok) + ' Failed: ' + str(fail) + ' Via 1 account ~ ' + str(round(int(ok)/int(n))))
    time.sleep(1800)
    print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Fuckup motherfuckers! Get Revolution! [0]')
    try:
        api[0].messages.send(peer_id=peer[0], attachment=at[random.randint(0, (len(at)-1))], random_id=(random.randint(0, 65535)))
    except Exception:
        print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Revolution Error..  [0]')
        loggerext.warning('Revolution Error..  [0]')
    db = 0

async def Ext():
    global db, msg, spd, ok, fail, smile, mof, mok
    msg = ''
    while True:
        for smile in range(0, n):
            try:
                msg = await SmileGen()
                api[smile].messages.send(peer_id=peer[smile], message=msg, random_id=(random.randint(0, 65535)))
                ok += 1
                mok[smile] += 1
                print(time.strftime('[%X\x1b[32m OK\x1b[0m]: ') + 'Bomb dropped! ['+str(smile)+'] (' + str(ok) + ')')
                time.sleep(spd)
                msg = ''
            except Exception:
                msg = ''
                fail += 1
                mof[smile] += 1
                print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Dropping bomb failed. ['+str(smile)+'] (' + str(fail) + ')')
                loggerext.error('Dropping bomb failed. ['+str(smile)+']')
                if bak == True:
                    db += 1
                    if db == 30:
                        Bak()
                time.sleep(1.5)
                continue

async def ExtCM():
    global db, msg, doge, spd, cm, ok, fail, smile, fus
    msg = ''
    doge = ''
    while True:
        for smile in range(0, n):
            try:
                msg = await SmileGen()
                if (fus == False and sel == 1):
                    doge = await SmileGenDoge()
                else:
                    doge = cm[random.randint(0, (len(cm)-1))]
                if (fus == True and sel == 1):
                    msg_id = api[smile].messages.send(peer_id=peer[smile], message=msg, random_id=(random.randint(0, 65535)))
                    api[smile].messages.delete(message_ids=msg_id, delete_for_all=1)
                else:
                    msg_id = api[smile].messages.send(peer_id=peer[smile], message=doge, random_id=(random.randint(0, 65535)))
                    api[smile].messages.edit(peer_id=peer[smile], message_id=msg_id, message=msg)
                ok += 1
                mok[smile] += 1
                print(time.strftime('[%X\x1b[32m OK\x1b[0m]: ') + 'Bomb dropped! ['+str(smile)+'] (' + str(ok) + ')')
                time.sleep(spd)
                msg = ''
                doge = ''
            except Exception:
                msg = ''
                doge = ''
                fail += 1
                mof[smile] += 1
                print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Dropping bomb failed. ['+str(smile)+'] (' + str(fail) + ')')
                loggerext.error('Dropping bomb failed. ['+str(smile)+']')
                if bak == True:
                    db += 1
                    if db == 30:
                        Bak()
                time.sleep(1.5)
                continue

def Status():
    global ok, fail, mok, mof, db
    while True:
        print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Changing Status..')
        loggerstatus.info('Changing Status..')
        for elizaveta in range(0, n):
            try:
                api[elizaveta].status.set(text='&#10004; ExtDoge ' + vertxt + ' ID: ' + str(elizaveta) + ' Успешно(A/О): ' + str(mok[elizaveta]) + '/' + str(ok) + ' Ошибка(А/О): ' + str(mof[elizaveta]) + '/' + str(fail))
                time.sleep(0.5)
            except:
                print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Changing Status Failed.  ['+str(elizaveta)+']')
                loggerstatus.error('Changing Status Failed.  ['+str(elizaveta)+']')
                time.sleep(3)
        if db == 30:
            for epk in range(0, n):
                try:
                    api[epk].status.set(text='&#9888; ExtDoge ' + vertxt + ' ID: ' + str(epk) + ' Успешно(A/О): ' + str(mok[epk]) + '/' + str(ok) + ' Ошибка(А/О): ' + str(mof[epk]) + '/' + str(fail))
                    time.sleep(0.5)
                except Exception:
                    print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Changing Status Failed.  ['+str(epk)+']')
                    loggerstatus.error('Changing Status Failed.  ['+str(epk)+']')
                    time.sleep(3)
            print(time.strftime('[%X\x1b[32m OK\x1b[0m]: ') + 'Status: OK')
            loggerstatus.info('Status: OK')
            time.sleep(1800)
        else:
            time.sleep(45)

def AntiKick():
    global db
    while True:
        if db == 30:
            time.sleep(1803)
        try:
            gaben = api[0].messages.getChat(chat_id=chat[0])['users']
            for kran in range(0, n):
                if str(uid[kran]) not in str(gaben):
                    print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Adding ' + str(kran)  + ' user from 0: ' + str(uid[kran]))
                    loggerdog.info('Adding user: ' + str(uid[kran]))
                    time.sleep(0.374)
                    api[0].messages.addChatUser(chat_id=chat[0], user_id = str(uid[kran]))
            time.sleep(0.65)
        except:
            print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: Error while adding 0 user from 0'))
            loggerdog.error('Error while adding user from 0!')
            try:
                loggerdog.info('Adding user: ' + str(uid[0]))
                r = random.randint(1, n)
                print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Main: ' + str(uid[0]) + ' [0] user may be kicked, adding it from: ' + str(uid[r]) + ' [' + str(r) + ']')
                api[r].messages.addChatUser(chat_id=chat[r], user_id = str(uid[0]))
            except:
                print(time.strftime('[%X\x1b[31m WARN\x1b[0m]: ') + 'Error when adding 0 user from ' +  str(r) + '..')
                loggerdog.error('Error when adding user from ' + str(r) + '!')
            time.sleep(0.95)

#Threads
def ExtLaunch():
    print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Starting Ext thread..')
    loggerext.info('Starting Ext thread..')
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(Ext())
    loop.run_forever()
def ExtCMLaunch():
    print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Starting ExtCM thread..')
    loggerext.info('Starting ExtCM thread..')
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(ExtCM())
    loop.run_forever()
def StatusLaunch():
    global th_status
    print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Starting Status thread..')
    loggerstatus.info('Starting Status thread..')
    th_status = threading.Thread(target=Status, name="Status")
    th_status.start()
def AKLaunch():
    print(time.strftime('[%X\x1b[33m INFO\x1b[0m]: ') + 'Starting AntiKick thread..')
    loggerdog.info('Starting AK-Doggy thread..')
    th_ak = threading.Thread(target=AntiKick, name="AK")
    th_ak.start()
if sel == 0:
    if state == True:
        StatusLaunch()
    if dog == True:
        AKLaunch()
    if fcm == False:
        ExtLaunch()
    elif fcm == True:
        ExtCMLaunch()
else:
    if state == True:
        StatusLaunch()
    if ((fcm == False) and (fus == False)):
        ExtLaunch()
    elif ((fcm == True) or (fus == True)):
        ExtCMLaunch()
