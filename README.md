# dog.seo
API Testing of dog.seo using Pytest

To run **test_list_all_breeds.py**:

`pytest test_random_images.py -s -v --base_url https://dog.ceo/api/ --num 15`

To run **test_random_images.py**:

`pytest test_list_all_breeds.py -s -v --base_url https://dog.ceo/api/`

To run **test_list_of_particular_breed.py**

`pytest test_list_of_particular_breed.py -v -s --base_url https://dog.ceo/api/`

To ran **all tests**:

`pytest --base_url https://dog.ceo/api/`

To run **test_random_img_breed.py**:

`pytest test_random_img_breed.py --breed bulldog --base_url https://dog.ceo/api/ -v -s` 

To run **test_img_by_sub_breed.py**:

`pytest test_img_by_sub_breed.py --base_url  https://dog.ceo/api/ --all_img_sub_breed hound` 