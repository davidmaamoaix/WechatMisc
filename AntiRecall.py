#AntiRecall

import itchat,time
from bs4 import BeautifulSoup

messages=[]

itchat.auto_login()

@itchat.msg_register(['Text','Note'])
def text_reply(msg):
    clearMemory(msg['CreateTime'])
    global messages
    print(len(messages))
    if msg['Type']=='Text':
        messages.append(msg)
    if msg['MsgType']==10002:
        recallId=BeautifulSoup(msg['Content'],'lxml').find('msgid').text
        for i in messages:
            if i['MsgId']==recallId:
                itchat.send('［撤回提示］@'+i['User']['NickName']+'\u2005刚才撤回了一条信息，内容为：'+i['Content'],msg['FromUserName'])

@itchat.msg_register(['Picture','Recording','Attachment','Video'])
def download_files(msg):
    fileDir = '%s%s'%(msg['Type'],int(time.time()))
    msg['Text'](fileDir)
    itchat.send('%s received'%msg['Type'],msg['FromUserName'])
    itchat.send('@%s@%s'%('img' if msg['Type'] == 'Picture' else 'fil',fileDir),msg['FromUserName'])

@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.get_contract()
    itchat.send_msg(msg['RecommendInfo']['UserName'],'Nice to meet you!')

@itchat.msg_register(['Text','Note'],isGroupChat = True)
def text_reply(msg):
    clearMemory(msg['CreateTime'])
    global messages
    print(len(messages))
    if msg['Type']=='Text':
        messages.append(msg)
    if msg['MsgType']==10002:
        recallId=BeautifulSoup(msg['Content'],'lxml').find('msgid').text
        for i in messages:
            if i['MsgId']==recallId:
                itchat.send('［撤回提示］@'+i['ActualNickName']+'\u2005刚才撤回了一条信息，内容为：'+i['Content'],msg['FromUserName'])

    """#Random Functions
    if msg['Content'][:2]=='刷屏':
        try:
            for i in range(0,int(msg['Content'].split('刷屏')[1].split('次')[0])):
                itchat.send(msg['Content'].split('次')[1][1:],msg['FromUserName'])
        except Exception:
            itchat.send('格式错误',msg['FromUserName'])"""

def clearMemory(currentTime):
    global messages
    for i in messages:
        if currentTime-i['CreateTime']>=120:
            messages.remove(i)

itchat.run()
