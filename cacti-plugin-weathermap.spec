# TODO
#  - config file, patches, package for not cacti plugin
#  - system vera ttf fonts, jquery
%define		plugin	weathermap
%define		php_min_version 5.2.0
Summary:	Plugin for Cacti - WeatherMap
Summary(pl.UTF-8):	Wtyczka do Cacti - WeatherMap (mapa pogody)
Name:		cacti-plugin-weathermap
Version:	0.97a
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.network-weathermap.com/files/php-%{plugin}-%{version}.zip
# Source0-md5:	7eb70243fef163721423b3e87d7e84b4
URL:		http://www.network-weathermap.com/
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.554
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	cacti
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(gd)
Requires:	php(mysql)
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

# provided by package itself
%define		_noautopear	pear(HTML_ImageMap.class.php) pear(Weathermap.class.php) pear(editor-config.php) pear(editor.inc.php)

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
Weathermap plugin for Cacti is a network visualisation tool, to take
data you already have and show you an overview of your network in map
form.

Support is built in for RRD, MRTG (RRD and old log-format), and
tab-delimited text files. Other sources are via plugins or external
scripts.

%description -l pl.UTF-8
Wtyczka Weathermap dla Cacti to narzędzie do wizualizacji sieci,
pobierające już istniejące dane i tworzące widok sieci w postaci mapy.

Ma wbudowaną obsługę plików RRD, MRTG (RRD i starego formatu logów)
oraz tekstowych rozdzielonych tabulacjami. Inne źródła są dostępne
przez wtyczki lub zewnętrzne skrypty.

%prep
%setup -qc

%undos -f php,inc

# fix php path
%{__sed} -i -e '1s,#!.*bin/php,#!%{_bindir}/php,' %{plugin}/%{plugin}

mv %{plugin}/editor-config.php{-dist,}

# in docs
mv %{plugin}/{CHANGES,COPYING,README} .
mv %{plugin}/docs .

# junk not neccessary for plugin run
mv %{plugin}/random-bits .
mv %{plugin}/net-data.txt .
mv %{plugin}/convert-to-dsstats.php .
rm -rf %{plugin}/output

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}/output
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%{plugindir}
