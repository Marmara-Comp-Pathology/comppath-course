"""Download the PatchCamelyon (Kaggle version) data used in lesson 1, for running on your own computer.

    pip install kagglehub==1.0.3
    python data/download_lesson01.py

You need a Kaggle account, an API token (kaggle.com/settings → Create New Token) and to have accepted
the competition rules at https://www.kaggle.com/competitions/histopathologic-cancer-detection/rules.
About 7 GB. The lesson notebook finds the data through kagglehub's cache, so you only download it once.
"""
import kagglehub

COMPETITION = "histopathologic-cancer-detection"

if __name__ == "__main__":
    path = kagglehub.competition_download(COMPETITION)
    print("Downloaded to:", path)
