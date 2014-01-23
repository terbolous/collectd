%define debug_package %{nil}

Summary:	   Statistics collection daemon for filling RRD files.
Name:		   collectd
Version:	   5.4.0
Release:	   1%{?dist}
Source:		   http://collectd.org/files/%{name}-%{version}.tar.gz
License:	   GPL
Group:		   System Environment/Daemons
BuildRoot:	   %{_tmppath}/%{name}-%{version}-root
BuildRequires:     libpcap-devel, libstatgrab-devel
BuildRequires:     libxml2-devel, libiptcdata-devel, iptables-devel
BuildRequires:     curl-devel,libidn-devel,openssl-devel
BuildRequires:     libesmtp-devel, ganglia-devel, libgcrypt-devel
BuildRequires:     yajl-devel, lvm2-devel
Requires:	   libstatgrab
Vendor:		   collectd development team <collectd@verplant.org>


%description
collectd is a small daemon which collects system information periodically and
provides mechanisms to monitor and store the values in a variety of ways. It
is written in C for performance. Since the daemon doesn't need to startup
every time it wants to update the values it's very fast and easy on the
system. Also, the statistics are very fine grained since the files are updated
every 10 seconds.


%package apache
Summary:	apache-plugin for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}, curl
%description apache
This plugin collects data provided by Apache's `mod_status'.

%package collection3
Summary:	Perl CGI webfrontend for collectd
Group:		System Environment/Daemons
Requires:	collectd = %{version}, perl(Regexp::Common)
%description collection3
collection3 is a graphing front-end for the RRD files created by and filled
with collectd. It is written in Perl and should be run as an CGI-script.
Graphs are generated on-the-fly, so no cron job or similar is necessary.

%package contrib
Summary:	All the stuff from the contrib directory
Group:		System Environment/Daemons
Requires:	collectd = %{version}, perl(Regexp::Common)
BuildRequires: perl(Mail::SpamAssassin::Logger), perl(Mail::SpamAssassin::Plugin)
%description contrib
This package contains all the stuff from the contrib packages.

%package dbi
Summary:	dbi-module for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}, libdbi
BuildRequires: libdbi-devel
%description dbi
DBI query plugin for interactive queries for collectd.

%package email
Summary:	email-plugin for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}, spamassassin
%description email
This plugin collects data provided by spamassassin.

%package gmond
Summary:	gmond-plugin for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}
BuildRequires: ganglia-devel
%description gmond
This plugin provides access to gmond, the ganglia monitoring
daemon.

%package java
Summary:	java-module for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}, java >= 1:1.6.0, jpackage-utils
BuildRequires: java-devel >= 1.6.0 , java >= 1.6.0, jpackage-utils
%description java
This plugin for collectd allows plugins to be written in Java and executed
in an embedded JVM.

%package liboping
Summary:	liboping-module for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}, liboping
BuildRequires: liboping-devel
%description liboping
liboping support für collectd

%package libnotify
Summary:	libnotify-module for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}, libnotify
BuildRequires: libnotify-devel
%description libnotify
libnotify plugin for collectd

%package libvirt
Summary:	libvirt-module for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}, libvirt
BuildRequires: libvirt-devel
%description libvirt
libvirt plugin for collectd.

%package memcache
Summary:	memcache-modules for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}
BuildRequires: memcached-devel, libmemcached-devel
%description memcache
Memcache plugins for collectd.

%package mysql
Summary:	mysql-module for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}, mysql
BuildRequires: mysql-devel
%description mysql
MySQL querying plugin. This plugins provides data of issued commands, called
handlers and database traffic.

%package nginx
Summary:	nginx-plugin for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}, curl
%description nginx
This plugin gets data provided by nginx.

%package OpenIPMI
Summary:	OpenIPMI-plugin for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}
BuildRequires: OpenIPMI-devel
%description OpenIPMI
OpenIPMI plugin for collectd

