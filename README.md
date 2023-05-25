# about project

The project is developed for the swu wifi verify, but you can modify serverPreFix(school net server ip) in the class schoolNet for any 锐捷网络, it's very useful for the console.

I also provide a compiled version on dist, type file\_name(such as net.exe) to replace 'python net.pt' for use.

# parameters

| full parameter | full parameter  |              tips               |
| :------------: | :-------------: | :-----------------------------: |
|       -h       |     --help      | show this help message and exit |
|    -u USER     |   --user USER   |            user name            |
|   -p PASSWD    | --passwd PASSWD |            password             |
|                |     --login     |              login              |
|                |    --logout     |             logout              |
|       -r       |    --regist     |       regist mac address        |
|       -c       |    --cancel     |       cancel mac address        |

# example

## login

1. login: python net.py --login [-u|--user] user [-p|--passwd] passwd
2. login with register mac: python net.py --login [-u|--user] user [-p|--passwd] passwd [-r|--regist]

# logout

1. logout: python net.py --logout
2. logout with unregister mac: python net.py --logout [-c|--cancel]

# do for mac address

1. register mac: python net.py [-r|--register]
2. unregister mac: python net.py [-c|--cancel]

