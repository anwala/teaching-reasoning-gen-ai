from __future__ import annotations
from typing import Any, Callable, Literal
import pandas as pd
import time
import textwrap

try:
    import wbdata as wb
except ModuleNotFoundError as e:
    message = f'''
        {e}\n
        Try running:
        \t!pip install wbdata
        first, and then retry.'''
    print(textwrap.dedent(message))

class WorldBankData:
    '''
    Upon instantiation this class loads country and indicator codes
    from a World Bank database. The default (source_id = 2) is the
    World Development Indicators database. A full list of databases and
    their ids can be found (as of November 2025) at:

    https://wbdata.readthedocs.io/en/stable/#installation

    The get_data() method can then be used to query the selected
    database. 
    
    Note that API requests may occasionally fail. By default,
    up to 5 attempts will be made per request and there will be a
    2 second delay between requests. These values can be adjusted by
    specifying retries and retry_delay, respectively.
    '''

    # Default number of attempts that will be made to fetch a request
    RETRIES: int = 5
    # Default delay (in seconds) before retrying a request
    RETRY_DELAY: float = 2

    # Class attributes
    __slots__ = ('_indicators',     # All available indicators
                 '_countries_all',  # Includes both countries and aggregations/regions
                 '_countries',      # Individual countries only
                 '_aggregates',     # Aggregations only
                 '_retries',        # Max number of retries for failed API requests
                 '_retry_delay'     # Time delay in seconds between retries
                )
    
    def __init__(self, 
                 source_id: int = 2,
                 retries: int = RETRIES,
                 retry_delay: float = RETRY_DELAY
                ):
        self._disclaimer()
        self._retries = retries
        self._retry_delay = retry_delay
        self._fetch_indicators(source_id)
        self._fetch_countries()
        self._clean_countries()
        return
    
    def _disclaimer(self) -> None:
        message = '''
            DISCLAIMER:
            This code may break at any time if either:
                1) The World Bank changes the format of their data
                2) Changes are made to the underlying wbdata library (https://github.com/OliverSherouse/wbdata)
            '''
        print(textwrap.dedent(message))
        return
    
    def _fetch_with_retries(self, 
                            identifier: str, 
                            fun: Callable, 
                            **kwargs
                            ) -> Any:
        for _ in range(self._retries):
            try:
                print(f'Fetching data for {identifier}...')
                result = fun(**kwargs)
                print(f'{identifier} succesfully fetched.\n')
                return result
            except Exception as e:
                print(f'Error fetching {identifier}: {e}.\nRetrying in {self._retry_delay} seconds...')
                time.sleep(self._retry_delay)
        raise Exception('Maximum number of retries reached. Try again later.')
        return None

    def _fetch_indicators(self, source_id: int) -> None:
        kwargs = {'source': source_id}
        self._indicators = self._fetch_with_retries('Indicators', wb.get_indicators, **kwargs)
        return None

    def _fetch_countries(self) -> None:
        self._countries_all = self._fetch_with_retries('Countries', wb.get_countries)
        return None
    
    def _clean_countries(self) -> None:
        self._countries = []
        self._aggregates = []
        for country in self._countries_all:
            if country['region']['value'] == 'Aggregates':
                self._aggregates.append(country)
            else:
                self._countries.append(country)
        self._aggregates.sort(key=lambda x: x['name'])
        self._countries.sort(key=lambda x: x['name'])
        return None

    def get_country_list(self, id_only: bool=False) -> list:
        '''
        Returns a list of all countries and their three-digit codes.
        Results are sorted by codes.

        Input:
            id_only: If True, only returns three-digit codes. Default is False.
        '''
        if id_only:
            country_list = [c['id'] for c in self._countries]
            country_list.sort()
        else:
            country_list = [(c['id'], c['name']) for c in self._countries]
            country_list.sort(key=lambda x: x[0])
        return country_list
    
    def get_aggregate_list(self, id_only: bool=False) -> list:
        '''
        Returns a list of all aggregations and their three-digit codes.
        Results are sorted by codes.

        Input:
            id_only: If True, only returns three-digit codes. Default is False.
        '''
        if id_only:
            agg_list = [a['id'] for a in self._aggregates]
            agg_list.sort()
        else:
            agg_list = [(a['id'], a['name']) for a in self._aggregates]
            agg_list.sort(key=lambda x: x[0])
        return agg_list
    
    def _validate_terms(self, terms: str | list[str] | tuple[str]) -> None:
        if type(terms) not in [str, list, tuple]:
            raise ValueError(f'Search terms should be a string, or a list or tuple of strings, not {type(terms)}.')
        if type(terms) == str:
            terms = [terms]
        return terms

    def search_indicators(self, 
                          terms: str | list[str] | tuple[str]
                         ) -> pd.DataFrame:
        '''
        Search for indicators by specifying one or more strings.
        Returns a pandas DataFrame containing indicator ids and descriptions
        where all search terms were found.

        Input:
            terms: A list of strings containing terms to search for. 
                   Comparisons are case-insensitive.
        '''
        
        terms = self._validate_terms(terms)
                
        matched_indicators = []
        for ind in self._indicators:
            ind_id = ind['id']
            ind_name = ind['name']

            match = True
            for term in terms:
                if term.lower() not in ind_name.lower():
                    match = False
                    break
            if match:
                matched_indicators.append([ind_id, ind_name])
        matched_indicators = pd.DataFrame(data=matched_indicators, 
                                          columns=['id', 'name']
                                         )
        matched_indicators.index = matched_indicators['id']
        matched_indicators.drop(columns=['id'], inplace=True)
        return matched_indicators

    def get_indicator_details(self,
                              indicator_id: str
                              ) -> dict | None:
        '''
        Prints all the details of the given indicator.

        Input:
            - indicator_id: A string, e.g. 'NY.GDP.PCAP.KD'
        '''
        def pretty_print_dict(d: dict, tabs: int=0) -> None:
            for key, value in d.items():
                if type(value) == dict:
                    print(f'{key}:\n')
                    pretty_print_dict(value, tabs+1)
                else:
                    print(f'{'\t'*tabs}{key}: {value}\n')
            return
        
        matched_ind = None
        for ind in self._indicators:
            if ind['id'] == indicator_id:
                matched_ind = ind
        
        if matched_ind is None:
            print(f'No match was found for indicator_id: {indicator_id}\n')
        else:
            pretty_print_dict(matched_ind)
        return None
    
    def search_countries(self,
                         terms: str | list[str] | tuple[str]
                         ) -> pd.DataFrame:
        '''
        Find countries that contain any of the terms. 
        Search is done by name (not code).

        Input:
            terms: A list of strings containing terms to search for.
                   Comparisons are case-insensitive.
        '''
        terms = self._validate_terms(terms)
        
        countries = self.get_country_list()

        matched_countries = []
        for c in countries:
            for term in terms:
                if term.lower() in c[1].lower():
                    matched_countries.append(c)
                    break
        matched_countries = pd.DataFrame(data=matched_countries, columns=['id', 'name'])
        matched_countries.index = matched_countries['id']
        matched_countries.drop(columns=['id'], inplace=True)
        return matched_countries
    
    def search_aggregations(self,
                            terms: list[str]
                            ) -> pd.DataFrame:
        '''
        Find aggregations that contain any of the terms. 
        Search is done by name (not code).

        Input:
            terms: A list of strings containing terms to search for.
                   Comparisons are case-insensitive.
        '''

        terms = self._validate_terms(terms)
        
        aggs = self.get_aggregate_list()

        matched_aggs = []
        for a in aggs:
            for term in terms:
                if term.lower() in a[1].lower():
                    matched_aggs.append(a)
                    break
        matched_aggs = pd.DataFrame(data=matched_aggs, columns=['id', 'name'])
        matched_aggs.index = matched_aggs['id']
        matched_aggs.drop(columns=['id'], inplace=True)
        return matched_aggs

    def _get_data_single(self, 
                         indicator: str,
                         countries: str | list[str] | tuple[str]
                        ) -> list[dict]:
        '''
        Gets data for a single indicator using the get_data function
        from the original API.
        '''
        kwargs = {'indicator': indicator,
                  'country': countries}
        return self._fetch_with_retries(indicator, wb.get_data, **kwargs)
    
    def get_data(self, 
                 indicators: str | list[str] | tuple[str],
                 countries: str | list[str] | tuple[str] | Literal['all'] = 'all'
                ) -> pd.DataFrame:
        '''
        Get data by specifying one or more indicators and countries.

        Input:
            indicators: A string or list of strings containing World Bank indicator codes
            countries:  A string or list of strings containing ISO3 country codes. 
                        Defaults to all countries if not specified. Aggregations are filtered out.
        
        Returns results as a pandas DataFrame.
        '''

        # If countries is 'all', avoid aggregations
        if countries == 'all':
            countries = self.get_country_list(id_only=True)

        # Validate search terms
        indicators = self._validate_terms(indicators)
        countries = self._validate_terms(countries)

        # Must query each indicator separately
        data = []
        for ind in indicators:
            chunk = self._get_data_single(ind, countries)
            data.extend(chunk)
        
        # Repackage results and convert to pandas DataFrame
        rows = []
        for item in data:
            row = {}
            row['country_iso3'] = item['countryiso3code']
            row['country_name'] = item['country']['value']
            row['indicator_id'] = item['indicator']['id']
            row['indicator_name'] = item['indicator']['value']
            row['year'] = item['date']
            row['value'] = item['value']
            row['unit'] = item['unit']
            row['obs_status'] = item['obs_status']
            row['decimal'] = item['decimal']
            rows.append(row)
        return pd.DataFrame(rows)