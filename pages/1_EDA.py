import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import fonts_config

# 폰트 설정은 초기 설정 시 한 번만 실행
fonts_config.setup_fonts()

# 스타일 설정
sns.set_style("whitegrid")

# 데이터 로드
DATA_PATH = "data"
df_pet_registration = pd.read_csv(f"{DATA_PATH}/반려동물 등록현황(2018~2023).csv", encoding='cp949')
df_pet_household = pd.read_excel(f"{DATA_PATH}/가구원수별_반려동물_보유_유형별가구시도_20240809190525.xlsx", engine='openpyxl')
beauty_df = pd.read_csv(f"{DATA_PATH}/농림축산식품부_반려동물 미용업 현황_20221231.csv", encoding='cp949')
express_df = pd.read_csv(f"{DATA_PATH}/농림축산식품부_반려동물 운송업 현황_20201230.csv", encoding='cp949')
funeral_df = pd.read_csv(f"{DATA_PATH}/농림축산식품부_반려동물 장묘업 현황_12_30_2020.csv", encoding='cp949')
exhibition_df = pd.read_csv(f"{DATA_PATH}/농림축산식품부_반려동물 전시업 현황_20221231.csv", encoding='cp949')

# 필터링 함수 정의
def filter_regions(df, region_col='지역'):
    excluded_regions = ['서울', '경기', '인천']
    return df[~df[region_col].isin(excluded_regions)]

# 지역 데이터를 시각화하는 함수 정의
def plot_region_data(df, region_col, company_col, employee_col, title, highlight_region):
    # 지역 필터링
    df_filtered = filter_regions(df, region_col)
    
    # NaN 값 제거
    df_filtered = df_filtered.dropna(subset=[region_col, company_col, employee_col])
    
    # 데이터 타입 변환 (필요한 경우)
    df_filtered[company_col] = pd.to_numeric(df_filtered[company_col], errors='coerce')
    df_filtered[employee_col] = pd.to_numeric(df_filtered[employee_col], errors='coerce')
    
    # 내림차순 정렬
    df_company_sorted = df_filtered.sort_values(by=company_col, ascending=False)
    df_employee_sorted = df_filtered.sort_values(by=employee_col, ascending=False)
    
    # 그래프 생성
    fig, axs = plt.subplots(1, 2, figsize=(20, 8))
    
    # 업체 수 그래프
    sns.barplot(
        data=df_company_sorted,
        x=company_col,
        y=region_col,
        palette='viridis',
        ax=axs[0]
    )
    axs[0].set_title(f"{title} - {company_col}", fontsize=16)
    axs[0].set_xlabel(company_col, fontsize=12)
    axs[0].set_ylabel(region_col, fontsize=12)
    
    # 종사자 수 그래프
    sns.barplot(
        data=df_employee_sorted,
        x=employee_col,
        y=region_col,
        palette='viridis',
        ax=axs[1]
    )
    axs[1].set_title(f"{title} - {employee_col}", fontsize=16)
    axs[1].set_xlabel(employee_col, fontsize=12)
    axs[1].set_ylabel("", fontsize=12)  # y축 라벨 제거
    
    # 강조할 지역 표시 함수
    def highlight_bar(ax, df_sorted, value_col):
        for i, region in enumerate(df_sorted[region_col]):
            if region == highlight_region:
                rect = ax.patches[i]
                rect.set_edgecolor('red')
                rect.set_linewidth(3)
                rect.set_facecolor('lightcoral')
    
    # 강조 표시 적용
    highlight_bar(axs[0], df_company_sorted, company_col)
    highlight_bar(axs[1], df_employee_sorted, employee_col)
    
    # X축과 Y축 라벨에 대한 폰트 강제 적용
    for ax in axs:
        ax.set_xticklabels(ax.get_xticklabels(), fontproperties=fm.FontProperties(fname=fonts_config.font_path))
        ax.set_yticklabels(ax.get_yticklabels(), fontproperties=fm.FontProperties(fname=fonts_config.font_path))
        
        # 제목 및 축 라벨의 폰트 설정
        ax.title.set_fontproperties(fm.FontProperties(fname=fonts_config.font_path))
        ax.xaxis.label.set_fontproperties(fm.FontProperties(fname=fonts_config.font_path))
        ax.yaxis.label.set_fontproperties(fm.FontProperties(fname=fonts_config.font_path))

    # 레이아웃 조정
    plt.tight_layout()

    st.pyplot(fig)


# 인터랙티브 선택 메뉴 추가
options = ["행정구역별 반려동물 보유 가구 수", "시군구별 동물소유자수 및 동물소유자당동물등록수",
           "전국 반려동물 미용업 현황", "전국 반려동물 운송업 현황", "전국 반려동물 장묘업 현황", "전국 반려동물 전시업 현황"]

selected_option = st.sidebar.selectbox("원하는 시각화를 선택하세요:", options)

