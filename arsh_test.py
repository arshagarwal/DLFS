import numpy as np
from PIL import Image
import os
from collections import OrderedDict
from options.test_options import TestOptions
from data.data_loader import CreateDataLoader
from models_distan.models import create_model
import util.util as util
from util.visualizer import Visualizer
import torch
import argparse

def get_translations(model, img_path, dataset):
  """
  model: model used
  img_path: path of the image file that is to be translated
  returns a row of images in the forms original image, translations
  """
  data = dataset.dataset.get_item_from_path(img_path)
  visuals = model.inference(data)
  images = visuals[0]['orig_img']

  for key in visuals[0].keys():
    if key == 'orig_img':
      continue
    curr_img = visuals[0][key]
    images = np.concatenate((images, curr_img), axis = 1)

  return images

def translate_images(model, dir_path, dataset):
  """
  model: model to be used
  dir_path: path of the directory containing images
  
  performs translations on all images and saves them in the result folder directory 
  """
  if 'results' not in os.listdir('./'):
    os.mkdir('results')

  for count, curr_img in enumerate(os.listdir(dir_path)):
    curr_res = get_translations(model, dir_path + '/' + curr_img, dataset)
    curr_res = Image.fromarray(curr_res)
    curr_res.save('results/{}.jpg'.format(count))

if __name__ == "__main__":
  
  opt = TestOptions().parse(save=False)
  opt.display_id = 0 # do not launch visdom
  opt.nThreads = 1   # test code only supports nThreads = 1
  opt.batchSize = 1  # test code only supports batchSize = 1
  opt.serial_batches = True  # no shuffle
  opt.no_flip = True  # no flip
  opt.in_the_wild = True # This triggers preprocessing of in the wild images in the dataloader
  opt.traverse = True # This tells the model to traverse the latent space between anchor classes
  opt.interp_step = 1
  data_loader = CreateDataLoader(opt)
  dataset = data_loader.load_data()

  opt.name = 'males_model' # change to 'females_model' if you're trying the code on a female image
  model = create_model(opt)
  model.eval()

  # command line args 
  parser = argparse.ArgumentParser()
  parser.add_argument('--test_dir', type = str, default = 'test')
  config = parser.parse_args()

  translate_images(model, config.test_dir, dataset)





