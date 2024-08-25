import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import os

font_path = 'NanumSquareL.otf'

def setup_fonts():
    
    font_path = 'NanumSquareL.otf'  # 파일이 루트 디렉토리에 있으므로 이 경로로 수정
    if os.path.exists(font_path):
        font_name = fm.FontProperties(fname=font_path).get_name()
        plt.rc('font', family=font_name)
        plt.rcParams['axes.unicode_minus'] = False
        print(f"Font loaded: {font_name}")
    else:
        print(f"Font not found at {font_path}")
        plt.rc('font', family='DejaVu Sans')  # 대체 폰트 설정 (한글 미지원)

    # matplotlib가 다른 폰트를 찾지 않도록 명시적으로 설정
    plt.rcParams['font.family'] = font_name
    plt.rcParams['font.sans-serif'] = [font_name]

setup_fonts()
