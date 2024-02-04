```bash
[root@rocky8 ~]# curl -X PUT "localhost:9200/user/_doc/1?pretty" -H 'Content-Type: application/json' -d '{ "username": "alden.kang" }'
{
  "_index" : "user",
  "_type" : "_doc",
  "_id" : "1",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 0,
  "_primary_term" : 1
}
```

```bash
[root@rocky8 ~]# curl -X GET "localhost:9200/user/_doc/1?pretty"
{
  "_index" : "user",
  "_type" : "_doc",
  "_id" : "1",
  "_version" : 1,
  "_seq_no" : 0,
  "_primary_term" : 1,
  "found" : true,
  "_source" : {
    "username" : "alden.kang"
  }
}
```

```bash
[root@rocky8 ~]# curl -X DELETE "localhost:9200/user/_doc/1?pretty"
{
  "_index" : "user",
  "_type" : "_doc",
  "_id" : "1",
  "_version" : 2,
  "result" : "deleted",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 1,
  "_primary_term" : 1
}
```

```bash
[root@rocky8 ~]# curl -X GET "localhost:9200/user/_doc/1?pretty"
{
  "_index" : "user",
  "_type" : "_doc",
  "_id" : "1",
  "found" : false
}
```

```bash
[root@rocky8 ~]# curl -X PUT "localhost:9200/contents?pretty"
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "contents"
}
```

```bash
[root@rocky8 ~]# curl -X GET "localhost:9200/_cat/indices?v"
health status index            uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   .geoip_databases icj3hTZSSI-s0x_MCEVrmA   1   0         40            0       38mb           38mb
yellow open   contents         u8ftopEHQz2s0fVOIrxxbw   1   1          0            0       227b           227b
yellow open   user             aulZP_yhQa-n3p1URJYMew   1   1          1            0      3.8kb          3.8kb
```

```bash
[root@rocky8 ~]# curl -X PUT "localhost:9200/contents/_doc/1?pretty" \
> -H 'Content-Type: application/json' \
> -d '{ "title": "How to use Elasticsearch", "author": "alden.kang" }'
{
  "_index" : "contents",
  "_type" : "_doc",
  "_id" : "1",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 0,
  "_primary_term" : 1
}
```

```bash
[root@rocky8 ~]# curl -X PUT "localhost:9200/contents/_doc/1?pretty" \
> -H 'Content-Type: application/json' \
> -d '{ "title": "How to use Elasticsearch", "author": "alden.kang, benjamin.butn" }'
{
  "_index" : "contents",
  "_type" : "_doc",
  "_id" : "1",
  "_version" : 2,
  "result" : "updated",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 1,
  "_primary_term" : 1
}
```

```bash
[root@rocky8 ~]# curl -X GET "localhost:9200/contents/_mapping?pretty"
{
  "contents" : {
    "mappings" : {
      "properties" : {
        "author" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "title" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        }
      }
    }
  }
}
```

```bash
[root@rocky8 ~]# curl -X PUT "localhost:9200/contents/_doc/2?pretty" \
> -H 'Content-Type: application/json' \
> -d '{ "title": "How to use Nginx", "author": "alden.kang, benjamin.butn", "rating": 5.0 }'
{
  "_index" : "contents",
  "_type" : "_doc",
  "_id" : "2",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 2,
  "_primary_term" : 1
}
```

```bash
[root@rocky8 ~]# curl -X GET "localhost:9200/contents/_mapping?pretty"
{
  "contents" : {
    "mappings" : {
      "properties" : {
        "author" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "rating" : {
          "type" : "float"
        },
        "title" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        }
      }
    }
  }
}
```

```bash
[root@rocky8 ~]# curl -X PUT "localhost:9200/contents/_doc/2?pretty" \
> -H 'Content-Type: application/json' \
> -d '{ "title": "How to use Apache", "author": "alden.kang, benjamin.butn", "rating": "N/A" }'
{
  "error" : {
    "root_cause" : [
      {
        "type" : "mapper_parsing_exception",
        "reason" : "failed to parse field [rating] of type [float] in document with id '2'. Preview of field's value: 'N/A'"
      }
    ],
    "type" : "mapper_parsing_exception",
    "reason" : "failed to parse field [rating] of type [float] in document with id '2'. Preview of field's value: 'N/A'",
    "caused_by" : {
      "type" : "number_format_exception",
      "reason" : "For input string: \"N/A\""
    }
  },
  "status" : 400
}
```

