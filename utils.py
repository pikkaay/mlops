import os
import xml.etree.ElementTree as ET
from functools import reduce
import urllib.parse
import numpy as np
from sklearn.cluster import KMeans


def get_anchors(path, num_anchors):
    '''
    Takes data and number of anchors required then returns anchor boxes
    Parameters
    ----------
    path: string
        path to labelled data in text forrmat
    num_anchors: int
        number of anchor boxes required
    
    Returns
    -------
    centroids : ndarray
        array of anchor boxes
    '''
    with open(path) as f:
        lines = f.readlines()
    
    boxData=[]
    for line in lines:
        line = line.split()
        box = [int(x) for x in line[1:][0].split(',') if x != '']
        boxData.append(box)
    boxData = np.array(boxData)
    
    boxes_wh = boxData[...,2:4] - boxData[...,0:2]
    
    kmeans = KMeans(n_clusters=num_anchors)
    kmeans = kmeans.fit(boxes_wh)
    
    centroids = kmeans.cluster_centers_
    centroids = centroids.astype(int)//32
    
    x = np.array(centroids)[...,0]*np.array(centroids)[...,1]
    mask = [index for index, num in sorted(enumerate(x), key=lambda x: x[-1])]
    
    return centroids[mask]

def train_test_split(path, split=0.9):
    """
    Split data to train and test
    """
    with open(path) as file:
        lines = file.readlines()
        
    np.random.shuffle(lines)
    
    train = lines[:int(len(lines) * split)]
    val = lines[len(train):]
    return np.array(train), np.array(val)

def xml_to_txt(path, labels):
    '''
    Converting xml created using labelimg tool @https://github.com/tzutalin/labelImg to text format
    
    '''
    for im in os.listdir(path):
        if im.endswith('.xml'):
            im = os.path.join(path, im)
            xml_list = []
            line = []
            tree = ET.parse(im)
            root = tree.getroot()
            
            for member in root.findall('size'):
                w = int(member[0].text)
                h = int(member[1].text)
            
            im = im.rsplit( ".", 1 )[ 0 ]+'.jpg'
            im = urllib.parse.quote(im) # To handle space or special charecter in file name
            
            # Append image path to line 
            line.append([im]) 
            
            # Append bbox and label to line
            for member in root.findall('object'): 
                label = labels.index(member[0].text)
                line.append([
                         str(' '+ str(round(int(member[4][0].text)*w//int(root.find('size')[0].text),2))),
                         round(int(member[4][1].text)*h//int(root.find('size')[1].text),2),
                         round(int(member[4][2].text)*w//int(root.find('size')[0].text),2),
                         round(int(member[4][3].text)*h//int(root.find('size')[1].text),2),
                         label
                            ])
                
            line = reduce(lambda x,y: x+y,line)
            with open ('./data.txt', 'a') as fo:
                fo.write(','.join([str(n) for n in line]))
                fo.write(' \n')