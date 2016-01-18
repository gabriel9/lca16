#Download and install Anaconda: http://docs.continuum.io/anaconda/install.html

conda create -p ./mlenv python=3.4 numpy scipy scikit-learn pandas xray pillow
source activate ./mlenv

conda install cython
conda install numpy scipy scikit-learn pandas xray pillow
conda install ipython ipython-notebook matplotlib seaborn
pip install theano
pip install keras
pip install tweepy

git clone https://github.com/danielfrg/word2vec
cd word2vec
python setup.py install
cd ..
rm -rf word2vec
