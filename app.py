import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(page_title="인사하는 강아지 웹앱", page_icon="🐶", layout="centered")

# 2. 배경색(핑크), 글씨색(흰색), 버튼 중앙 정렬 스타일 지정을 위한 CSS 주입
st.markdown("""
    <style>
    /* 전체 앱 배경색을 핑크색으로 설정 */
    .stApp {
        background-color: #FF69B4; /* HotPink 색상 */
    }
    
    /* 모든 텍스트 글자 색상을 흰색으로 강제 지정 및 가운데 정렬 */
    .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp span, .stApp label {
        color: white !important;
        font-family: 'Malgun Gothic', sans-serif;
        text-align: center;
    }

    /* 버튼을 감싸는 박스 자체를 화면 가운데로 정렬 (핵심!) */
    div.stButton {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin-top: 20px;
    }

    /* 버튼 자체 디자인 (흰색 배경, 핑크색 글씨, 둥근 테두리) */
    div.stButton > button {
        background-color: white !important;
        color: #FF69B4 !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border-radius: 25px !important;
        border: none !important;
        padding: 12px 35px !important;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }

    /* 버튼에 마우스를 올렸을 때(Hover) 효과 */
    div.stButton > button:hover {
        background-color: #FF1493 !important; /* 더 진한 핑크 */
        color: white !important;
        transform: scale(1.05); /* 살짝 커지는 효과 */
    }
    </style>
""", unsafe_allow_html=True)

# 3. 화면 전환을 위한 세션 상태(Session State) 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# =================================================================
# 4-A. 메인 화면
# =================================================================
if st.session_state.page == 'main':
    st.write("")
    st.write("")
    
    # 메인 문구
    st.markdown("<h1>안녕하세요😘😍💕</h1>", unsafe_allow_html=True)
    st.write("")

    # 손흔드는 귀여운 강아지 GIF (Giphy 이미지)
    dog_gif_url = "https://media.giphy.com/media/v6aOjy0Qo1fIA/giphy.gif"
    
    # 강아지 이미지를 화면 가운데 정렬하기 위한 컬럼 레이아웃
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(dog_gif_url, use_container_width=True)
    
    st.write("")

    # "나도 인사하기" 버튼 (CSS에 의해 완벽히 정중앙 정렬됨)
    if st.button("나도 인사하기"):
        st.session_state.page = 'celebrate'
        st.rerun()

# =================================================================
# 4-B. 축하 화면
# =================================================================
elif st.session_state.page == 'celebrate':
    # 축하 화면으로 전환되자마자 풍선이 펑펑 터지는 효과
    st.balloons() 
    
    st.write("")
    st.write("")
    st.write("")
    
    # 축하 문구
    st.markdown("<h1>첫 웹페이지 제작을 축하해요!🎇</h1>", unsafe_allow_html=True)
    
    st.write("")
    st.write("")

    # "돌아가기" 버튼 (CSS에 의해 완벽히 정중앙 정렬됨)
    if st.button("돌아가기"):
        st.session_state.page = 'main'
        st.rerun()
