import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import os

font_path = 'NanumSquareL.otf'

def setup_fonts():
    # 폰트 파일 경로를 수정 (프로젝트 폴더 내에 저장한 경우)
    font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'NanumSquareL.otf')
    
    if os.path.exists(font_path):
        font_name = fm.FontProperties(fname=font_path).get_name()
        plt.rc('font', family=font_name)
        plt.rcParams['axes.unicode_minus'] = False
        print(f"Font loaded: {font_name}")
    else:
        print(f"Font not found at {font_path}")
        plt.rc('font', family='Noto Sans KR')
        
    plt.rcParams['font.family'] = font_name
    plt.rcParams['font.sans-serif'] = [font_name]

setup_fonts()
