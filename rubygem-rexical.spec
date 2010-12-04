%define oname rexical

Summary:    Rexical is a lexical scanner generator
Name:       rubygem-%{oname}
Version:    1.0.4
Release:    %mkrel 1
Group:      Development/Ruby
License:    LGPLv2
URL:        http://github.com/tenderlove/rexical/tree/master
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Requires:   rubygem(hoe) >= 2.3.1
BuildRequires: rubygems
BuildArch:  noarch
Provides: rubygem(%{oname}) = %{version}

%description
Rexical is a lexical scanner generator.
It is written in Ruby itself, and generates Ruby program.
It is designed for use with Racc.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

sed -i 's!#!.*!#!/usr/bin/env ruby' %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/test/rex*

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/rex
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/sample/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.ja
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Manifest.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CHANGELOG.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/DOCUMENTATION.en.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/DOCUMENTATION.ja.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.rdoc
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