```bash
[root@rocky8 ~]# curl -X DELETE "localhost:9200/contents/_doc/1?pretty"
{
  "_index" : "contents",
  "_type" : "_doc",
  "_id" : "1",
  "_version" : 3,
  "result" : "deleted",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 3,
  "_primary_term" : 1
}
```

# https://github.com/benjamin-btn/ES-SampleData/blob/master/books.json
```bash
[root@rocky8 ~]# vi books.json
...
[root@rocky8 ~]# cat books.json
{"index":{"_id":"1"}}
{ "title" : "Kubernetes: Up and Running", "reviews": 10, "rating": 5.0, "authors": "Joe Beda, Brendan Burns, Kelsey Hightower", "topics": "Kubernetes", "publisher": "O'Reilly Media, Inc.", "ISBN": "9781491935675", "release_date": "2017/09/03", "description" : "What separates the traditional enterprise from the likes of Amazon, Netflix, and Etsy? Those companies have refined the art of cloud native development to maintain their competitive edge and stay well ahead of the competition. This practical guide shows Java/JVM developers how to build better software, faster, using Spring Boot, Spring Cloud, and Cloud Foundry." }
{"index":{"_id":"2"}}
{ "title" : "Cloud Native Java", "reviews": 33, "rating": 4.3, "authors": "Kenny Bastani, Josh Long", "topics": "Java", "publisher": "O'Reilly Media, Inc.", "ISBN": "9781449374648", "release_date": "2017/08/04", "description" : "What separates the traditional enterprise from the likes of Amazon, Netflix, and Etsy? Those companies have refined the art of cloud native development to maintain their competitive edge and stay well ahead of the competition. This practical guide shows Java/JVM developers how to build better software, faster, using Spring Boot, Spring Cloud, and Cloud Foundry." }
{"index":{"_id":"3"}}
{ "title" : "Learning Chef", "reviews": 20, "rating": 4.2, "authors": "Mischa Taylor, Seth Vargo", "topics": "Chef", "publisher": "O'Reilly Media, Inc.", "ISBN": "9781491944936", "release_date": "2014/11/08", "description" : "Get a hands-on introduction to the Chef, the configuration management tool for solving operations issues in enterprises large and small. Ideal for developers and sysadmins new to configuration management, this guide shows you to automate the packaging and delivery of applications in your infrastructure. You’ll be able to build (or rebuild) your infrastructure’s application stack in minutes or hours, rather than days or weeks." }
{"index":{"_id":"4"}}
{ "title" : "Elasticsearch Indexing", "reviews": 24, "rating": 4.6,  "authors": "Hüseyin Akdoğan", "topics": "ElasticSearch", "publisher": "Packt Publishing", "ISBN": "9781783987023", "release_date": "2015/12/22", "description" : "Improve search experiences with ElasticSearch’s powerful indexing functionality – learn how with this practical ElasticSearch tutorial, packed with tips!" }
{"index":{"_id":"5"}}
{ "title" : "Hadoop: The Definitive Guide, 4th Edition", "reviews": 15, "rating": 4.9, "authors": "Tom White", "topics": "Hadoop", "publisher": "O'Reilly Media, Inc.", "ISBN": "9781491901632", "release_date": "2015/04/14", "description" : "Get ready to unlock the power of your data. With the fourth edition of this comprehensive guide, you’ll learn how to build and maintain reliable, scalable, distributed systems with Apache Hadoop. This book is ideal for programmers looking to analyze datasets of any size, and for administrators who want to set up and run Hadoop clusters." }
{"index":{"_id":"6"}}
{ "title": "Getting Started with Impala", "reviews": 18, "rating": 3.8, "authors": "John Russell", "topics": "Impala", "publisher": "O'Reilly Media, Inc.", "ISBN": "9781491905777", "release_date": "2014/09/14", "description" : "Learn how to write, tune, and port SQL queries and other statements for a Big Data environment, using Impala—the massively parallel processing SQL query engine for Apache Hadoop. The best practices in this practical guide help you design database schemas that not only interoperate with other Hadoop components, and are convenient for administers to manage and monitor, but also accommodate future expansion in data size and evolution of software capabilities. Ideal for database developers and business analysts, the latest revision covers analytics functions, complex types, incremental statistics, subqueries, and submission to the Apache incubator." }
{"index":{"_id":"7"}}
{ "title": "NGINX High Performance", "reviews": 21, "rating": 4.7, "authors": "Rahul Sharma", "topics": "Nginx", "publisher": "Packt Publishing", "ISBN": "9781785281839", "release_date": "2015/07/29", "description": "Optimize NGINX for high-performance, scalable web applications" }
{"index":{"_id":"8"}}
{ "title": "Mastering NGINX - Second Edition", "reviews": 6, "rating": 3.6, "authors": "Dimitri Aivaliotis", "topics": "Nginx", "publisher": "Packt Publishing", "ISBN": "9781782173311", "release_date": "2016/07/28", "description": "An in-depth guide to configuring NGINX for your everyday server needs" }
{"index":{"_id":"9"}}
{ "title" : "Linux Kernel Development, Third Edition", "reviews": 3, "rating": 4.0, "authors": "Robert Love", "topics": "Linux", "publisher": "Addison-Wesley Professional", "ISBN": "9780672329463", "release_date": "2010/06/09", "description" : "Linux Kernel Development details the design and implementation of the Linux kernel, presenting the content in a manner that is beneficial to those writing and developing kernel code, as well as to programmers seeking to better understand the operating system and become more efficient and productive in their coding." }
{"index":{"_id":"10"}}
{ "title" : "Linux Kernel Development, Second Edition", "reviews": 29, "rating": 5.0, "authors": "Robert Love", "topics": "Linux", "publisher": "Sams", "ISBN": "9780672327209", "release_date": "2005/01/01", "description" : "The Linux kernel is one of the most important and far-reaching open-source projects. That is why Novell Press is excited to bring you the second edition of Linux Kernel Development, Robert Love's widely acclaimed insider's look at the Linux kernel. This authoritative, practical guide helps developers better understand the Linux kernel through updated coverage of all the major subsystems as well as new features associated with the Linux 2.6 kernel. You'll be able to take an in-depth look at Linux kernel from both a theoretical and an applied perspective as you cover a wide range of topics, including algorithms, system call interface, paging strategies and kernel synchronization. Get the top information right from the source in Linux Kernel Development." }
```

