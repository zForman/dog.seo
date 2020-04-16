import pytest
import requests
import json


def expected_data():
    return {
        'message':
            {
                'affenpinscher': [],
                'african': [],
                'airedale': [],
                'akita': [],
                'appenzeller': [],
                'australian': ['shepherd'],
                'basenji': [],
                'beagle': [],
                'bluetick': [],
                'borzoi': [],
                'bouvier': [],
                'boxer': [],
                'brabancon': [],
                'briard': [],
                'buhund': ['norwegian'],
                'bulldog': ['boston', 'english', 'french'],
                'bullterrier': ['staffordshire'],
                'cairn': [],
                'cattledog': ['australian'],
                'chihuahua': [],
                'chow': [],
                'clumber': [],
                'cockapoo': [],
                'collie': ['border'],
                'coonhound': [],
                'corgi': ['cardigan'],
                'cotondetulear': [],
                'dachshund': [],
                'dalmatian': [],
                'dane': ['great'],
                'deerhound': ['scottish'],
                'dhole': [],
                'dingo': [],
                'doberman': [],
                'elkhound': ['norwegian'],
                'entlebucher': [],
                'eskimo': [],
                'finnish': ['lapphund'],
                'frise': ['bichon'],
                'germanshepherd': [],
                'greyhound': ['italian'],
                'groenendael': [],
                'havanese': [],
                'hound': ['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker'],
                'husky': [],
                'keeshond': [],
                'kelpie': [],
                'komondor': [],
                'kuvasz': [],
                'labrador': [],
                'leonberg': [],
                'lhasa': [],
                'malamute': [],
                'malinois': [],
                'maltese': [],
                'mastiff': ['bull', 'english', 'tibetan'],
                'mexicanhairless': [],
                'mix': [],
                'mountain': ['bernese', 'swiss'],
                'newfoundland': [],
                'otterhound': [],
                'ovcharka': ['caucasian'],
                'papillon': [],
                'pekinese': [],
                'pembroke': [],
                'pinscher': ['miniature'],
                'pitbull': [],
                'pointer': ['german', 'germanlonghair'],
                'pomeranian': [],
                'poodle': ['miniature', 'standard', 'toy'],
                'pug': [],
                'puggle': [],
                'pyrenees': [],
                'redbone': [],
                'retriever': ['chesapeake', 'curly', 'flatcoated', 'golden'],
                'ridgeback': ['rhodesian'],
                'rottweiler': [],
                'saluki': [],
                'samoyed': [],
                'schipperke': [],
                'schnauzer': ['giant', 'miniature'],
                'setter': ['english', 'gordon', 'irish'],
                'sheepdog': ['english', 'shetland'],
                'shiba': [],
                'shihtzu': [],
                'spaniel': ['blenheim', 'brittany', 'cocker', 'irish', 'japanese', 'sussex', 'welsh'],
                'springer': ['english'],
                'stbernard': [],
                'terrier': ['american', 'australian', 'bedlington', 'border', 'dandie', 'fox', 'irish', 'kerryblue',
                            'lakeland', 'norfolk', 'norwich', 'patterdale', 'russell', 'scottish', 'sealyham', 'silky',
                            'tibetan', 'toy', 'westhighland', 'wheaten', 'yorkshire'],
                'vizsla': [],
                'waterdog': ['spanish'],
                'weimaraner': [],
                'whippet': [],
                'wolfhound': ['irish']
            },
        'status': 'success'
    }


@pytest.mark.parametrize('expected_data, breed, status_code, content_type', [
    (expected_data(), 'bulldog', [200], 'application/json'),
    (expected_data(), 'chihuahua', [300], 'application/json'),
    (expected_data(), 'husky', [200], 'application/json'),
    (expected_data(), 'labrador', [300], 'application/json')
])
def test_list_all_breed(get_list_all_breed, expected_data, breed, status_code, content_type):
    response = requests.get(get_list_all_breed)
    j = json.loads(response.text)
    for code in status_code:
        assert response.status_code <= code
        assert response.headers['Content-Type'] == content_type
        assert j == expected_data
        assert breed in j['message']
