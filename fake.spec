Summary:	Switches in redundant servers using arp spoofing
Name:		fake
Version:	1.1.1
Release:	2
Copyright:	GPL
Group:		Networking/Utilities
Source:		ftp://ftp.zipworld.com.au/pub/linux/fake/fake-%{ver}.tar.gz
URL:		http://linux.zipworld.com.au/redundant_linux/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Fake is a utility that enables the IP address be taken over by bringing up a
second interface on the host machine and using gratuitous arp. Designed to
switch in backup servers on a LAN.

%prep
%setup -q
make patch

%build
CFLAGS="${RPM_OPT_FLAGS}"
make

%install
rm -rf $RPM_BUILD_ROOT

make ROOT_DIR=$RPM_BUILD_ROOT install

gzip -9nf README AUTHORS ChangeLog docs/{arp_fun,redundant_linux.txt}.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/*.txt.gz
%{prefix}/bin/send_arp
%{prefix}/bin/fake
%config /etc/fake/.fakerc
%config /etc/fake/clear_routers
%config /etc/fake/instance_config/203.12.97.7.cfg
/etc/fake/run
