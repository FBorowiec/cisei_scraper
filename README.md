# *CISEI website scraper*

Repository for scraping the CISEI website.

## Notes

* As the CISEI websites allow only for querying when at least a family name is know,
    the website [cognomix.it](cognomix.it) (as of July 2021) was scraped in order
    to obtain a list of supposedly all Italian surnames (42065 results).
* To the aforementioned list was added a list of Jewish names (1602 results).
* Improperly formatted dates are nullified (ex.: Bernard Federico - trip date: 00-05-1851)
* There are duplicates due to the fact that some persons made the trip,
    came back and went again (f.e.: COMI PIO).
* There are spelling mistakes in the registers (f.e.: Guiseppe instead of Giuseppe.
