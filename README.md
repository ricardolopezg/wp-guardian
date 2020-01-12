# WP Guardian
Wordpress vulnerability scanner and reporting tool. 

## Installation
API keys required

https://www.wpvulndb.com

https://www.vulnersdb.com


Clone github repo

    git clone https://github.com/ricardolopezg/wp-guardian


Install dependencies

    pip install -r requirements.txt

Update config.py file with your api keys

Usage

    python3 wp_guardian.py http(s)://www.example.com/

Markdown report will be generated and saves to the reports folder, along with with a json formatted report.

Use your favorite Markdown viewer to view the .md file. You can also use google chrome extension Markdownviewer.

## Future Features
- [ ] plugin fuzzing
- [ ] theme fuzzing
- [ ] md5sum version fingerprinting 
