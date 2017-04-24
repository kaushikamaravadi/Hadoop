# HDFS File System Commands

## cat

Copies source paths to stdout

```
hadoop fs -cat /user/kaushik/some
```

## chown

change the owner of files. The user must be a super-user 

```
hadoop fs -chown -R root /user/kaushik/test.csv
```

## ls

ls [-C] [-d] [-h] [-q] [-R] [-t] [-S] [-r] [-u] [<path> ...] :
  List the contents that match the specified file pattern. If path is not
  specified, the contents of /user/<currentUser> will be listed. For a directory a
  list of its direct children is returned (unless -d option is specified).
  
  Directory entries are of the form:
        permissions - userId groupId sizeOfDirectory(in bytes)
  modificationDate(yyyy-MM-dd HH:mm) directoryName
  
  and file entries are of the form:
        permissions numberOfReplicas userId groupId sizeOfFile(in bytes)
  modificationDate(yyyy-MM-dd HH:mm) fileName
  
    -C  Display the paths of files and directories only.
    -d  Directories are listed as plain files.
    -h  Formats the sizes of files in a human-readable fashion
        rather than a number of bytes.
    -q  Print ? instead of non-printable characters.
    -R  Recursively list the contents of directories.
    -t  Sort files by modification time (most recent first).
    -S  Sort files by size.
    -r  Reverse the order of the sort.
    -u  Use time of last access instead of modification for
        display and sorting.
```
hadoop fs -ls /user/kaushik
```
```
permissions number_of_replicas userid groupid filesize modification_date modification_time filename
Found 2 items
drwxr-xr-x   - root supergroup          0 2017-04-09 19:17 /user/kaushik/directory
-rw-r--r--   3 root supergroup         16 2017-04-09 19:48 /user/kaushik/some
```
```
hadoop fs -ls -C /user/kaushik
/user/kaushik/directory
/user/kaushik/move
/user/kaushik/parent
/user/kaushik/some
/user/kaushik/test.csv
```
```
hadoop fs -ls -h /user/kaushik
Found 5 items
drwxrwxrwx   - root supergroup          0 2017-04-09 19:17 /user/kaushik/directory
-rw-r--r--   3 root supergroup          0 2017-04-09 20:45 /user/kaushik/move
drwxr-xr-x   - root supergroup          0 2017-04-09 20:37 /user/kaushik/parent
-rw-r--r--   3 root supergroup         16 2017-04-09 20:30 /user/kaushik/some
-rw-r--r--   3 root supergroup     19.2 K 2017-04-09 20:10 /user/kaushik/test.csv
```

## chmod

Change the permissions of files. With -R, make the change recursively through the directory structure. The user must be the owner of the file, or else a super-user.
* The -R option will make the change recursively through the directory structure.
```
hadoop fs -chmod -R 777 /user/kaushik
```
```
hadoop fs -ls /user/kaushik
```
```
Found 2 items
drwxrwxrwx   - root supergroup          0 2017-04-09 19:17 /user/kaushik/directory
-rwxrwxrwx   3 root supergroup         16 2017-04-09 19:48 /user/kaushik/some
```

## count

count the number of directories,files and bytes under the path
The -h option shows sizes in human readable format.
The -v option displays a header line.
```
hadoop fs -count -v -h /user/kaushik
   DIR_COUNT   FILE_COUNT       CONTENT_SIZE PATHNAME
           4            3             19.3 K /user/kaushik
```

## df -h

Displays free space.
```
hadoop fs -df -h /user/kaushik
```
```
Filesystem                                                Size     Used  Available  Use%
hdfs://datanode.c.spatial-rookery-140916.internal:8020  63.0 G  513.3 M     60.1 G    1%
```

## du -s

Displays sizes of files and directories contained in the given directory or the length of a file in case its just a file.
```
hadoop fs -du -s /user/kaushik
```
```
19718  59154  /user/kaushik
```

## du -h

```
hadoop fs -du -h /user/kaushik
```
```
0       0       /user/kaushik/directory
16      48      /user/kaushik/some
19.2 K  57.7 K  /user/kaushik/test.csv
```

## CopyToLocal - From hadoop to Local

```
hadoop fs -copyToLocal /user/kaushik/some /root
```

## CopyFromLocal - From Local to hadoop

```
hadoop fs -copyFromLocal -f some /user/kaushik/some
```

## get - From hadoop to Local

```
hadoop fs -get /user/kaushik/test.csv /root
```

## cp - In HDFS ONLY

The -f option will overwrite the destination if it already exists.
The -p option will preserve file attributes [topx] (timestamps, ownership, permission, ACL, XAttr). If -p is specified with no arg, then preserves timestamps, ownership, permission. If -pa is specified, then preserves permission also because ACL is a super-set of permission. Determination of whether raw namespace extended attributes are preserved is independent of the -p flag.
```
hadoop fs -cp -f /user/kaushik/some /tmp
```
f option overwrites if the file already exists

## GETFACL
## GETMERGE
## GETFATTR

## moveFromLocal - Deletes the local file and moves it to hadoop

