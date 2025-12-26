## Project Structure

travel_manitoba/
│
├── data/
│   ├── raw/                    # Original, immutable data files
│   ├── interim/                # Intermediate transformations (optional)
│   ├── processed/              # Cleaned, transformed data ready for analysis
│   └── external/               # Data from third-party sources
│
├── notebooks/                  # Jupyter notebooks for exploratory data analysis
│   └── *.ipynb                 # Numbered notebooks (e.g., 01_eda_airport.ipynb)
│
├── scripts/                    # Production ETL scripts and utilities
│   ├── paths.py               # Centralized path configuration
│   ├── extract/               # Data extraction scripts
│   ├── transform/             # Data cleaning and transformation scripts
│   └── etl_pipeline.py        # Main ETL orchestration
│
├── outputs/                    # Analysis outputs and deliverables
│   ├── powerbi/               # Power BI dashboard files (.pbix)
│   ├── reports/               # Generated reports and documentation
│   └── figures/               # Visualizations and charts
│
├── docs/                       # Project documentation
│   ├── data_dictionary.md     # Data definitions and schema
│   └── methodology.md         # Analysis methodology and decisions
│
├── tests/                      # Unit tests for data pipeline (optional)
│
├── .gitignore                  # Git ignore rules
├── README.md                   # Project overview and documentation
└── requirements.txt            # Python dependencies


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