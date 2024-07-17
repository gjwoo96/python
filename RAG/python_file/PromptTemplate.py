import OS_environ
from langchain_openai import OpenAI
# 프롬프트 템플릿
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

#프롬프트 템플릿은 통해 매개변수 삽입 가능한 문자열로 변환
string_prompt = PromptTemplate.from_template("tell me a joke about {subject}")

#매개변수 삽입한 결과를 string_prompt_value에 할당
string_prompt_value = string_prompt.format_prompt(subject='soccer')

#print(string_prompt_value)


llm = OpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()])

food_template = """
너는 요리사야. 내가 가진 재료들을 갖고 만들 수 있는 요리를 추천하고, 그 요리의 레시피를 제시해줘.
내가 가진 재료는 아래와 같아.

<재료>
{재료}

"""

prompt_template = PromptTemplate(
    input_variables=['재료'],
    template = food_template
)

#print(prompt_template.format(재료 = '계란,소고기,양파,소금'))

#print(llm.invoke(prompt_template.format(재료 = '계란,소고기,양파,소금')))

examples = [
    {
        "question" : "아이유로 삼행시 만들어줘",
        "answer" :
        """
        아: 아이유는
        이: 이런강의를 들을 이
        유: 유가없다.
        """
    },
    {
        "question" : "김민수로 삼행시 만들어줘",
        "answer" : 
        """
        김: 김치는 맛있다
        민: 민달팽이도 좋아하는 김치!
        수: 수억을 줘도 김치는 내꺼!
        """
    }
]

example_prompt = PromptTemplate(input_variables=["question","answer"], template="Question: {question}\n{answer}")
#print(example_prompt.format(question = "호날두로 삼행시 지어줘",answer= "호: 호두 날: 날다람쥐 두: 두부"))
#print(example_prompt.format(**examples[0]))

prompt = FewShotPromptTemplate(
    examples = examples,
    example_prompt = example_prompt,
    suffix = "Question: {input}",
    input_variables = ["input"]
)
#print(prompt.format(input="호날두로 삼행시 만들어줘"))

# 템플릿 없이 실행
#print(llm.invoke("호날두로 삼행시 만들어줘"))

#print("--------------------------------------------------------------------------------------")
# 템플릿 추가 후 실행
#print(llm.invoke(prompt.format(input="호날두로 삼행시 만들어줘")))

#반의어
example_prompt2 = PromptTemplate(
    input_variables = ["input","output"],
    template = "input: {input}\nOoutput: {output}",
)

examples2 = [
    {"input" : "행복","output" : "슬픔"},
    {"input" : "흥미","output" : "지루"},
    {"input" : "불안","output" : "안정"},
    {"input" : "긴 기차","output" : "짧은 기차"},
    {"input" : "큰 공","output" : "작은 공"}
]


example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples2,
    OpenAIEmbeddings,
    Chroma,
    k=1
)

silmiar_prompt = FewShotPromptTemplate(
    example_selector = example_selector,
    example_prompt = example_prompt2,
    prefix = "주어진 입력에 대해 반대의 의미를 가진 단어를 출력해줘",
    suffix = "Input: {단어}\nOutput:",
    input_variables=["단어"],
)

print(silmiar_prompt.format(단어="무서운"))