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

    md_request = MarketDataRequest(start_date="01 Jan 2001",
                                   finish_date="01 Dec 2008",
                                   tickers=["BLK"],
                                   vendor_tickers=["BLK"],
                                   fields=["close"],
                                   data_source="twelve")
    
    df = market.fetch_market(md_request)

    
    
    print(df)
