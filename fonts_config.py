import os
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

def setup_fonts():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(base_dir, 'fonts', 'NanumSquareL.otf')
    
    if os.path.exists(font_path):
        font_name = fm.FontProperties(fname=font_path).get_name()
        plt.rc('font', family=font_name)
        plt.rcParams['axes.unicode_minus'] = False
        print(f"Font loaded: {font_name}")
    else:
        print(f"Font not found at {font_path}")
        # 추가적으로 기본 폰트로 설정
        plt.rc('font', family='DejaVu Sans')

setup_fonts()
