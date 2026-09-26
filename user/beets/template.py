pkgname = "beets"
pkgver = "2.14.1"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # pytest fixture client not found
    "--ignore=test/plugins/test_aura.py",
    # requests_oauthlib
    "--ignore=test/plugins/test_beatport.py",
    # discogs_client
    "--ignore=test/plugins/test_discogs.py",
    # pylast
    "--ignore=test/plugins/test_lastgenre.py",
    # mpd
    "--ignore=test/plugins/test_mpdstats.py",
    # flakes
    "--ignore=test/test_importer.py",
    "--ignore=test/test_ui.py",
]
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
depends = [
    "python-confuse",
    "python-jellyfish",
    "python-lap",
    "python-mediafile",
    "python-munkres",
    "python-packaging",
    "python-platformdirs",
    "python-pyyaml",
    "python-requests",
    "python-requests-ratelimiter",
    "python-typing_extensions",
    "python-unidecode",
]
checkdepends = [
    "python-flask",
    "python-mock",
    "python-pytest-xdist",
    "python-pyxdg",
    "python-responses",
    *depends,
]
pkgdesc = "CLI media library management"
license = "MIT"
url = "https://beets.io"
source = f"$(PYPI_SITE)/b/beets/beets-{pkgver}.tar.gz"
sha256 = "b25dc7bf8ed093d8b6e043e88013736902c1082c958b81a598af5db5275539a5"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/beet.1")
    self.install_man("man/beetsconfig.5")
