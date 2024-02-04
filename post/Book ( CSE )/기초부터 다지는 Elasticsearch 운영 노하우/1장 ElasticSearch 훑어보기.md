# https://www.elastic.co/support/matrix
# 7.17 로 가자...
# Rocky 8 로 가자...


```bash
$ docker pull rockylinux:8
8: Pulling from library/rockylinux
a49f4b3e1553: Pull complete
Digest: sha256:c464612ef7e3d54d658c3eaa4778b5cdc990ec7a4d9ab63b0f00c9994c6ce980
Status: Downloaded newer image for rockylinux:8
docker.io/library/rockylinux:8
```

```bash
$ docker run -d --name 'rocky8' --hostname 'rocky8' rockylinux:8 sleep infinity
14c7dd4efa251885358c65c8d698b20a02958eefe08653760d3194cdc2b648eb
```

```bash
$ docker exec -it rocky8 systemctl status --no-pager
System has not been booted with systemd as init system (PID 1). Can't operate.
Failed to connect to bus: Host is down
```

```bash
$ docker stop rocky8
rocky8
```

```bash
$ docker container rm rocky8
rocky8
```

```bash
$ docker run -d --privileged --name 'rocky8' --hostname 'rocky8' rockylinux:8 /sbin/init
8bc54ed114ea4ffc7794d1fb06be88429b6cf9f31951b269f4c01bf48d0d1022
```

```bash
$ docker exec -it rocky8 systemctl status --no-pager
● rocky8
    State: running
     Jobs: 0 queued
   Failed: 0 units
    Since: Wed 2024-01-31 14:50:41 UTC; 12s ago
   CGroup: /
           ├─init.scope
           │ ├─ 1 /sbin/init
           │ └─54 systemctl status --no-pager
           └─system.slice
             ├─systemd-journald.service
             │ └─17 /usr/lib/systemd/systemd-journald
             └─dbus.service
               └─28 /usr/bin/dbus-daemon --system --address=systemd: --nofork...
```



```bash
$ docker exec -it rocky8 /bin/bash
[root@rocky8 /]#
```

```bash
[root@rocky8 /]# dnf update -y
```

```bash
[root@rocky8 /]# java -version
bash: java: command not found
[root@rocky8 /]# dnf install java -y
...
[root@rocky8 /]# java -version
openjdk version "1.8.0_402"
OpenJDK Runtime Environment (build 1.8.0_402-b06)
OpenJDK 64-Bit Server VM (build 25.402-b06, mixed mode)
```

# https://www.elastic.co/guide/en/elasticsearch/reference/7.17/rpm.html
```bash
[root@rocky8 /]# rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
[root@rocky8 /]# vi /etc/yum.repos.d/elasticsearch.repo
...
[root@rocky8 /]# cat /etc/yum.repos.d/elasticsearch.repo
[elasticsearch]
name=Elasticsearch repository for 7.x packages
baseurl=https://artifacts.elastic.co/packages/7.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=0
autorefresh=1
type=rpm-md
[root@rocky8 /]# dnf install elasticsearch -y --enablerepo=elasticsearch
...
[root@rocky8 /]# systemctl status elasticsearch
● elasticsearch.service - Elasticsearch
   Loaded: loaded (/usr/lib/systemd/system/elasticsearch.service; disabled; vendor preset: disabled)
   Active: inactive (dead)
     Docs: https://www.elastic.co
```

```bash
[root@rocky8 /]# systemctl start elasticsearch
[root@rocky8 /]# systemctl status elasticsearch --no-pager
● elasticsearch.service - Elasticsearch
   Loaded: loaded (/usr/lib/systemd/system/elasticsearch.service; disabled; vendor preset: disabled)
   Active: active (running) since Wed 2024-01-31 14:58:44 UTC; 20s ago
     Docs: https://www.elastic.co
 Main PID: 543 (java)
    Tasks: 77 (limit: 49514)
   Memory: 4.2G
   CGroup: /system.slice/elasticsearch.service
           ├─543 /usr/share/elasticsearch/jdk/bin/java -Xshare:auto -Des.networkaddress.cache.ttl=60 -Des.networkaddress.cache.negative.ttl=10 -XX:+AlwaysPreTouch -Xss1m -Djava.awt.h…
           └─740 /usr/share/elasticsearch/modules/x-pack-ml/platform/linux-aarch64/bin/controller

Jan 31 14:58:31 rocky8 systemd[1]: Starting Elasticsearch...
Jan 31 14:58:35 rocky8 systemd-entrypoint[543]: Jan 31, 2024 2:58:35 PM sun.util.locale.provider.LocaleProviderAdapter <clinit>
Jan 31 14:58:35 rocky8 systemd-entrypoint[543]: WARNING: COMPAT locale provider will be removed in a future release
Jan 31 14:58:44 rocky8 systemd[1]: Started Elasticsearch.
[root@rocky8 /]# curl localhost:9200
{
  "name" : "rocky8",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "0kiTnSpJQQecWK7Hsk3p9w",
  "version" : {
    "number" : "7.17.17",
    "build_flavor" : "default",
    "build_type" : "rpm",
    "build_hash" : "aba4da413a368e296dfc64fb20897334d0340aa1",
    "build_date" : "2024-01-18T10:05:03.821431920Z",
    "build_snapshot" : false,
    "lucene_version" : "8.11.1",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

```bash
[root@rocky8 elasticsearch]# systemctl stop elasticsearch
[root@rocky8 elasticsearch]# systemctl status elasticsearch --no-pager
● elasticsearch.service - Elasticsearch
   Loaded: loaded (/usr/lib/systemd/system/elasticsearch.service; disabled; vendor preset: disabled)
   Active: inactive (dead)
     Docs: https://www.elastic.co

Jan 31 14:58:31 rocky8 systemd[1]: Starting Elasticsearch...
Jan 31 14:58:35 rocky8 systemd-entrypoint[543]: Jan 31, 2024 2:58:35 PM sun.util.locale.provider.LocaleProviderAdapter <clinit>
Jan 31 14:58:35 rocky8 systemd-entrypoint[543]: WARNING: COMPAT locale provider will be removed in a future release
Jan 31 14:58:44 rocky8 systemd[1]: Started Elasticsearch.
Jan 31 15:02:03 rocky8 systemd[1]: Stopping Elasticsearch...
Jan 31 15:02:06 rocky8 systemd[1]: elasticsearch.service: Succeeded.
Jan 31 15:02:06 rocky8 systemd[1]: Stopped Elasticsearch.
```