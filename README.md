## Project Structure

```text
travel_manitoba/
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── reference/
├── notebooks/
├── scripts/
│   ├── paths.py
│   ├── extract/
│   ├── transform/
│   └── etl_pipeline.py
├── outputs/
│   ├── powerbi/
│   ├── reports/
│   └── figures/
├── docs/
│   ├── data_dictionary.md
│   └── methodology.md
├── tests/
├── .gitignore
├── README.md
├── requirements.txt
└── LICENSE
```

**Directory Descriptions:**
- `data/raw/` - Original, immutable data files
- `data/interim/` - Intermediate transformations
- `data/processed/` - Cleaned data ready for Power BI
- `data/reference/` - Lookup tables and reference data
- `notebooks/` - Jupyter notebooks for exploratory data analysis
- `scripts/` - Production ETL scripts and utilities
- `outputs/powerbi/` - Power BI dashboard files (.pbix)
- `outputs/reports/` - Generated reports and documentation
- `docs/` - Project documentation

## Running the ETL Pipeline

```bash
# Run the complete ETL pipeline
python scripts/etl_pipeline.py
```

## Path Management

Paths are managed through `scripts/paths.py` for consistent and portable file access.

```python
from paths import raw, processed, powerbi

# Load raw data
airport_pdf = raw() / 'Website_Statistics_Q3_2025.pdf'
df = pd.read_csv(raw() / 'statscan_data.csv')

# Save processed data
df.to_csv(processed() / 'airport_clean.csv', index=False)

# Reference Power BI output location
dashboard_path = powerbi() / 'tourism_indicators.pbix'
```

## Data Flow

```text
raw data → notebooks (EDA) → scripts (ETL) → processed data → Power BI
```

## Data Sources

### Airport Traffic Statistics
**Metrics:** Winnipeg Airport Traffic, YWG Direct Air Arrival (U.S. & Overseas)

- **Source:** Winnipeg Airports Authority
- **URL:** https://www.ywg.ca/assets/pages/Website_Statistics_Q3_2025.pdf
- **Local File:** `data/raw/Website_Statistics_Q3_2025.pdf`
- **Coverage:** Historical monthly data (2005-2025)
- **Update Frequency:** Quarterly

### International Visitor Entries
**Metrics:** U.S. Visitor Direct Entries into Manitoba, U.S. Visitor Direct Entries into Canada, Extended country-of-origin analysis

- **Source:** Statistics Canada, Table 24-10-0050-01
- **Title:** Non-resident visitors entering Canada, by country of residence
- **DOI:** https://doi.org/10.25318/2410005001-eng
- **URL:** https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2410005001
- **Local File:** `data/raw/2410005001eng.csv`
- **Coverage:** January 2023 - October 2025
- **Update Frequency:** Monthly

**Citation:**
> Statistics Canada. Table 24-10-0050-01 Non-resident visitors entering Canada, by country of residence. DOI: https://doi.org/10.25318/2410005001-eng

### International Visitor Entries (Canada-wide)
**Metrics:** U.S. Visitor Direct Entries into Canada, Extended country-of-origin analysis for Canada

- **Source:** Statistics Canada, Table 24-10-0050-01
- **Title:** Non-resident visitors entering Canada, by country of residence
- **DOI:** https://doi.org/10.25318/2410005001-eng
- **URL:** https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2410005001
- **Local File:** `data/raw/2410005001cad-eng.csv`
- **Coverage:** January 2020 - October 2025
- **Update Frequency:** Monthly
- **Geography:** Canada (national totals)

**Citation:**
> Statistics Canada. Table 24-10-0050-01 Non-resident visitors entering Canada, by country of residence. DOI: https://doi.org/10.25318/2410005001-eng

**Note:** This is the same table as the Manitoba entries above, but with Geography=Canada instead of Geography=Manitoba to provide national context for comparison.

### Food & Accommodation Employment
**Metric:** MB Food & Accommodation Sector Employment

- **Source:** Statistics Canada, Table 14-10-0355-01
- **Title:** Employment by industry, monthly, seasonally adjusted and unadjusted, and trend-cycle, last 5 months (x 1,000)
- **DOI:** https://doi.org/10.25318/1410035501-eng
- **URL:** https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410035501
- **Local File:** `data/raw/1410035501eng.csv`
- **Geography:** Manitoba
- **Industry:** Accommodation and food services [72]
- **Coverage:** January 2005 - November 2025
- **Update Frequency:** Monthly

**Citation:**
> Statistics Canada. Table 14-10-0355-01 Employment by industry, monthly, seasonally adjusted and unadjusted, and trend-cycle, last 5 months (x 1,000). DOI: https://doi.org/10.25318/1410035501-eng

### Hotel Market Data
**Metrics:** Manitoba Hotel Occupancy, Winnipeg Hotel Occupancy (including ADR, RevPAR forecasts)

- **Source:** CBRE Hotels - Canadian National Outlook Q3 2025
- **URL:** https://mktgdocs.cbre.com/2299/470e0586-9a5f-49dc-bb76-2ecd0887f3ad-1036477880/Cdn_National_Outlook_-_Q3_2025.pdf
- **Local File:** `data/raw/Cdn_National_Outlook__Q3_2025_manitoba.pdf`
- **Coverage:** Historical (2019-2024) and forecasts (2025-2026)
- **Update Frequency:** Quarterly

**Note:** This source replaces STR Reports data used in Travel Manitoba's original reports, as STR data requires a subscription.

### Consumer Confidence
**Metric:** Consumer Confidence (Canada and USA)

- **Source:** Trading Economics
- **URL:** https://tradingeconomics.com/canada/consumer-confidence
- **Local File:** `data/raw/consumer_confidence_tradEconDec2025.csv`
- **Coverage:** December 2024 - December 2025
- **Update Frequency:** Monthly

### YWG Direct Air Arrivals (U.S. & Overseas)
**Metrics:** Monthly air arrivals to Winnipeg by country group (United States, Overseas, Canada)

- **Source:** Statistics Canada, Frontier Counts Interactive Dashboard
- **Title:** Frontier Counts: Interactive Dashboard
- **URL:** https://www150.statcan.gc.ca/n1/pub/71-607-x/71-607-x2023020-eng.htm
- **Data Extraction Method:** 
  - Accessed interactive dashboard
  - Applied filter: "Winnipeg" airport
  - Extracted monthly arrivals data from visual: "Arrivals by Month"
  - Country groups: United States of America, Overseas, Canada
- **Coverage:** January 2021 - November 2025
- **Update Frequency:** Monthly
- **Note:** Data manually extracted from interactive dashboard; not available as a public downloadable dataset. This represents an alternative to Table 24-10-0053-02 which only provides annual Winnipeg air arrival data.

**Citation:**
> Statistics Canada. Frontier Counts: Interactive Dashboard. https://www150.statcan.gc.ca/n1/pub/71-607-x/71-607-x2023020-eng.htm