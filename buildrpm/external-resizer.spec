{{{$version := printf "%s.%s.%s" .major .minor .patch }}}

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global app_name                external-resizer
%global app_name_release        csi-resizer
%global app_version             {{{$version}}}
%global oracle_release_version  1
%global _buildhost              build-ol%{?oraclelinux}-%{?_arch}.oracle.com

Name:           %{app_name}
Version:        %{app_version}
Release:        %{oracle_release_version}%{?dist}
Summary:        Sidecar container that watches the Kubernetes API server for PersistentVolumeClaim updates and triggers ControllerExpandVolume operations against a CSI endpoint if user requested more storage on PersistentVolumeClaim object.
License:        Apache 2.0
Group:          Development/Tools
Url:            https://github.com/oracle-cne/external-resizer.git
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  golang
BuildRequires:	make

%description
Sidecar container that watches the Kubernetes API server for PersistentVolumeClaim updates and triggers ControllerExpandVolume operations against a CSI endpoint if user requested more storage on PersistentVolumeClaim object.

%prep
%setup -q

%build
make build

%install
install -m 755 bin/%{app_name_release} %{buildroot}/%{app_name_release}

%files
%license LICENSE olm/SECURITY.md
/%{app_name_release}

%changelog
* {{{.changelog_timestamp}}} - {{{$version}}}-1
- Added Oracle specific build files for CSI external-resizer.

