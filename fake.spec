Summary:	Switches in redundant servers using arp spoofing
Name:		fake
Version:	1.1.6
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Source0:	ftp://ftp.vergenet.net/pub/fake/%{version}/%{name}-%{version}.tar.gz
URL:		http://www.ca.us.vergenet.net/linux/fake/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fake is a simple utility designed to enable the switching in of backup
servers on a LAN. For example, fake can be used to switch in backup
mail, Web, and proxy servers during periods of both unscheduled and
scheduled down time. Fake works by bringing up an additional interface
and using ARP spoofing to take over the IP address of another machine
on the LAN. The additional interface can be a physical interface or a
logical interface (an IP alias). Fake is configurable and can be
automated using systems that monitor the availability of servers (like
Heartbeat and Heart).

%prep
%setup -q
%{__make} patch

%build
%{__make} CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} ROOT_DIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/fake/run/CVS

gzip -9nf README AUTHORS ChangeLog docs/{arp_fun,redundant_linux}.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/*.txt.gz
%config %{_sysconfdir}/fake/.fakerc
%config %{_sysconfdir}/fake/clear_routers
%config %{_sysconfdir}/fake/instance_config/203.12.97.7.cfg
%attr(755,root,root) %{_bindir}/send_arp
%attr(755,root,root) %{_bindir}/fake
