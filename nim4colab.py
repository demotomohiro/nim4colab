from IPython.core.magic import register_cell_magic, register_line_magic, register_line_cell_magic
from IPython.utils import io
import pathlib, shutil, subprocess, urllib.request, json, os, sys

def download(url, path):
  with urllib.request.urlopen(url) as response:
    with open(path, 'wb') as outfile:
      shutil.copyfileobj(response, outfile)

def downloadNim(archivePath, label):
  f = urllib.request.urlopen("https://api.github.com/repos/nim-lang/nightlies/releases")
  tree = json.loads(f.read().decode('utf-8'))
  for i in tree:
    if not label in i['tag_name']:
      continue
    for j in i['assets']:
      if j['name'].endswith("linux_x64.tar.xz"):
        url = j['browser_download_url']
        download(url, archivePath)
        return

def getNimDir(branch, root):
  assert(branch == "devel" or branch == "stable")
  return root / f"nim-{branch}" / "nim"

def nimInstallIfNotExist(branch, root):
  nimDir = getNimDir(branch, root)
  nimExe = nimDir / "bin" / "nim"
  if not nimExe.is_file():
    print(f"Installing Nim {branch}")
    if branch == "devel":
      label = "devel"
    else:
      # Get latest stable version number
      f = urllib.request.urlopen("https://api.github.com/repos/nim-lang/Nim/tags")
      tree = json.loads(f.read().decode('utf-8'))
      # latestStableVer is a text like 1.4.2
      latestStableVer = tree[0]['name'][1:]
      x = latestStableVer.find(".")
      major = latestStableVer[:x]
      y = latestStableVer.find(".", x + 1)
      minor = latestStableVer[x + 1: y]
      label = f"version-{major}-{minor}"
    archivePath = root / f"nim-{branch}.tar.xz"
    downloadNim(archivePath, label)
    nimParDir = nimDir.parent
    pathlib.Path.mkdir(nimParDir)
    shutil.unpack_archive(str(archivePath), nimParDir)
    for i in nimParDir.glob("nim*"):
      i.rename(nimParDir / "nim")
      break
    print("done")

def nimBin(exe, param, branch, root = pathlib.Path.home()):
  nimInstallIfNotExist(branch, root)
  nimDir = getNimDir(branch, root)
  nimExe =  nimDir / "bin" / exe
  newEnv = os.environ.copy()
  newEnv['PATH'] = str(nimDir / "bin") + ':' + newEnv['PATH']
  ret = subprocess.run(
      str(nimExe) + ' ' + param,
      shell = True,
      env = newEnv,
      stdout = subprocess.PIPE,
      stderr = subprocess.STDOUT,
      universal_newlines = True
  )
  print(ret.stdout)

def nimRun(param, code, branch):
  nimCode = pathlib.Path.home() / "code.nims"
  nimCode.write_text(code)
  nimBin("nim", param + " " + str(nimCode), branch)

@register_line_cell_magic
def nim(line, cell = None):
  if cell is None:
    nimBin("nim", line, "stable")
  else:
    nimRun(line, cell, "stable")

@register_line_cell_magic
def nimdev(line, cell = None):
  if cell is None:
    nimBin("nim", line, "devel")
  else:
    nimRun(line, cell, "devel")

@register_cell_magic
def nimc(line, cell):
  nimRun("c -r --verbosity:0" + line, cell, "stable")

@register_cell_magic
def nims(line, cell):
  nimRun("e -r --verbosity:0 " + line, cell, "stable")

@register_cell_magic
def nimdevc(line, cell):
  nimRun("c -r " + line, cell, "devel")

@register_line_magic
def nimble(line):
  nimBin("nimble", line, "stable")

@register_line_magic
def nimbledev(line):
  nimBin("nimble", line, "devel")

def load_ipython_extension(ipython):
  pass
