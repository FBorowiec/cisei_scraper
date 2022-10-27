# *CISEI website scraper*

Repository for scraping the CISEI website.

Special thanks to [Michele Falcone (Michał Sokołowski)](https://github.com/Sokolowski-Michal-Piotr)
for his highly appreciated help setting up the reverse proxy and Grafana dashboards.

## Notes

* As the CISEI websites allow only for querying when at least a family name is know,
    the website [cognomix.it](cognomix.it) (as of July 2021) was scraped in order
    to obtain a list of supposedly all Italian surnames (42065 results).
* To the aforementioned list was added a list of Jewish names (1602 results).
* Improperly formatted dates are nullified (ex.: Bernard Federico - trip date: 00-05-1851)
* There are duplicates due to the fact that some persons made the trip,
    came back and went again (f.e.: COMI PIO).
* There are spelling mistakes in the registers (f.e.: Guiseppe instead of Giuseppe.

## Visualization

The database is accessible at the following link:

[fborowiec.com](https://www.fborowiec.com)

The site is using a Grafana dashboard for visualization of different statistics:

* Years of departure heatmap
* Age of departure barchart
* Gender piechart
* number of emigrants from a given city
* top 10 provinces with most emigrants
* top 10 regions with most emigrants
* top 10 destinations

# TODO

## User Permission

The database user should only be granted SELECT permissions on the specified database & tables you want to query.
Grafana does not validate that queries are safe so queries can contain any SQL statement.
For example, statements like DELETE FROM user; and DROP TABLE user; would be executed.
To protect against this we Highly recommmend you create a specific PostgreSQL user with restricted permissions.
