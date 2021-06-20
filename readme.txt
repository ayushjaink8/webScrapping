How to Setup!

################################################################################################

**For linux or mac users :

git clone https://github.com/ayushjaink8/webScrapping.git             # to clone the git repository

cd webScrapping                                                    # enter into the project

python3 -m pip install --user virtualenv                        # install virtual environment
python3 -m venv venv                                          # Creating the virtual environment
. venv/bin/activate                                          # Activate the virtual environment
[ (venv) will appear in front of your directory ]

pip install -r requirements.txt                                 # Install all the requirements

python3 scrap.py                                         # run the code

################################################################################################

**For Windows users:

git clone https://github.com/ayushjaink8/webScrapping.git             # to clone git repository

cd webScrapping                                                     # enter into the project

python -m pip install --user virtualenv                        # install virtual environment
python -m venv venv                                          # Creating the virtual environment
cd venv/Scripts && activate                                  # Activate the virtual environment
[ (venv) will appear in front of your directory ]

cd ../../                                                       # to change directory back to webScrapping

pip install -r requirements.txt                                 # Install the requirements

python scrap.py                                         # run the code

################################################################################################



1) scrap.py
-- scraps property data from "https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi"

2) filters.py
--- scraps the data after applying filters