```
hadoop fs -moveFromLocal move /user/kaushik
```
## checksum

Returns the checksum information of a file

```
hadoop fs -checksome /user/kaushik/some
```
```

/user/kaushik/some      MD5-of-0MD5-of-512CRC32C        000002000000000000000000d9780362638a5f748973d76ad21bc730
```
## find

Finds all files that match the specified expression and applies selected actions to them. If no path is specified then defaults to the current working directory. If no expression is specified then defaults to -print.
-name pattern
-iname pattern

Evaluates as true if the basename of the file matches the pattern using standard file system globbing. If -iname is used then the match is case insensitive.
```
hadoop fs -find / -name some -print

```
```
find: Permission denied: user=root, access=READ_EXECUTE, inode="/tmp/hive":hive:supergroup:drwx-wx-wx
/tmp/some
find: Permission denied: user=root, access=READ_EXECUTE, inode="/user/history/done":mapred:hadoop:drwxrwx---
find: Permission denied: user=root, access=READ_EXECUTE, inode="/user/hue/.Trash":hue:hue:drwx------
/user/kaushik/some
```

## mkdir

Takes path uri’s as argument and creates directories
```
hdfs dfs -mkdir -p /user/kaushik/parent/child/
```

## rm

```hdfs dfs -rm /user/kaushik/move
```
```
17/04/09 23:06:42 INFO fs.TrashPolicyDefault: Moved: 'hdfs://datanode.c.spatial-rookery-140916.internal:8020/user/kaushik
/move' to trash at: hdfs://datanode.c.spatial-rookery-140916.internal:8020/user/hdfs/.Trash/Current/user/kaushik/move
```

## rm -r(-R), 
-f -  will not display a diagnostic message or modify the exit status to reflect an error if the file does not exist

```
hdfs dfs -rm -r /user/kaushik/parent
```
```
17/04/09 23:09:43 INFO fs.TrashPolicyDefault: Moved: 'hdfs://datanode.c.spatial-rookery-140916.internal:8020/user/kaushik
/parent' to trash at: hdfs://datanode.c.spatial-rookery-140916.internal:8020/user/hdfs/.Trash/Current/user/kaushik/parent
```

## rm -skipTrash 

The -skipTrash option will bypass trash, if enabled, and delete the specified file(s) immediately. This can be useful when it is necessary to delete files from an over-quota directory
```
hdfs dfs -rm -skipTrash /user/kaushik/some
```
```
Deleted /user/kaushik/some
```

## setrep

Changes the replication factor of a file. If path is a directory then the command recursively changes the replication factor of all files under the directory tree rooted at path
The -w flag requests that the command wait for the replication to complete. This can potentially take a very long time.
The -R flag is accepted for backwards compatibility. It has no effect

```
hdfs dfs -setrep 2 /user/kaushik/test.csv
```
```
Replication 2 set: /user/kaushik/test.csv
```
```
hdfs dfs -setrep -w 1 /user/kaushik/test.csv

```
```
Replication 1 set: /user/kaushik/test.csv
Waiting for /user/kaushik/test.csv ... done
```

## stat

Print statistics about the file/directory at <path> in the specified format. Format accepts filesize in blocks (%b), type (%F), group name of owner (%g), name (%n), block size (%o), replication (%r), user name of owner(%u), and modification date (%y, %Y). %y shows UTC date as “yyyy-MM-dd HH:mm:ss” and %Y shows milliseconds since January 1, 1970 UTC. If the format is not specified, %y is used by default.

```
hdfs dfs -stat /user
```
```
2017-04-09 23:06:42
```
hadoop fs -stat "%F %u:%g %b %y %n" /user
```
directory hdfs:supergroup 0 2017-04-09 23:06:42 user
```

## tail

Displays last kilobyte of the file to stdou
```
hdfs dfs -tail /user/kaushik/test.csv
```
```
;0000;13,2899;;;
150921;0000;10,1809;;;
150922;0000;8,51982;;;
150923;0000;9,35185;;;
150924;0000;7,37266;;;
```

## test

test if a file or directory exists 
Usage: hadoop fs -test -[defsz] URI

Options:

-d: f the path is a directory, return 0.
-e: if the path exists, return 0.
-f: if the path is a file, return 0.
-s: if the path is not empty, return 0.
-z: if the file is zero length, return 0.
```
hadoop fs -test -e /user/kaushik/test.csv
```
```
echo $?
0
```
## text

Takes a source file and outputs the file in text format. The allowed formats are zip and TextRecordInputStream.
```
hdfs dfs -text /user/kaushik/test.csv
```
```
FECHA (YYMMDD);HORA (HHMM);Registros validados;Registros preliminares;Registros no validados;
130601;0000;22,3333;;;
130602;0000;25,5833;;;
```

## touchz

create a file of zero length

```
hdfs dfs -touchz /user/kaushik/marv.txt
```

## usage

displays the usage for given command or all commands if non is specified

```
hdfs dfs -usage appendToFile
```
```
Usage: hadoop fs [generic options] -appendToFile <localsrc> ... <dst>
```

