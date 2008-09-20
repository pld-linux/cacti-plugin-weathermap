# TODO
#  - config file, patches, package for not cacti plugin
%define		namesrc	weathermap
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - WeatherMap
Summary(pl.UTF-8):	Wtyczka do Cacti - WeatherMap (mapa pogody)
Name:		cacti-plugin-weathermap
Version:	0.95b
Release:	2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.network-weathermap.com/files/php-%{namesrc}-%{version}.zip
# Source0-md5:	6481970ad971dfe659eed535b440e678
URL:		http://www.network-weathermap.com
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

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
%setup -q -n %{namesrc}

# undos the source
find '(' -name '*.php' -o -name '*.inc' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

# fix php path
%{__sed} -i -e '1s,#!.*bin/php,#!%{_bindir}/php,' %{namesrc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -a . $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%{webcactipluginroot}
