import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import os


def setup_fonts():
    font_path = '/app/fonts/NanumSquareL.otf'  # Streamlit 클라우드에서의 폰트 경로
    if os.path.exists(font_path):
        font_name = fm.FontProperties(fname=font_path).get_name()
        plt.rc('font', family=font_name)
        plt.rcParams['axes.unicode_minus'] = False
        print(f"Font loaded: {font_name}")
    else:
        print(f"Font not found at {font_path}")
        plt.rc('font', family='NanumGothic')  # 폰트가 없을 경우 대체 폰트 사용

setup_fonts()
