# JobsWebScapping

A Python project to automate the extraction and transformation of remote job postings from multiple job boards. The project scrapes job listings, processes the data, and outputs structured JSON files for further analysis or integration.

## Features
- Scrapes job postings from multiple sources (currently: WeWorkRemotely, SkipTheDrive)
- Extracts job details such as title, company, location, salary, and posting date
- Organizes raw HTML and processed data by date
- Outputs results as JSON files for easy consumption

## Project Structure
```
JobsWebScapping/
  app.py                # Main script to run extraction and transformation
  endpoints.py          # Job board endpoints and configuration
  methods/
    extract.py          # Extraction logic (web scraping)
    transform.py        # Data transformation and parsing
    utils.py            # Utility functions for file and directory handling
  lake/                 # Raw HTML data (auto-generated, ignored by git)
  output/               # Processed JSON data (auto-generated, ignored by git)
  README.MD             # Project documentation
```

## Installation
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd JobsWebScapping
   ```
2. **Install dependencies:**
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage
1. Edit the `queries` list in `app.py` to specify your job search terms.
2. Uncomment the extraction loop in `app.py`:
   ```python
   for query in queries:
       extract.extractData(query=query)
   ```
3. Run the main script:
   ```bash
   python app.py
   ```
4. Scraped HTML files will be saved in the `lake/` directory, and processed job data will be output as JSON in the `output/` directory, organized by date and source.

## Adding New Job Boards
- Add new entries to the `urls` dictionary in `endpoints.py`.
- Implement parsing logic in `methods/transform.py` for the new source.

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements or new features.
