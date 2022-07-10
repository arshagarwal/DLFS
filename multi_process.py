import argparse
import os
import numpy as np

parser = argparse.ArgumentParser()
# Model configuration.
parser.add_argument('--data', type=str, default='data', help='path to dataset')
parser.add_argument('--n_samples', type=int, default=-1, help='number of samples to be chosen')
parser.add_argument('--t_per_domain', type=int, help='number of translations per domain')
config = parser.parse_args()

path = config.data
names = np.array(os.listdir(path))
np.random.shuffle(names)
if config.n_samples != -1:
  names = names[:config.n_samples]

def create_temp(root, dest, img_list, suffix):
  """
  Creates copies of image files by adding suffix to names
  root: path to the folder containing test images\
  dest: path to the destination folder where images are to be copied 
  img_list: list of names of images in the root directory
  suffix: suffix to be added behind an image name
  """
  for curr_img in img_list:
    os.system("cp {}/{} {}/{}_{}.jpg".format(root, curr_img, dest, curr_img.split('.')[0], suffix))
  
  return 
dest = path
if config.t_per_domain > 1:
  dest = config.data + "t_" + str(config.t_per_domain)
  os.mkdir(dest)
  for img in names:
    os.system("cp -r {}/{} {}".format(config.data, img, dest)) 
  for i in range(1, config.t_per_domain):
    suffix = "t_{}".format(i)
    create_temp(config.data, dest, names, suffix)
    print("root path: {} dest path {} img_list {} suffix {}".format(config.data, 
    dest, names, suffix))



  