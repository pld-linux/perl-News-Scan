%include	/usr/lib/rpm/macros.perl
%define	pdir	News
%define	pnam	Scan
Summary:	News::Scan perl module
Summary(pl):	Modu³ perla News::Scan
Name:		perl-News-Scan
Version:	0.52
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-MailTools
BuildRequires:	perl-TimeDate
BuildRequires:	perl-libnet
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
News::Scan - Perl Compiler backend to statistic News.

%description -l pl
Modu³ perla do prowadzenia statystyk News.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/News/Scan.pm
%{perl_sitelib}/News/Scan
%{_mandir}/man3/*
