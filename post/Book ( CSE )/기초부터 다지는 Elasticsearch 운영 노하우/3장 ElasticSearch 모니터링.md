```bash
[root@rocky8 ~]# dnf install git -y
```

```bash
[root@rocky8 ~]# git clone https://github.com/mobz/elasticsearch-head.git
```

```bash
[root@rocky8 ~]# dnf install npm -y
```

```bash
[root@rocky8 ~]# cd elasticsearch-head/
[root@rocky8 elasticsearch-head]#
```

```bash
[root@rocky8 elasticsearch-head]# cat package.json
{
  "name": "elasticsearch-head",
  "version": "0.0.0",
  "description": "Front end for an elasticsearch cluster",
  "main": "_site/index.html",
  "directories": {
    "test": "test"
  },
  "scripts": {
    "start": "grunt server",
    "test": "grunt jasmine",
    "proxy": "node proxy/index.js"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/mobz/elasticsearch-head.git"
  },
  "author": "",
  "license": "Apache2",
  "gitHead": "0c2ac0b5723b493e4454baa7398f386ecb829412",
  "readmeFilename": "README.textile",
  "devDependencies": {
    "grunt": "1.0.1",
    "grunt-contrib-concat": "1.0.1",
    "grunt-contrib-watch": "1.0.0",
    "grunt-contrib-connect": "1.0.2",
    "grunt-contrib-copy": "1.0.0",
    "grunt-contrib-clean": "1.0.0",
    "grunt-contrib-jasmine": "1.0.3",
    "karma": "1.3.0",
    "grunt-karma": "2.0.0",
    "http-proxy": "1.16.x"
  }
}
```

```bash
[root@rocky8 elasticsearch-head]# npm install
```

---

# bt-ada-es01.ay2dev.krane.9rum.cc