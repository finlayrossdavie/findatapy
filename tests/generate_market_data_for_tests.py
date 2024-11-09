__author__ = "saeedamen"  # Saeed Amen

#
# Copyright 2016 Cuemacro
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on a "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#


from findatapy.market import MarketDataGenerator, Market, MarketDataRequest

from findatapy.util.dataconstants import DataConstants
    
DataConstants.reset_api_key("TWELVE", "b6bf6ca2ee9a4747a964336acb85a769")


def generate_market_data_for_tests():
    # generate daily S&P500 data from Quandl


    md_request = MarketDataRequest(start_date="01 Jan 2001",
                                   finish_date="01 Dec 2008",
                                   tickers=["BLK"],
                                   vendor_tickers=["BLK"],
                                   fields=["close"],
                                   data_source="twelve")

    market = Market(market_data_generator=MarketDataGenerator())

    df = market.fetch_market(md_request)
    df.to_csv("S&P500.csv")

    # generate tick data from DukasCopy for EURUSD
    md_request = MarketDataRequest(start_date="14 Jun 2016",
                                   finish_date="15 Jun 2016", cut="NYC",
                                   category="fx",
                                   fields=["bid"], freq="tick",
                                   data_source="dukascopy",
                                   tickers=["EURUSD"])

    market = Market(market_data_generator=MarketDataGenerator())

    df = market.fetch_market(md_request)
    df.to_csv("EURUSD_tick.csv")


if __name__ == "__main__":
    generate_market_data_for_tests()
