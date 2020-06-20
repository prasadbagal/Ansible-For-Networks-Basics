# Usage

## how to trigger backout option?

```
ansible-playbook -i inventory main.yml -u prasad -k --extra-vars "backout=true"
```

# inventory - Dependancy

## inventory Should contain 'ios' group and below hosts.

```
[ios]
192.168.122.161
192.168.122.162
192.168.122.163
```