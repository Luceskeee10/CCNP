# Automation lab

`python automation/mock_api.py` in terminal A; `python automation/api_client.py` in terminal B. Modify the API to require a bearer token, handle 401/403, corrupt a JSON field and document recovery.

Ansible example: install `ansible-core` and collections `cisco.ios` and `ansible.netcommon`, configure inventory for *your lab only*, keep credentials out of Git. The playbook is illustrative and needs reachable real IOS devices.
