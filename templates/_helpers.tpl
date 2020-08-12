{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "persistence-query-service.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "persistence-query-service.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "persistence-query-service.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create DB node label.
*/}}
{{- define "db.node" -}}
{{- .Values.persdb.dbip -}}
{{- end -}}


{{/*
Create chart resource req and limits.
*/}}
{{- define "resources.requests.memory" -}}
{{- .Values.resources.requests.memory -}}
{{- end -}}

{{- define "resources.requests.cpu" -}}
{{- .Values.resources.requests.cpu -}}
{{- end -}}

{{- define "resources.limits.memory" -}}
{{- .Values.resources.limits.memory -}}
{{- end -}}

{{- define "resources.limits.cpu" -}}
{{- .Values.resources.limits.cpu -}}
{{- end -}}



{{- define "chartref" -}}
  {{- replace "+" "_" .Chart.Version | printf "%s-%s" .Chart.Name -}}
{{- end -}}

{{- define "labels.standard" -}}
app: {{ template "persistence-query-service.name" . }}
heritage: {{ .Release.Service | quote }}
release: {{ .Release.Name | quote }}
chart: {{ template "chartref" . }}
{{- end -}}
