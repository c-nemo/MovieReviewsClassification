import streamlit as st
from model import *
from streamlit_star_rating import st_star_rating

st.set_page_config(
    page_title="Movie Reviews Classification",
    layout="centered"
    )

ph = 'This movie is disgustingly good!' # placeholder

@st.cache_resource(show_spinner='Loading model...')
def get_pipe():
    name = 'bert'
    PATH = 'c-nemo/bert-for-movie-review-classification'
    model = AutoModelForSequenceClassification.from_pretrained(PATH, use_auth_token='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')
    tokenizer = AutoTokenizer.from_pretrained(PATH, use_auth_token='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')
    pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, return_all_scores=True)
    return pipe

if 'clicked' not in st.session_state:
    st.session_state.clicked = False
    st.session_state.stars = '0'
    st.session_state.sentiment = 'positive'
    st.session_state.text = ph
    st.session_state.star_obj = None
    st.session_state.placeholder = st.empty()

pipe = get_pipe()

def get_stars(num):
    return st_star_rating(" ", 10,
                           defaultValue=int(num),
                           # key="rating",
                           read_only=True)

def click_button():
    ls = pipe(text)
    prediction = get_prediction(ls)

    st.session_state.clicked = True
    st.session_state.stars = prediction['stars']
    st.session_state.sentiment = prediction['sentiment']
    st.session_state.text = text
    st.subheader('Prediction:')
    st.session_state.placeholder.empty()
    st.session_state.placeholder = st_star_rating(" ", 10, size=30,
                   defaultValue=int(st.session_state.stars),
                   read_only=True)
    st.session_state.placeholder = st.empty()

st.title('Welcome to the movie rating prediction app!')
st.write('Based on the text of a movie review in English, predict the corresponding rating.')
st.write('Source code and model available on ' +
'[![GitHub](https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/c-nemo/MovieReviewsClassification)' + ' &  ' +
'[![HuggingFace](https://img.shields.io/badge/Hugging%20Face-orange?style=for-the-badge)](https://huggingface.co/c-nemo/bert-for-movie-review-classification)')

st.subheader('Input the review:')
text = st.text_area('input',
                     ph,
                     label_visibility = "collapsed")

button_ind = st.button("Submit and get classification",
                       # on_click=click_button,
                       type='primary')
if button_ind:
    click_button()

if st.session_state.clicked:
    st.write('Text:', st.session_state.text)
    st.write('Stars:', str(st.session_state.stars), ' / 10')
    st.write('Sentiment:', st.session_state.sentiment)



