# PROJEKT 2
Wtyczka do QGIS 
# ZASTOSOWANIE #
_wytyczne_

Żeby wtyczka zadziałała poprawnie należy mieć zainstalowany program QGIS.

_wykorzystanie_

Wtyczka służy do liczenia różnic wysokości dwóch wybranych punktów. 

Wtyczka oblicza pole powierzchni, którego wierzchołkami są wybrane punkty.

Jednostką otrzymanych wyników jest odpowiednio:
- do róznic wysokości metr
- do pola poligonu metr kwadratowy

# SPOSÓB UŻYCIA #
Należy pobrać wtyczkę do folderu, w którym pobrane są już wtyczki do programu QGIS oraz załadować ją w programie. 

Następnie należy otworzyć mapę, której wartswy zawierać będą potrzebne atrybuty. Po uruchomieniu wtyczki otrzymamy komunikat "wybierz obiekty" i wyświetli nam się lista punktów z warstwy.

_możliwości wyboru punktów_
- 2 punkty - jeśli wybierzymy dwa dowolne punkty, wtyczka pozwoli nam obliczyć różnice wysokości tj. obliczy ją za nas
- ≥ 3 punktów - wtyczka wyznaczy nam pole otrzymanego przez wybór punktów poligonu.

# BŁĘDY #
Zgodnie z powyższymi informacjami ∆h możemy policzyć __TYLKO__ zaznaczając dwa punkty, jeśli tego nie zrobimy wyskoczy nam błąd "Zbyt mała liczba zaznaczonych punktów" . Błąd możemy zniwelować jedynie wybierając __DWA__
dowolne punkty. 

# Przykładowe użycie # 
Wtyczka działać będzie na przykładowym pliku "agencje zatrudnienia.shx" ze względu na odpowiednie atrybuty. 









