# QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
# Lean CLI v1.0. Copyright 2021 QuantConnect Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
from pathlib import Path
from typing import List

from ablean.components.config.storage import Storage
from ablean.components.util.xml_manager import XMLManager
from ablean.constants import PROJECT_CONFIG_FILE_NAME


class ProjectConfigManager:
    """The ProjectConfigManager class manages the configuration of a single project."""

    def __init__(self, xml_manager: XMLManager) -> None:
        """Creates a new ProjectConfigManager instance.

        :param xml_manager: the XMLManager instance to use when parsing XML files
        """
        self._xml_manager = xml_manager

    def get_project_config(self, project_directory: Path) -> Storage:
        """Returns a Storage instance to get/set the configuration for a project.

        :param project_directory: the path to the project to retrieve the configuration of
        :return: the Storage instance containing the project-specific configuration of the given project
        """
        return Storage(str(project_directory / PROJECT_CONFIG_FILE_NAME))

    def get_local_id(self, project_directory: Path) -> int:
        """Returns the local id of a project.

        Every Lean CLI project has a unique local id, regardless of whether the project is synchronized with the cloud.

        :param project_directory: the path to the project to retrieve the local id of
        :return: the local id of the given project
        """
        project_config = self.get_project_config(project_directory)

        if project_config.has("local-id"):
            return project_config.get("local-id")

        project_id = random.randint(100_000_000, 999_999_999)
        project_config.set("local-id", project_id)

        return project_id
