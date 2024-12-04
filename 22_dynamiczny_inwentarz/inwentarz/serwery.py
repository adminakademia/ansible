#!/usr/bin/env python3

import json
output = {
    "_meta": {
        "hostvars": {
            "ansible1": {
                "ansible_become": "false",
                "ansible_connection": "local",
                "ansible_host": "ansible1"
            },
            "lb1.private": {
                "ansible_become": "true",
                "ansible_connection": "ssh",
                "ansible_host": "192.168.122.7",
                "ansible_ssh_pass": {
                    "__ansible_vault": "$ANSIBLE_VAULT;1.1;AES256\n33623039363462616539313934646662356563303338323031323764366231303632373136643938\n3861663762363062376130373766333164303930613031660a393962313233616637343665633236\n32363538613763373138616335393736363531376263303538653030613933383932353637363938\n6161666333336364390a343635613265333235633863663839373432636361643937653736613936\n3338\n"
                },
                "ansible_ssh_user": "user"
            },
            "lb2.private": {
                "ansible_become": "true",
                "ansible_host": "192.168.122.8"
            },
            "nowak.private": {
                "ansible_become": "true",
                "ansible_become_method": "runas",
                "ansible_become_user": "{{ ansible_user }}",
                "ansible_connection": "winrm",
                "ansible_host": "192.168.122.13",
                "ansible_password": "Zaq12wsx",
                "ansible_port": 5986,
                "ansible_shell_type": "cmd",
                "ansible_user": "jnowak",
                "ansible_winrm_server_cert_validation": "ignore"
            },
            "r1.private": {
                "ansible_connection": "ssh",
                "ansible_host": "192.168.122.240"
            },
            "s1.private": {
                "ansible_connection": "ssh",
                "ansible_host": "192.168.122.241"
            },
            "web1.private": {
                "ansible_become": "true",
                "ansible_connection": "ssh",
                "ansible_host": "192.168.122.201"
            },
            "web2.private": {
                "ansible_become": "true",
                "ansible_host": "192.168.122.202"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "servers",
            "local"
        ]
    },
    "ansible1": {
        "hosts": [
            "ansible1"
        ]
    },
    "cisco": {
        "hosts": [
            "r1.private",
            "s1.private"
        ]
    },
    "loadbalancers": {
        "hosts": [
            "lb1.private",
            "lb2.private"
        ]
    },
    "local": {
        "children": [
            "ansible1"
        ]
    },
    "servers": {
        "children": [
            "serweryweb",
            "loadbalancers",
            "cisco",
            "windows"
        ]
    },
    "serweryweb": {
        "hosts": [
            "web1.private",
            "web2.private"
        ]
    },
    "windows": {
        "hosts": [
            "nowak.private"
        ]
    }
}

print(json.dumps(output))
