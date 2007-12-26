# TODO
#  - config file, patches, package for not cacti plugin
%define		namesrc	weathermap
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - WeatherMap
Summary(pl.UTF-8):	Wtyczka do Cacti - WeatherMap
Name:		cacti-plugin-weathermap
Version:	0.941
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.network-weathermap.com/files/php-%{namesrc}-%{version}.zip
# Source0-md5:	8214a2a323db250ac3b783fc5674b163
URL:		http://www.network-weathermap.com
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - Weathermap - is a network visualisation tool, to
take data you already have and show you an overview of your network
in map form.

Support is built in for RRD, MRTG (RRD and old log-format), and
tab-delimited text files. Other sources are via plugins or external
scripts.

%description -l pl.UTF-8
Wtyczka do Cacti - Weathermap

%prep
%setup -q -n %{namesrc}

# undos the source
find '(' -name '*.php' -o -name '*.inc' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -a * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%{webcactipluginroot}
