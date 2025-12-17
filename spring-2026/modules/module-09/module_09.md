# Analyzing World Development Indicators
**Designed by:** Dr. Ron Smith

In this unit we will obtain data from the [World Bank](https://en.wikipedia.org/wiki/World_Bank_Group)'s [World Development Indicators (WDI) database](https://databank.worldbank.org/source/world-development-indicators) and explore trends in measures such as life expectancy, gross domestic product, greenhouse gas emissions, and perhaps others (feel free to make suggestions!).

Along the way, we will:
* be introduced to the concept of an API (Application Programming Interface)
* learn about some commonly used Python libraries such as [pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/), and [Matplotlib](https://matplotlib.org/) (and a few others!)
* get more practice with structured project planning and AI prompting
* discuss effective ways to communicate findings visually and in writing
* troubleshoot potential issues and/or uncertainties in our data, analysis, and results

## Warm-up Data

[gapminder.tsv](gapminder.tsv): This is a commonly used warmup data set. Before we delve into the World Bank data, we'll use this to learn some fundamentals about the pandas, numpy, and matplotlib libraries for Python. (In case you are curious about the name, read more about Gapminder here: https://www.gapminder.org/).

Fields (mostly self-explanatory):
* `country`
* `continent`
* `year`
* `lifeExp`: Life Expectancy
* `pop`: Population
* `gdpPercap`: Per capita gross domestic product. That is, the total value of all goods and services produced domestically, divided by the country's population.

### Part 1 - Intro to Pandas

* [Intro to Pandas](Gapminder_part1.ipynb)

**Practice problems:**
In the most recent year's data (2007 in this dataset), how many countries (both a count, and which ones?) have a population greater than the average population across all countries?

**Group activity (WITH/WITHOUT the aid of GenAI:)**:

Create a new column for totalGDP, and compute it as `gdpPercap*pop`. In the earliest year (1952) which country in Europe had the lowest totalGDP, and what was their totalGDP in the most recent year?

Additional questions:
1. What subproblems did you address
2. Explain the solutions/prompts for each subproblem and how they were combined to solve the problem.

### Part 2 - [Basic plotting](Gapminder_part2.ipynb)

**Individual activities**

1. First, create folder named `GDP-Per-Cap`. Second, plot `gdpPercap` (GDP per capita) for all years from the earliest to the latest (`1952` -- `2007`). Name each file `GDP-Per-Cap/{year}_gdp_per_cap_.png`.
2. Create function for the combined boxplot + stripplot and the scatterplot
3. Similar to the `Life Expectacy` vs. `GDP per capita (US$)` scatterplot, visualize `Life Expectacy` vs. `Population`

### Part 3 - [Choropleth maps with Plotly](Gapminder_part3.ipynb)

**Group activity**

Study `gapminder.tsv` to identify the countries with the highest increase/decrease in population and/or life expectancy.

Questions:
1. Without going into too much detail, how did you intend to identify increase/decrease in population?
2. Explain the solutions/prompts for each subproblem and how they were combined to solve the problem.

## World Bank Data & API

The [World Bank's online tool](https://databank.worldbank.org/source/world-development-indicators): The API tools they list here were a bit clunky and partially broken, so Dr. Ron wrote one for you!

The code is all in [worldbankapi.py](https://drive.google.com/file/d/1rfbAR9b3qf_RHhnQJIJyev91jBliXvFZ/view?usp=drive_link). Examples of how to use it are in [WorldBankAPI_ExampleUsage.ipynb](https://drive.google.com/file/d/1jlzKr1Ysk5T0CCLEwkhh_ResDxpeL_w_/view?usp=drive_link)

Here's a list of databases and id numbers last update Nov 14, 2025 from the [wdata Python package documentation](https://wbdata.readthedocs.io/en/stable/#installation)

<details>
  <summary>Databases and id numbers</summary>
  ```
    id  name
    ----  --------------------------------------------------------------------
       1  Doing Business
       2  World Development Indicators
       3  Worldwide Governance Indicators
       5  Subnational Malnutrition Database
       6  International Debt Statistics
      11  Africa Development Indicators
      12  Education Statistics
      13  Enterprise Surveys
      14  Gender Statistics
      15  Global Economic Monitor
      16  Health Nutrition and Population Statistics
      18  IDA Results Measurement System
      19  Millennium Development Goals
      20  Quarterly Public Sector Debt
      22  Quarterly External Debt Statistics SDDS
      23  Quarterly External Debt Statistics GDDS
      25  Jobs
      27  Global Economic Prospects
      28  Global Financial Inclusion
      29  The Atlas of Social Protection: Indicators of Resilience and Equity
      30  Exporter Dynamics Database – Indicators at Country-Year Level
      31  Country Policy and Institutional Assessment
      32  Global Financial Development
      33  G20 Financial Inclusion Indicators
      34  Global Partnership for Education
      35  Sustainable Energy for All
      37  LAC Equity Lab
      38  Subnational Poverty
      39  Health Nutrition and Population Statistics by Wealth Quintile
      40  Population estimates and projections
      41  Country Partnership Strategy for India (FY2013 - 17)
      43  Adjusted Net Savings
      45  Indonesia Database for Policy and Economic Research
      46  Sustainable Development Goals
      50  Subnational Population
      54  Joint External Debt Hub
      57  WDI Database Archives
      58  Universal Health Coverage
      59  Wealth Accounts
      60  Economic Fitness
      61  PPPs Regulatory Quality
      62  International Comparison Program (ICP) 2011
      63  Human Capital Index
      64  Worldwide Bureaucracy Indicators
      65  Health Equity and Financial Protection Indicators
      66  Logistics Performance Index
      67  PEFA 2011
      68  PEFA 2016
      69  Global Financial Inclusion and Consumer Protection Survey
      70  Economic Fitness 2
      71  International Comparison Program (ICP) 2005
      73  Global Financial Inclusion and Consumer Protection Survey (Internal)
      75  Environment, Social and Governance (ESG) Data
      76  Remittance Prices Worldwide (Sending Countries)
      77  Remittance Prices Worldwide (Receiving Countries)
      78  ICP 2017
      79  PEFA_GRPFM
      80  Gender Disaggregated Labor Database (GDLD)
      81  International Debt Statistics: DSSI
      82  Global Public Procurement
      83  Statistical Performance Indicators (SPI)
      84  Education Policy
      85  PEFA_2021_SNG
      86  Global Jobs Indicators Database (JOIN)
      87  Country Climate and Development Report (CCDR)
      88  Food Prices for Nutrition
      89  Identification for Development (ID4D) Data
    ```
    </summary>
</details>

**(Fixed) Group activity**

Consider the World Bank list of databases. 
* Identify a simple research question to investigate. Discuss with me to finalize the question.
* Apply the PSP to decompose the research problem into smaller subcomponents. 
* With the aid of our all tutorial explored in this module and GenAI, design prompts to address each subcomponent to solve the problem.