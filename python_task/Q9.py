

wifi_standards = [".11b",".11a",".11g",".11n",".11ac",".11ax"]
bands=["2.4GHz","5GHz","6GHz"]


for standards, band in zip(wifi_standards , bands):
    print(standards, band)
