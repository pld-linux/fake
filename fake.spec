Summary:	Switches in redundant servers using arp spoofing
Summary(es.UTF-8):   Software para arp spoofing
Summary(pl.UTF-8):   Przełączanie redundantnych serwerów poprzez arp spoofing
Summary(pt_BR.UTF-8):   Software para arp spoofing
Name:		fake
Version:	1.1.10
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.vergenet.net/linux/fake/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8ad9af87b9fdff4d8b8d1bac7ed8aef9
URL:		http://www.vergenet.net/linux/fake/
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

%description -l es.UTF-8
Fake es un utilitario que permite que otras maquinas en la red puedan
tomar direcciones IP. Este software fue desarrollado para permitir el
uso de servidores de copias de seguridad (backup) en una red local.

%description -l pl.UTF-8
Fake jest prostym narzędziem pozwalającym na włączanie zapasowych
serwerów w sieci. Na przykład, może być użyty do włączenia zapasowego
serwera poczty, WWW, proxy w czasie zamierzonego lub niezamierzonego
nie działania podstawowego serwera. Fake działa poprzez podnoszenie
dodatkowego interfejsu i spoofowanie adresu ARP aby przejąć adres IP
innej maszyny w sieci lokalnej. Dodatkowy interfejs może być
interfejsem fizycznym lub logicznym (aliasem IP). Fake jest
konfigurowalny i może używać systemów automatycznie monitorujących
dostępność serwerów (np. Heartbeat lub Heart).

%description -l pt_BR.UTF-8
O Fake é um utilitário que permite que endereços IP possam ser tomados
por outras máquinas na rede. Este software foi desenvolvido para se
permitir o uso de servidores de backup em uma rede local.

%prep
%setup -q
%{__make} patch

%build
%{__make} CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	ROOT_DIR=$RPM_BUILD_ROOT \
	MAN8_DIR=$RPM_BUILD_ROOT%{_mandir}/man8

rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/fake/run/CVS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README docs/{arp_fun,redundant_linux}.txt
%dir %{_sysconfdir}/fake
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/fake/.fakerc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/fake/clear_routers
%dir %{_sysconfdir}/fake/instance_config
%config %{_sysconfdir}/fake/instance_config/203.12.97.7.cfg
%attr(755,root,root) %{_sbindir}/send_arp
%attr(755,root,root) %{_sbindir}/fake
%{_mandir}/man8/*