```bash
[root@rocky8 ~]# curl -X POST "localhost:9200/books/_doc/_bulk?pretty&refresh" -H 'Content-Type: application/json' --data-binary "@books.json"
{
  "took" : 155,
  "errors" : false,
  "items" : [
    {
      "index" : {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "1",
        "_version" : 1,
        "result" : "created",
        "forced_refresh" : true,
        "_shards" : {
          "total" : 2,
          "successful" : 1,
          "failed" : 0
        },
        "_seq_no" : 0,
        "_primary_term" : 1,
        "status" : 201
      }
    },
    {
      "index" : {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "2",
        "_version" : 1,
        "result" : "created",
        "forced_refresh" : true,
        "_shards" : {
          "total" : 2,
          "successful" : 1,
          "failed" : 0
        },
        "_seq_no" : 1,
        "_primary_term" : 1,
        "status" : 201
      }
    },
    {
      "index" : {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "3",
        "_version" : 1,
        "result" : "created",
        "forced_refresh" : true,
        "_shards" : {
          "total" : 2,
          "successful" : 1,
          "failed" : 0
        },
        "_seq_no" : 2,
        "_primary_term" : 1,
        "status" : 201
      }
    },
    {
      "index" : {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "4",
        "_version" : 1,
        "result" : "created",
        "forced_refresh" : true,
        "_shards" : {
          "total" : 2,
          "successful" : 1,
          "failed" : 0
        },
        "_seq_no" : 3,
        "_primary_term" : 1,
        "status" : 201
      }
    },
    {
      "index" : {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "5",
        "_version" : 1,
        "result" : "created",
        "forced_refresh" : true,
        "_shards" : {
          "total" : 2,
          "successful" : 1,
          "failed" : 0
        },
        "_seq_no" : 4,
        "_primary_term" : 1,
        "status" : 201
      }
    },
    {
      "index" : {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "6",
        "_version" : 1,
        "result" : "created",
        "forced_refresh" : true,
        "_shards" : {
          "total" : 2,
          "successful" : 1,
          "failed" : 0
        },
        "_seq_no" : 5,
        "_primary_term" : 1,
        "status" : 201
      }
    },
    {
      "index" : {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "7",
        "_version" : 1,
        "result" : "created",
        "forced_refresh" : true,
        "_shards" : {
          "total" : 2,
          "successful" : 1,
          "failed" : 0
        },
        "_seq_no" : 6,
        "_primary_term" : 1,
        "status" : 201
      }
    },
    {
      "index" : {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "8",
        "_version" : 1,
        "result" : "created",
        "forced_refresh" : true,
        "_shards" : {
          "total" : 2,
          "successful" : 1,
          "failed" : 0
        },
        "_seq_no" : 7,
        "_primary_term" : 1,
        "status" : 201
      }
    },
    {
      "index" : {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "9",
        "_version" : 1,
        "result" : "created",
        "forced_refresh" : true,
        "_shards" : {
          "total" : 2,
          "successful" : 1,
          "failed" : 0
        },
        "_seq_no" : 8,
        "_primary_term" : 1,
        "status" : 201
      }
    },
    {
      "index" : {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "10",
        "_version" : 1,
        "result" : "created",
        "forced_refresh" : true,
        "_shards" : {
          "total" : 2,
          "successful" : 1,
          "failed" : 0
        },
        "_seq_no" : 9,
        "_primary_term" : 1,
        "status" : 201
      }
    }
  ]
}
```

