import pandas as pd
import requests


def get_json():
    res = requests.get('htts://steamspy.com/api.php?request=all').json()
    names = set()
    for attribute, value in res.items():
        names.add(value['name'])
    return names


def write_app_id_to_csv(api_result):
    data = pd.read_csv('AllApps.csv')
    print(len(data))
    # data['appid'] = data['name'].map(lambda x: get_app_id(api_result, x))
    num = 0
    rows = []
    for index, row in data.iterrows():
        if row['appid'] == None or row['appid'] == '':
            print(row)

    # a = filter(lambda p: p['appid'] is None, data)
    # data = data[(data['appid'] in (None, ""))]
    # return data
    print(num)
    return rows


def get_app_id(api_result, game_name):
    for i in api_result:
        if i[1] == game_name:
            return i[0]


def work():
    api_result = get_json()
    print(len(api_result))
    # export_csv()
    df = pd.read_csv('apps.csv')
    df = df[~df['name'].isin(api_result)]
    df.to_csv('not_in.csv', index=False)

    # file_result = write_app_id_to_csv(api_result)
    # print(len(file_result))

    # intersection = set(api_result).intersection(set(file_result))
    # print(len(intersection))


def export_csv():
    df = pd.read_excel('AllApps.xlsx')
    df.to_csv('apps.csv', index=False)


if __name__ == '__main__':
    work()



