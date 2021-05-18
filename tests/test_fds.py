import unittest
from unittest.mock import patch

from fds.services.fds_service import FdsService


class TestFds(unittest.TestCase):

    @patch('fds.services.dvc_service.DVCService')
    @patch('fds.services.git_service.GitService')
    def test_init_success(self, mock_git_service, mock_dvc_service):
        fds_service = FdsService(mock_git_service, mock_dvc_service)
        fds_service.init()
        assert mock_git_service.init.called
        assert mock_dvc_service.init.called

    @patch('fds.services.dvc_service.DVCService')
    @patch('fds.services.git_service.GitService')
    def test_status_success(self, mock_git_service, mock_dvc_service):
        fds_service = FdsService(mock_git_service, mock_dvc_service)
        fds_service.status()
        assert mock_git_service.status.called
        assert mock_dvc_service.status.called

    @patch('fds.services.dvc_service.DVCService')
    @patch('fds.services.git_service.GitService')
    def test_status_git_failure(self, mock_git_service, mock_dvc_service):
        mock_git_service.status.side_effect = Exception
        fds_service = FdsService(mock_git_service, mock_dvc_service)
        fds_service.status()
        self.assertRaises(Exception, mock_git_service.status)
        assert mock_git_service.status.called
        assert mock_dvc_service.status.called

    @patch('fds.services.dvc_service.DVCService')
    @patch('fds.services.git_service.GitService')
    def test_status_dvc_failure(self, mock_git_service, mock_dvc_service):
        mock_dvc_service.status.side_effect = Exception
        fds_service = FdsService(mock_git_service, mock_dvc_service)
        fds_service.status()
        self.assertRaises(Exception, mock_dvc_service.status)
        assert mock_git_service.status.called
        assert mock_dvc_service.status.called

    @patch('fds.services.dvc_service.DVCService')
    @patch('fds.services.git_service.GitService')
    def test_add_success(self, mock_git_service, mock_dvc_service):
        fds_service = FdsService(mock_git_service, mock_dvc_service)
        fds_service.add(".")
        assert mock_git_service.add.called
        assert mock_dvc_service.add.called

    @patch('fds.services.dvc_service.DVCService')
    @patch('fds.services.git_service.GitService')
    def test_add_git_failure(self, mock_git_service, mock_dvc_service):
        mock_git_service.add.side_effect = Exception
        fds_service = FdsService(mock_git_service, mock_dvc_service)
        fds_service.add(".")
        self.assertRaises(Exception, mock_git_service.add)
        assert mock_git_service.add.called
        assert mock_dvc_service.add.called

    @patch('fds.services.dvc_service.DVCService')
    @patch('fds.services.git_service.GitService')
    def test_add_dvc_failure(self, mock_git_service, mock_dvc_service):
        mock_dvc_service.add.side_effect = Exception
        fds_service = FdsService(mock_git_service, mock_dvc_service)
        fds_service.add(".")
        self.assertRaises(Exception, mock_dvc_service.add)
        assert mock_git_service.add.called
        assert mock_dvc_service.add.called

    @patch('fds.services.dvc_service.DVCService')
    @patch('fds.services.git_service.GitService')
    def test_commit_success(self, mock_git_service, mock_dvc_service):
        fds_service = FdsService(mock_git_service, mock_dvc_service)
        fds_service.commit("some commit message")
        assert mock_git_service.commit.called
        assert mock_dvc_service.commit.called

    @patch('fds.services.dvc_service.DVCService')
    @patch('fds.services.git_service.GitService')
    def test_commit_git_failure(self, mock_git_service, mock_dvc_service):
        mock_git_service.commit.side_effect = Exception
        fds_service = FdsService(mock_git_service, mock_dvc_service)
        fds_service.commit("some commit message")
        self.assertRaises(Exception, mock_git_service.commit)
        assert mock_git_service.commit.called
        assert mock_dvc_service.commit.called

    @patch('fds.services.dvc_service.DVCService')
    @patch('fds.services.git_service.GitService')
    def test_commit_dvc_failure(self, mock_git_service, mock_dvc_service):
        mock_dvc_service.commit.side_effect = Exception
        fds_service = FdsService(mock_git_service, mock_dvc_service)
        fds_service.commit("some commit message")
        self.assertRaises(Exception, mock_dvc_service.commit)
        assert mock_git_service.commit.called
        assert mock_dvc_service.commit.called