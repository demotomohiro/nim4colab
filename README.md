# Nim4Colab
Nim4Colab is a IPython extension to integrate Nim language on Google Colaboratory.

## How to use
Copy and paste following code to a cell on Google Colaboratory and run.
This code download, install and load Nim4Colab extension.

```
!pip install git+https://github.com/nehtr/nim4colab.git
%load_ext nim4colab
```

Then, you can use line and cell magics in Nim4Colab extenson.

```
#Run Nim code with nimc cell magic.
%%nims
echo "Nim version is ", NimVersion
```

Nim4Colab downloads and installs latest Nim from [Nim nightlies](https://github.com/nim-lang/nightlies) when first time one of Nim4Colab's magic is called.
User code is saved to ``~/code.nims`` file before ``nim`` command is called.

## Cell magics

### %%nimc [options]
Compile and run Nim code.
Equivalent to calling ``nim c --verbosity:0 [options] ~/code.nim``

### %%nims [options]
Run the code as a Nim script (without compiling it).  
ATTENTION: not all the Nim libraries are supported in Nimscript, though most of them are.
Equivalent to calling ``nim c --verbosity:0 [options] ~/code.nim``

### %%nim command [options]
Equivalent to calling ``nim command [options] ~/code.nim``

### %%nimdevc [options]
Same to ``%%nimc`` but uses devel branch Nim.

### %%nimdev command [options]
Same to ``%%nim`` but uses devel branch Nim.

## Line magics

### %nim [parameters]
Execute ``nim [parameters]``.

### %nimdev [parameters]
Execute ``nim [parameters]`` using devel branch Nim.

### %nimble [parameters]
Execute ``nimble [parameters]``.

Refer [Nim Compiler User Guide](https://nim-lang.org/docs/nimc.html).

<!-- ## Samples
- [Basic](https://colab.research.google.com/drive/1aNmsJmgnxz-4yr1hT0ZdHh9-XQ_8dcRk)
- [Make PNG image](https://colab.research.google.com/drive/15w2dtk9QE8QDTsqMeRnWCzR7f2kSseoq)
- [Make animation PNG using EGL & OpenGL](https://colab.research.google.com/drive/1J0B0qVvovrJZJI1OU75jIMUjWnymi_6G) -->
