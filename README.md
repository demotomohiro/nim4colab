# Nim4Colab
Nim4Colab is a IPython extension to use Nim language on Google Colaboratory.

## How to use
Copy and paste following code to a cell on Google Colaboratory and run.
This code download, install and load Nim4Colab extension.

```
!pip install git+https://github.com/demotomohiro/nim4colab.git
%load_ext nim4colab
```

Then, you can use line and cell magics in Nim4Colab extenson.

```
#Run Nim code with nimc cell magic.
%%nimc
echo "Nim version is ", NimVersion
```

Nim4Colab downloads and installs latest Nim from [Nim nightlies](https://github.com/nim-lang/nightlies) when first time one of Nim4Colab's magic is called.
User code is saved to ``~/code.nim`` file before ``nim`` command is called.

## Examples

Print Nim version:
```
%nim -v
```
Example output:
```
Nim Compiler Version 2.0.1 [Linux: amd64]
Compiled at 2023-12-09
Copyright (c) 2006-2023 by Andreas Rumpf
```

Print Nim devel version:
```
%nimdev -v
```
Example output:
```
Nim Compiler Version 2.1.1 [Linux: amd64]
Compiled at 2023-12-08
Copyright (c) 2006-2023 by Andreas Rumpf
```

Run Nim code and print Nim version:
```
%%nimc
echo NimVersion
```
Example output:
```
Hint: used config file '/root/nim-stable/nim/config/nim.cfg' [Conf]
Hint: used config file '/root/nim-stable/nim/config/config.nims' [Conf]
......................................................................
CC: code.nim
Hint:  [Link]
Hint: mm: orc; threads: on; opt: none (DEBUG BUILD, `-d:release` generates faster code)
27611 lines; 0.612s; 30.391MiB peakmem; proj: /root/code.nim; out: /root/code [SuccessX]
Hint: /root/code [Exec]
2.0.1
```

Run Nim code and print Nim version with devel branch Nim:
```
%%nimdevc
echo NimVersion
```
Example output:
```
Hint: used config file '/root/nim-devel/nim/config/nim.cfg' [Conf]
Hint: used config file '/root/nim-devel/nim/config/config.nims' [Conf]
Hint: mm: orc; threads: on; opt: none (DEBUG BUILD, `-d:release` generates faster code)
10215 lines; 0.030s; 10.449MiB peakmem; proj: /root/code.nim; out: /root/code [SuccessX]
Hint: /root/code [Exec]
2.1.1
```

Run code as Nimscript file:
(Nimscript has limitations: https://nim-lang.org/docs/nims.html)
```
%%nim e
when nimvm:
  echo "Running on NimVM"
else:
  echo "Not running on NimVM"
```
Example output:
```
Hint: used config file '/root/nim-stable/nim/config/nim.cfg' [Conf]
Hint: used config file '/root/nim-stable/nim/config/config.nims' [Conf]
Running on NimVM
Hint: used config file '/root/code.nim' [Conf]
```

## Cell magics

### %%nimc [options]
Compile and run Nim code.
Equivalent to calling ``nim c -r [options] ~/code.nim``

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

## Samples
- [Basic](https://colab.research.google.com/drive/1aNmsJmgnxz-4yr1hT0ZdHh9-XQ_8dcRk)
- [Make PNG image](https://colab.research.google.com/drive/15w2dtk9QE8QDTsqMeRnWCzR7f2kSseoq)
- [Make animation PNG using EGL & OpenGL](https://colab.research.google.com/drive/1J0B0qVvovrJZJI1OU75jIMUjWnymi_6G)
