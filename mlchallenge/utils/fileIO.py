#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
fileIO.py
Description:

Author: PhatLuu
Contact: tpluu2207@gmail.com
Created on: 2020/12/10
"""

#%%
# ================================IMPORT PACKAGES====================================

# Standard Packages
import functools
import os
import re
import shutil
from pathlib import Path

# FileIO Packages
import json
import yaml

# Data Analytics
import numpy as np

# Web pages and URL Related
import requests

# Utilities
import time
from tqdm import tqdm

# Custom Packages
from tf_handpose.utils.decorator import verbose
from tf_handpose.utils.logging_config import logger as logging


script_dir = os.path.dirname(os.path.abspath(Path(__file__)))
workspace_dir = os.path.dirname(script_dir)

# =====================================MAIN==========================================
def makedir(inputDir, remove=False):
    """Summary:

        Make directory

    Inputs:

        inputDir (str): fullpath to directory to be created

        remove (bool): option to remove current existing folder

    """
    if remove is True and os.path.exists(inputDir):
        logging.warning("Remove existing folder")
        shutil.rmtree(inputDir)

    if not os.path.exists(inputDir):
        logging.info("Making directory: {}".format(os.path.abspath(inputDir)))
        os.makedirs(inputDir)
    else:
        logging.info(
            "mkdir: Directory already exist: {}".format(os.path.abspath(inputDir))
        )


def get_valid_filename(s):
    s = s.strip().replace(" ", "_")
    return re.sub(r"(?u)[^-\w.]", "", s)


def list_file_with_extension(root_dir=os.getcwd(), ext=".all"):
    """
    Summary:

        Get all files (fullpath) from root_dir with extension

    Inputs:

        root_dir (str, optional): dir path. Defaults to os.getcwd().

        ext (str, optional): file extension. e.g., '.csv','.py'. Defaults to ".all".

    Returns:

        fullfile_list: list of file paths
    """
    fullfile_list = []
    for path, subdirs, files in os.walk(root_dir):
        for filename in files:
            name, this_ext = os.path.splitext(filename)
            if this_ext == ext or ext == ".all":
                fullfile_list.append(os.path.join(path, filename))
    return fullfile_list


def unzip_file(filename, **kwargs):
    """
    Summary:

        unzip file

    Options:

        output -- str. Directory path. Default. Same as input filename

        remove -- Boolean. Option to delete zip file. Default. True

    """
    zip_dir, zip_basename = os.path.dirname(filename), os.path.basename(filename)
    default_output_dir = os.path.join(zip_dir, os.path.splitext(zip_basename)[0])
    output_dir = kwargs.get("output_dir", default_output_dir)
    # Standard Packages
    import zipfile

    with zipfile.ZipFile(filename, "r") as fid:
        logging.info(f"Extracing: {filename}")
        fid.extractall(output_dir)


def download_url(url, **kwargs):
    default_filename = get_valid_filename(url.split("/")[-1])
    default_output_filename = os.path.join(workspace_dir, default_filename)
    output_filepath = kwargs.get("output_filepath", default_output_filename)
    logging.info(output_filepath)

    if os.path.exists(output_filepath):
        logging.info(f"File exists: {output_filepath}. Skip downloading")
        return -1
    logging.info("Downloading to: {}".format(output_filepath))
    makedir(os.path.dirname(output_filepath))
    r = requests.get(url, stream=True, timeout=None)
    # Total size in bytes.
    total_size = int(r.headers.get("content-length", 0))
    block_size = 1024  # 1 Kibibyte
    with open(output_filepath, "wb") as fid, tqdm(
        total=total_size, unit="iB", unit_scale=True
    ) as tqdm_bar:
        for data in r.iter_content(block_size):
            tqdm_bar.update(len(data))
            fid.write(data)


def glob_files(input_dir, query_list=[], **kwargs):
    """Summary:
    --------
    Get list of files in a directory

    Inputs:
    -------
        ckpts_dir (str): directory path
        model_name (str): model name

    Returns:
    --------
        list: list of .ckpts files
    """
    query_list = [query_list] if query_list is str else query_list
    fullfile_list = []
    for path, subdirs, files in os.walk(input_dir):
        for filename in files:
            if len(query_list):
                if all(key in filename for key in query_list):
                    fullfile_list.append(os.path.join(path, filename))
            else:
                fullfile_list.append(os.path.join(path, filename))
    return fullfile_list


@verbose
def save_npz(input_dict, npz_filepath):
    output_dir = os.path.dirname(npz_filepath)
    makedir(output_dir)
    np.savez_compressed(npz_filepath, **input_dict)


@verbose
def load_json(json_filepath):
    output = None
    if not os.path.isfile(json_filepath):
        logging.warning(f"{json_filepath} is not a file")
        return output
    with open(json_filepath, "r") as fid:
        output = json.load(fid)
    return output


@verbose
def save_json(json_data, json_filepath):
    with open(json_filepath, "w") as fid:
        json.dump(json_data, fid)


@verbose
def save_yaml(input_dict, yaml_filepath):
    """Summary:
    --------
    Save input dictionary to yaml file

    Inputs:
    -------
        input_dict (dict): Input dict
        output_filepath (str): output yaml file path
    """
    with open(yaml_filepath, "w") as fid:
        yaml.dump(input_dict, fid)


@verbose
def load_yaml(yaml_filepath):
    """Summary:
    --------
    Load yaml file to python dict

    Inputs:
    -------
        yaml_filepath (str): yaml file path

    Returns:
    --------
        dict: return from yaml file
    """
    with open(yaml_filepath, "r") as fid:
        try:
            output = yaml.safe_load(fid)
            return output
        except yaml.YAMLError as exc:
            logging.error(exc)


# =====================================DEBUG=========================================

if __name__ == "__main__":
    main()
