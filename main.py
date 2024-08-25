import streamlit as st
from pathlib import Path
import fonts_config
from streamlit_option_menu import option_menu
import streamlit as st

# Streamlit 앱에서 사용할 폰트 설정을 CSS로 지정합니다.
st.markdown(
    """
    <style>
    @font-face {
        font-family: 'NanumSquare';
        src: url('/app/fonts/NanumSquareL.otf'); /* 폰트 파일 경로를 지정합니다. */
    }
    html, body, [class*="css"] {
        font-family: 'NanumSquare'; /* 위에서 정의한 폰트를 기본 폰트로 설정합니다. */
    }
    </style>
    """,
    unsafe_allow_html=True
)

fonts_config.setup_fonts()

st.set_page_config(
    page_title="메인 메뉴",
    layout="wide",
    initial_sidebar_state="collapsed",  # 사이드바를 기본적으로 접힌 상태로 설정
)

# 페이지 딕셔너리 설정
PAGES = {
    "천안 현황": "pages/1_EDA.py",
    "반려동물 친화시설 입지 추천": "pages/2_Location_recommendation.py",
    "부록": "pages/3_Appendix.py"
}

# 사이드바 메뉴 설정 및 스타일 적용
with st.sidebar:
    selection = option_menu("메인 메뉴", list(PAGES.keys()),
                            icons=['house', 'pin-map', 'book'],  # 각 메뉴에 아이콘 추가
                            menu_icon="cast",  # 메인 메뉴 아이콘
                            default_index=0,  # 기본 선택 항목 설정
                            styles={
                                "container": {"padding": "5!important", "background-color": "#fafafa"},
                                "icon": {"color": "black", "font-size": "25px"},
                                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                                "nav-link-selected": {"background-color": "#08c7b4"},
                            })

# 선택된 페이지 파일을 실행
page = PAGES.get(selection)
if page:
    exec(Path(page).read_text(encoding='utf-8'), globals())
else:
    st.write("Main 페이지")