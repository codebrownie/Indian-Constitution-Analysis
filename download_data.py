"""
Subprocess calls that will download latest constitution data from the website. 
"""
import subprocess
import os
try:
    os.mkdir('./dataset/')
except:
    print('Dataset folder exists.')

print('Downloading files from constitution website.')
subprocess.call(['curl','-o','./dataset/coi_preface.pdf','https://www.india.gov.in/sites/upload_files/npi/files/coi_preface.pdf'])
subprocess.call(['curl','-o','./dataset/coi_contents.pdf','https://www.india.gov.in/sites/upload_files/npi/files/coi_contents.pdf'])
subprocess.call(['curl','-o','./dataset/coi_part_full.pdf','https://www.india.gov.in/sites/upload_files/npi/files/coi_part_full.pdf'])
subprocess.call(['curl','-o','./dataset/coi-eng-schedules_1-12.pdf','https://www.india.gov.in/sites/upload_files/npi/files/coi-eng-schedules_1-12.pdf'])
subprocess.call(['curl','-o','./dataset/coi_appendix.pdf','https://www.india.gov.in/sites/upload_files/npi/files/coi_appendix.pdf'])
subprocess.call(['curl','-o','./dataset/coi-eng-index.pdf','https://www.india.gov.in/sites/upload_files/npi/files/coi-eng-index.pdf'])
