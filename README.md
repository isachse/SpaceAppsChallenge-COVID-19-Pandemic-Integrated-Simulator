# COVID-19 Pandemic Integrated Simulator
## The Challenge

Your challenge is to integrate various Earth Observation-derived features with available socio-economic data in order to discover or enhance our understanding of COVID-19 impacts.

## Datasources

### FlightRadar Statistics
- Number of commercial flights tracked by Flightradar24, per day (UTC time), last 120 days
- https://www.flightradar24.com/data/statistics

### meteomatics API
- Guide https://www.meteomatics.com/en/api/getting-started/
- Madrid temperature data: https://api.meteomatics.com/2020-01-01T00:00:00ZP5M:PT1H/t_2m:C/40.416775,-3.703790/csv?model=mix
- Rome temperature data: https://api.meteomatics.com/2020-01-01T00:00:00ZP5M:PT1H/t_2m:C/41.902782,12.496366/csv?model=mix

### Ozone Monitoring Instrument (OMI)
- https://giovanni.gsfc.nasa.gov/giovanni
- Nitrogen Dioxide: "The number of molecules of NO2 in an atmospheric column (from the Earth's surface to the top of the atmosphere) above a square centimeter of the surface. In L2G Giovanni, NO2 data is provided only for near clear sky conditions (i.e only those NO2 retrievals are used in the analysis for which Cloud radiance fraction is less than 30%)." (https://disc.gsfc.nasa.gov/information/glossary?title=Giovanni%20Parameter%20Definitions:%20Nitrogen%20Dioxide)

### Twitter timeline sample
- Small sample dataset of retweeted COVID-19 news since beginning 2020
- Not representative, just showcase dataset