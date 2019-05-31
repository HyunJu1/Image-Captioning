import json
import os
import download
from cache import cache
data_dir = "data/coco/"
train_dir = "data/coco/train2017"
val_dir = "data/coco/val2017"
data_url = "http://images.cocodataset.org/"
def _load_records(train=True):
    if train:
        filename = "captions_train2017.json"
    else:
        filename = "captions_val2017.json"

    path = os.path.join(data_dir, "annotations", filename)

    with open(path, "r", encoding="utf-8") as file:
        data_raw = json.load(file)

    images = data_raw['images']
    annotations = data_raw['annotations']
    records = dict()
    for image in images:
        image_id = image['id']
        filename = image['file_name']
        record = dict()
        record['filename'] = filename
        record['captions'] = list()
        records[image_id] = record
    for ann in annotations:
        image_id = ann['image_id']
        caption = ann['caption']
        record = records[image_id]
        record['captions'].append(caption)

    records_list = [(key, record['filename'], record['captions'])
                    for key, record in sorted(records.items())]

    ids, filenames, captions = zip(*records_list)
    return ids, filenames, captions

def set_data_dir(new_data_dir):

    global data_dir, train_dir, val_dir

    data_dir = new_data_dir
    train_dir = os.path.join(new_data_dir, "train2017")
    val_dir = os.path.join(new_data_dir, "val2017")


def maybe_download_and_extract():

    filenames = ["zips/train2017.zip", "zips/val2017.zip",
                 "annotations/annotations_trainval2017.zip"]

    for filename in filenames:
        url = data_url + filename
        print("Downloading " + url)
        download.maybe_download_and_extract(url=url, download_dir=data_dir)


def load_records(train=True):
    if train:
        cache_filename = "records_train.pkl"
    else:
        cache_filename = "records_val.pkl"

    cache_path = os.path.join(data_dir, cache_filename)
    records = cache(cache_path=cache_path,
                    fn=_load_records,
                    train=train)

    return records
