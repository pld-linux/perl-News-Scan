%include	/usr/lib/rpm/macros.perl
Summary:	News-Scan perl module
Summary(pl):	Modu³ perla News-Scan
Name:		perl-News-Scan
Version:	0.51
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/News/News-Scan-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-TimeDate
BuildRequires:	perl-MailTools
BuildRequires:	perl-libnet
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
News-Scan - Perl Compiler backend to statistic News.

%description -l pl
Modu³ perla do prowadzenia statystyk News.

%prep
%setup -q -n News-Scan-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/News/Scan.pm
%{perl_sitelib}/News/Scan/*.pm
%{_mandir}/man3/*