```bash
[root@rocky8 ~]# curl -X GET "localhost:9200/books/_search?q=*&pretty"
{
  "took" : 10,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 10,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 1.0,
        "_ignored" : [
          "description.keyword"
        ],
        "_source" : {
          "title" : "Kubernetes: Up and Running",
          "reviews" : 10,
          "rating" : 5.0,
          "authors" : "Joe Beda, Brendan Burns, Kelsey Hightower",
          "topics" : "Kubernetes",
          "publisher" : "O'Reilly Media, Inc.",
          "ISBN" : "9781491935675",
          "release_date" : "2017/09/03",
          "description" : "What separates the traditional enterprise from the likes of Amazon, Netflix, and Etsy? Those companies have refined the art of cloud native development to maintain their competitive edge and stay well ahead of the competition. This practical guide shows Java/JVM developers how to build better software, faster, using Spring Boot, Spring Cloud, and Cloud Foundry."
        }
      },
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "2",
        "_score" : 1.0,
        "_ignored" : [
          "description.keyword"
        ],
        "_source" : {
          "title" : "Cloud Native Java",
          "reviews" : 33,
          "rating" : 4.3,
          "authors" : "Kenny Bastani, Josh Long",
          "topics" : "Java",
          "publisher" : "O'Reilly Media, Inc.",
          "ISBN" : "9781449374648",
          "release_date" : "2017/08/04",
          "description" : "What separates the traditional enterprise from the likes of Amazon, Netflix, and Etsy? Those companies have refined the art of cloud native development to maintain their competitive edge and stay well ahead of the competition. This practical guide shows Java/JVM developers how to build better software, faster, using Spring Boot, Spring Cloud, and Cloud Foundry."
        }
      },
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "3",
        "_score" : 1.0,
        "_ignored" : [
          "description.keyword"
        ],
        "_source" : {
          "title" : "Learning Chef",
          "reviews" : 20,
          "rating" : 4.2,
          "authors" : "Mischa Taylor, Seth Vargo",
          "topics" : "Chef",
          "publisher" : "O'Reilly Media, Inc.",
          "ISBN" : "9781491944936",
          "release_date" : "2014/11/08",
          "description" : "Get a hands-on introduction to the Chef, the configuration management tool for solving operations issues in enterprises large and small. Ideal for developers and sysadmins new to configuration management, this guide shows you to automate the packaging and delivery of applications in your infrastructure. You’ll be able to build (or rebuild) your infrastructure’s application stack in minutes or hours, rather than days or weeks."
        }
      },
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "4",
        "_score" : 1.0,
        "_source" : {
          "title" : "Elasticsearch Indexing",
          "reviews" : 24,
          "rating" : 4.6,
          "authors" : "Hüseyin Akdoğan",
          "topics" : "ElasticSearch",
          "publisher" : "Packt Publishing",
          "ISBN" : "9781783987023",
          "release_date" : "2015/12/22",
          "description" : "Improve search experiences with ElasticSearch’s powerful indexing functionality – learn how with this practical ElasticSearch tutorial, packed with tips!"
        }
      },
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "5",
        "_score" : 1.0,
        "_ignored" : [
          "description.keyword"
        ],
        "_source" : {
          "title" : "Hadoop: The Definitive Guide, 4th Edition",
          "reviews" : 15,
          "rating" : 4.9,
          "authors" : "Tom White",
          "topics" : "Hadoop",
          "publisher" : "O'Reilly Media, Inc.",
          "ISBN" : "9781491901632",
          "release_date" : "2015/04/14",
          "description" : "Get ready to unlock the power of your data. With the fourth edition of this comprehensive guide, you’ll learn how to build and maintain reliable, scalable, distributed systems with Apache Hadoop. This book is ideal for programmers looking to analyze datasets of any size, and for administrators who want to set up and run Hadoop clusters."
        }
      },
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "6",
        "_score" : 1.0,
        "_ignored" : [
          "description.keyword"
        ],
        "_source" : {
          "title" : "Getting Started with Impala",
          "reviews" : 18,
          "rating" : 3.8,
          "authors" : "John Russell",
          "topics" : "Impala",
          "publisher" : "O'Reilly Media, Inc.",
          "ISBN" : "9781491905777",
          "release_date" : "2014/09/14",
          "description" : "Learn how to write, tune, and port SQL queries and other statements for a Big Data environment, using Impala—the massively parallel processing SQL query engine for Apache Hadoop. The best practices in this practical guide help you design database schemas that not only interoperate with other Hadoop components, and are convenient for administers to manage and monitor, but also accommodate future expansion in data size and evolution of software capabilities. Ideal for database developers and business analysts, the latest revision covers analytics functions, complex types, incremental statistics, subqueries, and submission to the Apache incubator."
        }
      },
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "7",
        "_score" : 1.0,
        "_source" : {
          "title" : "NGINX High Performance",
          "reviews" : 21,
          "rating" : 4.7,
          "authors" : "Rahul Sharma",
          "topics" : "Nginx",
          "publisher" : "Packt Publishing",
          "ISBN" : "9781785281839",
          "release_date" : "2015/07/29",
          "description" : "Optimize NGINX for high-performance, scalable web applications"
        }
      },
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "8",
        "_score" : 1.0,
        "_source" : {
          "title" : "Mastering NGINX - Second Edition",
          "reviews" : 6,
          "rating" : 3.6,
          "authors" : "Dimitri Aivaliotis",
          "topics" : "Nginx",
          "publisher" : "Packt Publishing",
          "ISBN" : "9781782173311",
          "release_date" : "2016/07/28",
          "description" : "An in-depth guide to configuring NGINX for your everyday server needs"
        }
      },
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "9",
        "_score" : 1.0,
        "_ignored" : [
          "description.keyword"
        ],
        "_source" : {
          "title" : "Linux Kernel Development, Third Edition",
          "reviews" : 3,
          "rating" : 4.0,
          "authors" : "Robert Love",
          "topics" : "Linux",
          "publisher" : "Addison-Wesley Professional",
          "ISBN" : "9780672329463",
          "release_date" : "2010/06/09",
          "description" : "Linux Kernel Development details the design and implementation of the Linux kernel, presenting the content in a manner that is beneficial to those writing and developing kernel code, as well as to programmers seeking to better understand the operating system and become more efficient and productive in their coding."
        }
      },
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "10",
        "_score" : 1.0,
        "_ignored" : [
          "description.keyword"
        ],
        "_source" : {
          "title" : "Linux Kernel Development, Second Edition",
          "reviews" : 29,
          "rating" : 5.0,
          "authors" : "Robert Love",
          "topics" : "Linux",
          "publisher" : "Sams",
          "ISBN" : "9780672327209",
          "release_date" : "2005/01/01",
          "description" : "The Linux kernel is one of the most important and far-reaching open-source projects. That is why Novell Press is excited to bring you the second edition of Linux Kernel Development, Robert Love's widely acclaimed insider's look at the Linux kernel. This authoritative, practical guide helps developers better understand the Linux kernel through updated coverage of all the major subsystems as well as new features associated with the Linux 2.6 kernel. You'll be able to take an in-depth look at Linux kernel from both a theoretical and an applied perspective as you cover a wide range of topics, including algorithms, system call interface, paging strategies and kernel synchronization. Get the top information right from the source in Linux Kernel Development."
        }
      }
    ]
  }
}
```

