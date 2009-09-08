%define name tiobench
%define version 0.3.3
%define release %mkrel 5

Summary: A test program for filesystem performance
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Development/Kernel
Url: http://sourceforge.net/projects/tiobench/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
Threaded I/O bench for Linux (or any *nix system with POSIX threads
support library).

%prep
%setup -q

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
install -d %buildroot/%_bindir
install tiotest %buildroot/%_bindir
install tiobench.pl %buildroot/%_bindir
install tiosum.pl %buildroot/%_bindir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/tiotest
%{_bindir}/tiobench.pl
%{_bindir}/tiosum.pl
%doc README BUGS TODO ChangeLog

