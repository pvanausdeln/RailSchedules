import os
import sys
import json
import copy
import requests
import datetime
import glob
import csv
import string
from google.cloud import storage

def main():
    storage_client = storage.Client().from_service_account_json("C:\\Users\\pvanausdeln\\absolute-alloy-213205-09f72e18aefe.json")

    buckets = list(storage_client.list_buckets())
    bucket = storage_client.get_bucket("dev-platform-data")
    blob = bucket.get_blob("rail_schedules/Norfolk/")
    try:
        blob.download_to_filename("hi.csv")
        blob.upload_from_filename("C:\\Users\\pvanausdeln\\OneDrive - Blume Global\\UiPath\\RailSchedules\\RailSchedules\\Norfolk_Intermodal_Schedules.csv")
    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()
