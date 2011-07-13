#
# spec file for package rubygem-restility
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild
Name:           rubygem-restility
Version:        0.0.1
Release:        0
%define mod_name restility
#
Group:          Development/Languages/Ruby
License:        GPLv2

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  rubygems_with_buildroot_patch
Requires:       rubygems >= 1.2.0

BuildRequires:  rubygem-rake
Requires:	rubygem-rake

# this actually doesn't work, but it is specified in the gem
# so it is used also here...
Url:            http://restility.rubyforge.org

Source:         %{mod_name}-%{version}.gem

Summary:        Utilities for writing REST web services
%description
The package contains rest_doc utility for generating documentation
for a REST API and rest_test utility for testing REST API.

%prep
%build
%install
%gem_install %{S:0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/ruby/gems/%{rb_ver}/cache/%{mod_name}-%{version}.gem
%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_name}-%{version}/
%{_libdir}/ruby/gems/%{rb_ver}/specifications/%{mod_name}-%{version}.gemspec
%doc %{_libdir}/ruby/gems/%{rb_ver}/doc/%{mod_name}-%{version}/
/usr/bin/rest_doc
/usr/bin/rest_test


%changelog
