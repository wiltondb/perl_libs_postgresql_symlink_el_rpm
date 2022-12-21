#perl-libs-postgresql-symlink

This packages provides the symlink `/usr/lib64/libperl.so` that points to `/usr/lib64/perl5/libperl.so`. This allows to prevent PostgreSQL problems with `plperl` extension (without modifying PostgreSQL linking details) like the following:

```
 NOTICE:  installing required extension "plperl"
 ERROR:  could not load library "/usr/lib64/pgsql/plperl.so": libperl.so: cannot open shared object file: No such file or directory
```