```bash
[root@rocky8 ~]# curl -X GET "localhost:9200/books/_search?q=elasticsearch&pretty"
{
  "took" : 44,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 2.7367249,
    "hits" : [
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "4",
        "_score" : 2.7367249,
        "_source" : {
          "title" : "Elasticsearch Indexing",
          "reviews" : 24,
          "rating" : 4.6,
          "authors" : "Hüseyin Akdoğan",
          "topics" : "ElasticSearch",
          "publisher" : "Packt Publishing",
          "ISBN" : "9781783987023",
          "release_date" : "2015/12/22",
          "description" : "Improve search experiences with ElasticSearch’s powerful indexing functionality – learn how with this practical ElasticSearch tutorial, packed with tips!"
        }
      }
    ]
  }
}
```

```bash
[root@rocky8 ~]# curl -X GET "localhost:9200/books/_search?pretty" \
> -H 'Content-Type: application/json' \
> -d \
> '{
>   "query": {
>     "match": {
>       "rating": 5.0
>     }
>   }
> }'
{
  "took" : 12,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 1.0,
        "_ignored" : [
          "description.keyword"
        ],
        "_source" : {
          "title" : "Kubernetes: Up and Running",
          "reviews" : 10,
          "rating" : 5.0,
          "authors" : "Joe Beda, Brendan Burns, Kelsey Hightower",
          "topics" : "Kubernetes",
          "publisher" : "O'Reilly Media, Inc.",
          "ISBN" : "9781491935675",
          "release_date" : "2017/09/03",
          "description" : "What separates the traditional enterprise from the likes of Amazon, Netflix, and Etsy? Those companies have refined the art of cloud native development to maintain their competitive edge and stay well ahead of the competition. This practical guide shows Java/JVM developers how to build better software, faster, using Spring Boot, Spring Cloud, and Cloud Foundry."
        }
      },
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "10",
        "_score" : 1.0,
        "_ignored" : [
          "description.keyword"
        ],
        "_source" : {
          "title" : "Linux Kernel Development, Second Edition",
          "reviews" : 29,
          "rating" : 5.0,
          "authors" : "Robert Love",
          "topics" : "Linux",
          "publisher" : "Sams",
          "ISBN" : "9780672327209",
          "release_date" : "2005/01/01",
          "description" : "The Linux kernel is one of the most important and far-reaching open-source projects. That is why Novell Press is excited to bring you the second edition of Linux Kernel Development, Robert Love's widely acclaimed insider's look at the Linux kernel. This authoritative, practical guide helps developers better understand the Linux kernel through updated coverage of all the major subsystems as well as new features associated with the Linux 2.6 kernel. You'll be able to take an in-depth look at Linux kernel from both a theoretical and an applied perspective as you cover a wide range of topics, including algorithms, system call interface, paging strategies and kernel synchronization. Get the top information right from the source in Linux Kernel Development."
        }
      }
    ]
  }
}
```