%package perl
Summary:	perl-plugin for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}
BuildRequires: perl-devel, perl(ExtUtils::MakeMaker), perl(ExtUtils::Embed)
%description perl
The Perl plugin embeds a Perl interpreter into collectd and provides an
interface to the collectd's plugin system. This makes it possible to write
collectd plugins in the Perl language.

%package php-collection
Summary:	PHP webfrontend for collectd
Group:		System Environment/Daemons
Requires:	collectd = %{version}, php
%description php-collection
php-collection is a graphing front-end for the RRD files created by and filled
with collectd. It is written in PHP.  Graphs are generated on-the-fly, so no
cron job or similar is necessary.

%package python
Summary:	python-plugin for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}
BuildRequires: python-devel
%description python
The python plugin embeds a python interpreter into collectd and provides an
interface to the collectd's plugin system. This makes it possible to write
collectd plugins in the python language.

%package rrdtool
Summary:	rrd-plugin for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}, rrdtool
BuildRequires: rrdtool-devel
%description rrdtool
This plugin provides the data backend for collectd to write to rrd databases.


%package postgresql
Summary:	postgresql-plugin for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}, postgresql
BuildRequires: postgresql-devel
%description postgresql
This plugin gets data provided by postgresql

%package sensors
Summary:	libsensors-module for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}, lm_sensors
BuildRequires: lm_sensors-devel
%description sensors
This plugin for collectd provides querying of sensors supported by lm_sensors.

%package snmp
Summary:	snmp-module for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}, net-snmp
BuildRequires: net-snmp-devel
%description snmp
This plugin for collectd allows querying of network equipment using SNMP.

%package varnish
Summary:	varnish-module for collectd.
Group:		System Environment/Daemons
Requires:	collectd = %{version}
BuildRequires: varnish-libs-devel
%description varnish
Varnish plugin for collectd


%prep
rm -rf %{buildroot}
%setup

%build
%configure --with-java=/usr/lib/jvm/java-1.6.0-openjdk-1.6.0.0.x86_64 --enable-java --disable-battery
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}/etc/rc.d/init.d %{buildroot}/usr/share %{buildroot}/var/www/cgi-bin
mkdir -p %{buildroot}/%{_docdir}
cp -r contrib %{buildroot}/%{_docdir}/
cp contrib/redhat/init.d-collectd $RPM_BUILD_ROOT/etc/rc.d/init.d/collectd
mkdir -p %{buildroot}/etc/collectd.d
mkdir -p %{buildroot}/var/lib/collectd
mv contrib/collection3 %{buildroot}/var/www/cgi-bin/
mv contrib/php-collection %{buildroot}/usr/share/
### Clean up docs
find contrib/ -type f -exec %{__chmod} a-x {} \;

###Modify Config for Redhat Based Distros
sed -i 's:#BaseDir     "/usr/var/lib/collectd":BaseDir     "/var/lib/collectd":' $RPM_BUILD_ROOT/etc/collectd.conf
sed -i 's:#PIDFile     "/usr/var/run/collectd.pid":PIDFile     "/var/run/collectd.pid":' $RPM_BUILD_ROOT/etc/collectd.conf
sed -i 's:#PluginDir   "/usr/lib/collectd":PluginDir   "%{_libdir}/collectd":' $RPM_BUILD_ROOT/etc/collectd.conf
sed -i 's:#TypesDB     "/usr/share/collectd/types.db":TypesDB     "/usr/share/collectd/types.db":' $RPM_BUILD_ROOT/etc/collectd.conf
sed -i 's:#Interval     10:Interval     30:' $RPM_BUILD_ROOT/etc/collectd.conf
sed -i 's:#ReadThreads  5:ReadThreads  5:' $RPM_BUILD_ROOT/etc/collectd.conf
###Include broken out config directory
echo -e '\nInclude "/etc/collectd.d"' >> $RPM_BUILD_ROOT/etc/collectd.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add collectd
/sbin/chkconfig collectd on

%preun
if [ "$1" = 0 ]; then
   /sbin/chkconfig collectd off
   /etc/init.d/collectd stop
   /sbin/chkconfig --del collectd
fi
exit 0

