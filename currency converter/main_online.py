import requests

def download_rates() -> dict[str, float]:
    api_key = 'b22f612e87a55327602b6b6aae959796'
    url = 'http://data.fixer.io/api/latest'

    params = {
        'access_key': api_key,
        'symbols': 'USD,EUR,GBP,CAD,AUD,JPY,CHF,CNY,INR,BRL,ZAR,MXN,NZD,SGD,HKD,SEK,NOK,DKK,RUB,KRW,TRY,IDR,THB,HUF,CZK,PLN,ILS,PHP,MYR,TWD,ARS,CLP,COP,PEN,VND,AED,SAR,QAR,KWD,BHD,OMR,JOD,LKR,BDT,PKR,NGN,GHS,EGP,DZD,MAD,TND,UAH,KZT,UZS,GEL,MNT,KES,UGX,TZS,RWF,ETB,XAF,XOF,XCD,XPF,BSD,BBD,BZD,TTD,JMD,HTG,DOP,CUP,GIP,FJD,PGK,SBD,WST,VUV,TOP,MOP,NAD,BWP,ZMW,MWK,MUR,LSL,SZL,BND,KHR,MMK,LAK,KGS,TMT,BYN'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("rates", {})
    else:
        raise Exception(f'API request failed with status code {response.status_code}')

def convert(amount: float, base: str, to: str, rates: dict[str, float]) -> float:
    base: str = base.upper() # type:ignore
    to: str = to.upper() # type:ignore

    from_rates: float | None = rates.get(base)
    to_rates: float | None = rates.get(to)

    if from_rates is not None and to_rates is not None:
        return amount * (to_rates / from_rates)
    else:
        print('The \'from\' and/or \'to\' currency values are not valid. The valid values are:')
        for key in rates:
            if key != list(rates)[-1]:
                print(key + ', ',  end='')
            else:
                print(key)
        return 0.0

def main() -> None:
    rates: dict[str, float] = download_rates()
    if rates:
        result: float = convert(amount=2000, base='usd', to='cop', rates=rates)
    else:
        print("No answer from the server in this moment.")
    if result:
        print(result)

if __name__ == '__main__':
    main()