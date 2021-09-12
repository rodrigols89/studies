# Data types

## Contents

 - [01 - Introduction to Data types](#data-types)

<div id="data-types"></div>

## 01 - Introduction to Data types

You will not always receive a dataset all ready and cute to work. Sometimes it is necessary to adjust the data and only then work with it.

Let's start with a dataset provided by Kaggle - [SEA Building Energy Benchmarking](https://www.kaggle.com/city-of-seattle/sea-building-energy-benchmarking):

Ok, after downloading we will do some initial steps with our dataset:

[init.py](src/init.py)  
```python
import pandas as pd
pd.set_option('display.max_columns', 42)

data = pd.read_csv('../datasets/2015-building-energy-benchmarking.csv')
print(data.head())
```

**NOTE:**
Well, I will not leave the output here because there will be a lot of columns *(42 as we configured)*, but you can test it on your computer.

But how can I see the data types for each column in my dataset? Simple, just use the Pandas **dtypes** attribute:

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

**NOTE:**  
Luckily for us the data types in our dataset are almost the way we want them. But just for practice suppose that we want to change the type of column **"DataYear"** that is in **int64** for **object** how we would do it?

Simple just use the Pandas **astype()** function:

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
DataYear                                                          object <----------
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
Note that the **"DataYear"** column is object type.

---

**REFERENCES:**  
[Didática Tech - Inteligência Artificial & Data Science](https://didatica.tech/)  

---

**Rodrigo Leite -** *Software Engineer*
