import subprocess
import os

os.environ['KAGGLE_CONFIG_DIR'] = '/Users/dk2251n/Desktop/Spring2026/JupyterNoteBookBullShit/rds_final_project/kaggle_jigsaw'
os.chdir('/Users/dk2251n/Desktop/Spring2026/JupyterNoteBookBullShit/rds_final_project/kaggle_jigsaw/input')

subprocess.run(['/Users/dk2251n/Desktop/Spring2026/JupyterNoteBookBullShit/venv/bin/kaggle', 'competitions', 'download', '-c', 'jigsaw-unintended-bias-in-toxicity-classification'], check=True)
subprocess.run(['/Users/dk2251n/Desktop/Spring2026/JupyterNoteBookBullShit/venv/bin/kaggle', 'competitions', 'download', '-c', 'jigsaw-toxic-comment-classification-challenge'], check=True)

subprocess.run(['unzip', '-q', '-n', 'jigsaw-unintended-bias-in-toxicity-classification.zip'])
subprocess.run(['unzip', '-q', '-n', 'jigsaw-toxic-comment-classification-challenge.zip'])
