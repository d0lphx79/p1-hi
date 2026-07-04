import streamlit as st

# 1. 페이지 기본 설정 (브라우저 탭에 표시될 정보)
st.set_page_config(page_title="인사하는 강아지", page_icon="🐶", layout="centered")

# 2. 배경색(핑크) 및 글씨색(흰색), 버튼 스타일 지정을 위한 CSS 주입
st.markdown("""
    <style>
    /* 전체 앱 배경색을 핑크색으로 설정 */
    .stApp {
        background-color: #FF69B4; /* HotPink 색상 */
    }
    
    /* 모든 텍스트 글자 색상을 흰색으로 강제 지정 */
    .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp span, .stApp label {
        color: white !important;
        font-family: 'Malgun Gothic', sans-serif;
        text-align: center;
    }

    /* 버튼 기본 스타일 지정 (흰색 배경, 핑크색 글씨, 둥근 테두리) */
    div.stButton > button {
        background-color: white !important;
        color: #FF69B4 !important;
        font-weight: bold !important;
        font-size: 16px !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 10px 25px !important;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.15);
        transition: all 0.3s ease;
        display: block;
        margin: 0 auto;
    }

    /* 버튼에 마우스를 올렸을 때(Hover) 효과 */
    div.stButton > button:hover {
        background-color: #FF1493 !important; /* 더 진한 핑크 */
        color: white !important;
        transform: scale(1.05); /* 살짝 커지는 효과 */
    }
    </style>
""", unsafe_html=True)

# 3. 화면 전환을 위한 세션 상태(Session State) 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# =================================================================
# 4-A. 메인 화면 라이팅
# =================================================================
if st.session_state.page == 'main':
    # 상단 여백 확보
    st.write("")
    st.write("")
    
    # 메인 문구
    st.markdown("<h1>안녕하세요😘😍💕</h1>", unsafe_html=True)
    st.write("")

    # 손흔드는 귀여운 강아지 GIF (Giphy 무료 오픈 소스 링크)
    dog_gif_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2Zic3VwaXN3Y3F4M3ZxaDZidW1mYW94ZXh0am9uN2szY3R4Y3ZpbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/v6aOjy0Qo1fIA/giphy.gif"
    
    # 이미지를 가운데 정렬하기 위해 컬럼 배치 활용
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(dog_gif_url, use_container_width=True)
    
    st.write("")
    st.write("")

    # "나도 인사하기" 버튼
    if st.button("나도 인사하기"):
        st.session_state.page = 'celebrate'
        st.rerun() # 화면 새로고침하여 페이지 전환

# =================================================================
# 4-B. 축하 화면 라이팅
# =================================================================
elif st.session_state.page == 'celebrate':
    # 축하 화면으로 전환되자마자 펑펑 터지는 효과 주기
    st.balloons() 
    
    st.write("")
    st.write("")
    st.write("")
    
    # 축하 문구
    st.markdown("<h1>첫 웹페이지 제작을 축하해요!🎇</h1>", unsafe_html=True)
    
    st.write("")
    st.write("")
    st.write("")

    # "돌아가기" 버튼
    if st.button("돌아가기"):
        st.session_state.page = 'main'
        st.rerun() # 화면 새로고침하여 메인으로 이동
