pkgname = "llama-cpp"
pkgver = "0.0.9775"
pkgrel = 0
build_style = "cmake"
make_check_args = [
    "-E",
    "(test-jinja-py|test-download-model|test-thread-safety|test-arg-parser|test-state-restore-fragmented|test-recurrent-state-rollback|test-save-load-state|test-eval-callback-download-model|test-eval-callback)",
]
cmake_dir = f"llama.cpp-b{pkgver.split('.')[2]}"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    # "libgcc-chimera",
    "linux-headers",
    "ninja",
    "nodejs",
    "openssl3-devel",
    "pkgconf",
]
checkdepends = ["bash"]
pkgdesc = "LLM inference in C/C++"
license = "MIT"
url = "https://github.com/ggml-org/llama.cpp"
source = [
    f"{url}/archive/b{pkgver.split('.')[2]}.tar.gz",
    f"{url}/releases/download/b{pkgver.split('.')[2]}/llama-b{pkgver.split('.')[2]}-ui.tar.gz",
]
sha256 = [
    "e4826441645ece8a2280087d0a2c14074c234943acf30f623f1da9356490b960",
    "7a9f384da5b4b4dc65f0744ce6c9299ac10ad6c2bb12620d8bfe88abbada031a",
]


def post_extract(self):
    # Build UI
    # with self.pushd("tools/ui"):
    #     self.do("npm", "ci", allow_network=True)
    #     # HACK: Node can't find the file by default
    #     self.do(
    #         "cp",
    #         "node_modules/lightningcss-linux-x64-musl/lightningcss.linux-x64-musl.node",
    #         "node_modules/lightningcss/lightningcss.linux-x64-musl.node",
    #     )
    #     self.do("npm", "run", "build")

    # Copy precompiled UI
    with self.pushd(f"llama.cpp-b{pkgver.split('.')[2]}/tools/ui"):
        self.do("cp", "-r", f"../../../llama-b{pkgver.split('.')[2]}", "dist")


def post_install(self):
    self.install_license(f"llama.cpp-b{pkgver.split('.')[2]}/LICENSE")
