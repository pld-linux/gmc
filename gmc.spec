#
# Conditional build:
%bcond_without	gnome		# without GNOME support
%bcond_with	ext2undel	# with ext2 undelete fs
%bcond_with	samba		# with SAMBA vfs support
%bcond_with	x		# with text edit in X support
%bcond_with	mo		# alters the M-o functionality
#
Summary:	A user-friendly file manager and visual shell
Summary(de.UTF-8):	Visuelle Shell Midnight Commander
Summary(es.UTF-8):	Interpretador de comandos visual Midnight Commander
Summary(fr.UTF-8):	Un gestionnaire de fichiers puissant et agréable en mode console
Summary(ja.UTF-8):	使いやすいファイルマネージャとビジュアルシェル
Summary(pl.UTF-8):	Midnight Commander - powłoka wizualna
Summary(pt_BR.UTF-8):	Interpretador de comandos visual Midnight Commander
Summary(ru.UTF-8):	Диспетчер файлов Midnight Commander
Summary(tr.UTF-8):	Midnight Commander görsel kabuğu
Summary(uk.UTF-8):	Диспетчер файлів Midnight Commander
Summary(zh_CN.UTF-8):	一个方便实用的文件管理器和虚拟Shell
Name:		mc
Version:	4.5.55
Release:	12
License:	GPL
Group:		Applications/Shells
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/mc/4.5/%{name}-%{version}.tar.gz
# Source0-md5:	bb670d48589f26f00b7fce8d25f66bd6
Source1:	%{name}serv.pamd
Source2:	%{name}serv.init
Source3:	%{name}-non-english-man-pages.tar.bz2
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5:	17d7b574e1b85ad6f8ddceda9e841f19
Source4:	%{name}-srpm
Patch0:		%{name}-mimekeys.patch
Patch1:		%{name}-rpmfs.patch
Patch2:		%{name}-system_popt.patch
Patch3:		%{name}-spec-syntax.patch
Patch4:		%{name}-gdeskpopt.patch
Patch5:		%{name}-prototype.patch
Patch6:		%{name}-gnome-editor.patch
Patch7:		%{name}-def_config.patch
Patch8:		%{name}-mouse_in_rxvt.patch
Patch9:		%{name}-proxy.patch
Patch10:	%{name}-nognome-amfix.patch
Patch11:	%{name}-urar.patch
Patch12:	%{name}-samba.patch
Patch13:	%{name}-nobashism.patch
Patch14:	%{name}-tinfo.patch
Patch15:	%{name}-vfs.patch
Patch16:	%{name}-mo.patch
Patch17:	%{name}-%{name}.ext-ear_war.patch
Patch18:	%{name}-home_etc.patch
Patch19:	%{name}-tmout.patch
Patch20:	%{name}-new_icons_am.patch
Patch21:	%{name}-pl.patch
Patch22:	%{name}-zh.patch
URL:		http://www.gnome.org/mc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	indent
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pam-devel
BuildRequires:	popt-devel
%ifnarch s390 s390x
BuildRequires:	gpm-devel
%endif
%{?with_gnome:BuildRequires:	ORBit-devel}
%{?with_x:BuildRequires:	XFree86-devel}
%{?with_ext2undel:BuildRequires:	e2fsprogs-devel}
%{?with_gnome:BuildRequires:	gnome-libs-devel >= 1.2.13}
%{?with_gnome:BuildRequires:	imlib-devel}
Requires:	file
Obsoletes:	tkmc
Conflicts:	rpm < 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
Midnight Commander is a visual shell much like a file manager, only
with way more features. It is text mode, but also includes mouse
support if you are running GPM. Its coolest feature is the ability to
FTP, view tar, zip files, and poke into RPMs for specific files. :-)

%description -l de.UTF-8
Midnight Commander ist ein Visual-Shell, ähnlich einem Dateimanager,
aber mit zusätzlichen Funktionen. Es läuft im Textmodus, kann jedoch
eine Maus unterstützen, wenn GPM betrieben wird. Seine coolsten
Fähigkeiten sind die FTP-Option, das Einsehen von tar- und zip-Dateien
und das Herausfischen von spezifischen Dateien aus RPMs.

