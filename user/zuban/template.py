pkgname = "zuban"
pkgver = "0.10.0"
pkgrel = 0
build_style = "cargo"
make_dir = f"zuban-{pkgver}"
hostmakedepends = ["cargo-auditable", "git"]
makedepends = ["rust-std"]
pkgdesc = "Python Type Checker / Language Server"
license = "AGPL-3.0-only"
url = "https://zubanls.com"
_typeshed_commit = "c981c922a32f74c0f4717b038d4dbb1ac11170ad"
_mypy_commit = "8236c93d899fa5225eb23644db802cf1e09196a7"
_django_stubs_commit = "c7b59a09461784a6ec07704fcfc67391f7e8000d"
source = [
    f"https://github.com/zubanls/zuban/archive/v{pkgver}.tar.gz",
    f"https://github.com/python/typeshed/archive/{_typeshed_commit}.tar.gz",
    f"https://github.com/davidhalter/mypy/archive/{_mypy_commit}.tar.gz",
    f"https://github.com/typeddjango/django-stubs/archive/{_django_stubs_commit}.tar.gz",
]
sha256 = [
    "ef18bed5412da00667862751e16b4cf66039ae39e3618ef891f58d089fabe5c0",
    "c1614e49b4d8bda4d5dc50417529516c4fb613c677d5b892c7abfdd6671ff84a",
    "b72ca9451aeced6cfa4897af69902b953e1c88503ad56b6cdeb382f831ee300f",
    "34829bbdb0d233ba03454afd4a89ae4f7b5a06151ae8ff67c3a7ea02c9ea6a95",
]


def post_extract(self):
    self.rm(f"zuban-{pkgver}/third_party/typeshed", recursive=True)
    self.rm(
        f"zuban-{pkgver}/crates/zuban_python/tests/mypylike/mypy",
        recursive=True,
    )
    self.rm(f"zuban-{pkgver}/third_party/django-stubs", recursive=True)
    self.mv(
        f"typeshed-{_typeshed_commit}",
        f"zuban-{pkgver}/third_party/typeshed",
    )
    self.mv(
        f"mypy-{_mypy_commit}",
        f"zuban-{pkgver}/crates/zuban_python/tests/mypylike/mypy",
    )
    self.mv(
        f"django-stubs-{_django_stubs_commit}",
        f"zuban-{pkgver}/third_party/django-stubs",
    )


def pre_build(self):
    # This can probably be done better.
    self.cp(f"zuban-{pkgver}/vendor", "vendor", recursive=True)


def post_install(self):
    self.install_license("LICENSE")
