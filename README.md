# xv6-tester

## Prerequisites

Make sure you have installed all of the following prerequisites on your development machine:

- python 3.x
- virtualenv
- qemu with riscv emulation

In order to test the qemu tools, you can run

```shell
$ riscv64-unknown-elf-gcc --version
riscv64-unknown-elf-gcc (GCC) 10.1.0
...

$ qemu-system-riscv64 --version
QEMU emulator version 5.1.0

# Check if xv6 is running correctly:

$ git clone git://g.csail.mit.edu/xv6-labs-2020
$ cd xv6-labs-2020
$ make qemu
# ... lots of output ...
init: starting sh
$
```

## Installation

1. Clone the repository:

   ```shell script
   $ clone https://github.com/omria123/xv6-tester.git
   ...
   $ cd xv6-tester 
   ```
2. Run the install script:

    ```shell script
    $ ./scripts/install.sh
    ...
    $ source .env/bin/activate
    [xv6-tester] $ # you're good to go!

## Usage

The student must submit his repository's URL. Then, in order to check his exercise run the following command:

```shell
$ pytest --repo-url=<REPO_URL> --exercise=<EXERCISE_NAME>
```