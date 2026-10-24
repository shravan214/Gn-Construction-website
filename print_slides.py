import json

with open('gn_ppt_assets/slides_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for slide in data:
    if slide['texts']:
        print('--- SLIDE', slide['slide'], '---')
        for t in slide['texts']:
            print(repr(t))
