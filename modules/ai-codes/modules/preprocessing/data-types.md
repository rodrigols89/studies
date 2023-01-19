# Tipos de Dados

## Conteúdo

 - [01 - Introdução aos tipos de dados](#01)
 - [02 - Alterando os tipos de dados](#02)

---

<div id='01'></div>

## 01 - Introdução aos tipos de dados

Nem sempre você vai receber uma amostra (dataset) toda pronta e bonitinha para trabalhar. As vezes é preciso adequar os dados para só depois trabalhar com eles.

Vamos começar com uma amostra (dataset) disponibilizada pelo Kaggle referente ao [consumo de energia de alguns prêdios (SEA Building Energy Benchmarking)](https://www.kaggle.com/city-of-seattle/sea-building-energy-benchmarking).

Ok, depois de baixado vamos fazer alguns passos iniciais com a nossa amostra (dataset):

[first_sample.py](src/first_sample.py)
```python
import pandas as pd
pd.set_option('display.max_columns', 42)

data = pd.read_csv('../datasets/2015-building-energy-benchmarking.csv')
print(data.head())
```

**NOTE:**  
Bem, eu não vou deixar aqui a saída porque vão ser muitas colunas (42 como nós configuramos), mas você pode testar no seu computador.

Mas como eu posso ver os tipos de dados de cada coluna da minha amostra de dados (dataset)? Simples, basta utilizar o atributo **dtypes** do Pandas:

[dtypes_pandas.py](src/dtypes_pandas.py)
```python
import pandas as pd
pd.set_option('display.max_columns', 42)

data = pd.read_csv('../datasets/2015-building-energy-benchmarking.csv')
print(data.dtypes)
```

**OUTPUT:**  
```python
OSEBuildingID                                                      int64
DataYear                                                           int64
BuildingType                                                      object
PrimaryPropertyType                                               object
PropertyName                                                      object
TaxParcelIdentificationNumber                                     object
Location                                                          object
CouncilDistrictCode                                                int64
Neighborhood                                                      object
YearBuilt                                                          int64
NumberofBuildings                                                  int64
NumberofFloors                                                   float64
PropertyGFATotal                                                   int64
PropertyGFAParking                                                 int64
PropertyGFABuilding(s)                                             int64
ListOfAllPropertyUseTypes                                         object
LargestPropertyUseType                                            object
LargestPropertyUseTypeGFA                                        float64
SecondLargestPropertyUseType                                      object
SecondLargestPropertyUseTypeGFA                                  float64
ThirdLargestPropertyUseType                                       object
ThirdLargestPropertyUseTypeGFA                                   float64
YearsENERGYSTARCertified                                          object
ENERGYSTARScore                                                  float64
SiteEUI(kBtu/sf)                                                 float64
SiteEUIWN(kBtu/sf)                                               float64
SourceEUI(kBtu/sf)                                               float64
SourceEUIWN(kBtu/sf)                                             float64
SiteEnergyUse(kBtu)                                              float64
SiteEnergyUseWN(kBtu)                                            float64
SteamUse(kBtu)                                                   float64
Electricity(kWh)                                                 float64
Electricity(kBtu)                                                float64
NaturalGas(therms)                                               float64
NaturalGas(kBtu)                                                 float64
OtherFuelUse(kBtu)                                               float64
GHGEmissions(MetricTonsCO2e)                                     float64
GHGEmissionsIntensity(kgCO2e/ft2)                                float64
DefaultData                                                       object
Comment                                                           object
ComplianceStatus                                                  object
Outlier                                                           object
2010 Census Tracts                                               float64
Seattle Police Department Micro Community Policing Plan Areas    float64
City Council Districts                                           float64
SPD Beats                                                        float64
Zip Codes                                                          int64
dtype: object
```

---

<div id="02"></div>

## 02 - Alterando os tipos de dados

Para a nossa sorte os tipos de dados da nossa amostra estão quase da maneira que nós queremos. Mas só para praticar suponha que nós queremos trocar o tipo da coluna **"DataYear"** que está em `int64` para `object` como faríamos?

Simples, basta utilizar a função **astype()** do **pandas.DataFrame**:

[astype.py](src/astype.py)
```python
import pandas as pd
pd.set_option('display.max_columns', 42)

data = pd.read_csv('../datasets/2015-building-energy-benchmarking.csv')

data['DataYear'] = data['DataYear'].astype(object)
print(data.dtypes)
```

**OUTPUT:**  
```python
OSEBuildingID                                                      int64
DataYear                                                          object <-----
BuildingType                                                      object
PrimaryPropertyType                                               object
PropertyName                                                      object
TaxParcelIdentificationNumber                                     object
Location                                                          object
CouncilDistrictCode                                                int64
Neighborhood                                                      object
YearBuilt                                                          int64
NumberofBuildings                                                  int64
NumberofFloors                                                   float64
PropertyGFATotal                                                   int64
PropertyGFAParking                                                 int64
PropertyGFABuilding(s)                                             int64
ListOfAllPropertyUseTypes                                         object
LargestPropertyUseType                                            object
LargestPropertyUseTypeGFA                                        float64
SecondLargestPropertyUseType                                      object
SecondLargestPropertyUseTypeGFA                                  float64
ThirdLargestPropertyUseType                                       object
ThirdLargestPropertyUseTypeGFA                                   float64
YearsENERGYSTARCertified                                          object
ENERGYSTARScore                                                  float64
SiteEUI(kBtu/sf)                                                 float64
SiteEUIWN(kBtu/sf)                                               float64
SourceEUI(kBtu/sf)                                               float64
SourceEUIWN(kBtu/sf)                                             float64
SiteEnergyUse(kBtu)                                              float64
SiteEnergyUseWN(kBtu)                                            float64
SteamUse(kBtu)                                                   float64
Electricity(kWh)                                                 float64
Electricity(kBtu)                                                float64
NaturalGas(therms)                                               float64
NaturalGas(kBtu)                                                 float64
OtherFuelUse(kBtu)                                               float64
GHGEmissions(MetricTonsCO2e)                                     float64
GHGEmissionsIntensity(kgCO2e/ft2)                                float64
DefaultData                                                       object
Comment                                                           object
ComplianceStatus                                                  object
Outlier                                                           object
2010 Census Tracts                                               float64
Seattle Police Department Micro Community Policing Plan Areas    float64
City Council Districts                                           float64
SPD Beats                                                        float64
Zip Codes                                                          int64
dtype: object
```

**NOTE:**  
Veja que agora a coluna **"DataYear"** está do tipo `object`.

---

**REFERÊNCIA:**  
[Didática Tech - Inteligência Artificial & Data Science](https://didatica.tech)  
