import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
import folium
from streamlit_folium import st_folium
import matplotlib.cm as cm
import matplotlib.colors as colors
import numpy as np
from folium.plugins import FastMarkerCluster
import time
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import silhouette_score


DATA_PATH = "data"
df = pd.read_csv(f"{DATA_PATH}/한국문화정보원_전국 반려동물 동반 가능 문화시설 위치 데이터_20221130.CSV", encoding='cp949')

progress_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)
    progress_bar.progress(percent_complete + 1)

options = ["전국 반려동물 동반 가능 문화시설 위치", "천안시 반려동물 동반 가능 문화시설 현황", "DBSCAN + K-means","천안시 반려동물 친화시설 입지 추천", "천안 관광 트렌드"]
selected_option = st.sidebar.selectbox("지도를 선택하세요:", options)

if selected_option == "전국 반려동물 동반 가능 문화시설 위치":
    st.title("🐶전국 반려동물 동반 가능 문화시설 위치")
    m = folium.Map(location=[36.5, 127.5], zoom_start=7)
    fast_marker_cluster = FastMarkerCluster(df[['위도', '경도']].values.tolist())
    fast_marker_cluster.add_to(m)
    st_folium(m, width=700, height=500)

elif selected_option == "천안시 반려동물 동반 가능 문화시설 현황":
    st.title("😺천안시 반려동물 동반 가능 문화시설 위치")
    df_pet_culture_cheonan = df[
        (df['시군구 명칭'] == '천안시 서북구') |
        (df['시군구 명칭'] == '천안시 동남구')
    ]
    selected_columns = ['시설명', '카테고리3', '시군구 명칭', '법정읍면동명칭', '리 명칭',
           '위도', '경도', '도로명주소',
           '반려동물 동반 가능정보', '반려동물 전용 정보', '입장 가능 동물 크기', '반려동물 제한사항', '장소(실내) 여부', '장소(실외)여부',
           '기본 정보_장소설명', '애견 동반 추가 요금', '최종작성일']
    df_selected_cheonan = df_pet_culture_cheonan[selected_columns]

    df_pet_tourist_attraction = df_selected_cheonan[
        (df_selected_cheonan['카테고리3'] == '카페') |
        (df_selected_cheonan['카테고리3'] == '여행지') |
        (df_selected_cheonan['카테고리3'] == '문예회관') |
        (df_selected_cheonan['카테고리3'] == '박물관') |
        (df_selected_cheonan['카테고리3'] == '미술관')
    ]

    map_center = [df_pet_tourist_attraction['위도'].mean(), df_pet_tourist_attraction['경도'].mean()]
    mymap = folium.Map(location=map_center, zoom_start=12)

    for _, row in df_pet_tourist_attraction.iterrows():
        folium.Marker(
            location=[row['위도'], row['경도']],
            popup=row['시설명'],
            tooltip=row['시설명']
        ).add_to(mymap)

    st_folium(mymap, width=700, height=500)
    
