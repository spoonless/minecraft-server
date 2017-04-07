#!/bin/bash -e

ansible-playbook -k -K -b -i inventory.ini playbook.yml
