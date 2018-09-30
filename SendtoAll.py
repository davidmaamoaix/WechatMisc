#SendtoAll
#晓马制作
#Version 1.0

try:
    import time,itchat,pyautogui,sys
except Exception as e:
    print('Error: 第三方模块加载失败 ('+str(e)+')')

def send(content,firstNameOnly=True,lowerCase=True):
    friends=itchat.get_friends(update=True)[1:]
    for friend in friends:
        if firstNameOnly==True:
            name=friend['RemarkName'].split(' ')[0].split('@')[0]
        else:
            name=friend['RemarkName']
        if lowerCase==True:
            name=name.lower()
        if name=='':
            name=friend['NickName']
        try:
            print('已发送'+content.replace('#',name))
            itchat.send(content.replace('#',name),friend['UserName'])
        except Exception as e:
            print('Warning: 获取昵称失败 ('+str(e)+')')
            print('已发送'+content+content)
            itchat.send(content,friend['UserName'])
            
        #延迟的作用是假如你搞砸了，那么还有补救的时间 
        time.sleep(.1)

itchat.auto_login()
wish=pyautogui.prompt(text='请输入祝福 (用#代替对方名字):',title='群发OWO',default='')
if wish==None:
    sys.exit(0)
if '#' not in wish:
    pyautogui.alert(text='Error: 未检测到#', title='群发OWO', button='OK')
else:
    send(wish)

