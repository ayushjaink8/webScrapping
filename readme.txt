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

python3 scrap_properties.py                                         # run the code

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

python scrap_properties.py                                         # run the code

################################################################################################