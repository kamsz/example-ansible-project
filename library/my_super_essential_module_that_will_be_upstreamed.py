#!/usr/bin/python

try:
    import super_library
    HAS_SUPERLIBRARY = True
except ImportError:
    HAS_SUPERLIBRARY = False

def main():
    argument_spec = dict(
        arg1=dict(required=True),
        arg2=dict(required=True, type='int', default=1)
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    if not HAS_SUPERLIBRARY:
        module.fail_json(msg='Missing super library!')

    module.exit_json(changed=True, my_important_result='OK!')

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
