import asyncio
import subprocess
from typing import List, Optional

from utils.logger import get_logger
from utils.timeout import timeout

logger = get_logger("Sshd")


class Sshd:

    @staticmethod
    def execute_sync(cmd: str) -> Optional[str]:
        try:
            logger.info(f"Running command: {cmd}")
            result = subprocess.run(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    encoding="utf-8", shell=True)
            logger.info(f"Command output: {result.stdout.strip()}")
            return result.stdout.strip()
        except Exception as e:
            print(f"Error executing command: {cmd}, Error message: {str(e)}")
            return None

    @staticmethod
    @timeout(30)
    async def execute(cmd: str, args: List[str] = None) -> str:
        """
        执行命令行，返回命令行输出结果

        :param cmd: str, 命令行字符串
        :param args: list, 命令行参数列表
        :return: str, 命令行输出结果
        """

        cmd_args = [cmd]
        if args:
            cmd_args += args

        logger.info(f"Running command: {' '.join(cmd_args)}")

        proc = await asyncio.create_subprocess_exec(
            *cmd_args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await proc.communicate()
        output = (stdout + stderr).decode().strip()

        logger.info(f"Command output: {output}")

        return output

    @staticmethod
    @timeout(30)
    async def execute_multiple(commands: List[str]) -> List[str]:
        """
        执行多个命令行，返回每个命令行的输出结果

        :param commands: list, 命令行列表
        :return: list, 命令行输出结果列表
        """
        results = []

        for cmd in commands:
            logger.info(f"Running command: {cmd}")
            result = await Sshd.execute(cmd)
            results.append(result)

        return results

    @staticmethod
    async def executeByString(cmd: str) -> str:
        logger.info(f"Running command: {cmd}")

        try:
            # Use `async with` to automatically clean up resources
            proc = await asyncio.create_subprocess_shell(
                cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE, shell=True
            )
            stdout, stderr = await asyncio.gather(proc.stdout.readline(), proc.stderr.readline())
            output = stdout.decode().strip() if stdout else stderr.decode().strip()
            logger.info(f"Command output: {output}")
            return output

        except Exception as e:
            logger.error(f"Error executing command {cmd}: {e}")
            return ""
