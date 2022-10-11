load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "cisei_scrapper",
    srcs = [
        "cisei_database.py",
        "cisei_scrapper.py",
        "names.py",
    ],
    data = [
        "//cognomix:names",
        "//database:queries",
    ],
    deps = [
        "//third_party:beautifulsoup4",
        "//third_party:psycopg2",
        "//third_party:pydantic",
        "//third_party:requests",
        "//third_party:tenacity",
        "//third_party:urllib3",
    ],
)
