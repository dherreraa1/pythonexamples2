import json

def load_rates(json_file: str) -> dict[str, dict]:
    with open(json_file, 'r') as file:
        return json.load(file)

def convert(amount: float, base: str, to: str, rates: dict[str, dict]) -> float:
    base: str = base.lower() # type:ignore
    to: str = to.lower() # type:ignore

    if base == 'eur' and to == 'eur':
        return amount

    from_rates: dict | None = rates.get(base)
    to_rates: dict | None = rates.get(to)

    if from_rates is not None and to_rates is not None:
        return amount * (to_rates['rate'] / from_rates['rate'])
    elif to_rates is not None and base == 'eur':
        return amount * to_rates['rate'] 
    elif from_rates is not None and to == 'eur':
        return amount * from_rates['inverseRate']
    else:
        print('The \'from\' and/or \'to\' currency values are not valid. The valid values are:')
        for key in rates:
            if key != list(rates)[-1]:
                print(key + ', ',  end='')
            else:
                print(key)
        return 0.0

def main() -> None:
    rates: dict[str, dict] = load_rates('rates.json')
    result: float = convert(amount=1000, base='eur', to='usd', rates=rates)
    if result:
        print(result)

if __name__ == '__main__':
    main()