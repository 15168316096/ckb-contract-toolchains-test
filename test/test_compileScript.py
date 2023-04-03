import asyncio
import os
import time

import pytest

from helper.Sshd import Sshd
from utils.randString import generate_random_string
from utils.logger import get_logger

logger = get_logger("CompileScript")


class TestCompileScript:

    @pytest.mark.parametrize("toolchain, compiletype", [
        ("nervos/ckb-riscv-gnu-toolchain:xenial", "riscv64-unknown-elf-gcc"),
        ("docker.io/xxuejie/ckb-contract-toolchains:20230331-2", "riscv64-ckb-elf-gcc")
    ])
    def test_generateScriptBinByToolChain(self, toolchain, compiletype):
        container_name = generate_random_string(5)
        scriptBin = generate_random_string(3) + "-" + compiletype + "Bin"
        scripts_dir = os.path.join(os.getcwd(), "testData/scripts")
        asyncio.run(
            Sshd.execute("docker", ["run", "-itd", "--name", f"{container_name}", "-v", f"{scripts_dir}:/code",
                                    f"{toolchain}", "bash"]))
        time.sleep(30)
        asyncio.run(Sshd.executeByString(
            f"docker exec -itd {container_name} sh -c ' cd code/ && {compiletype}  -Os always_success.c -o {scriptBin}'"))
