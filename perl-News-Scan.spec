#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network!)

%define		pdir	News
%define		pnam	Scan
Summary:	News::Scan perl module
Summary(pl.UTF-8):	Moduł Perla News::Scan
Name:		perl-News-Scan
Version:	0.53
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bd2583e134a98d38779acbb50987fb80
URL:		http://search.cpan.org/dist/News-Scan/
BuildRequires:	perl-MailTools
BuildRequires:	perl-TimeDate
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libnet
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
News::Scan - Perl Compiler backend to statistic News.

%description -l pl.UTF-8
Moduł Perla do prowadzenia statystyk News.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/News/Scan.pm
%{perl_vendorlib}/News/Scan
%{_mandir}/man3/*
