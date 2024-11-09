__author__ = "finlayrossdavie"  # Finlay Ross-Davie





if __name__ == '__main__':
    ###### below line CRUCIAL when running Windows, otherwise multiprocessing
    # doesn't work! (not necessary on Linux)
    from findatapy.util import SwimPool;
    from findatapy.util.dataconstants import DataConstants
    
    DataConstants.reset_api_key("TWELVE", "b6bf6ca2ee9a4747a964336acb85a769")

    SwimPool()

    from findatapy.market import Market, MarketDataRequest, MarketDataGenerator

    market = Market(market_data_generator=MarketDataGenerator())

    # Get the first release for GDP and also print the release date of that
    md_request = MarketDataRequest(
        start_date="01 Jun 2000",
        # start date (download data over past decade)
        data_source='twelve',  # use Twelve Data as source 
        tickers=['BLK'],  # ticker
        fields=['actual-release', 'release-date-time-full'],
        # which fields to download
        vendor_tickers=['BLK'],  # ticker (FRED)
        vendor_fields=['actual-release',
                       'release-date-time-full'])  # which FRED fields to download
    df = market.fetch_market(md_request)


    print(df)

    # Compare the close and actual release of US GDP (and the final)
    md_request = MarketDataRequest(
        start_date="01 Jun 2000",
        # start date (download data over past decade)
        data_source='twelve',  # use ALFRED/FRED as data source
        tickers=['US GDP'],  # ticker
        fields=['actual-release', 'close'],  # which fields to download
        vendor_tickers=['GDP'],  # ticker (FRED)
        vendor_fields=['actual-release',
                       'close'])  # which FRED fields to download

    df = market.fetch_market(md_request)

    from chartpy import Chart, Style

    style = Style(title="US GDP first vs last")

    Chart().plot(df, style=style)

    # Get the change NFP SA (need to calculate that from the acutal-release and first-revision)
    md_request = MarketDataRequest(
        start_date="01 Jun 2000",
        # start date (download data over past decade)
        data_source='twelve',  
        tickers=['US NFP'],  # ticker
        fields=['actual-release', 'first-revision', 'release-date-time-full'],
        # which fields to download
        vendor_tickers=['PAYEMS'],  # ticker (FRED)
        vendor_fields=['actual-release', 'first-revision',
                       'release-date-time-full'])  # which FRED fields to download

    df = market.fetch_market(md_request)

    # calculate the headline change in NFP
    df['US NFP change'] = df['US NFP.actual-release'] - df[
        'US NFP.first-revision'].shift(1)

    print(df)

    from chartpy import Chart, Style
    import pandas

    style = Style(title="US NFP change (actual)")

    df1 = pandas.DataFrame(df['US NFP change'])

    Chart().plot(df1, style=style)

    # Get release times on their own
    # Get the change NFP SA
    # need to calculate that from the acutal-release and first-revision)
    md_request = MarketDataRequest(
        start_date="01 Aug 2013",
        finish_date="30 Nov 2019",
        data_source='twelve',
        tickers=['US NFP'],
        fields=['release-date-time-full'],
        vendor_tickers=['PAYEMS'],
        vendor_fields=['release-date-time-full'])

    market = Market(market_data_generator=MarketDataGenerator())

    df_nfp = market.fetch_market(md_request)

    print(df_nfp)
