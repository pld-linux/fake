Summary:	Switches in redundant servers using arp spoofing
Summary(es):	Software para arp spoofing
Summary(pl):	Prze³±czanie redundantnych serwerów poprzez arp spoofing
Summary(pt_BR):	Software para arp spoofing
Name:		fake
Version:	1.1.8
Release:	2
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.vergenet.net/linux/fake/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	75227cf5a2a3dd0f505bad83bb651fdc
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

%description -l es
Fake es un utilitario que permite que otras maquinas en la red puedan
tomar direcciones IP. Este software fue desarrollado para permitir el
uso de servidores de copias de seguridad (backup) en una red local.

%description -l pl
Fake jest prostym narzêdziem pozwalaj±cym na w³±czanie zapasowych
serwerów w sieci. Na przyk³ad, mo¿e byæ u¿yty do w³±czenia zapasowego
serwera poczty, WWW, proxy w czasie zamierzonego lub niezamierzonego
nie dzia³ania podstawowego serwera. Fake dzia³a poprzez podnoszenie
dodatkowego interfejsu i spoofowanie adresu ARP aby przej±æ adres IP
innej maszyny w sieci lokalnej. Dodatkowy interfejs mo¿e byæ
interfejsem fizycznym lub logicznym (aliasem IP). Fake jest
konfigurowalny i mo¿e u¿ywaæ systemów automatycznie monitoruj±cych
dostêpno¶æ serwerów (np. Heartbeat lub Heart).

%description -l pt_BR
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
%doc README AUTHORS ChangeLog docs/{arp_fun,redundant_linux}.txt
%dir %{_sysconfdir}/fake
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/fake/.fakerc
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/fake/clear_routers
%dir %{_sysconfdir}/fake/instance_config
%config %{_sysconfdir}/fake/instance_config/203.12.97.7.cfg
%attr(755,root,root) %{_sbindir}/send_arp
%attr(755,root,root) %{_sbindir}/fake
%{_mandir}/man8/*
