#
# Copyright (c) 2020 Red Hat Training <training@redhat.com>
#
# All rights reserved.
# No warranty, explicit or implied, provided.

from labs import labconfig
from labs.grading import Default
from labs.common import steps, labtools, userinterface

# Course SKU
SKU = labconfig.get_course_sku().upper()

# List of hosts involved in that module. Before doing anything,
# the module checks that they can be reached on the network
_targets = ["workstation", "servera"]
_workstation = "workstation"
_servera = "servera"


class AapImagebuild(Default):
    __LAB__ = "aap-imageBuild"

    def start(self):
        items = [
                {
                "label": "Checking lab systems",
                "task": labtools.check_host_reachable,
                "hosts": _targets,
                "fatal": True,
            },
                ]
        userinterface.Console(items).run_items(action="Starting")

    def grade(self):
        items = [
                {
                "label": "Checking lab systems",
                "task": labtools.check_host_reachable,
                "hosts": _targets,
                "fatal": True,
            },
            steps.run_command(
                label="Checking images on " + _servera,
                hosts=[_servera],
                command="""sudo podman images  | grep ansiblebuilder""",
                returns="0",
                shell=True,
            ),
                ]
        ui = userinterface.Console(items)
        ui.run_items(action="Grading")
        ui.report_grade()
