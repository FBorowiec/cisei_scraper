# CISEI data visualization

This is a Grafana dashboard used for visualization of the emigration data available at
[ciseionline.it](https://ciseionline.it).

As the aforementioned website is not actively maintained (last update dates back to 2014)
trying to obtain the database was not possible. I therefore downloaded a list of (supposedly)
all Italian surnames from the [cognomix.it](https://cognomix.it) website and fed it one by one
to the Cisei website (which accepts a surname and gives back a paginated list of results).

The resulting scraping of the data is based of approximately 43k Italian surnames.

The Cisei website was checked for a `robots.txt` and the scraping was performed according to
the allowed form from the websites creators.

```http
User-agent: *
Disallow: /_consolledownload/
Disallow: /_2010KMS2656/
Disallow: /_consolledownload/
```

## Notes

* As the CISEI websites allow only for querying when at least a family name is know,
    the website [cognomix.it](cognomix.it) (as of July 2021) was scraped in order
    to obtain a list of supposedly all Italian surnames (42065 results).
* To the aforementioned list was added a list of Jewish surnames (1602 results).
* Improperly formatted dates are nullified (ex.: Bernard Federico - trip date: 00-05-1851)
* There are duplicates due to the fact that some persons made the trip,
    came back and went again (f.e.: COMI PIO).
* There are spelling mistakes in the registers (f.e.: Guiseppe instead of Giuseppe) leading to a lot of data
    probably missing in this database (wrt. the original Cisei one) as the misspelled surnames won't be present.
* An aggregator of results is available under: [top statistics](https://fborowiec.com/d/KeMYNuIVk/top-statistics).
* Around 100 keys are showing in the details page - many of them mapping the same keys to values,
    therefore leaving the possibility to further reprocess the data.
