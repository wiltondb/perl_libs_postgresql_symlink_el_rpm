Name: perl-libs-postgresql-symlink
Version: 1.0.0
Release: 1%{?dist}
Summary: Symlink for perl-libs package
License: PostgreSQL
BuildArch: noarch
 
%description
Symlink for perl-libs package to support PostgreSQL plperl extension.

%prep

%build

%install
mkdir -p %{buildroot}%{_libdir}
pushd %{buildroot}%{_libdir}
ln -s ./perl5/CORE/libperl.so
popd

%files
%{_libdir}/libperl.so
 
%changelog
	
* Wed Dec 21 2022 Alex Kasko <alex@staticlibs.net> - 1.0.0-1
	
- Initial package