%description -l es.UTF-8
Midnight Commander es un interpretador de comandos visual que más
parece un administrador de archivos, solamente con varias
características a más. Es un programa en modo texto, pero incluye
soporte para ratón, si estuviera ejecutando GPM o en una ventana
xterm. Su característica más genial es la habilidad de cotillear en
RPMs buscando archivos específicos. :-)

%description -l fr.UTF-8
Midnight Commander est une interface pour la ligne de commande qui
tient beaucoup du gestionnaire de fichiers, mais est bien plus
puissant. Il fonctionne en mode console (texte), mais peut être
contrôlé à la souris si GPM est présent. Ses caractéristiques les plus
remarquables sont la possibilité de se connecter à un serveur FTP, de
visualiser des archives tar, de compresser des fichiers avec zip, de
récupérer des fichiers dans les packages RPM, et tout ceci simplement.

%description -l ja.UTF-8
Midnight Commander はいろいろな機能を持ったファイルマネージャ兼
ビジュアルシェルです。これはテキストモードのアプリケーションですが、
GPM を使っている場合、マウスが使えます。 Midnight Commander には、 FTP
に接続できたり、 tar や zip や RPM の中が見えるなど、クールな機能
があります。

%description -l pl.UTF-8
Midnight Commander jest wizualną powłoką podobną do Norton Commandera.
Pracuje w trybie tekstowym, ale ma także wspomaganie dla myszki. Jest
super ;) MC ma wbudowanego klienta FTP, może zaglądać do
skompresowanego archiwum tarowego, do *.zip oraz *.rpm. Teraz również
pracuje z urządzeniami /dev/pts/{0-2048} - standard Unix98.

%description -l pt_BR.UTF-8
Midnight Commander é um interpretador de comandos visual que mais
parece um gerenciador de arquivos, somente com várias características
a mais. Ele é um programa de modo texto, mas inclui suporte para mouse
se você estiver rodando GPM ou em uma janela xterm. Sua característica
mais legal é a habilidade de bisbilhotar em RPMs procurando arquivos
específicos. :-)

%description -l tr.UTF-8
Midnight Commander bir dosya yöneticisine çok benzeyen ancak daha
yetenekli bir görsel kabuktur. Metin ekranda çalışır ve GPM
çalışıyorsa fare desteği vardır. En hoş özellikleri FTP yapabilmesi,
tar, zip ve RPM dosyalarının içeriklerini gösterebilmesidir.

%package -n mcserv
Summary:	Server for the Midnight Commander network file management system
Summary(de.UTF-8):	Midnight Commander File-Server
Summary(es.UTF-8):	Servidor de archivos del Midnight Commander
Summary(fr.UTF-8):	Serveur réseau pour le gestionnaire de fichiers Midnight Commander
Summary(ja.UTF-8):	Midnight Commander でネットワークファイルマネージメントを行うサーバ
Summary(pl.UTF-8):	Serwer plików Midnight Commandera
Summary(pt_BR.UTF-8):	Servidor de arquivos do Midnight Commander
Summary(ru.UTF-8):	Midnight Commander файл-сервер
Summary(tr.UTF-8):	Midnight Commander dosya sunucusu
Summary(uk.UTF-8):	Midnight Commander файл-сервер
Summary(zh_CN.UTF-8):	mc 网络文件管理系统的服务器。
Group:		Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	pam >= 0.66
Requires:	portmap
Requires:	rc-scripts >= 0.4.1.5

%description -n mcserv
The Midnight Commander file management system will allow you to
manipulate the files on a remote machine as if they were local. This
is only possible if the remote machine is running the mcserv server
program. Mcserv provides clients running Midnight Commander with
access to the host's file systems.

%description -n mcserv -l de.UTF-8
mcserv ist das Server-Programm für das Netzwerkdateisystem Midnight
Commander. Es ermöglicht den Zugriff auf das Host-Dateisystem für
Clients, die das Midnight-Dateisystem ausführen (z.Zt. nur Midnight
Commander file manager).