%postun
if [ "$1" -ge 1 ]; then
    /etc/init.d/collectd restart
fi
exit 0

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%config %attr(0644,root,root) /etc/collectd.conf
%attr(0755,root,root) /etc/rc.d/init.d/collectd
%attr(0755,root,root) %{_sbindir}/collectd
%attr(0755,root,root) %{_bindir}/collectd-nagios
%attr(0755,root,root) %{_bindir}/collectdctl
%attr(0755,root,root) %{_bindir}/collectd-tg
%attr(0755,root,root) %{_sbindir}/collectdmon
%attr(0644,root,root) %{_mandir}/man1/*
%attr(0644,root,root) %{_mandir}/man5/*
%dir /etc/collectd.d

# client
%attr(0644,root,root) /usr/include/collectd/client.h
%attr(0644,root,root) /usr/include/collectd/lcc_features.h
%attr(0644,root,root) /usr/include/collectd/network.h
%attr(0644,root,root) /usr/include/collectd/network_buffer.h

%attr(0644,root,root) %{_libdir}/libcollectdclient.*
%attr(0644,root,root) %{_libdir}/pkgconfig/libcollectdclient.pc

# macro to grab binaries for a plugin, given a name
%define plugin_macro() \
%attr(0644,root,root) %{_libdir}/%{name}/%1.a \
%attr(0644,root,root) %{_libdir}/%{name}/%1.so* \
%attr(0644,root,root) %{_libdir}/%{name}/%1.la

%plugin_macro aggregation
%plugin_macro amqp
%plugin_macro apcups
%plugin_macro ascent
%plugin_macro bind
%plugin_macro cgroups
%plugin_macro conntrack
%plugin_macro contextswitch
%plugin_macro cpufreq
%plugin_macro cpu
%plugin_macro csv
%plugin_macro curl
%plugin_macro curl_json
%plugin_macro curl_xml
%plugin_macro df
%plugin_macro disk
%plugin_macro dns
%plugin_macro entropy
%plugin_macro email
%plugin_macro ethstat
%plugin_macro exec
%plugin_macro filecount
%plugin_macro fscache
%plugin_macro hddtemp
%plugin_macro interface
%plugin_macro iptables
%plugin_macro ipvs
%plugin_macro irq
%plugin_macro load
%plugin_macro logfile
%plugin_macro lvm
%plugin_macro madwifi
%plugin_macro match_empty_counter
%plugin_macro match_hashed
%plugin_macro match_regex
%plugin_macro match_timediff
%plugin_macro match_value
%plugin_macro mbmon
%plugin_macro md
%plugin_macro memory
%plugin_macro multimeter
%plugin_macro network
%plugin_macro nfs
%plugin_macro ntpd
%plugin_macro numa
%plugin_macro openvpn
%plugin_macro olsrd
%plugin_macro powerdns
%plugin_macro processes
%plugin_macro protocols
%plugin_macro serial
%plugin_macro statsd
%plugin_macro swap
%plugin_macro syslog
%plugin_macro table
%plugin_macro tail
%plugin_macro tail_csv
%plugin_macro target_notification
%plugin_macro target_replace
%plugin_macro target_scale
%plugin_macro target_set
%plugin_macro target_v5upgrade
%plugin_macro tcpconns
%plugin_macro teamspeak2
%plugin_macro ted
%plugin_macro thermal
%plugin_macro threshold
%plugin_macro unixsock
%plugin_macro uptime
%plugin_macro users
%plugin_macro uuid
%plugin_macro vmem
%plugin_macro vserver
%plugin_macro wireless
%plugin_macro write_http
%plugin_macro write_graphite

%attr(0644,root,root) %{_datadir}/%{name}/types.db
%exclude /usr/lib64/perl5/perllocal.pod
%dir /var/lib/collectd

%files apache
%plugin_macro apache

%files collection3
/var/www/cgi-bin/collection3

%files contrib
%{_docdir}/contrib*

%files dbi
%plugin_macro dbi

%files email
%attr(0644,root,root) %{_libdir}/%{name}/email.so*
%attr(0644,root,root) %{_libdir}/%{name}/email.la

%files gmond
%plugin_macro gmond

%files java
/usr/share/collectd/java/collectd-api.jar
/usr/share/collectd/java/generic-jmx.jar
%plugin_macro java

%files libvirt
%plugin_macro libvirt

%files libnotify
%plugin_macro notify_desktop
%plugin_macro notify_email

%files liboping
%plugin_macro ping

%files memcache
%plugin_macro memcachec
%plugin_macro memcached

%files mysql
%plugin_macro mysql

%files nginx
%plugin_macro nginx

%files OpenIPMI
%plugin_macro ipmi

%files perl
/usr/share/perl5/Collectd.pm
/usr/share/perl5/Collectd/Unixsock.pm
/usr/share/perl5/Collectd/Plugins/OpenVZ.pm
/usr/share/man/man3/Collectd::Unixsock.3pm.gz
/usr/lib64/perl5/auto/Collectd/.packlist
%plugin_macro perl

%files php-collection
/usr/share/php-collection

%files python
%plugin_macro python

%files postgresql
#%config %attr(0644,root,root) /etc/collectd.d/postgresql.conf
/usr/share/collectd/postgresql_default.conf
%plugin_macro postgresql

%files rrdtool
%plugin_macro rrdtool

%files sensors
#%attr(0644,root,root) %{_libdir}/%{name}/sensors.so*
#%attr(0644,root,root) %{_libdir}/%{name}/sensors.la
%plugin_macro sensors

%files snmp
%plugin_macro snmp

%files varnish
%plugin_macro varnish

%changelog
* Mon Aug 19 2013 Ulrich Habel <rhaen@pkgbox.de> 5.4.0-1
- updated to upstream 5.4.0
- enabled cgroups
- lvm2 support

* Fri May 10 2013 Ulrich Habel <me@rhaen.pm> 5.3.0-5
- fixed missing postgresql_default.conf query file
- fixed problem with name convention of rrd vs rrdtool
- split gmond/ganglia package

* Fri May 10 2013 Ulrich Habel <me@rhaen.pm> 5.3.0-4
- internal version

* Thu May 09 2013 Ulrich Habel <me@rhaen.pm> 5.3.0-3
- split into more subpackages

* Wed May 08 2013 Ulrich Habel <me@rhaen.pm> 5.3.0-2
- split into more subpackages

* Fri May 02 2013 Ulrich Habel <me@rhaen.pm> 5.3.0-1
- New upstream version

* Fri Mar 01 2013 Ulrich Habel <me@rhaen.pm> 5.2.1-2
- added libvirt support

* Fri Mar 01 2013 Ulrich Habel <me@rhaen.pm> 5.2.1-1
- New upstream version
- Dependency fixes
- spec file fixes
- Added postgresql support

* Tue Jan 03 2011 Monetate <jason.stelzer@monetate.com> 5.0.1
- New upstream version
- Changes to support 5.0.1

* Tue Jan 04 2010 Rackspace <stu.hood@rackspace.com> 4.9.0
- New upstream version
- Changes to support 4.9.0
- Added support for Java/GenericJMX plugin

* Mon Mar 17 2008 RightScale <support@rightscale.com> 4.3.1
- New upstream version
- Changes to support 4.3.1
- Added More Prereqs to support more plugins
- Added support for perl plugin

* Mon Aug 06 2007 Kjell Randa <Kjell.Randa@broadpark.no> 4.0.6
- New upstream version

* Wed Jul 25 2007 Kjell Randa <Kjell.Randa@broadpark.no> 4.0.5
- New major releas
- Changes to support 4.0.5

* Wed Jan 11 2007 Iain Lea <iain@bricbrac.de> 3.11.0-0
- fixed spec file to build correctly on fedora core
- added improved init.d script to work with chkconfig
- added %post and %postun to call chkconfig automatically

* Sun Jul 09 2006 Florian octo Forster <octo@verplant.org> 3.10.0-1
- New upstream version

* Tue Jun 25 2006 Florian octo Forster <octo@verplant.org> 3.9.4-1
- New upstream version

* Tue Jun 01 2006 Florian octo Forster <octo@verplant.org> 3.9.3-1
- New upstream version

* Tue May 09 2006 Florian octo Forster <octo@verplant.org> 3.9.2-1
- New upstream version

* Tue May 09 2006 Florian octo Forster <octo@verplant.org> 3.8.5-1
- New upstream version

* Fri Apr 21 2006 Florian octo Forster <octo@verplant.org> 3.9.1-1
- New upstream version

* Fri Apr 14 2006 Florian octo Forster <octo@verplant.org> 3.9.0-1
- New upstream version
- Added the `apache' package.

* Thu Mar 14 2006 Florian octo Forster <octo@verplant.org> 3.8.2-1
- New upstream version

* Thu Mar 13 2006 Florian octo Forster <octo@verplant.org> 3.8.1-1
- New upstream version

* Thu Mar 09 2006 Florian octo Forster <octo@verplant.org> 3.8.0-1
- New upstream version

* Sat Feb 18 2006 Florian octo Forster <octo@verplant.org> 3.7.2-1
- Include `tape.so' so the build doesn't terminate because of missing files..
- New upstream version

* Sat Feb 04 2006 Florian octo Forster <octo@verplant.org> 3.7.1-1
- New upstream version

* Mon Jan 30 2006 Florian octo Forster <octo@verplant.org> 3.7.0-1
- New upstream version
- Removed the extra `hddtemp' package

* Tue Jan 24 2006 Florian octo Forster <octo@verplant.org> 3.6.2-1
- New upstream version

* Fri Jan 20 2006 Florian octo Forster <octo@verplant.org> 3.6.1-1
- New upstream version

* Fri Jan 20 2006 Florian octo Forster <octo@verplant.org> 3.6.0-1
- New upstream version
- Added config file, `collectd.conf(5)', `df.so'
- Added package `collectd-mysql', dependency on `mysqlclient10 | mysql'

* Wed Dec 07 2005 Florian octo Forster <octo@verplant.org> 3.5.0-1
- New upstream version

* Sat Nov 26 2005 Florian octo Forster <octo@verplant.org> 3.4.0-1
- New upstream version

* Sat Nov 05 2005 Florian octo Forster <octo@verplant.org> 3.3.0-1
- New upstream version

* Tue Oct 26 2005 Florian octo Forster <octo@verplant.org> 3.2.0-1
- New upstream version
- Added statement to remove the `*.la' files. This fixes a problem when
  `Unpackaged files terminate build' is in effect.
- Added `processes.so*' to the main package

* Fri Oct 14 2005 Florian octo Forster <octo@verplant.org> 3.1.0-1
- New upstream version
- Added package `collectd-hddtemp'

* Fri Sep 30 2005 Florian octo Forster <octo@verplant.org> 3.0.0-1
- New upstream version
- Split the package into `collectd' and `collectd-sensors'

* Fri Sep 16 2005 Florian octo Forster <octo@verplant.org> 2.1.0-1
- New upstream version

* Mon Sep 10 2005 Florian octo Forster <octo@verplant.org> 2.0.0-1
- New upstream version

* Mon Aug 29 2005 Florian octo Forster <octo@verplant.org> 1.8.0-1
- New upstream version

* Sun Aug 25 2005 Florian octo Forster <octo@verplant.org> 1.7.0-1
- New upstream version

* Sun Aug 21 2005 Florian octo Forster <octo@verplant.org> 1.6.0-1
- New upstream version

* Sun Jul 17 2005 Florian octo Forster <octo@verplant.org> 1.5.1-1
- New upstream version

* Sun Jul 17 2005 Florian octo Forster <octo@verplant.org> 1.5-1
- New upstream version

* Mon Jul 11 2005 Florian octo Forster <octo@verplant.org> 1.4.2-1
- New upstream version

* Sat Jul 09 2005 Florian octo Forster <octo@verplant.org> 1.4-1
- Built on RedHat 7.3

