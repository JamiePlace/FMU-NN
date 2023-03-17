import os


repo_path = 'C:/Users/jamie/projects/Reference-FMUs' 
fmu_path = '/FMUs'

def bouncing_ball():
    file_path = '/1.0/cs/BouncingBall.fmu'
    fmu_file_path = repo_path + fmu_path + file_path

    return fmu_file_path
