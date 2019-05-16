#!/usr/bin/env python
# init_py_dont_write_bytecode

#init_boilerplate

from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from fabric.contrib.project import *


# import multiprocessing
# total_cpu_threads = multiprocessing.cpu_count()


# def threaded_local(command):
#     local(command, capture=True)

CWD = os.path.dirname(os.path.abspath(__file__))
ESP_OPEN_SDK_PATH = os.path.join(CWD, 'esp-open-sdk')
ESP_OPEN_SDK_EXAMPLE_PATH = os.path.join(ESP_OPEN_SDK_PATH, 'examples/blinky')
ESP_OPEN_RTOS_PATH = os.path.join(CWD,'esp-open-rtos')

XTENSA_LX106_ELF_BIN_PATH='/home/logic/_workspace/esp8266-tryout/esp-open-rtos-tryout/esp-open-sdk/xtensa-lx106-elf/bin'

@task
def helloworld():
    # with lcd(CWD):
    #     local('git submodule sync')
    #     local('git submodule update --init --recursive')

    # with lcd(ESP_OPEN_SDK_PATH):
    #     with settings(warn_only=True):
    #         local('make clean')
    #     local('make toolchain esptool libhal STANDALONE=n')

    # with lcd(ESP_OPEN_SDK_EXAMPLE_PATH):
    #     with settings(warn_only=True):
    #         local('make clean')

    #     with shell_env(PATH='%s:$PATH' % XTENSA_LX106_ELF_BIN_PATH):
    #         local('make')

    with lcd(ESP_OPEN_RTOS_PATH):
        with settings(warn_only=True):
            local('make clean')
        with lcd('/home/logic/_workspace/esp8266-tryout/esp-open-rtos-tryout/esp-open-rtos/examples/blink'):
            with shell_env(PATH='%s:$PATH' % XTENSA_LX106_ELF_BIN_PATH):
                local('make')
        # local('make flash -j4 -C examples/http_get ESPPORT=/dev/ttyUSB0')