%description -n mcserv -l es.UTF-8
Mcserv es un servidor para el sistema de archivos en red del Midnight
Commander. Permite que clientes usando el mc accedan remotamente al
sistema de archivos de la máquina en que está ejecutando.

%description -n mcserv -l fr.UTF-8
Le système de gestion de fichier Midnight Commander vous permet de
manipuler des fichiers sur une machine distante comme si ils étaient
sur votre propre machine. Ceci est possible seulement si la machine
distante possède le programme mcserv et que celui-ci est activé.
Mcserv apporte aux machines clientes qui font tourner Midnight
Commander un accès aux fichiers situés sur l'hôte.

%description -l ja.UTF-8
Midnight Commander
のファイル管理システムは、リモートマシンにあるファイルを
ローカルにあるかのように扱うことができます。この機能は mcserv
プログラムを 実行しているリモートマシンに対してのみ働きます。 Mcserv
は Midnight Commander
クライアントに対して、このホストのファイルシステムを提供します。

%description -n mcserv -l pl.UTF-8
Mcserv jest aplikacją dla sieciowego systemy plików Midnight
Commandera. Pozwala na dostęp do systemu plików dla klienta
pracującego pod MC i używającego jego systemu plików.

%description -n mcserv -l pt_BR.UTF-8
Mcserv é um servidor para o sistema de arquivos em rede do Midnight
Commander. Ele permite que clientes usando o mc acessem remotamente o
sistema de arquivos da máquina em que está rodando.

%description -n mcserv -l ru.UTF-8
mcserv - это серверная программа для сетевой файловой системы Midnight
Commander. Она обеспечивает доступ к удаленной файловой системе
клиентам, поддерживающим файловую систему Midnight Commander (в
настоящее время только собственно Midnight Commander).

%description -n mcserv -l tr.UTF-8
mcserv, Midnight Commander ağ dosya sisteminin sunucu programıdır.
Midnight dosya sistemini çalıştıran istemcilerin sunucu dosya
sistemine erişimini sağlar.

%description -n mcserv -l uk.UTF-8
mcserv - це серверна програма для мережевої файлової системи Midnight
Commander. Вона забезпечує доступ до віддаленої файлової системи
клієнтам, що підтримують файлову систему Midnight Commander (наразі
тільки власне Midnight Commander).