```bash
[root@rocky8 ~]# curl -X GET "localhost:9200/books/_search?pretty" \
> -H 'Content-Type: application/json' \
> -d \
> '{
>   "query": {
>     "bool": {
>       "must": { "match_all": {} },
>       "filter": {
>         "range": {
>           "reviews": {
>             "gte": 10
>           }
>         }
>       }
>     }
>   }
> }'
{
  "took" : 20,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 8,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 1.0,
        "_ignored" : [
          "description.keyword"
        ],
        "_source" : {
          "title" : "Kubernetes: Up and Running",
          "reviews" : 10,
          "rating" : 5.0,
          "authors" : "Joe Beda, Brendan Burns, Kelsey Hightower",
          "topics" : "Kubernetes",
          "publisher" : "O'Reilly Media, Inc.",
          "ISBN" : "9781491935675",
          "release_date" : "2017/09/03",
          "description" : "What separates the traditional enterprise from the likes of Amazon, Netflix, and Etsy? Those companies have refined the art of cloud native development to maintain their competitive edge and stay well ahead of the competition. This practical guide shows Java/JVM developers how to build better software, faster, using Spring Boot, Spring Cloud, and Cloud Foundry."
        }
      },
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "2",
        "_score" : 1.0,
        "_ignored" : [
          "description.keyword"
        ],
        "_source" : {
          "title" : "Cloud Native Java",
          "reviews" : 33,
          "rating" : 4.3,
          "authors" : "Kenny Bastani, Josh Long",
          "topics" : "Java",
          "publisher" : "O'Reilly Media, Inc.",
          "ISBN" : "9781449374648",
          "release_date" : "2017/08/04",
          "description" : "What separates the traditional enterprise from the likes of Amazon, Netflix, and Etsy? Those companies have refined the art of cloud native development to maintain their competitive edge and stay well ahead of the competition. This practical guide shows Java/JVM developers how to build better software, faster, using Spring Boot, Spring Cloud, and Cloud Foundry."
        }
      },
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "3",
        "_score" : 1.0,
        "_ignored" : [
          "description.keyword"
        ],
        "_source" : {
          "title" : "Learning Chef",
          "reviews" : 20,
          "rating" : 4.2,
          "authors" : "Mischa Taylor, Seth Vargo",
          "topics" : "Chef",
          "publisher" : "O'Reilly Media, Inc.",
          "ISBN" : "9781491944936",
          "release_date" : "2014/11/08",
          "description" : "Get a hands-on introduction to the Chef, the configuration management tool for solving operations issues in enterprises large and small. Ideal for developers and sysadmins new to configuration management, this guide shows you to automate the packaging and delivery of applications in your infrastructure. You’ll be able to build (or rebuild) your infrastructure’s application stack in minutes or hours, rather than days or weeks."
        }
      },
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "4",
        "_score" : 1.0,
        "_source" : {
          "title" : "Elasticsearch Indexing",
          "reviews" : 24,
          "rating" : 4.6,
          "authors" : "Hüseyin Akdoğan",
          "topics" : "ElasticSearch",
          "publisher" : "Packt Publishing",
          "ISBN" : "9781783987023",
          "release_date" : "2015/12/22",
          "description" : "Improve search experiences with ElasticSearch’s powerful indexing functionality – learn how with this practical ElasticSearch tutorial, packed with tips!"
        }
      },
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "5",
        "_score" : 1.0,
        "_ignored" : [
          "description.keyword"
        ],
        "_source" : {
          "title" : "Hadoop: The Definitive Guide, 4th Edition",
          "reviews" : 15,
          "rating" : 4.9,
          "authors" : "Tom White",
          "topics" : "Hadoop",
          "publisher" : "O'Reilly Media, Inc.",
          "ISBN" : "9781491901632",
          "release_date" : "2015/04/14",
          "description" : "Get ready to unlock the power of your data. With the fourth edition of this comprehensive guide, you’ll learn how to build and maintain reliable, scalable, distributed systems with Apache Hadoop. This book is ideal for programmers looking to analyze datasets of any size, and for administrators who want to set up and run Hadoop clusters."
        }
      },
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "6",
        "_score" : 1.0,
        "_ignored" : [
          "description.keyword"
        ],
        "_source" : {
          "title" : "Getting Started with Impala",
          "reviews" : 18,
          "rating" : 3.8,
          "authors" : "John Russell",
          "topics" : "Impala",
          "publisher" : "O'Reilly Media, Inc.",
          "ISBN" : "9781491905777",
          "release_date" : "2014/09/14",
          "description" : "Learn how to write, tune, and port SQL queries and other statements for a Big Data environment, using Impala—the massively parallel processing SQL query engine for Apache Hadoop. The best practices in this practical guide help you design database schemas that not only interoperate with other Hadoop components, and are convenient for administers to manage and monitor, but also accommodate future expansion in data size and evolution of software capabilities. Ideal for database developers and business analysts, the latest revision covers analytics functions, complex types, incremental statistics, subqueries, and submission to the Apache incubator."
        }
      },
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "7",
        "_score" : 1.0,
        "_source" : {
          "title" : "NGINX High Performance",
          "reviews" : 21,
          "rating" : 4.7,
          "authors" : "Rahul Sharma",
          "topics" : "Nginx",
          "publisher" : "Packt Publishing",
          "ISBN" : "9781785281839",
          "release_date" : "2015/07/29",
          "description" : "Optimize NGINX for high-performance, scalable web applications"
        }
      },
      {
        "_index" : "books",
        "_type" : "_doc",
        "_id" : "10",
        "_score" : 1.0,
        "_ignored" : [
          "description.keyword"
        ],
        "_source" : {
          "title" : "Linux Kernel Development, Second Edition",
          "reviews" : 29,
          "rating" : 5.0,
          "authors" : "Robert Love",
          "topics" : "Linux",
          "publisher" : "Sams",
          "ISBN" : "9780672327209",
          "release_date" : "2005/01/01",
          "description" : "The Linux kernel is one of the most important and far-reaching open-source projects. That is why Novell Press is excited to bring you the second edition of Linux Kernel Development, Robert Love's widely acclaimed insider's look at the Linux kernel. This authoritative, practical guide helps developers better understand the Linux kernel through updated coverage of all the major subsystems as well as new features associated with the Linux 2.6 kernel. You'll be able to take an in-depth look at Linux kernel from both a theoretical and an applied perspective as you cover a wide range of topics, including algorithms, system call interface, paging strategies and kernel synchronization. Get the top information right from the source in Linux Kernel Development."
        }
      }
    ]
  }
}
```

