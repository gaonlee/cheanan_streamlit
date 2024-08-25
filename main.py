import streamlit as st
from pathlib import Path
from streamlit_option_menu import option_menu

# st.set_page_config는 반드시 스크립트의 가장 위쪽에서 호출되어야 합니다.
st.set_page_config(
    page_title="메인 메뉴",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 페이지 딕셔너리 설정
PAGES = {
    "천안 현황": "pages/1_EDA.py",
    "반려동물 친화시설 입지 추천": "pages/2_Location_recommendation.py",
    "부록": "pages/3_Appendix.py"
}

# 사이드바 메뉴 설정 및 스타일 적용
with st.sidebar:
    try:
        selection = option_menu("메인 메뉴", list(PAGES.keys()),
                                icons=['house', 'pin-map', 'book'],
                                menu_icon="cast",
                                default_index=0,
                                styles={
                                    "container": {"padding": "5!important", "background-color": "#fafafa"},
                                    "icon": {"color": "black", "font-size": "25px"},
                                    "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                                    "nav-link-selected": {"background-color": "#08c7b4"},
                                })
    except Exception as e:
        st.error(f"Error in sidebar option menu: {e}")

# 선택된 페이지 파일을 실행
page = PAGES.get(selection)
if page:
    try:
        with open(page, "r", encoding='utf-8') as file:
            exec(file.read(), globals())
    except Exception as e:
        st.error(f"Error executing page script {page}: {e}")
else:
    st.write("Main 페이지")
