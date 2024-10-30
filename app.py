import streamlit as st
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import chains
from utils import safe_write
from langchain.callbacks import StreamingStdOutCallbackHandler
from chains import (
    product_manager_chain,
    tech_lead_chain,
    test_lead_chain,
    file_structure_chain,
    file_path_chain,
    code_chain,
    missing_chain,
    new_classes_chain
)

load_dotenv()

gpt_4o = init_chat_model('gpt-4o',
                         model_provider='openai',
                         temperature=0,
                         streaming=True,
                         callbacks=[StreamingStdOutCallbackHandler()])

gpt_4o_mini = init_chat_model('gpt-4o-mini',
                              model_provider='openai',
                              temperature=0,
                              streaming=True,
                              callbacks=[StreamingStdOutCallbackHandler()])

claude_3_5_sonnet = init_chat_model('claude-3-5-sonnet-20240620',
                                    model_provider='anthropic',
                                    temperature=0,
                                    streaming=True,
                                    callbacks=[StreamingStdOutCallbackHandler()])

mistral_large = init_chat_model('mistral-large-latest',
                                model_provider='mistralai',
                                temperature=0,
                                streaming=True,
                                callbacks=[StreamingStdOutCallbackHandler()])

mistral_codestral = init_chat_model('codestral-latest',
                                    model_provider='mistralai',
                                    temperature=0,
                                    streaming=True,
                                    callbacks=[StreamingStdOutCallbackHandler()])

mistral_codestral_mamba = init_chat_model('open-codestral-mamba',
                                          model_provider='mistralai',
                                          temperature=0,
                                          streaming=True,
                                          callbacks=[StreamingStdOutCallbackHandler()])

llama_3_1_groq = init_chat_model('llama-3.1-70b-versatile',
                                 model_provider='groq',
                                 temperature=0,
                                 streaming=True,
                                 callbacks=[StreamingStdOutCallbackHandler()])

st.title('Code Generator')

language = st.radio('Select Language:',
                    ['Python', 'Java', 'Rust', 'Kotlin', 'Go'])

st.markdown(
    '''
    <style>
        section[data-testid="stSidebar"] {
            width: 400px !important; # Set the width to your desired value
        }
    </style>
    ''',
    unsafe_allow_html=True,
)

with st.sidebar:
    st.image('image/software_eng.png')
    add_radio = st.radio(
        'Select the LLM to be used!',
        ('openai-gpt-4o',
         'openai-gpt_4o_mini',
         'claude-3-5-sonnet',
         'mistralai-large',
         'mistralai-codestral',
         'mistralai-codestral-mamba',
         'groq-llama-3-1-70b-versatile'))

if add_radio == 'openai-gpt-4o':
    chains.set_llm(gpt_4o)
elif add_radio == 'openai-gpt_4o_mini':
    chains.set_llm(gpt_4o_mini)
elif add_radio == 'claude-3-5-sonnet':
    chains.set_llm(claude_3_5_sonnet)
elif add_radio == 'mistralai-large':
    chains.set_llm(mistral_large)
elif add_radio == 'mistralai-codestral':
    chains.set_llm(mistral_codestral)
elif add_radio == 'mistralai-codestral-mamba':
    chains.set_llm(mistral_codestral_mamba)
elif add_radio == 'groq-llama-3-1-70b-versatile':
    chains.set_llm(llama_3_1_groq)

request = st.text_area('Please Detail Your Desired Use Case for Code Generation! ', height=100)
st.write('Generate a microservice to manage Trades. Use Redis as the DB.')
app_name = st.text_input('Enter Project Name:')
submit = st.button('submit', type='primary')

if language and submit and request and app_name:

    dir_path = app_name + '/'

    requirements = product_manager_chain.run(request)
    req_doc_path = dir_path + '/requirements' + '/requirements.txt'
    safe_write(req_doc_path, requirements)
    st.markdown(''' :blue[Business Requirements : ] ''', unsafe_allow_html=True)
    st.write(requirements)

    tech_design = tech_lead_chain.run({'language': language, 'input': request})
    tech_design_path = dir_path + '/tech_design' + '/tech_design.txt'
    safe_write(tech_design_path, tech_design)
    st.markdown(''' :blue[Technical Design :] ''', unsafe_allow_html=True)
    st.write(tech_design)

    test_plan = test_lead_chain.run(requirements)
    test_plan_path = dir_path + '/test_plan' + '/test_plan.txt'
    safe_write(test_plan_path, test_plan)
    st.markdown(''' :blue[Test Plan :] ''', unsafe_allow_html=True)
    st.write(test_plan)

    file_structure = file_structure_chain.run({'language': language, 'input': tech_design})
    file_structure_path = dir_path + '/file_structure' + '/file_structure.txt'
    safe_write(file_structure_path, file_structure)
    st.markdown(''' :blue[File Names :] ''', unsafe_allow_html=True)
    st.write(file_structure)

    files = file_path_chain.run({'language': language, 'input': file_structure})
    files_path = dir_path + '/files' + '/files.txt'
    safe_write(files_path, files)
    st.markdown(''' :blue[File Paths :] ''', unsafe_allow_html=True)
    st.write(files)

    files_list = files.split('\n')

    missing = True
    missing_dict = {
        file: True for file in files_list
    }

    code_dict = {}

    while missing:

        missing = False
        new_classes_list = []

        for file in files_list:

            code_path = os.path.join(dir_path, 'code', file)
            norm_code_path = code_path

            if not missing_dict[file]:
                safe_write(norm_code_path, code_dict[file])
                st.markdown(''' :red[Code & Unit Tests: 2nd Iteration] ''', unsafe_allow_html=True)
                st.write(code_dict[file])
                continue

            code = code_chain.predict(
                language=language,
                class_structure=tech_design,
                structure=file_structure,
                file=file,
            )

            code_dict[file] = code
            response = missing_chain.run({'language': language, 'code': code})
            if '<TRUE>' in response:
                missing = missing or missing_dict[file]
            else:
                safe_write(norm_code_path, code)
                st.markdown(''' :blue[Complete Code & Unit Tests: 1st Iteration] ''', unsafe_allow_html=True)
                st.write(code)
                continue

            if missing_dict[file]:
                new_classes = new_classes_chain.predict(
                    language=language,
                    class_structure=tech_design,
                    code=code
                )
                new_classes_list.append(new_classes)

        tech_design += '\n\n' + '\n\n'.join(new_classes_list)
