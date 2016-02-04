#Download and install Anaconda: http://docs.continuum.io/anaconda/install.html

conda create -p ./mlenv python=3.4 python
source activate ./mlenv

conda install cython
conda install numpy scipy scikit-learn pandas xray pillow
conda install ipython ipython-notebook matplotlib seaborn
#pip install theano  # note -- keras depends on latest devel

cd source_packages
git clone https://github.com/Theano/Theano.git
pip install -e ./source_packages/Theano/
cd ../


pip install keras
pip install tweepy

cd source_packages
git clone https://github.com/danielfrg/word2vec
cd word2vec
python setup.py install
cd ..
rm -rf word2vec
cd ..
