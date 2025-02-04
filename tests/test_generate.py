import pytest
import os
import sys
from memory_profiler import profile
import matplotlib.pyplot as plt
precision = 10
import h5py
import pandas as pd

fp = open('memory_profiler_basic_mean.log', 'w+')

#Path hack
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(parent_path)
from DeepForest import Generate, preprocess, config
DeepForest_config = config.load_config(dir="..")

site = "NIWO"

def test_Generate_xml_small(tile_xml, DeepForest_config, site):
    #Create generate
    csv_file, h5_file = Generate.run(site=site, tile_xml=tile_xml, DeepForest_config=DeepForest_config, mode="retrain")
    
    #view sample 
    hf = h5py.File(h5_file, 'r')
    image = hf["train_imgs"][10,...]    
    
    #Check csv has correct length
    plt.imshow(image[:,:,:3].astype("int"))
   
    #assert
    df = pd.read_csv(csv_file)
    assert df.shape[0] > 0, "Data is empty"
    
    #Check h5 has correct length
    assert  len(hf["train_imgs"]) == 256, "Images have the incorrect length"
    
tile_xml = "../data/NIWO/annotations/NIWO_002.xml"
test_Generate_xml_small(site=site, tile_xml=tile_xml, DeepForest_config=DeepForest_config)

@profile(precision=precision, stream=fp)
def test_Generate_xml_large(tile_xml, DeepForest_config, site):
    #Create generate
    csv_file, h5_file = Generate.run(site=site, tile_xml=tile_xml, DeepForest_config=DeepForest_config, mode="retrain")
    
    #view sample 
    hf = h5py.File(h5_file, 'r')
    image = hf["train_imgs"][10,...]    
    
    #Check csv has correct length
    plt.imshow(image[:,:,:3].astype("int"))
   
    #assert
    df = pd.read_csv(csv_file)
    assert df.shape[0] > 0, "Data is empty"
    
    #Check h5 has correct length
    assert  len(hf["train_imgs"]) == 256, "Images have the incorrect length"
    
tile_xml = "../data/NIWO/annotations/2018_NIWO_2_450000_4426000_image_crop.xml"
test_Generate_xml_large(site=site, tile_xml=tile_xml, DeepForest_config=DeepForest_config)

tile_csv = "/Users/ben/Documents/DeepLidar/data/TEAK/training/NEON_D17_TEAK_DP1_324000_4104000_classified_point_cloud_colorized.csv"
def test_Generate_csv(tile_csv, DeepForest_config, site):
    csv_file, h5_file  = Generate.run(tile_csv, DeepForest_config=DeepForest_config, site=site)

#test_Generate_csv(tile_csv, DeepForest_config, site)