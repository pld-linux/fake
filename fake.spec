# Note that this is NOT a relocatable package
%define ver      1.1.1
%define rel      1
%define prefix   /usr

Summary: Switches in redundant servers using arp spoofing
Name: fake
Version: %ver
Release: %rel
Copyright: GPL
Group: Networking/Utilities
Source: ftp://ftp.zipworld.com.au/pub/linux/fake/fake-%{ver}.tar.gz
Obsoletes: fake
BuildRoot:	/tmp/%{name}-%{version}-root
Packager: Horms <horms@zipworld.com.au>
URL: http://linux.zipworld.com.au/redundant_linux/
Docdir: %{prefix}/doc

%description
Fake is a utility that enables the IP address be taken over
by bringing up a second interface on the host machine and
using gratuitous arp. Designed to switch in backup servers
on a LAN.


%prep
%setup -n fake-%{ver}
make patch

%build
CFLAGS="${RPM_OPT_FLAGS}"
make

%install
rm -rf $RPM_BUILD_ROOT

make ROOT_DIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
%defattr(-,root,root)

%doc README 
%doc AUTHORS 
%doc COPYING 
%doc ChangeLog
%doc docs
%doc docs/arp_fun.txt
%doc docs/redundant_linux.txt
%doc docs/redundant_linux.ps.gz
%doc docs/redundant_linux.tar.gz

%{prefix}/bin/send_arp
%{prefix}/bin/fake
%config /etc/fake/.fakerc
%config /etc/fake/clear_routers
%config /etc/fake/instance_config/203.12.97.7.cfg
/etc/fake/run