elif selected_option == "DBSCAN + K-means":
    st.title('🔎DBSCAN')
    
    df_pet_tourist_attraction = df[
        (df['시군구 명칭'] == '천안시 서북구') |
        (df['시군구 명칭'] == '천안시 동남구')
    ]
    
    if '위도' in df_pet_tourist_attraction.columns and '경도' in df_pet_tourist_attraction.columns:
        df_pet_tourist_attraction = df_pet_tourist_attraction.dropna(subset=['위도', '경도'])
        coordinates = df_pet_tourist_attraction[['위도', '경도']].values
        
        dbscan = DBSCAN(eps=0.01, min_samples=3)
        clusters = dbscan.fit_predict(coordinates)
        df_pet_tourist_attraction['Cluster'] = clusters
        
        fig, ax = plt.subplots(figsize=(10, 6))
        scatter = ax.scatter(df_pet_tourist_attraction['경도'], df_pet_tourist_attraction['위도'], 
                             c=df_pet_tourist_attraction['Cluster'], cmap='plasma', s=50, marker='x')
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        ax.set_title('DBSCAN Clustering of Pet-Friendly Facilities in Cheonan')
        plt.colorbar(scatter, ax=ax, label='Cluster')
        st.pyplot(fig)
        
        st.markdown("""
        <div style="
        background-color: #f9f9f9; 
        padding: 15px; 
        border-radius: 10px; 
        border: 2px solid #1c64a8;
        ">
        <p style="font-size: 1.2em; font-weight: bold;">
           반려동물 친화시설이 몰려있는 곳이 확인됨.
        </p>
    </div>
    """, unsafe_allow_html=True)
        
    else:
        st.error("Latitude ('위도') or Longitude ('경도') columns are missing or incorrectly named.")

    st.title("🔎KMeans 클러스터링 - 천안시 반려동물 동반 가능 문화시설")
    
    target_areas = ['천안시 동남구', '천안시 서북구']
    df_filtered = df[df['시군구 명칭'].isin(target_areas)]
    exclude_categories = ['동물병원', '동물약국', '반려동물용품', '미용', '위탁관리']
    df_filtered = df_filtered[~df_filtered['카테고리3'].isin(exclude_categories)]
    df_filtered = df_filtered[['시도 명칭', '시군구 명칭', '법정읍면동명칭', '카테고리3', '위도', '경도']]
    df_onehot = pd.get_dummies(df_filtered[['카테고리3']], prefix="", prefix_sep="")
    df_onehot['법정읍면동명칭'] = df_filtered['법정읍면동명칭']
    df_grouped = df_onehot.groupby('법정읍면동명칭').mean().reset_index()

    n_clusters = 5
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(df_grouped.drop('법정읍면동명칭', axis=1))
    df_grouped['Cluster Labels'] = kmeans.labels_
    
    silhouette_avg = silhouette_score(df_grouped.drop(['법정읍면동명칭', 'Cluster Labels'], axis=1), kmeans.labels_)
    st.write(f"n_clusters = {n_clusters}, silhouette score = {silhouette_avg}")
    
    final_merged = df_filtered[['법정읍면동명칭', '위도', '경도']].drop_duplicates()
    final_merged = final_merged.merge(df_grouped[['법정읍면동명칭', 'Cluster Labels']], on='법정읍면동명칭')
    clusterdata = pd.merge(df_onehot, df_grouped[['법정읍면동명칭', 'Cluster Labels']], on='법정읍면동명칭')
    numeric_data = clusterdata.drop(['법정읍면동명칭'], axis=1)
    cluster_avg = numeric_data.groupby('Cluster Labels').mean().transpose()
    
    st.write(cluster_avg)
    
    colors_array = cm.rainbow(np.linspace(0, 1, n_clusters))
    rainbow = [colors.rgb2hex(i) for i in colors_array]
    

    map_clusters = folium.Map(location=[36.818, 127.156], zoom_start=12)
    
    for lat, lon, poi, cluster in zip(final_merged['위도'], final_merged['경도'], final_merged['법정읍면동명칭'], final_merged['Cluster Labels']):
        label = folium.Popup(str(poi) + ' Cluster ' + str(cluster), parse_html=True)
        folium.CircleMarker(
            [lat, lon],
            radius=5,
            popup=label,
            color=rainbow[int(cluster)],
            fill=True,
            fill_color=rainbow[int(cluster)],
            fill_opacity=0.7).add_to(map_clusters)
    
    st.markdown("""Cluster 0 : 보라, Cluster 1 : 하늘, Cluster 2 : 연두, Cluster 3 : 주황, Cluster 4 : 빨강""")
    st.markdown("""
    <div style="
        background-color: #f9f9f9; 
        padding: 15px; 
        border-radius: 10px; 
        border: 2px solid #1c64a8;
        ">
        <p style="font-size: 1.2em; font-weight: bold;">
            * [표] 클러스터별 카테고리 빈도 확인<br> 
            * 각 클러스터별로 어떤 카테고리의 특성이 높은지 비율로 나타내고 있다.<br>
            예) Cluster 0 (보라색) - 카페 빈도가 높은 지역<br>
            시설 카테고리 선정 시 참고할 수 있음.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st_folium(map_clusters, width=700, height=500)
    
    
elif selected_option == "천안시 반려동물 친화시설 입지 추천":
    st.title('🚩천안시 반려동물 친화시설 입지 추천')
    target_areas = ['천안시 동남구', '천안시 서북구']
    df_filtered = df[df['시군구 명칭'].isin(target_areas)]
    exclude_categories = ['동물병원', '동물약국', '반려동물용품', '미용', '위탁관리']
    df_filtered = df_filtered[~df_filtered['카테고리3'].isin(exclude_categories)]
    df_filtered = df_filtered[['시도 명칭', '시군구 명칭', '법정읍면동명칭', '카테고리3', '위도', '경도']]
    df_onehot = pd.get_dummies(df_filtered[['카테고리3']], prefix="", prefix_sep="")
    df_onehot['법정읍면동명칭'] = df_filtered['법정읍면동명칭']
    df_grouped = df_onehot.groupby('법정읍면동명칭').mean().reset_index()

    n_clusters = 5
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(df_grouped.drop('법정읍면동명칭', axis=1))
    df_grouped['Cluster Labels'] = kmeans.labels_

    dbscan = DBSCAN(eps=0.045, min_samples=5)
    df_filtered['DBSCAN_Cluster'] = dbscan.fit_predict(df_filtered[['위도', '경도']])

    final_merged = df_filtered.merge(df_grouped[['법정읍면동명칭', 'Cluster Labels']], on='법정읍면동명칭')
    preferred_category_per_cluster = final_merged.groupby('DBSCAN_Cluster')['Cluster Labels'].agg(lambda x: x.mode()[0])
    final_merged['Preferred_Category'] = final_merged['DBSCAN_Cluster'].map(preferred_category_per_cluster)

    map_clusters = folium.Map(location=[36.818, 127.156], zoom_start=12)
    colors_array = cm.rainbow(np.linspace(0, 1, n_clusters))
    rainbow = [colors.rgb2hex(i) for i in colors_array]

    for lat, lon, poi, dbscan_cluster, preferred_category in zip(final_merged['위도'], final_merged['경도'], final_merged['법정읍면동명칭'], final_merged['DBSCAN_Cluster'], final_merged['Preferred_Category']):
        label = folium.Popup(f"{poi}<br>DBSCAN Cluster: {dbscan_cluster}<br>Preferred Category: {preferred_category}", parse_html=True)
        folium.CircleMarker(
            [lat, lon],
            radius=5,
            popup=label,
            color=rainbow[int(preferred_category) % len(rainbow)],
            fill=True,
            fill_color=rainbow[int(preferred_category) % len(rainbow)],
            fill_opacity=0.7).add_to(map_clusters)

    st_folium(map_clusters, width=700, height=500)
    
    st.markdown("""
    <div style="
        background-color: #f9f9f9; 
        padding: 15px; 
        border-radius: 10px; 
        border: 2px solid #1c64a8;
        ">
        <p style="font-size: 1.2em; font-weight: bold;">
            마크가 찍힌 곳이 반려동물 친화시설이며,<br> 
            이를 중심으로 반려동물 친화도시를 만들어나갈 수 있을 것으로 기대됨.<br>
            천안 중심지에 반려동물 친화시설이 몰려있는 것이 확인됨<br>
            또한 카테고리별로 색을 구분하여,<br>
            시설 종류 선정 시 참고할 수 있음.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("Cluster 0 : 보라(카페), Cluster 1 : 하늘(박물관), Cluster 2 : 연두(카페, 문예회관, 미술회관), Cluster 3 : 주황(여행지), Cluster 4 : 빨강(문예회관)")
    
elif selected_option == "천안 관광 트렌드":
    st.title("🚗천안 관광 트렌드 - 동남구 vs 서북구 비교")

    col1, col2 = st.columns(2)

    with col1:
        st.image("images/천안 관광 트렌드_동남구.png", caption="동남구 관광 트렌드")

    with col2:
        st.image("images/천안 관광 트렌드_서북구.png", caption="서북구 관광 트렌드")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("동남구")
        st.markdown("""
        **'문화관광' 검색건수가 가장 많음**

        - **SNS 언급량**은 **31% 증가**\*
        - 최대 동반유형 키워드는 **[신부, 가족, 친구]**
        - 최대 여행유형 키워드는 **[힐링, 캠핑, 나들이]**
        - 외지인 인기관광지**는 [클라임맥스, 호텔왈츠, 중앙공원]
        - 내국인 관심 관광지 비율은 **[역사관광지, 문화시설, 자연관광지]**
        """)

    with col2:
        st.subheader("서북구")
        st.markdown("""
        **'쇼핑' 검색건수가 가장 많음**

        - **SNS 언급량**은 **55.5% 증가**\*
        - 최대 동반유형 키워드는 **[친구, 직원, 가족]**
        - 최대 여행유형 키워드는 **[힐링, 캠핑, 나들이]**
        - 외지인 인기관광지**는 [아늑호텔성정점, 조상현탁구클럽, 슈슈몰리]
        - 내국인 관심 관광지 비율은 **[음식점, 쇼핑, 유흥관광지]**
        """)

    st.markdown("""
    \*자료: 한국관광데이터랩, 지역별 관광 현황, 2024.08 조회기준; **조회기간 기준 전년 동기대비(2023.07 ~ 2024.06)**
    """)