#!/usr/bin/python3

import subprocess
from subprocess import DEVNULL
from tqdm import tqdm
import argparse
import os
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

VALI_DIR='crossvalidation'
TRAIN_DIR='crossvalidation/training'
TEST_DIR='crossvalidation/test'



def crossvalidate(folds: int, run_id: str, gor: list[int], name_of_db: str):
    for model in tqdm(gor, desc='Models', leave=False):
        paths_of_summary = []
        for fold in tqdm(range(1, folds + 1), desc='Folds'):
            command = ["java", "-jar", "JARS/trainPredict.jar", 
                       "--model",  f"models/gor{model}_fold{fold}_{run_id}.mod",
                       "--seq", f"{TEST_DIR}/fasta_test_{fold}.fasta",
                       "--format", "txt",
                       "--db",  f"{TRAIN_DIR}/train_{fold}.db",
                       "--method", f"gor{model}",
                       "--modelT", f"models/gor{model}_fold{fold}_{run_id}.mod",
                       "--out", f"predictions/gor{model}_fold{fold}_{run_id}.prd"]
            subprocess.run(command, stdout=DEVNULL)

            command = ["java", "-jar", "JARS/evalGor.jar", 
                       "-p", f"predictions/gor{model}_fold{fold}_{run_id}.prd", 
                       "-r", f"{TEST_DIR}/test_{fold}.db",
                       "-s", f"validation/gor{model}_fold{fold}_{run_id}_SUMMARY.txt",
                       "-d", f"validation/gor{model}_fold{fold}_{run_id}_DETAILED.txt",
                       "-b"]
            subprocess.run(command, stdout=DEVNULL)

            paths_of_summary.append(f"validation/gor{model}_fold{fold}_{run_id}_SUMMARY_plot.scores")

        # concatenate all the summary files per model
        write_summary_to_file(paths_of_summary, name_of_db)



def crossvalidate_gor_v(folds: int, run_id: str, gor: list[int], name_of_db: str):
    for model in tqdm(gor, desc='Models', leave=False):
        paths_of_summary = []
        for fold in tqdm(range(1, folds + 1), desc='Folds'):
            command = ["java", "-jar", "JARS/trainPredict.jar", 
                       "--model",  f"models/gor5_{model}_fold{fold}_{run_id}.mod", 
                       "--maf", "train/CB513MultipleAlignments/",  # hard coded, we only have that 
                       "--format", "txt",
                       "--db",  f"{TRAIN_DIR}/train_{fold}.db",
                       "--method", f"gor{model}",
                       "--modelT", f"models/gor5_{model}_fold{fold}_{run_id}.mod",
                       "--out", f"predictions/gor5_{model}_fold{fold}_{run_id}.prd"]
            subprocess.run(command, stdout=DEVNULL)


            command = ["java", "-jar", "JARS/evalGor.jar", 
                       "-p", f"predictions/gor5_{model}_fold{fold}_{run_id}.prd", 
                       "-r", f"validation/cb513.db",
                       "-s", f"validation/gor5_{model}_fold{fold}_{run_id}_SUMMARY.txt",
                       "-d", f"validation/gor5_{model}_fold{fold}_{run_id}_DETAILED.txt",
                       "-b"]
            subprocess.run(command, stdout=DEVNULL)

            paths_of_summary.append(f"validation/gor5_{model}_fold{fold}_{run_id}_SUMMARY_plot.scores")

        # concatenate all the summary files per model
        write_summary_to_file(paths_of_summary, name_of_db)


def write_summary_to_file(paths: list[str], name_of_db: str):

    summary_out_path = paths[0].split(".")[0].replace("fold1_", "") + "_ALL.scores"
    os.system(f"touch {summary_out_path}")
    with open(summary_out_path, 'w') as merged_file:
        # crate file (summary_out_path)
        # Iterate over each file path
        for file_path in paths:
            try:
                # Open each file and read its content
                with open(file_path, 'r') as file:
                    content = file.read()
                    # Write the content to the merged file
                    merged_file.write(content)
                    # Add a newline after each file's content
                    merged_file.write('\n')
            except FileNotFoundError:
                print(f"File {file_path} not found.")

    plot_summary_per_fold(summary_out_path, name_of_db)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crossvalidat on dataset")
    parser.add_argument('--gor', type=int, nargs="+", required=False, help="Gor type to crossvalidate on")
    parser.add_argument('--id', type=str, required=True, help="Run id for the crossvalidation")
    parser.add_argument('--ali', action='store_true', required=False, help="Run gor 5 for all gor given in the list")
    parser.add_argument('--folds', type=int, required=True, default=None, help="Number of folds for crossvalidation")
    parser.add_argument('--db', type=str, required=True, default=None, help="File to split into folds")
    args = parser.parse_args()
    run_id = args.id
    folds = args.folds
    gor = args.gor
    db = args.db
    name_of_db = db.split(".")[-2].split("/")[-1]

    create_folds(folds, db)  # create folds

    crossvalidate(folds, run_id, gor, name_of_db)  # gor I III IV

    if args.ali: 
        crossvalidate_gor_v(folds, run_id, gor, name_of_db)  # for gor V
    
