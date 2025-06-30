from datetime import datetime
from endpoints import urls
from methods.utils import Utils
from methods.extract import Extract
from methods.transform import Transform
import json

output = "output"
path  = "lake"
year  = datetime.now().year
month = datetime.now().month
day   = datetime.now().day

utils = Utils()

utils.createDirectory(f"{path}")
utils.createDirectory(f"{path}/{year}")
utils.createDirectory(f"{path}/{year}/{month}")
utils.createDirectory(f"{path}/{year}/{month}/{day}")

extract = Extract(
    urls = urls,
    date = {"year": year,
            "month": month,
            "day": day},
    utils = utils
)

queries = [
    "python Junior Developer",
    "python Developer",
    "Junior DevOps Engeneer",
    "Entry Level DevOps Engeneer",
    "Junior SRE",
    "Junior Cloud Engeneer"
]

# for query in queries:
#      extract.extractData(query=query)

transform = Transform()

directories = utils.listDir(f"{path}/{year}/{month}/{day}")

for dir in directories:
    files = utils.listDir(f"{path}/{year}/{month}/{day}/{dir}")
    jobs = []
    for file_name in files:
        html_text = utils.loadFile((f"{path}/{year}/{month}/{day}/{dir}/{file_name}"))
        soup = transform.soupHtml(html_text)
        print(transform.getJobs(dir, soup))

    utils.createDirectory(f"{output}")
    utils.createDirectory(f"{output}/{year}")
    utils.createDirectory(f"{output}/{year}/{month}")
    utils.createDirectory(f"{output}/{year}/{month}/{day}")
    
    json_data = json.dumps(jobs, indent=4)

    with open(f"{output}/{year}/{month}/{day}/{dir}.json", 'w', encoding='utf-8') as json_file:
        json.dump(jobs, json_file, ensure_ascii=False, indent=4)    