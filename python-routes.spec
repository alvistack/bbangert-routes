# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-routes
Epoch: 100
Version: 2.5.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Routing Recognition and Generation Tools
License: MIT
URL: https://github.com/bbangert/routes/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Routes is a Python re-implementation of the Rails routes system for
mapping URL’s to Controllers/Actions and generating URL’s. Routes makes
it easy to create pretty and concise URL’s that are RESTful with little
effort.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-routes
Summary: Routing Recognition and Generation Tools
Requires: python3
Requires: python3-six
Requires: python3-repoze.lru >= 0.3
Provides: python3-routes = %{epoch}:%{version}-%{release}
Provides: python3dist(routes) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-routes = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(routes) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-routes = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(routes) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-routes
Routes is a Python re-implementation of the Rails routes system for
mapping URL’s to Controllers/Actions and generating URL’s. Routes makes
it easy to create pretty and concise URL’s that are RESTful with little
effort.

%files -n python%{python3_version_nodots}-routes
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-routes
Summary: Routing Recognition and Generation Tools
Requires: python3
Requires: python3-six
Requires: python3-repoze.lru >= 0.3
Provides: python3-routes = %{epoch}:%{version}-%{release}
Provides: python3dist(routes) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-routes = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(routes) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-routes = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(routes) = %{epoch}:%{version}-%{release}

%description -n python3-routes
Routes is a Python re-implementation of the Rails routes system for
mapping URL’s to Controllers/Actions and generating URL’s. Routes makes
it easy to create pretty and concise URL’s that are RESTful with little
effort.

%files -n python3-routes
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version})
%package -n python3-routes
Summary: Routing Recognition and Generation Tools
Requires: python3
Requires: python3-six
Requires: python3-repoze-lru >= 0.3
Provides: python3-routes = %{epoch}:%{version}-%{release}
Provides: python3dist(routes) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-routes = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(routes) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-routes = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(routes) = %{epoch}:%{version}-%{release}

%description -n python3-routes
Routes is a Python re-implementation of the Rails routes system for
mapping URL’s to Controllers/Actions and generating URL’s. Routes makes
it easy to create pretty and concise URL’s that are RESTful with little
effort.

%files -n python3-routes
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%changelog