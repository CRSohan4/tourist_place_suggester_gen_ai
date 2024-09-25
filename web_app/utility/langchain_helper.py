from langchain.llms import ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain

llm = ollama.Ollama(
    model='llama3.1'
)

def suggest_tourist_place_name(country):

    prompt_template_name = PromptTemplate(
        input_variables = ['country'],
        template = "Suggest me a tourist place in '{country}' country. I only want one or two word with place name"
    )

    tourist_place_name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='tourist_place_name')
    
    prompt_template_description = PromptTemplate(
        input_variables = ['tourist_place_name'],
        template = "Tell me more about this '{tourist_place_name}' tourist place."
    )

    description_chain = LLMChain(llm=llm, prompt=prompt_template_description, output_key='description')

    chain = SequentialChain(
        chains = [tourist_place_name_chain, description_chain],
        input_variables = ['country'],
        output_variables = ['tourist_place_name', 'description']
    )

    response = chain({'country': country})
    print(response)
    return response