%package -n gmc
Summary:	Midnight Commander visual shell (GNOME version)
Summary(de.UTF-8):	Midnight Commander Visual-Shell (GNOME Version)
Summary(es.UTF-8):	Shell visual Midnight Commander (Versión GNOME)
Summary(fr.UTF-8):	Version GNOME du gestionnaire de fichiers Midnight Commander
Summary(ja.UTF-8):	GNOME 用 Midnight Commander ファイルマネージャ
Summary(pl.UTF-8):	Midnight Commander - wizualna powłoka (wersja GNOME)
Summary(pt_BR.UTF-8):	Shell visual Midnight Commander (Versão GNOME)
Summary(ru.UTF-8):	GNOME версия файлового менеджера Midnight Commander
Summary(tr.UTF-8):	Midnight Commander görsel kabuğu (GNOME sürümü)
Summary(uk.UTF-8):	GNOME версія файлового менеджера Midnight Commander
Summary(zh_CN.UTF-8):	GNOME 下的 MC 版本
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description -n gmc
Midnight Commander is a visual shell much like a file manager, only
with way more features. This is the GNOME version. It's coolest
feature is the ability to FTP, view tar, zip files and poke into RPMs
for specific files. The GNOME version of Midnight Commander is not yet
finished though. :-(

%description -n gmc -l es.UTF-8
Midnight Commander es un interpretador de comandos visual, muy
parecido con un administrador de archivos, solamente que con _muchas_
otras capacidades. Una de sus características más interesantes es su
habilidad para conectarse a servidores FTP, visualizar archivos tar,
zip y rpms.

%description -n gmc -l fr.UTF-8
Midnight Commander est une interface pour la ligne de commande qui
tient beaucoup du gestionnaire de fichiers, mais est bien plus
puissant. Ceci est la version pour GNOME. Ses caractéristiques les
plus remarquables sont la possibilité de se connecter à un serveur
FTP, de visualiser des archives tar, de compresser des fichiers avec
zip, et de récupérer des fichiers dans les packages RPM. La version
GNOME de Midnight Commander n'est pas encore terminée cependant. :-(

%description -l ja.UTF-8
GMC (GNU Midnight Commander) は、ターミナル版の Midnight Commanderを
元にした GNOME GUI デスクトップを実現するファイルマネージャです。 GMC
は FTP に接続できたり、 tar や zip や RPM の中を見たりすることが
できます。

%description -n gmc -l pl.UTF-8
Midnight Commander jest wizualną powłoką, posiadającą znacznie więcej
funkcji niż samo zarządzanie plikami. Ma wbudowanego klienta FTP,
potrafi przeglądać pliki tar, zip oraz sięgać do konkretnych plików
pakietów rpm. To jest wersja pracująca pod GNOME. Niestety nie jest
ona jeszcze skończona.

%description -n gmc -l pt_BR.UTF-8
Midnight Commander é um interpretador de comandos visual, muito
parecido com um gerenciador de arquivos, somente com _muitas_ outras
capacidades. Uma de suas características mais interessantes é sua
habilidade de conectar-se a servidores FTP, visualizar arquivos tar,
zip e rpms.

%description -n gmc -l ru.UTF-8
GMC (GNU Midnight Commander) - это файловый менеджер, основанный на
терминальной версии Midnight Commander и добавляющий к нему
графический интерфейс десктопа GNOME.

%description -n gmc -l uk.UTF-8
GMC (GNU Midnight Commander) - це файловий менеджер, що базується на
термінальній версії Midnight Commander та додає до нього графічний
інтерфейс десктопу GNOME.

%prep
%setup -q -a3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%{?with_mo:%patch16 -p1}
%patch17 -p1
#%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1

mv -f po/zh_CN{.GB2312,}.po
mv -f po/zh_TW{.Big5,}.po

%build
%{__gettextize}
%{__aclocal} -I \
	%{?with_gnome:%{_aclocaldir}/gnome}%{!?with_gnome:macros}
%{__autoconf}
%{__automake}
X11_WWW="
if [ -f /usr/X11R6/bin/netscape ]; then
	netscape;
else
	if [ -f /usr/X11R6/bin/galeon ]; then
		galeon
	else
		if [ -f /usr/X11R6/bin/mozilla ]; then
			mozilla
		else
			xterm -c lynx
		fi;
	fi;
fi"
%configure \
	%{?with_ext2undel:--with-ext2-undel}%{!?with_ext2undel:--without-ext2undel} \
	--with-vfs \
	--with-netrc \
	--with-x \
	%{?with_x:--with-tm-x-support} \
	--without-debug \
	--with-included-slang \
	--enable-largefile \
	--enable-mcserv-install \
	%{?with_gnome:--with-gnome}%{!?with_gnome:--without-gnome} \
	%{?with_samba:--with-samba}

%{__make} confdir=%{_sysconfdir}/

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/{rc.d/init.d,pam.d,profile.d}}

%{__make} install \
	confdir=%{_sysconfdir} \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/mcserv
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/mcserv

