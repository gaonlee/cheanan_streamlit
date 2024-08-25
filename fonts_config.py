import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import os

font_path = 'NanumSquareL.otf'

def setup_fonts():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(current_dir, 'fonts', 'NanumSquareL.otf')
    
    print(f"Attempting to load font from: {font_path}")  # 폰트 경로 출력
    
    if os.path.exists(font_path):
        font_name = fm.FontProperties(fname=font_path).get_name()
        plt.rc('font', family=font_name)
        plt.rcParams['axes.unicode_minus'] = False
        print(f"Font loaded: {font_name}")  # 폰트 이름 출력
    else:
        print(f"Font not found at {font_path}")  # 폰트가 없을 경우 출력
        plt.rc('font', family='DejaVu Sans')

    plt.rcParams['font.family'] = font_name
    plt.rcParams['font.sans-serif'] = [font_name]

setup_fonts()
