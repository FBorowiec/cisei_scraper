load("@rules_python//python:defs.bzl", "py_binary")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
load("@io_bazel_rules_docker//container:container.bzl", "container_image", "container_push")

package(default_visibility = ["//visibility:public"])

container_image(
    name = "ubuntu_python3",
    base = "@ubuntu_python3//image",
)

py_binary(
    name = "cisei_runner",
    srcs = ["cisei_runner.py"],
    main = "cisei_runner.py",
    deps = ["//cisei:cisei_scrapper"],
)

py3_image(
    name = "cisei_image",
    srcs = ["cisei_runner.py"],
    base = "ubuntu_python3",
    main = "cisei_runner.py",
    deps = ["//cisei:cisei_scrapper"],
)

container_push(
    name = "push_cisei_image",
    format = "Docker",
    image = "cisei_image",
    registry = "index.docker.io",
    repository = "framaxwlad/cisei",
    tag = "$(image_tag)",
    tags = ["manual"],
)
