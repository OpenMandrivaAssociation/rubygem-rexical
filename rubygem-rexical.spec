# Generated from rexical-1.0.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	rexical

Summary:	Rexical is a lexical scanner generator
Name:		rubygem-%{rbname}

Version:	1.0.4
Release:	%mkrel 1
Group:		Development/Ruby
License:	GPLv2+ or Ruby                     
URL:		http://github.com/tenderlove/rexical/tree/master
Source0:	http://rubygems.org/gems//%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Rexical is a lexical scanner generator.
It is written in Ruby itself, and generates Ruby program.
It is designed for use with Racc.

%package	doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
rm -rf %{buildroot}
%gem_install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/rex
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/rex
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rexical
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rexical/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.txt
%doc %{ruby_gemdir}/doc/rexical-1.0.4

