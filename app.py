from flask import Flask, render_template
import folium
import geopandas as gpd
import rasterio
from matplotlib.colors import LinearSegmentedColormap


app = Flask(__name__)

@app.route('/')
def map_view():
    # Создаем базовую карту
    m = folium.Map(location=[51.6, 53.6], zoom_start=12)

    # Добавляем базовые карты
    folium.TileLayer('OpenStreetMap', name='OpenStreetMap').add_to(m)
    folium.TileLayer(
        tiles='https://core-renderer-tiles.maps.yandex.net/tiles?l=map&x={x}&y={y}&z={z}&scale=1&lang=ru_RU',
        name='Yandex',
        attr="<a href=https://yandex.ru/maps>Yandex</a>"
    ).add_to(m)
    folium.TileLayer(
        tiles='https://sat02.maps.yandex.net/tiles?l=sat&v=3.1493.0&x={x}&y={y}&z={z}&scale=1&lang=ru_RU',
        name='Yandex (satellite)',
        attr="<a href=https://yandex.ru/maps>Yandex</a>"
    ).add_to(m)
    folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        name='Google',
        attr="<a href=https://google.com/maps>Google</a>"
    ).add_to(m)
    folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        name='Google (satellite)',
        attr="<a href=https://google.com/maps>Google</a>"
    ).add_to(m)

    roads = gpd.read_file('data/roads.gpkg', layer='highway')
    buildings = gpd.read_file('data/buildings.gpkg', layer='building_yes')
    landuse = gpd.read_file('data/landuse.gpkg', layer='landuse')

    folium.GeoJson(
        roads,
        name="Дороги",
        popup=folium.GeoJsonPopup(fields=["name"], labels=True),
        style_function=lambda x: {'color': 'white', 'weight': 3}
    ).add_to(m)
    folium.GeoJson(
        buildings,
        name="Здания",
        style_function=lambda x: {'color': 'blue', 'weight': 2, 'fillOpacity': 0.5}
    ).add_to(m)
    folium.GeoJson(
        landuse,
        name="Фермы",
        style_function=lambda x: {'color': 'green', 'weight': 2, 'fillOpacity': 0.5}
    ).add_to(m)

    # Добавляем растровый слой из GeoTIFF
    with rasterio.open("data/dem.tif") as src:
        bounds = src.bounds
        img = src.read(1)  # только первый канал

    # Определяем границы
    bounds_coords = [[bounds.bottom, bounds.left], [bounds.top, bounds.right]]

    # Создаем цветовую карту
    cmap = LinearSegmentedColormap.from_list("raster_colormap", ["white", "yellow", "orange", "red"])

    # Накладываем растр
    folium.raster_layers.ImageOverlay(
        image=img,
        bounds=bounds_coords,
        opacity=0.6,
        name='ЦМР',
        colormap=lambda x: cmap(x / img.max())  # Нормируем цвета
    ).add_to(m)

    # Добавляем переключатель слоев
    folium.LayerControl().add_to(m)

    # Сохраняем карту в HTML для flask
    map_html = m._repr_html_()

    return render_template('map.html', map_html=map_html)

@app.route('/info')
def info_view():
    return render_template('info.html')

if __name__ == '__main__':
    app.run(debug=True)
