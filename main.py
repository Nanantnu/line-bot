import json
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


app = Flask(__name__)
# LINE BOT info
line_bot_api = LineBotApi('hbhqR1idxfnPYWmfiWyg+oIaHlTf7mXVKZ2lkGIjlW8UClGYwydliL+XUwluTb6kaqRIJzWEqIkib/HiNCUMkrvFnk/SzSAsl7I9ZYCKvYo6+xXMmEQfYNTsqmlyiILRU59ecXikW+0ALrRZpQzcawdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0318c8d8f7210c34e298b5a5acfca1a9')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print(body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# Message event
@handler.add(MessageEvent)
def handle_message(event):
    message_type = event.message.type
    user_id = event.source.user_id
    reply_token = event.reply_token
    message = event.message.text

    if(message == 'Chat'):
        FlexMessage = json.load(open('chat.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('Chat',FlexMessage))

    elif(message == '安安~你最近在忙什麼呢?'):
        FlexMessage = json.load(open('doing.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('安安~你最近在忙什麼呢?',FlexMessage))

    elif(message == '你平常做什麼事來紓解壓力呢?'):
        FlexMessage = json.load(open('release_press.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('你平常做什麼事來紓解壓力呢?',FlexMessage))

    elif(message == '壓力是不是害你睡不好呢？'):
        FlexMessage = json.load(open('press_to_badsleep.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('壓力是不是害你睡不好呢？',FlexMessage))

    elif(message == '最近常看到關於電子煙的討論，你有聽過電子煙比紙菸安全的說法嗎?'):
        FlexMessage = json.load(open('esmoke.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('最近常看到關於電子煙的討論，你有聽過電子煙比紙菸安全的說法嗎?',FlexMessage))

    elif(message == '昨天去爬山，肌肉好痠痛啊～你也有肌肉痠痛的經驗嗎？'):
        FlexMessage = json.load(open('Muscle_ache.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('昨天去爬山，肌肉好痠痛啊～你也有肌肉痠痛的經驗嗎？',FlexMessage))

    elif(message == '沒有欸，不知道那是什麼感覺'):
        FlexMessage = json.load(open('more_muscle_ache.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('沒有欸，不知道那是什麼感覺',FlexMessage))

    elif(message == '當然有啊，超難受的'):
        FlexMessage = json.load(open('more_muscle_ache.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('當然有啊，超難受的',FlexMessage))

    elif(message == '你這禮拜的健身課表跑完了嗎？'):
        FlexMessage = json.load(open('work_out.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('你這禮拜的健身課表跑完了嗎？',FlexMessage))

    elif(message == '我又發現好吃的甜點了！你也是一吃到甜點就會很開心嗎？'):
        FlexMessage = json.load(open('dessert.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('我又發現好吃的甜點了！你也是一吃到甜點就會很開心嗎？',FlexMessage))

    elif(message == '最近運動後反而睡不好，你也有這種困擾嗎？'):
        FlexMessage = json.load(open('insomnia.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('最近運動後反而睡不好，你也有這種困擾嗎？',FlexMessage))

    elif(message == '最近工作壓力大，經常失眠，你也有這種困擾嗎？'):
        FlexMessage = json.load(open('insomnia.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('最近工作壓力大，經常失眠，你也有這種困擾嗎？',FlexMessage))

    elif(message == '關鍵字'):
        FlexMessage = json.load(open('keyword.json','r',encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('關鍵字',FlexMessage))



##---------------------------------------------------------------------------------------------------------------------------

    elif message == "其他常見問題":
        FlexMessage = json.load(open('but.json', 'r', encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('其他常見問題', FlexMessage))
    
    #Button_a
    elif message == '紙菸/電子菸':
        FlexMessage = json.load(open('buta.json', 'r', encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('紙菸/電子菸', FlexMessage))
    #a_1
    elif message == '電子煙能幫助戒菸嗎?':
        FlexMessage = json.load(open('a1.json', 'r', encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('電子煙能幫助戒菸嗎?', FlexMessage))
    elif (message == '可以！') or (message =='不可以/不知道'):
        FlexMessage = json.load(open('ra1.json', 'r', encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('戒治資源', FlexMessage))
    #a_2
    elif message == '紙菸和電子煙哪個比較無害?':
        FlexMessage = json.load(open('a2.json', 'r', encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('紙菸和電子煙哪個比較無害?', FlexMessage))
    elif message == '不知道耶':
        line_bot_api.reply_message(
            reply_token, 
            TextSendMessage(text="不論是哪種，裡面都含有上癮成分-尼古丁，都會造成健康危害呦!")
        )
    elif (message == '紙菸') or (message == '電子菸'):
        line_bot_api.reply_message(
            reply_token, 
            TextSendMessage(text="答錯! 兩者都含有上癮成分-尼古丁，都會造成健康危害呦!")
        )
    elif message == '一樣有害！':
        line_bot_api.reply_message(
            reply_token, 
            TextSendMessage(text="Bingo! 不論是哪種，裡面都含有上癮成分-尼古丁，都會造成健康危害呦!")
        )
    #a_3
    elif message == '有人說電子煙是「維他命棒」，這是有益健康的新科技嗎?':
        FlexMessage = json.load(open('a3.json', 'r', encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('有人說電子煙是「維他命棒」，這是有益健康的新科技嗎?', FlexMessage))
    elif (message == '不是！') or (message == '應該是吧') or (message == '不知道欸'):
        line_bot_api.reply_message(
            reply_token, 
            TextSendMessage(text="不論名字取得多神奇，維他命棒、電子果汁或水果棒，都是電子煙~大多數電子煙都含有尼古丁，會導致上癮，而且透過電子煙加熱而產生的物質非常複雜，可能導致肺部損傷甚至致死，絕對不是有益健康的東西！")
        )

    #Button_b
    elif message == '非法藥物分級':
        FlexMessage = json.load(open('butb.json', 'r', encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('非法藥物分級', FlexMessage))
    elif message == '分級的依據':
        FlexMessage = json.load(open('b1.json', 'r', encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('非法藥物分級', FlexMessage))
    elif message == '第一級':
        line_bot_api.reply_message(
            reply_token, 
            TextSendMessage(text="第一級的毒品有古柯鹼、海洛因、嗎啡、鴉片等，若是製造、運輸、販售、持有，根據毒品危害防治條例，罰則是最重的喔!")
        )
    elif message == '第二級':
        line_bot_api.reply_message(
            reply_token, 
            TextSendMessage(text="第二級的毒品有大麻、安非他命、搖頭丸等，別被國外電影誤導，大麻在台灣是屬於二級毒品喔!")
        )
    elif message == '第三級':
        line_bot_api.reply_message(
            reply_token, 
            TextSendMessage(text="第三級毒品有FM2俗稱約會強暴丸、K他命等，另外有些鎮靜安眠藥也屬於第三級管制藥品。\n另外，有些鎮靜安眠藥屬於第三、四級管制藥品，必須經醫師診斷開列處方才能使用，如果轉售或送給別人會觸法喔!")
        )
    elif message == '第四級':
        FlexMessage = json.load(open('b2.json', 'r', encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('非法藥物分級', FlexMessage))

    #Button_c
    elif message == '使用非法藥物的危害':
        FlexMessage = json.load(open('butc.json', 'r', encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('使用非法藥物的危害', FlexMessage))
    elif message == '為什麼就算知道成癮藥物有害，還是有人要使用呢?':
        line_bot_api.reply_message(
            reply_token, 
            TextSendMessage(text="使用成癮藥物的原因有很多，可能是好奇或想緩解壓力。但這些藥物會影響大腦，導致成癮。\n而大腦功能失調後，會影響認知功能和行為表現，很難自主停藥，產生戒斷症狀會非常痛苦呦！")
        )
    elif message == '吸毒對健康造成的影響是終生的嗎？':
        line_bot_api.reply_message(
            reply_token, 
            TextSendMessage(text="很遺憾的，沒錯！\n不要以爲戒掉就沒事囉，成癮是一種會復發的慢性病，難以擺脫，像是K他命更是會讓你「尿布一生」。\n我們一起先思考未來可能發生的後果，做出健康的決定，否則會後悔莫及的呀！")
        )

    #Button_d
    elif message == '用藥小撇步':
        FlexMessage = json.load(open('butd.json', 'r', encoding='utf-8'))
        line_bot_api.reply_message(reply_token, FlexSendMessage('用藥小撇步', FlexMessage))
    elif message == '錯過吃藥時間怎麼辦？':
        line_bot_api.reply_message(
            reply_token, 
            TextSendMessage(text="若錯過服藥時間應立刻補服，若已經接近下一次服藥時間，只要在下個原定的服藥時間使用一次劑量就可以囉！\n教你一個小撇步，例如：一天吃一次的藥，原本每天都是早上9點吃，如果今天早上忘記吃藥，在晚上9點前可以補吃。如果已經超過晚上9點，就等明天早上9點再依照原本劑量吃藥。\n但這只是參考原則，建議詢問藥師比較安心。")
        )
    elif message == '為什麼一般超商買不到維士比、保力達B？':
        line_bot_api.reply_message(
            reply_token, 
            TextSendMessage(text="維士比保力達B為指示用藥，需經藥師指示使用，所以要去藥局才能買喔！")
        )
    elif message == '退熱貼有藥性嗎？':
        line_bot_api.reply_message(
            reply_token, 
            TextSendMessage(text="退熱貼沒有藥性！\n因為退熱貼不是退燒藥，是由凝膠組成，貼上去之後，退熱貼的凝膠可以幫助散熱。")
        )
    elif message == '聽說咳嗽藥水喝多了會成癮，這是真的嗎？':
        line_bot_api.reply_message(
            reply_token, 
            TextSendMessage(text="止咳藥水種類繁多，部分止咳藥水含有阿片類止咳成分，如可待因(codeine)，長期服用有成癮的可能，但一般情形下，遵照醫師指示與標示的用法用量，正確使用是安全的！")
        )

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)