from sec_edgar_downloader import Downloader

dl = Downloader("MyCompanyName", "my.email@domain.com")

dl.get("8-K", "AAPL")
