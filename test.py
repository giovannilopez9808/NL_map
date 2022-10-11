import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd

mapa = gpd.read_file('conjunto_de_datos')
mapa = mapa.set_index("CVEGEO")
data = pd.read_csv("data.csv")
data = data[data["AÑO"] == 2010]
data["CVE_MUN"] = data["CVE_MUN"].map(lambda number:
                                      str(number).zfill(5))
data = data.set_index("CVE_MUN")
data = data.drop(columns=["CVE_ENT"])
mapa = mapa.join(data, how="left")
mapa = mapa.drop(columns=["LUG_NAC",
                          "LUGAR_EST",
                          "AÑO",
                          "GM"])
fig, ax = plt.subplots()
mapa.plot(column='IM',
          # legend=True,
          scheme='quantiles',
          k=5,
          cmap='viridis_r',
          ax=ax)
plt.show()
print(mapa.columns)
print(mapa)
