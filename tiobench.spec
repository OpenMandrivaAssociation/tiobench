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



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.3.3-5mdv2010.0
+ Revision: 434400
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3.3-4mdv2009.0
+ Revision: 261562
- rebuild
- rebuild
- fix summary-ended-with-dot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.3.3-1mdv2008.1
+ Revision: 128470
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import tiobench


* Tue Apr 27 2004 Juan Quintela <quintela@mandrakesoft.com> 0.3.3-1mdk
- 1st Mandrake version.
