### Change Ownership

```sh
hdfs dfs -mkdir /user/kaushik_amaravadi
```
```sh
hdfs dfs -chown -R kaushik_amaravadi:kaushik_amaravadi /user/kaushik_amaravadi
```
```sh
hdfs@master ~]$ hdfs dfs -ls /user/
```
```
Found 9 items
drwxr-xr-x   - admin             admin                      0 2017-05-26 20:33 /user/admin
drwxr-xr-x   - hdfs              supergroup                 0 2017-05-26 20:33 /user/hdfs
drwxrwxrwx   - mapred            hadoop                     0 2017-05-25 22:26 /user/history
drwxrwxr-t   - hive              hive                       0 2017-05-25 22:27 /user/hive
drwxrwxr-x   - hue               hue                        0 2017-05-25 22:27 /user/hue
drwxrwxrwx   - hdfs              supergroup                 0 2017-05-26 20:53 /user/kaushik
drwxr-xr-x   - kaushik_amaravadi kaushik_amaravadi          0 2017-05-26 22:45 /user/kaushik_amaravadi
drwxrwxr-x   - oozie             oozie                      0 2017-05-25 22:27 /user/oozie
drwxr-x--x   - spark             spark                      0 2017-05-25 22:26 /user/spark
```
