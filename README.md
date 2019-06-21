# Combining LIDAR and RGB airborne imagery for individual tree-crown detection

Ben. G. Weinstein

## Dependencies

DeepForest uses conda environments to manage python dependencies

Some key dependencies that have some build specific installs include

* OpenCV
* Keras + Tensorflow
* GDAL

I've forked my own version of the wonderful keras retinanet implementation.

https://github.com/bw4sz/keras-retinanet

```
conda env create --name DeepForest -f=environment.yml
```

Depending on conda env, you may need to download laszip directly see: https://stackoverflow.com/questions/49500149/laspy-cannot-find-laszip-when-is-installed-from-source-laszip-is-in-path

All configurations are in the _config.yml 

To install the retinanet, activate the conda env and pip install

For example:
```
MacBook-Pro:keras-retinanet ben$ conda activate DeepLidar_dask
(DeepLidar_dask) MacBook-Pro:keras-retinanet ben$ pip install .
Processing /Users/ben/Documents/keras-retinanet
```


Generate data

```
python dask_generate.py
```

## Training

```
python train.py
```

## Evalution

```
python eval.py
```

## Published articles

Our first article was published in *Remote Sensing* and can be found [here](https://www.mdpi.com/2072-4292/11/11/1309). 

This codebase is constantly evolving and improving. To access the code at the time of publication, see Releases.
The results of the full model can be found on our [comet page](https://www.comet.ml/bw4sz/deeplidar/2645e41bf83b47e68a313f3c933aff8a).

## Data

See the data repo: https://github.com/weecology/NeonTreeEvaluation
* With the exception of the two hand annotated tiles that are too big to fit on github. See README of that repo.
Data from [SJER](https://www.neonscience.org/field-sites/field-sites-map/SJER) were used in the first publication. We are happy to share any data, any time.
