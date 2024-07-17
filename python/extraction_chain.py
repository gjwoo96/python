#pip install openai langchain -U langchain-community googletrans==4.0.0-rc1 httpcore

from langchain.chat_models import ChatOpenAI
from langchain.chains import create_extraction_chain
from googletrans import Translator

OPENAI_KEY = ""

schema = {
    "properties": {
        "player_name" : {"type" : "string"},
        "back_number" : {"type" : "string"},
        "team" : {"type" : "string"}
    }
}
inp = """메시는 바르샤에서 10번 등번호를 달고 뛰엇으며, 파리생제르맹에 이적하면서 30번이라는 등번호를 부여받았다.
호날두는 맨유에서 7번을 부여받고, 스페인의 레알마드리드로 이적후 첫시즌은 9번을 달고 뛰었으며, 그다음시즌부터는 7번을 부여받앗었다.
"""
translate = Translator()
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", openai_api_key=OPENAI_KEY)
chain = create_extraction_chain(schema,llm)
chainValue = chain.run(inp)
print("chainValue: ",chainValue)
for i in chainValue:
    if 'team' in i:
        tr = translate.translate(i['team'], dest='en')
        print("tr str : ",tr)
        i['team'] = tr.text
print("chainValue check: ",chainValue)        
#tr = translate.translate(inp, dest='en')
#print(tr)