# 각 시각화에 따라 적절한 그래프를 렌더링
if selected_option == "행정구역별 반려동물 보유 가구 수":
    st.title("'행정구역별 반려동물 보유 가구 수 (가구원수=계)'")

    df_filtered1 = df_pet_household[(df_pet_household['가구원수'] == '계') &
                                    (~df_pet_household['행정구역별(시도)'].isin(['전국', '동부', '읍부', '면부', '서울특별시', '경기도']))]
    df_plot1 = df_filtered1[['행정구역별(시도)', '반려동물보유가구-계']]
    df_plot1 = df_plot1.sort_values(by='반려동물보유가구-계', ascending=False)

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x='반려동물보유가구-계', y='행정구역별(시도)', data=df_plot1, palette='viridis', ax=ax)

    highlight_region = '충청남도'

    def highlight_bar(ax, df_sorted, value_col):
        for i, region in enumerate(df_sorted['행정구역별(시도)']):
            if region == highlight_region:
                rect = ax.patches[i]
                rect.set_edgecolor('red')
                rect.set_linewidth(3)
                rect.set_facecolor('lightcoral')

    highlight_bar(ax, df_plot1, '반려동물보유가구-계')

    # 제목 및 축 라벨의 폰트 설정
    ax.set_title('행정구역별 반려동물 보유 가구 수 (가구원수=계)', fontsize=16, fontproperties=fm.FontProperties(fname=fonts_config.font_path))
    ax.set_xlabel('반려동물 보유 가구 수', fontsize=12, fontproperties=fm.FontProperties(fname=fonts_config.font_path))
    ax.set_ylabel('행정구역별(시도)', fontsize=12, fontproperties=fm.FontProperties(fname=fonts_config.font_path))

    # X축과 Y축 라벨에 대한 폰트 강제 적용
    ax.set_xticklabels(ax.get_xticklabels(), fontproperties=fm.FontProperties(fname=fonts_config.font_path))
    ax.set_yticklabels(ax.get_yticklabels(), fontproperties=fm.FontProperties(fname=fonts_config.font_path))

    st.pyplot(fig)

elif selected_option == "시군구별 동물소유자수 및 동물소유자당동물등록수":
    st.title('시군구별 동물소유자수 및 동물소유자당동물등록수')

    x = range(len(df_pet_registration['시군구']))
    fig, ax1 = plt.subplots(figsize=(12, 6))

    color = 'tab:blue'
    ax1.set_xlabel('시군구', fontproperties=fm.FontProperties(fname=fonts_config.font_path))
    ax1.set_ylabel('동물소유자수', color=color, fontproperties=fm.FontProperties(fname=fonts_config.font_path))
    bars1 = ax1.bar(x, df_pet_registration['동물소유자수'], color=color, width=0.4, label='동물소유자수(명)')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:orange'
    ax2.set_ylabel('동물소유자당동물등록수', color=color, fontproperties=fm.FontProperties(fname=fonts_config.font_path))
    line2 = ax2.plot(x, df_pet_registration['동물소유자당동물등록수'], color=color, marker='o', linestyle='-', linewidth=2, label='동물소유자당동물등록수(마리)')
    ax2.tick_params(axis='y', labelcolor=color)

    ax1.set_xticks(x)
    ax1.set_xticklabels(df_pet_registration['시군구'], rotation=45, ha="right", fontproperties=fm.FontProperties(fname=fonts_config.font_path))

    highlight_region = ['천안시']

    def highlight_bar(ax, bars, labels, highlight_region):
        for bar, label in zip(bars, labels):
            if label in highlight_region:
                bar.set_edgecolor('red')
                bar.set_linewidth(3)
                bar.set_facecolor('lightcoral')

    highlight_bar(ax1, bars1, df_pet_registration['시군구'], highlight_region)

    # 제목에 폰트 적용
    plt.title('시군구별 동물소유자수 및 동물소유자당동물등록수', fontproperties=fm.FontProperties(fname=fonts_config.font_path))
    fig.tight_layout()

    # 범례에 폰트 적용
    legend1 = ax1.legend(loc='upper left', prop=fm.FontProperties(fname=fonts_config.font_path))
    legend2 = ax2.legend(loc='upper right', prop=fm.FontProperties(fname=fonts_config.font_path))

    st.pyplot(fig)


else:
    # 전국 반려동물 관련 현황 선택 처리
    dataframes = {
        '전국 반려동물 미용업 현황': beauty_df,
        '전국 반려동물 운송업 현황': express_df,
        '전국 반려동물 장묘업 현황': funeral_df,
        '전국 반려동물 전시업 현황': exhibition_df
    }

    highlight_region = '충남'
    df = dataframes[selected_option]
    
    # 타이틀 추가
    st.header(f"📊 {selected_option}")

    if selected_option == '전국 반려동물 장묘업 현황':
        plot_region_data(df, '지역', '동물장묘업(업체 수)', '종사자수(명)', selected_option, highlight_region)
    else:
        plot_region_data(df, '지역', '업체수(개소)', '종사자수(명)', selected_option, highlight_region)
