load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "cognomix_scrapper",
    srcs = glob(["*.py"]),
    deps = [
        "//third_party:tenacity",
    ],
)

filegroup(
    name = "names",
    srcs = [
        "jewish_italian_names.csv",
        "names.csv",
    ],
)
