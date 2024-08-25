import os

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
        plt.rc('font', family='NanumGothic')  # 폰트가 없을 경우 대체 폰트 사용

setup_fonts()