#!/usr/bin/env python3

import csv
import json
import urllib.request

INDEX_URL = 'https://petition.parliament.uk/archived/petitions.json'
ONS_CODES_URL = 'https://petition.parliament.uk/archived/petitions/131215.json'

def fetch_json(petition_url):
    return json.load(urllib.request.urlopen(petition_url))

def parse_index(next_url):
    while next_url:
        index_json = fetch_json(next_url)
        next_url = index_json['links']['next']
        for petition in index_json['data']:
            yield petition['links']['self']

def parse_petition(petition_url):
    petition_json = fetch_json(petition_url)
    data = petition_json['data']
    attributes = data['attributes']
    signatures = { cons['ons_code']: cons['signature_count'] for cons in attributes['signatures_by_constituency'] }
    return (data['id'], attributes['action'], *(signatures.get(cons, 0) for cons in ONS_CODES))
    

ONS_CODES = sorted([cons['ons_code'] for cons in fetch_json(ONS_CODES_URL)['data']['attributes']['signatures_by_constituency']])
header = ('id', 'action', *ONS_CODES)

with open('petitions.csv', 'w') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(header)
    for petition_url in parse_index(INDEX_URL):
        writer.writerow(parse_petition(petition_url))
