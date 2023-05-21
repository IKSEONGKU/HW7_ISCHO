import pandas as pd

def main():
    data = [[1000,25],[280,120],[900,30]]
    indx = ['store1','store2','store3']
    col = ['unit price','number']
    df = pd.DataFrame(data, index = indx, columns = col)
    print(df)
    print()

    df['total price'] = df['unit price'] * df['number']
    print(df)
    print()

    df = df.sort_values(by=['total price'], ascending=False)
    print(df.iloc[0:2])

if __name__ == '__main__':
    main()