for a in es pl ; do
	for b in man1 man8 ; do
		install -d $RPM_BUILD_ROOT%{_mandir}/{$a,$a/$b}
		for c in man/$a/$b/* ; do
			install $c $RPM_BUILD_ROOT%{_mandir}/$a/$b
		done
	done
done

install %{SOURCE4} $RPM_BUILD_ROOT%{_libdir}/mc/extfs/srpm

install lib/{mc.sh,mc.csh} $RPM_BUILD_ROOT/etc/profile.d

mv -f $RPM_BUILD_ROOT%{_bindir}/mcserv $RPM_BUILD_ROOT%{_sbindir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n mcserv
/sbin/chkconfig --add mcserv
if [ -f /var/lock/subsys/mcserv ]; then
	/etc/rc.d/init.d/mcserv restart >&2
else
	echo "Run \"/etc/rc.d/init.d/mcserv start\" to start mcserv daemon."
fi

%preun -n mcserv
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/mcserv ]; then
		/etc/rc.d/init.d/mcserv stop >&2
	fi
	/sbin/chkconfig --del mcserv
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc FAQ NEWS README

%attr(755,root,root) %{_bindir}/mc*

%{_libdir}/mc/mc.ext

%{_libdir}/mc/mc.hlp
%lang(hu) %{_libdir}/mc/mc.hlp.hu
%{_libdir}/mc/mc.lib
%{_libdir}/mc/mc.menu
%{_libdir}/mc/mc.hint
%lang(cs) %{_libdir}/mc/mc.hint.cs
%lang(es) %{_libdir}/mc/mc.hint.es
%lang(hu) %{_libdir}/mc/mc.hint.hu
%lang(it) %{_libdir}/mc/mc.hint.it
%lang(nl) %{_libdir}/mc/mc.hint.nl
%lang(pl) %{_libdir}/mc/mc.hint.pl
%lang(ru) %{_libdir}/mc/mc.hint.ru
%lang(uk) %{_libdir}/mc/mc.hint.uk
%lang(zh) %{_libdir}/mc/mc.hint.zh

%attr(755,root,root) %{_libdir}/mc/bin/cons.saver

%{_libdir}/mc/extfs/README
%attr(755,root,root) %{_libdir}/mc/extfs/a
%attr(755,root,root) %{_libdir}/mc/extfs/apt
%attr(755,root,root) %{_libdir}/mc/extfs/audio
%attr(755,root,root) %{_libdir}/mc/extfs/bpp
%attr(755,root,root) %{_libdir}/mc/extfs/deb*
%attr(755,root,root) %{_libdir}/mc/extfs/dpkg
%attr(755,root,root) %{_libdir}/mc/extfs/ftplist
%attr(755,root,root) %{_libdir}/mc/extfs/hp48
%attr(755,root,root) %{_libdir}/mc/extfs/lslR
%attr(755,root,root) %{_libdir}/mc/extfs/mailfs
%attr(755,root,root) %{_libdir}/mc/extfs/patchfs
%attr(755,root,root) %{_libdir}/mc/extfs/rpm*
%attr(755,root,root) %{_libdir}/mc/extfs/trpm
%attr(755,root,root) %{_libdir}/mc/extfs/uar*
%attr(755,root,root) %{_libdir}/mc/extfs/ucpio
%attr(755,root,root) %{_libdir}/mc/extfs/uha
%attr(755,root,root) %{_libdir}/mc/extfs/ulha
%attr(755,root,root) %{_libdir}/mc/extfs/urar
%attr(755,root,root) %{_libdir}/mc/extfs/uzip
%attr(755,root,root) %{_libdir}/mc/extfs/uzoo
%attr(755,root,root) %{_libdir}/mc/extfs/srpm
%{_libdir}/mc/extfs/extfs.ini
%{_libdir}/mc/extfs/sfs.ini
%{_libdir}/mc/syntax

%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%attr(755,root,root) %config /etc/profile.d/*

%dir %{_libdir}/mc
%dir %{_libdir}/mc/bin
%dir %{_libdir}/mc/extfs

%files -n mcserv
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/*

%attr(754,root,root) %config /etc/rc.d/init.d/mcserv
%{_mandir}/man8/mcserv.8*
%lang(es) %{_mandir}/es/man8/mcserv.8*
%lang(pl) %{_mandir}/pl/man8/mcserv.8*
%attr(755,root,root) %{_sbindir}/mcserv

%{?with_gnome:%files -n gmc}
%{?with_gnome:%defattr(644,root,root,755)}

%{?with_gnome:%attr(755,root,root) %{_bindir}/gdesktoplnk}
%{?with_gnome:%attr(755,root,root) %{_bindir}/gmc*}
%{?with_gnome:%attr(755,root,root) %{_bindir}/plain-gmc}

%{?with_gnome:%{_sysconfdir}/mc.global}
%{?with_gnome:%{_sysconfdir}/CORBA/servers/gmc.gnorba}
%{?with_gnome:%{_datadir}/mime-info}
%{?with_gnome:%{_pixmapsdir}}
%{?with_gnome:%{_datadir}/mc}
