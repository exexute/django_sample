#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: owefsad@gmail.cn
# datetime: 2022/4/13 下午6:17

import requests
import time
from lxml import etree

base_url = "https://hz.zu.ke.com"

GLOBAL_FILTER = {
    '居民住宅': False,
    '天然气': False,
}


def base_requests(house_url):
    time.sleep(0.8)
    req = requests.get(url=house_url)
    return etree.HTML(req.text)


# todo: read info for house info
def read_house_info(house_uri):
    house_url = base_url + house_uri
    html = base_requests(house_url=house_url)
    base_infos = set()

    try:
        name = html.xpath('/html/body/div[3]/div[1]/div[3]/p/text()')[0].strip()
        base_infos.add(name)
    except Exception as e:
        print(f'{house_url}')

    info = html.xpath("/html/body/div[3]/div[1]/div[3]/div[3]/div[2]/div[3]/ul[1]/li[12]/text()")
    if info is None:
        return

    if GLOBAL_FILTER['居民住宅'] and '民水' not in info[0]:
        return

    base_info_list = html.xpath("/html/body/div[3]/div[1]/div[3]/div[3]/div[2]/div[3]/ul[1]/li")
    for base_info_item in base_info_list:
        base_infos.add(base_info_item.xpath('text()')[0])

    base_info_list = html.xpath("/html/body/div[3]/div[1]/div[3]/div[3]/div[2]/ul/li")
    for base_info_item in base_info_list:
        try:
            base_infos.add(base_info_item.xpath('text()')[1].strip())
        except Exception as e:
            continue

    # todo: 根据输入条件处理该判断条件
    fire = html.xpath('/html/body/div[3]/div[1]/div[3]/div[3]/div[2]/ul/li[11]/i/@style')[0].strip().replace(
        'background-image: url(https://ke-image.ljcdn.com/rent-front-image/', '')
    support_gas = fire.startswith('aa2df480d8496d0851febe38022b1da2.1524906515169_c731df5b-234f-4716-ba42-0058f833204c')
    if GLOBAL_FILTER['天然气'] and support_gas is False:
        return
    if fire.startswith('aa2df480d8496d0851febe38022b1da2.1524906515169_c731df5b-234f-4716-ba42-0058f833204c'):
        base_infos.add('天然气：有')
    else:
        base_infos.add('天然气：无')
    print(f'{house_url} - {info}')
    print(base_infos)


def read_house_list(house_list_url):
    html = base_requests(house_url=house_list_url)

    html_data = html.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div')

    if len(html_data) > 0:
        for house_item in html_data:
            href = house_item.xpath('a/@href')
            if href and not href[0].startswith('/apartment/'):
                read_house_info(href[0])
        return True
    else:
        print("no house data.")
        return False


# 输入位置后，以输入的位置为中心，自动查找上下几站地（共5站地）的房子
if __name__ == '__main__':
    house_list_uri = input(
        '请粘贴目标地铁站对应的url地址，如：杭州5号线创景路站，https://hz.zu.ke.com/ditiezufang/li1820044952055481s18000002564946/rt200600000001l0l1/\n> ')
    house_list_uri = house_list_uri.replace(base_url, '')
    station_interval = int(input('请输入目标地铁站上下的站地数量，如：3，表示以目标地铁站为中心，同时看前后3站地，共7站地的房子\n> '))
    GLOBAL_FILTER['居民住宅'] = input('是否选择居民楼？y or n\n>') == 'y'
    GLOBAL_FILTER['天然气'] = input('是否必须带天然气? y or n\n>') == 'y'

    target_house_list_uris = list()
    house_list_url = base_url + house_list_uri
    html = base_requests(house_list_url)

    current_station_index = 0
    subway_stations = html.xpath('/html/body/div[3]/div[1]/div[4]/div[1]/ul[4]/li')
    for index in range(len(subway_stations)):
        station = subway_stations[index]
        station_class = station.xpath('@class')[0].strip()
        if 'strong' in station_class:
            current_station_index = index
        name = station.xpath('a/text()')[0].strip()
        uri = station.xpath('a/@href')[0].strip()
        uris = uri.split('/')
        uris[3] = 'pg{page}' + uris[3]
        uri = '/'.join(uris)
        target_house_list_uris.append({
            'name': name,
            'uri': uri
        })
    _left = current_station_index - station_interval
    _right = current_station_index + station_interval + 1
    left_index = _left if _left >= 1 else 1
    right_index = _right if _right <= len(target_house_list_uris) else len(target_house_list_uris)

    target_house_list_uris = target_house_list_uris[left_index:right_index]
    subways_name = ','.join([_['name'] for _ in target_house_list_uris])
    print(f'即将开始找房，条件如下：')
    print(f'\t地铁站：{",".join([_["name"] for _ in target_house_list_uris])}')
    print(f'\t居民住宅：{"是" if GLOBAL_FILTER["居民住宅"] else "否"}')
    print(f'\t带天然气：{"是" if GLOBAL_FILTER["天然气"] else "否"}')

    for target_house_list_uri in target_house_list_uris:
        current_page = 1
        while True:
            house_list_url = base_url + target_house_list_uri['uri'].format(page=current_page)
            print(house_list_url)
            if read_house_list(house_list_url):
                current_page += 1
            else:
                break
