Summary:	Switches in redundant servers using arp spoofing
Name:		fake
Version:	1.1.2
Release:	2
License:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Source0:	ftp://ftp.zipworld.com.au/pub/linux/fake/%{name}-%{version}.tar.gz
URL:		http://linux.zipworld.com.au/redundant_linux/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fake is a utility that enables the IP address be taken over by
bringing up a second interface on the host machine and using
gratuitous arp. Designed to switch in backup servers on a LAN.

%prep
%setup -q
%{__make} patch

%build
%{__make} CC="gcc $RPM_OPT_FLAGS"

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
%attr(755,root,root) %{_bindir}/send_arp
%attr(755,root,root) %{_bindir}/fake
%config %{_sysconfdir}/fake/.fakerc
%config %{_sysconfdir}/fake/clear_routers
%config %{_sysconfdir}/fake/instance_config/203.12.97.7.cfg
%{_sysconfdir}/fake/run
