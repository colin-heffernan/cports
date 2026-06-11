pkgname = "llama-swap"
pkgver = "0.0.229"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go", "libgcc-chimera"]
makedepends = ["nodejs"]
pkgdesc = "Model swapping for any local OpenAI/Anthropic compatible server"
license = "MIT"
url = "https://github.com/mostlygeek/llama-swap"
source = f"{url}/archive/v{pkgver.split('.')[2]}.tar.gz"
sha256 = "42b144fcba9ebabb9b520e0d75ff01c25005e41bc9b0a027bbad2de4bf601f84"


def post_prepare(self):
    with self.pushd("ui-svelte"):
        self.do("npm", "ci", allow_network=True)
        self.do(
            "cp",
            "node_modules/lightningcss-linux-x64-musl/lightningcss.linux-x64-musl.node",
            "node_modules/lightningcss/lightningcss.linux-x64-musl.node",
        )
        self.do("npm", "run", "build")
    self.do("touch", "internal/server/ui_dist/placeholder.txt")


def check(self):
    return  # FIXME: Disable tests more granularly


def install(self):
    self.install_license("LICENSE.md")
