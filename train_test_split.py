import os
files_list = os.listdir('/Users/shiqinchoo/Desktop/satellite/rgb')
print (files_list)

path = '/Users/shiqinchoo/Desktop/satellite/rgb/'
folders_list = []
for i in range(len(files_list)):
  folder_name = path + files_list[i]
  folders_list.append(folder_name)

folders_list

folder_length = []
for i in range(len(folders_list)):
  length = len(os.listdir(folders_list[i]))
  folder_length.append(length)

folder_length

import json #create the json
import shutil #copy images to train, test and valid dirs
import os #files and dirs manipulation
import math #split calculate

parent_dir = '/Users/shiqinchoo/Desktop/satellite/rgb/'

os.chdir(parent_dir)
category_list = list(filter(lambda x: os.path.isdir(x), os.listdir()))
for category in category_list:
 print(category)

data_set_dirs= ['train','test']
for dsdirs in data_set_dirs:
 path = parent_dir + '/'+ dsdirs
 os.mkdir( path,755 )

train_prop = 0.8
test_prop = 1-train_prop

def create_dataset():
  for ii,cat in enumerate(category_list): 
    src_path = parent_dir + '/' + cat
    dest_dir1 = parent_dir+'/train/'+str(ii)
    dest_dir2 = parent_dir+'/test/'+str(ii)
    
    dest_dirs_list = [dest_dir1,dest_dir2]
    
    for dirs in dest_dirs_list:
      os.mkdir(dirs,755 )

    #get files' names list from respective directories
    os.chdir(src_path)
    files = [f for f in os.listdir() if os.path.isfile(f)]

    #get training, testing and validation files count
    train_count = math.ceil(train_prop*len(files))
    test_count = int(len(files)-train_count)

    #get files to segragate for train and test data set
    train_data_list = files[0: train_count]
    test_data_list = files[train_count:]

    for train_data in train_data_list:
      train_path = src_path + '/' + train_data
      shutil.copy(train_path,dest_dir1)

    for test_data in test_data_list:
      test_path = src_path + '/' + test_data
      shutil.copy(test_path,dest_dir2)


create_dataset()

#save category data as dictionary in a json file
cat_data = {}
for ix,cat in enumerate(category_list):
 cat_data[ix] = cat
with open('/Users/shiqinchoo/Desktop/satellite/rgb/cat_data.json', 'w') as outfile: 
 json.dump(cat_data , outfile)


import os
train_folder_length = []
train_list = os.listdir('/Users/shiqinchoo/Desktop/satellite/rgb/train')

len(train_list)


path = '/Users/shiqinchoo/Desktop/satellite/rgb/train'
train_folder_list = []
for i in range(len(train_list)):
  folder_name = path + train_list[i]
  train_folder_list.append(folder_name)

train_folder_list

import os
test_list = os.listdir('/Users/shiqinchoo/Desktop/satellite/rgb/test')

len(test_list)

path = '/Users/shiqinchoo/Desktop/satellite/rgb/test/'
test_folder_list = []
for i in range(len(test_list)):
  folder_name = path + test_list[i]
  test_folder_list.append(folder_name)

test_folder_list






