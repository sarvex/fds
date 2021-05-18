import os
from typing import Any

import pygit2

from fds.services.base_service import BaseService
from fds.utils import execute_command, convert_bytes_to_string, does_file_exist


class GitService(BaseService):
    """
    Git Service responsible for all the git commands of fds
    """
    def __init__(self):
        self.repo_path = os.path.curdir

    def init(self) -> bool:
        """
        Responsible for running git init
        :return:
        """
        try:
            pygit2.init_repository(self.repo_path)
            return True
        except:
            return False

    def status(self) -> Any:
        """
        Responsible for running git status
        :return:
        """
        return execute_command(["git", "status"], capture_output=False)

    def add(self, add_argument: str) -> Any:
        """
        Responsible for running git add
        :param add_argument: extra agruments of git add
        :return: 
        """
        git_output = execute_command(["git", "check-ignore", add_argument], capture_output=True)
        if convert_bytes_to_string(git_output.stdout) != '':
            return
        # This will take care of adding everything in the argument to add including the .dvc files inside it
        execute_command(["git", "add", add_argument])
        # Explicitly adding the .dvc file in the root because that wont be added by git
        dvc_file = f"{add_argument}.dvc"
        if does_file_exist(dvc_file):
            execute_command(["git", "add", f"{add_argument}.dvc"])
        ignore_file = ".gitignore"
        if does_file_exist(ignore_file):
            execute_command(["git", "add", ignore_file])

    def commit(self, message: str) -> Any:
        execute_command(["git", "commit", "-am", message], capture_output=False)