Summary:	Switches in redundant servers using arp spoofing
Summary(pl):	Prze��czanie redundantnych serwer�w poprzez arp spoofing
Name:		fake
Version:	1.1.6
Release:	2
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narz�dzia
Group(pt_BR):	Rede/Utilit�rios
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

%description -l pl
Fake jest prostym narz�dziem pozwalaj�cym na w��czanie zapasowych
serwer�w w sieci. Na przyk�ad, mo�e by� u�yty do w��czenia zapasowego
serwera poczty, WWW, proxy w czasie zamierzonego lub niezamierzonego
nie dzia�ania podstawowego serwera. Fake dzia�a poprzez podnoszenie
dodatkowego interfejsu i spoofowanie adresu ARP aby przej�� adres IP
innej maszyny w sieci lokalnej. Dodatkowy interfejs mo�e by�
interfejsem fizycznym lub logicznym (aliasem IP). Fake jest
konfigurowalny i mo�e u�ywa� system�w automatycznie monitoruj�cych
dost�pno�� serwer�w (np. Heartbeat lub Heart).

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
%dir %{_sysconfdir}/fake
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/fake/.fakerc
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/fake/clear_routers
%dir %{_sysconfdir}/fake/instance_config
%config %{_sysconfdir}/fake/instance_config/203.12.97.7.cfg
%attr(755,root,root) %{_bindir}/send_arp
%attr(755,root,root) %{_bindir}/fake
