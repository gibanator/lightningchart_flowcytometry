import pandas as pd
import lightningchart as lc

with open("license_key.txt", "r") as file:  # License key is stored in 'license_key.txt'
    key = file.read()
lc.set_license(key)

df = pd.read_csv('data/flowcytometry.csv')
fscs = df['FSC'].tolist()
sscs = df['SSC'].tolist()
kde = df['KDE'].tolist()
min_kde = min(kde)
max_kde = max(kde)
normalized_kde = [(x - min_kde) / (max_kde - min_kde) for x in kde]

chart = lc.ChartXY(
    theme=lc.Themes.White,
    title='Flow Cytometry Chart'
)

series = chart.add_point_series(
    lookup_values=True,
)

series.append_samples(
    x_values=fscs,
    y_values=sscs,
    lookup_values=normalized_kde
)
series.set_individual_point_color_enabled()
series.set_palette_colors(
    steps=[
        {'value': 0, 'color': lc.Color(0, 0, 255, 128)},
        {'value': 0.15, 'color': lc.Color(204, 204, 0, 128)},
        {'value': 0.5, 'color': lc.Color(255, 140, 0, 128)},
        {'value': 1, 'color': lc.Color(255, 0, 0, 128)},
    ],
    look_up_property='value',
    percentage_values=True
)

chart.open()