```bash
[root@rocky8 /]# curl -X GET "localhost:9200/books/_search?pretty" \
> -H 'Content-Type: application/json' \
> -d \
> '{
>   "size": 0,
>   "aggs": {
>     "group_by_state": {
>       "terms": {
>         "field": "topics.keyword"
>       }
>     }
>   }
> }'
{
  "took" : 76,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 10,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [ ]
  },
  "aggregations" : {
    "group_by_state" : {
      "doc_count_error_upper_bound" : 0,
      "sum_other_doc_count" : 0,
      "buckets" : [
        {
          "key" : "Linux",
          "doc_count" : 2
        },
        {
          "key" : "Nginx",
          "doc_count" : 2
        },
        {
          "key" : "Chef",
          "doc_count" : 1
        },
        {
          "key" : "ElasticSearch",
          "doc_count" : 1
        },
        {
          "key" : "Hadoop",
          "doc_count" : 1
        },
        {
          "key" : "Impala",
          "doc_count" : 1
        },
        {
          "key" : "Java",
          "doc_count" : 1
        },
        {
          "key" : "Kubernetes",
          "doc_count" : 1
        }
      ]
    }
  }
}
```

```bash
[root@rocky8 /]# curl -X GET "localhost:9200/books/_search?pretty" \
> -H 'Content-Type: application/json' \
> -d \
> '{
>   "size": 0,
>   "aggs": {
>     "group_by_state": {
>       "terms": {
>         "field": "topics.keyword"
>       },
>       "aggs": {
>         "average_reviews": {
>           "avg": {
>             "field": "reviews"
>           }
>         }
>       }
>     }
>   }
> }'
{
  "took" : 67,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 10,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [ ]
  },
  "aggregations" : {
    "group_by_state" : {
      "doc_count_error_upper_bound" : 0,
      "sum_other_doc_count" : 0,
      "buckets" : [
        {
          "key" : "Linux",
          "doc_count" : 2,
          "average_reviews" : {
            "value" : 16.0
          }
        },
        {
          "key" : "Nginx",
          "doc_count" : 2,
          "average_reviews" : {
            "value" : 13.5
          }
        },
        {
          "key" : "Chef",
          "doc_count" : 1,
          "average_reviews" : {
            "value" : 20.0
          }
        },
        {
          "key" : "ElasticSearch",
          "doc_count" : 1,
          "average_reviews" : {
            "value" : 24.0
          }
        },
        {
          "key" : "Hadoop",
          "doc_count" : 1,
          "average_reviews" : {
            "value" : 15.0
          }
        },
        {
          "key" : "Impala",
          "doc_count" : 1,
          "average_reviews" : {
            "value" : 18.0
          }
        },
        {
          "key" : "Java",
          "doc_count" : 1,
          "average_reviews" : {
            "value" : 33.0
          }
        },
        {
          "key" : "Kubernetes",
          "doc_count" : 1,
          "average_reviews" : {
            "value" : 10.0
          }
        }
      ]
    }
  }
}
```