{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Part 4: Geospatial Analysis\n",
    "#### Create a Rest API that given a latitude and longitude returns the 10 closest properties."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import folium\n",
    "from folium import plugins\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import requests\n",
    "import csv\n",
    "import math\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'distance': 0.0,\n",
       "  'latitude': 34.280990000000003,\n",
       "  'longitude': -118.488536,\n",
       "  'parcelid': 11016594.0},\n",
       " {'distance': 0.108,\n",
       "  'latitude': 34.280997999999997,\n",
       "  'longitude': -118.489711,\n",
       "  'parcelid': 11016589.0},\n",
       " {'distance': 0.1288,\n",
       "  'latitude': 34.281758000000004,\n",
       "  'longitude': -118.48748700000002,\n",
       "  'parcelid': 11013083.0},\n",
       " {'distance': 0.1583,\n",
       "  'latitude': 34.280559999999994,\n",
       "  'longitude': -118.48689299999999,\n",
       "  'parcelid': 11013235.0},\n",
       " {'distance': 0.16420000000000001,\n",
       "  'latitude': 34.282440999999999,\n",
       "  'longitude': -118.488867,\n",
       "  'parcelid': 11016400.0},\n",
       " {'distance': 0.17510000000000001,\n",
       "  'latitude': 34.280297999999995,\n",
       "  'longitude': -118.486824,\n",
       "  'parcelid': 11013237.0},\n",
       " {'distance': 0.19109999999999999,\n",
       "  'latitude': 34.281228000000013,\n",
       "  'longitude': -118.486476,\n",
       "  'parcelid': 11013092.0},\n",
       " {'distance': 0.20039999999999999,\n",
       "  'latitude': 34.281709999999997,\n",
       "  'longitude': -118.49053499999999,\n",
       "  'parcelid': 11016546.0},\n",
       " {'distance': 0.2097,\n",
       "  'latitude': 34.281289000000001,\n",
       "  'longitude': -118.49078900000001,\n",
       "  'parcelid': 11016610.0},\n",
       " {'distance': 0.24859999999999999,\n",
       "  'latitude': 34.283221999999995,\n",
       "  'longitude': -118.488696,\n",
       "  'parcelid': 11016429.0}]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url = 'http://localhost:5000/search/34.280990/-118.488536'\n",
    "response = requests.get(url)\n",
    "response = response.json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>latitude</th>\n",
       "      <th>longitude</th>\n",
       "      <th>parcelid</th>\n",
       "      <th>distance</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>34.280990</td>\n",
       "      <td>-118.488536</td>\n",
       "      <td>11016594</td>\n",
       "      <td>0.0000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>82357</th>\n",
       "      <td>34.280998</td>\n",
       "      <td>-118.489711</td>\n",
       "      <td>11016589</td>\n",
       "      <td>0.1080</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>133461</th>\n",
       "      <td>34.281758</td>\n",
       "      <td>-118.487487</td>\n",
       "      <td>11013083</td>\n",
       "      <td>0.1288</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11775</th>\n",
       "      <td>34.280560</td>\n",
       "      <td>-118.486893</td>\n",
       "      <td>11013235</td>\n",
       "      <td>0.1583</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>89509</th>\n",
       "      <td>34.282441</td>\n",
       "      <td>-118.488867</td>\n",
       "      <td>11016400</td>\n",
       "      <td>0.1642</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14260</th>\n",
       "      <td>34.280298</td>\n",
       "      <td>-118.486824</td>\n",
       "      <td>11013237</td>\n",
       "      <td>0.1751</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>51259</th>\n",
       "      <td>34.281228</td>\n",
       "      <td>-118.486476</td>\n",
       "      <td>11013092</td>\n",
       "      <td>0.1911</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>65258</th>\n",
       "      <td>34.281710</td>\n",
       "      <td>-118.490535</td>\n",
       "      <td>11016546</td>\n",
       "      <td>0.2004</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>123725</th>\n",
       "      <td>34.281289</td>\n",
       "      <td>-118.490789</td>\n",
       "      <td>11016610</td>\n",
       "      <td>0.2097</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>87616</th>\n",
       "      <td>34.283222</td>\n",
       "      <td>-118.488696</td>\n",
       "      <td>11016429</td>\n",
       "      <td>0.2486</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         latitude   longitude  parcelid  distance\n",
       "0       34.280990 -118.488536  11016594    0.0000\n",
       "82357   34.280998 -118.489711  11016589    0.1080\n",
       "133461  34.281758 -118.487487  11013083    0.1288\n",
       "11775   34.280560 -118.486893  11013235    0.1583\n",
       "89509   34.282441 -118.488867  11016400    0.1642\n",
       "14260   34.280298 -118.486824  11013237    0.1751\n",
       "51259   34.281228 -118.486476  11013092    0.1911\n",
       "65258   34.281710 -118.490535  11016546    0.2004\n",
       "123725  34.281289 -118.490789  11016610    0.2097\n",
       "87616   34.283222 -118.488696  11016429    0.2486"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[34.280998, -118.489711]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "locations = df[['latitude', 'longitude']]\n",
    "locationlist = locations.values.tolist()\n",
    "\n",
    "locationlist[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div style=\"width:100%;\"><div style=\"position:relative;width:100%;height:0;padding-bottom:60%;\"><iframe src=\"data:text/html;base64,CiAgICAgICAgPCFET0NUWVBFIGh0bWw+CiAgICAgICAgPGhlYWQ+CiAgICAgICAgICAgIAogICAgICAgIAogICAgICAgICAgICA8bWV0YSBodHRwLWVxdWl2PSJjb250ZW50LXR5cGUiIGNvbnRlbnQ9InRleHQvaHRtbDsgY2hhcnNldD1VVEYtOCIgLz4KICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9sZWFmbGV0LzAuNy4zL2xlYWZsZXQuanMiPjwvc2NyaXB0PgogICAgICAgIAogICAgICAgIAogICAgICAgIAogICAgICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vYWpheC5nb29nbGVhcGlzLmNvbS9hamF4L2xpYnMvanF1ZXJ5LzEuMTEuMS9qcXVlcnkubWluLmpzIj48L3NjcmlwdD4KICAgICAgICAKICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIDxzY3JpcHQgc3JjPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9qcy9ib290c3RyYXAubWluLmpzIj48L3NjcmlwdD4KICAgICAgICAKICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5taW4uanMiPjwvc2NyaXB0PgogICAgICAgIAogICAgICAgIAogICAgICAgIAogICAgICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY2RuanMuY2xvdWRmbGFyZS5jb20vYWpheC9saWJzL2xlYWZsZXQubWFya2VyY2x1c3Rlci8wLjQuMC9sZWFmbGV0Lm1hcmtlcmNsdXN0ZXItc3JjLmpzIj48L3NjcmlwdD4KICAgICAgICAKICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9sZWFmbGV0Lm1hcmtlcmNsdXN0ZXIvMC40LjAvbGVhZmxldC5tYXJrZXJjbHVzdGVyLmpzIj48L3NjcmlwdD4KICAgICAgICAKICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvbGVhZmxldC8wLjcuMy9sZWFmbGV0LmNzcyIgLz4KICAgICAgICAKICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC5taW4uY3NzIiAvPgogICAgICAgIAogICAgICAgIAogICAgICAgIAogICAgICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLXRoZW1lLm1pbi5jc3MiIC8+CiAgICAgICAgCiAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIAogICAgICAgIAogICAgICAgICAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuMS4wL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIgLz4KICAgICAgICAKICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuY3NzIiAvPgogICAgICAgIAogICAgICAgIAogICAgICAgIAogICAgICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9sZWFmbGV0Lm1hcmtlcmNsdXN0ZXIvMC40LjAvTWFya2VyQ2x1c3Rlci5EZWZhdWx0LmNzcyIgLz4KICAgICAgICAKICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvbGVhZmxldC5tYXJrZXJjbHVzdGVyLzAuNC4wL01hcmtlckNsdXN0ZXIuY3NzIiAvPgogICAgICAgIAogICAgICAgIAogICAgICAgIAogICAgICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vcHl0aG9uLXZpc3VhbGl6YXRpb24vZm9saXVtL21hc3Rlci9mb2xpdW0vdGVtcGxhdGVzL2xlYWZsZXQuYXdlc29tZS5yb3RhdGUuY3NzIiAvPgogICAgICAgIAogICAgICAgIAogICAgICAgIAogICAgICAgICAgICAKICAgICAgICAgICAgPHN0eWxlPgoKICAgICAgICAgICAgaHRtbCwgYm9keSB7CiAgICAgICAgICAgICAgICB3aWR0aDogMTAwJTsKICAgICAgICAgICAgICAgIGhlaWdodDogMTAwJTsKICAgICAgICAgICAgICAgIG1hcmdpbjogMDsKICAgICAgICAgICAgICAgIHBhZGRpbmc6IDA7CiAgICAgICAgICAgICAgICB9CgogICAgICAgICAgICAjbWFwIHsKICAgICAgICAgICAgICAgIHBvc2l0aW9uOmFic29sdXRlOwogICAgICAgICAgICAgICAgdG9wOjA7CiAgICAgICAgICAgICAgICBib3R0b206MDsKICAgICAgICAgICAgICAgIHJpZ2h0OjA7CiAgICAgICAgICAgICAgICBsZWZ0OjA7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIDwvc3R5bGU+CiAgICAgICAgICAgIAogICAgICAgIAogICAgICAgICAgICAKICAgICAgICAgICAgPHN0eWxlPiAjbWFwX2Q3ODlkNjYyZTQwOTRkMWI4OTk1YTNiMWJhNGUyOTEyIHsKICAgICAgICAgICAgICAgIHBvc2l0aW9uIDogcmVsYXRpdmU7CiAgICAgICAgICAgICAgICB3aWR0aCA6IDEwMC4wJTsKICAgICAgICAgICAgICAgIGhlaWdodDogMTAwLjAlOwogICAgICAgICAgICAgICAgbGVmdDogMC4wJTsKICAgICAgICAgICAgICAgIHRvcDogMC4wJTsKICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgPC9zdHlsZT4KICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIDxzdHlsZT4gI21hcF85OTY1ZDRiYTEwN2Q0ZjliOWY4ODk0NDU0YjY2ZTI4MiB7CiAgICAgICAgICAgICAgICBwb3NpdGlvbiA6IHJlbGF0aXZlOwogICAgICAgICAgICAgICAgd2lkdGggOiAxMDAuMCU7CiAgICAgICAgICAgICAgICBoZWlnaHQ6IDEwMC4wJTsKICAgICAgICAgICAgICAgIGxlZnQ6IDAuMCU7CiAgICAgICAgICAgICAgICB0b3A6IDAuMCU7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIDwvc3R5bGU+CiAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfZDg4YzZmNGZiYmQ5NDFiNTgyOGMwYzliYmRkMGVlOGQgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAogICAgICAgIAogICAgICAgICAgICAKICAgICAgICAgICAgPHN0eWxlPiAjbWFwX2E4N2NlMDJiODU5MDQ4MTBhZTMwN2Y3ZmJhYWNhZWIxIHsKICAgICAgICAgICAgICAgIHBvc2l0aW9uIDogcmVsYXRpdmU7CiAgICAgICAgICAgICAgICB3aWR0aCA6IDEwMC4wJTsKICAgICAgICAgICAgICAgIGhlaWdodDogMTAwLjAlOwogICAgICAgICAgICAgICAgbGVmdDogMC4wJTsKICAgICAgICAgICAgICAgIHRvcDogMC4wJTsKICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgPC9zdHlsZT4KICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIDxzdHlsZT4gI21hcF8zOGZkMjkyMDlmZTA0OGMxYmI5MzBjNjNiNTI2NzdjZSB7CiAgICAgICAgICAgICAgICBwb3NpdGlvbiA6IHJlbGF0aXZlOwogICAgICAgICAgICAgICAgd2lkdGggOiAxMDAuMCU7CiAgICAgICAgICAgICAgICBoZWlnaHQ6IDEwMC4wJTsKICAgICAgICAgICAgICAgIGxlZnQ6IDAuMCU7CiAgICAgICAgICAgICAgICB0b3A6IDAuMCU7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIDwvc3R5bGU+CiAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfOGZjMjhkYjZjNGY2NDJmYWE0MDYyYzYwZWJjMjYyZjIgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAogICAgICAgIAogICAgICAgICAgICAKICAgICAgICAgICAgPHN0eWxlPiAjbWFwXzY1M2Q0NjkxM2EwYTQ4NDViMDQ3YWIyY2ZmZmNjZDQyIHsKICAgICAgICAgICAgICAgIHBvc2l0aW9uIDogcmVsYXRpdmU7CiAgICAgICAgICAgICAgICB3aWR0aCA6IDEwMC4wJTsKICAgICAgICAgICAgICAgIGhlaWdodDogMTAwLjAlOwogICAgICAgICAgICAgICAgbGVmdDogMC4wJTsKICAgICAgICAgICAgICAgIHRvcDogMC4wJTsKICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgPC9zdHlsZT4KICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIDxzdHlsZT4gI21hcF85YjgxYzNmYTMzNTc0NTQ4ODdmYmIwZGVkMGYwNzZjYyB7CiAgICAgICAgICAgICAgICBwb3NpdGlvbiA6IHJlbGF0aXZlOwogICAgICAgICAgICAgICAgd2lkdGggOiAxMDAuMCU7CiAgICAgICAgICAgICAgICBoZWlnaHQ6IDEwMC4wJTsKICAgICAgICAgICAgICAgIGxlZnQ6IDAuMCU7CiAgICAgICAgICAgICAgICB0b3A6IDAuMCU7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIDwvc3R5bGU+CiAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfZmJlZGIzMDhmOGNlNDBjNTlmMWE5OTdkY2EzMjEyY2QgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAogICAgICAgIAogICAgICAgICAgICAKICAgICAgICAgICAgPHN0eWxlPiAjbWFwX2Q1MTI1NWRmNjc3OTQ3ZTA5NjQ1Zjg3ZWZlNWZiOTQzIHsKICAgICAgICAgICAgICAgIHBvc2l0aW9uIDogcmVsYXRpdmU7CiAgICAgICAgICAgICAgICB3aWR0aCA6IDEwMC4wJTsKICAgICAgICAgICAgICAgIGhlaWdodDogMTAwLjAlOwogICAgICAgICAgICAgICAgbGVmdDogMC4wJTsKICAgICAgICAgICAgICAgIHRvcDogMC4wJTsKICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgPC9zdHlsZT4KICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIDxzdHlsZT4gI21hcF8wN2YxZWQwYjc0MzQ0NjhiYjJkYjUzNDRlODU0MjEzMSB7CiAgICAgICAgICAgICAgICBwb3NpdGlvbiA6IHJlbGF0aXZlOwogICAgICAgICAgICAgICAgd2lkdGggOiAxMDAuMCU7CiAgICAgICAgICAgICAgICBoZWlnaHQ6IDEwMC4wJTsKICAgICAgICAgICAgICAgIGxlZnQ6IDAuMCU7CiAgICAgICAgICAgICAgICB0b3A6IDAuMCU7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIDwvc3R5bGU+CiAgICAgICAgCiAgICAgICAgCiAgICAgICAgCiAgICAgICAgPC9oZWFkPgogICAgICAgIDxib2R5PgogICAgICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfZDc4OWQ2NjJlNDA5NGQxYjg5OTVhM2IxYmE0ZTI5MTIiID48L2Rpdj4KICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfOTk2NWQ0YmExMDdkNGY5YjlmODg5NDQ1NGI2NmUyODIiID48L2Rpdj4KICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfZDg4YzZmNGZiYmQ5NDFiNTgyOGMwYzliYmRkMGVlOGQiID48L2Rpdj4KICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfYTg3Y2UwMmI4NTkwNDgxMGFlMzA3ZjdmYmFhY2FlYjEiID48L2Rpdj4KICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfMzhmZDI5MjA5ZmUwNDhjMWJiOTMwYzYzYjUyNjc3Y2UiID48L2Rpdj4KICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfOGZjMjhkYjZjNGY2NDJmYWE0MDYyYzYwZWJjMjYyZjIiID48L2Rpdj4KICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfNjUzZDQ2OTEzYTBhNDg0NWIwNDdhYjJjZmZmY2NkNDIiID48L2Rpdj4KICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfOWI4MWMzZmEzMzU3NDU0ODg3ZmJiMGRlZDBmMDc2Y2MiID48L2Rpdj4KICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfZmJlZGIzMDhmOGNlNDBjNTlmMWE5OTdkY2EzMjEyY2QiID48L2Rpdj4KICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfZDUxMjU1ZGY2Nzc5NDdlMDk2NDVmODdlZmU1ZmI5NDMiID48L2Rpdj4KICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfMDdmMWVkMGI3NDM0NDY4YmIyZGI1MzQ0ZTg1NDIxMzEiID48L2Rpdj4KICAgICAgICAKICAgICAgICAKICAgICAgICAKICAgICAgICA8L2JvZHk+CiAgICAgICAgPHNjcmlwdD4KICAgICAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIHNvdXRoV2VzdCA9IEwubGF0TG5nKC05MCwgLTE4MCk7CiAgICAgICAgICAgIHZhciBub3J0aEVhc3QgPSBMLmxhdExuZyg5MCwgMTgwKTsKICAgICAgICAgICAgdmFyIGJvdW5kcyA9IEwubGF0TG5nQm91bmRzKHNvdXRoV2VzdCwgbm9ydGhFYXN0KTsKCiAgICAgICAgICAgIHZhciBtYXBfZDc4OWQ2NjJlNDA5NGQxYjg5OTVhM2IxYmE0ZTI5MTIgPSBMLm1hcCgnbWFwX2Q3ODlkNjYyZTQwOTRkMWI4OTk1YTNiMWJhNGUyOTEyJywgewogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2VudGVyOlszNC4yODA5OTgsLTExOC40ODk3MTFdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogNiwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1heEJvdW5kczogYm91bmRzLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbGF5ZXJzOiBbXSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB9KTsKICAgICAgICAgICAgCiAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIAogICAgICAgICAgICB2YXIgdGlsZV9sYXllcl9mYjE3OGVkOTI3MTU0MGExODMwMGY4NDBkYjNkNzdlNCA9IEwudGlsZUxheWVyKAogICAgICAgICAgICAgICAgJ2h0dHBzOi8ve3N9LnRpbGUub3BlbnN0cmVldG1hcC5vcmcve3p9L3t4fS97eX0ucG5nJywKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBtYXhab29tOiAxOCwKICAgICAgICAgICAgICAgICAgICBtaW5ab29tOiAxLAogICAgICAgICAgICAgICAgICAgIGF0dHJpYnV0aW9uOiAnRGF0YSBieSA8YSBocmVmPSJodHRwOi8vb3BlbnN0cmVldG1hcC5vcmciPk9wZW5TdHJlZXRNYXA8L2E+LCB1bmRlciA8YSBocmVmPSJodHRwOi8vd3d3Lm9wZW5zdHJlZXRtYXAub3JnL2NvcHlyaWdodCI+T0RiTDwvYT4uJywKICAgICAgICAgICAgICAgICAgICBkZXRlY3RSZXRpbmE6IGZhbHNlCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZDc4OWQ2NjJlNDA5NGQxYjg5OTVhM2IxYmE0ZTI5MTIpOwoKICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCgogICAgICAgICAgICB2YXIgc291dGhXZXN0ID0gTC5sYXRMbmcoLTkwLCAtMTgwKTsKICAgICAgICAgICAgdmFyIG5vcnRoRWFzdCA9IEwubGF0TG5nKDkwLCAxODApOwogICAgICAgICAgICB2YXIgYm91bmRzID0gTC5sYXRMbmdCb3VuZHMoc291dGhXZXN0LCBub3J0aEVhc3QpOwoKICAgICAgICAgICAgdmFyIG1hcF85OTY1ZDRiYTEwN2Q0ZjliOWY4ODk0NDU0YjY2ZTI4MiA9IEwubWFwKCdtYXBfOTk2NWQ0YmExMDdkNGY5YjlmODg5NDQ1NGI2NmUyODInLCB7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjZW50ZXI6WzM0LjI4MDk5LC0xMTguNDg4NTM2XSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHpvb206IDEwLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbWF4Qm91bmRzOiBib3VuZHMsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsYXllcnM6IFtdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY3JzOiBMLkNSUy5FUFNHMzg1NwogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0pOwogICAgICAgICAgICAKICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyXzNhM2Y1YzI4YzU3ZDQ2MWViMGFjYWIwOWM4MDJhN2EyID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAnaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmcnLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIG1heFpvb206IDE4LAogICAgICAgICAgICAgICAgICAgIG1pblpvb206IDEsCiAgICAgICAgICAgICAgICAgICAgYXR0cmlidXRpb246ICdEYXRhIGJ5IDxhIGhyZWY9Imh0dHA6Ly9vcGVuc3RyZWV0bWFwLm9yZyI+T3BlblN0cmVldE1hcDwvYT4sIHVuZGVyIDxhIGhyZWY9Imh0dHA6Ly93d3cub3BlbnN0cmVldG1hcC5vcmcvY29weXJpZ2h0Ij5PRGJMPC9hPi4nLAogICAgICAgICAgICAgICAgICAgIGRldGVjdFJldGluYTogZmFsc2UKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OTY1ZDRiYTEwN2Q0ZjliOWY4ODk0NDU0YjY2ZTI4Mik7CgogICAgICAgIAogICAgICAgIAogICAgICAgICAgICAKCiAgICAgICAgICAgIHZhciBzb3V0aFdlc3QgPSBMLmxhdExuZygtOTAsIC0xODApOwogICAgICAgICAgICB2YXIgbm9ydGhFYXN0ID0gTC5sYXRMbmcoOTAsIDE4MCk7CiAgICAgICAgICAgIHZhciBib3VuZHMgPSBMLmxhdExuZ0JvdW5kcyhzb3V0aFdlc3QsIG5vcnRoRWFzdCk7CgogICAgICAgICAgICB2YXIgbWFwX2Q4OGM2ZjRmYmJkOTQxYjU4MjhjMGM5YmJkZDBlZThkID0gTC5tYXAoJ21hcF9kODhjNmY0ZmJiZDk0MWI1ODI4YzBjOWJiZGQwZWU4ZCcsIHsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNlbnRlcjpbMzQuMjgwOTk4LC0xMTguNDg5NzExXSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHpvb206IDEwLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbWF4Qm91bmRzOiBib3VuZHMsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsYXllcnM6IFtdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY3JzOiBMLkNSUy5FUFNHMzg1NwogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0pOwogICAgICAgICAgICAKICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyXzc0NjlkNTQ1MzNhYTQzODA4ZTgxOThiMjFkNmYyOWI2ID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAnaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmcnLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIG1heFpvb206IDE4LAogICAgICAgICAgICAgICAgICAgIG1pblpvb206IDEsCiAgICAgICAgICAgICAgICAgICAgYXR0cmlidXRpb246ICdEYXRhIGJ5IDxhIGhyZWY9Imh0dHA6Ly9vcGVuc3RyZWV0bWFwLm9yZyI+T3BlblN0cmVldE1hcDwvYT4sIHVuZGVyIDxhIGhyZWY9Imh0dHA6Ly93d3cub3BlbnN0cmVldG1hcC5vcmcvY29weXJpZ2h0Ij5PRGJMPC9hPi4nLAogICAgICAgICAgICAgICAgICAgIGRldGVjdFJldGluYTogZmFsc2UKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9kODhjNmY0ZmJiZDk0MWI1ODI4YzBjOWJiZGQwZWU4ZCk7CgogICAgICAgIAogICAgICAgIAogICAgICAgICAgICAKCiAgICAgICAgICAgIHZhciBzb3V0aFdlc3QgPSBMLmxhdExuZygtOTAsIC0xODApOwogICAgICAgICAgICB2YXIgbm9ydGhFYXN0ID0gTC5sYXRMbmcoOTAsIDE4MCk7CiAgICAgICAgICAgIHZhciBib3VuZHMgPSBMLmxhdExuZ0JvdW5kcyhzb3V0aFdlc3QsIG5vcnRoRWFzdCk7CgogICAgICAgICAgICB2YXIgbWFwX2E4N2NlMDJiODU5MDQ4MTBhZTMwN2Y3ZmJhYWNhZWIxID0gTC5tYXAoJ21hcF9hODdjZTAyYjg1OTA0ODEwYWUzMDdmN2ZiYWFjYWViMScsIHsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNlbnRlcjpbMzQuMjgxNzU4LC0xMTguNDg3NDg3MDAwMDAwMDJdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogMTAsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyczogW10sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjcnM6IEwuQ1JTLkVQU0czODU3CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7CiAgICAgICAgICAgIAogICAgICAgIAogICAgICAgIAogICAgICAgICAgICAKICAgICAgICAgICAgdmFyIHRpbGVfbGF5ZXJfZmJhOTgxZjg5MzAyNDU4MThiZTk3ZTM4ZWFiMWM4YzcgPSBMLnRpbGVMYXllcigKICAgICAgICAgICAgICAgICdodHRwczovL3tzfS50aWxlLm9wZW5zdHJlZXRtYXAub3JnL3t6fS97eH0ve3l9LnBuZycsCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgbWF4Wm9vbTogMTgsCiAgICAgICAgICAgICAgICAgICAgbWluWm9vbTogMSwKICAgICAgICAgICAgICAgICAgICBhdHRyaWJ1dGlvbjogJ0RhdGEgYnkgPGEgaHJlZj0iaHR0cDovL29wZW5zdHJlZXRtYXAub3JnIj5PcGVuU3RyZWV0TWFwPC9hPiwgdW5kZXIgPGEgaHJlZj0iaHR0cDovL3d3dy5vcGVuc3RyZWV0bWFwLm9yZy9jb3B5cmlnaHQiPk9EYkw8L2E+LicsCiAgICAgICAgICAgICAgICAgICAgZGV0ZWN0UmV0aW5hOiBmYWxzZQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E4N2NlMDJiODU5MDQ4MTBhZTMwN2Y3ZmJhYWNhZWIxKTsKCiAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIHNvdXRoV2VzdCA9IEwubGF0TG5nKC05MCwgLTE4MCk7CiAgICAgICAgICAgIHZhciBub3J0aEVhc3QgPSBMLmxhdExuZyg5MCwgMTgwKTsKICAgICAgICAgICAgdmFyIGJvdW5kcyA9IEwubGF0TG5nQm91bmRzKHNvdXRoV2VzdCwgbm9ydGhFYXN0KTsKCiAgICAgICAgICAgIHZhciBtYXBfMzhmZDI5MjA5ZmUwNDhjMWJiOTMwYzYzYjUyNjc3Y2UgPSBMLm1hcCgnbWFwXzM4ZmQyOTIwOWZlMDQ4YzFiYjkzMGM2M2I1MjY3N2NlJywgewogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2VudGVyOlszNC4yODA1NTk5OTk5OTk5OTQsLTExOC40ODY4OTNdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogMTAsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyczogW10sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjcnM6IEwuQ1JTLkVQU0czODU3CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7CiAgICAgICAgICAgIAogICAgICAgIAogICAgICAgIAogICAgICAgICAgICAKICAgICAgICAgICAgdmFyIHRpbGVfbGF5ZXJfZWEyYTdhNDdjYWFhNDNiOThkMjczNmIwOWY3MDk0MzYgPSBMLnRpbGVMYXllcigKICAgICAgICAgICAgICAgICdodHRwczovL3tzfS50aWxlLm9wZW5zdHJlZXRtYXAub3JnL3t6fS97eH0ve3l9LnBuZycsCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgbWF4Wm9vbTogMTgsCiAgICAgICAgICAgICAgICAgICAgbWluWm9vbTogMSwKICAgICAgICAgICAgICAgICAgICBhdHRyaWJ1dGlvbjogJ0RhdGEgYnkgPGEgaHJlZj0iaHR0cDovL29wZW5zdHJlZXRtYXAub3JnIj5PcGVuU3RyZWV0TWFwPC9hPiwgdW5kZXIgPGEgaHJlZj0iaHR0cDovL3d3dy5vcGVuc3RyZWV0bWFwLm9yZy9jb3B5cmlnaHQiPk9EYkw8L2E+LicsCiAgICAgICAgICAgICAgICAgICAgZGV0ZWN0UmV0aW5hOiBmYWxzZQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzM4ZmQyOTIwOWZlMDQ4YzFiYjkzMGM2M2I1MjY3N2NlKTsKCiAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIHNvdXRoV2VzdCA9IEwubGF0TG5nKC05MCwgLTE4MCk7CiAgICAgICAgICAgIHZhciBub3J0aEVhc3QgPSBMLmxhdExuZyg5MCwgMTgwKTsKICAgICAgICAgICAgdmFyIGJvdW5kcyA9IEwubGF0TG5nQm91bmRzKHNvdXRoV2VzdCwgbm9ydGhFYXN0KTsKCiAgICAgICAgICAgIHZhciBtYXBfOGZjMjhkYjZjNGY2NDJmYWE0MDYyYzYwZWJjMjYyZjIgPSBMLm1hcCgnbWFwXzhmYzI4ZGI2YzRmNjQyZmFhNDA2MmM2MGViYzI2MmYyJywgewogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2VudGVyOlszNC4yODI0NDEsLTExOC40ODg4NjddLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogMTAsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyczogW10sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjcnM6IEwuQ1JTLkVQU0czODU3CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7CiAgICAgICAgICAgIAogICAgICAgIAogICAgICAgIAogICAgICAgICAgICAKICAgICAgICAgICAgdmFyIHRpbGVfbGF5ZXJfYzlhMGQzZmRhMTVkNDA2MGE1NGIzMGRjZWE2OTFmMjEgPSBMLnRpbGVMYXllcigKICAgICAgICAgICAgICAgICdodHRwczovL3tzfS50aWxlLm9wZW5zdHJlZXRtYXAub3JnL3t6fS97eH0ve3l9LnBuZycsCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgbWF4Wm9vbTogMTgsCiAgICAgICAgICAgICAgICAgICAgbWluWm9vbTogMSwKICAgICAgICAgICAgICAgICAgICBhdHRyaWJ1dGlvbjogJ0RhdGEgYnkgPGEgaHJlZj0iaHR0cDovL29wZW5zdHJlZXRtYXAub3JnIj5PcGVuU3RyZWV0TWFwPC9hPiwgdW5kZXIgPGEgaHJlZj0iaHR0cDovL3d3dy5vcGVuc3RyZWV0bWFwLm9yZy9jb3B5cmlnaHQiPk9EYkw8L2E+LicsCiAgICAgICAgICAgICAgICAgICAgZGV0ZWN0UmV0aW5hOiBmYWxzZQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzhmYzI4ZGI2YzRmNjQyZmFhNDA2MmM2MGViYzI2MmYyKTsKCiAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIHNvdXRoV2VzdCA9IEwubGF0TG5nKC05MCwgLTE4MCk7CiAgICAgICAgICAgIHZhciBub3J0aEVhc3QgPSBMLmxhdExuZyg5MCwgMTgwKTsKICAgICAgICAgICAgdmFyIGJvdW5kcyA9IEwubGF0TG5nQm91bmRzKHNvdXRoV2VzdCwgbm9ydGhFYXN0KTsKCiAgICAgICAgICAgIHZhciBtYXBfNjUzZDQ2OTEzYTBhNDg0NWIwNDdhYjJjZmZmY2NkNDIgPSBMLm1hcCgnbWFwXzY1M2Q0NjkxM2EwYTQ4NDViMDQ3YWIyY2ZmZmNjZDQyJywgewogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2VudGVyOlszNC4yODAyOTc5OTk5OTk5OTUsLTExOC40ODY4MjRdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogMTAsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyczogW10sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjcnM6IEwuQ1JTLkVQU0czODU3CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7CiAgICAgICAgICAgIAogICAgICAgIAogICAgICAgIAogICAgICAgICAgICAKICAgICAgICAgICAgdmFyIHRpbGVfbGF5ZXJfYjBmMGZlZTVlZWNiNDc4MDk3MDBkOTg2Zjk4NWY4YmMgPSBMLnRpbGVMYXllcigKICAgICAgICAgICAgICAgICdodHRwczovL3tzfS50aWxlLm9wZW5zdHJlZXRtYXAub3JnL3t6fS97eH0ve3l9LnBuZycsCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgbWF4Wm9vbTogMTgsCiAgICAgICAgICAgICAgICAgICAgbWluWm9vbTogMSwKICAgICAgICAgICAgICAgICAgICBhdHRyaWJ1dGlvbjogJ0RhdGEgYnkgPGEgaHJlZj0iaHR0cDovL29wZW5zdHJlZXRtYXAub3JnIj5PcGVuU3RyZWV0TWFwPC9hPiwgdW5kZXIgPGEgaHJlZj0iaHR0cDovL3d3dy5vcGVuc3RyZWV0bWFwLm9yZy9jb3B5cmlnaHQiPk9EYkw8L2E+LicsCiAgICAgICAgICAgICAgICAgICAgZGV0ZWN0UmV0aW5hOiBmYWxzZQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzY1M2Q0NjkxM2EwYTQ4NDViMDQ3YWIyY2ZmZmNjZDQyKTsKCiAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIHNvdXRoV2VzdCA9IEwubGF0TG5nKC05MCwgLTE4MCk7CiAgICAgICAgICAgIHZhciBub3J0aEVhc3QgPSBMLmxhdExuZyg5MCwgMTgwKTsKICAgICAgICAgICAgdmFyIGJvdW5kcyA9IEwubGF0TG5nQm91bmRzKHNvdXRoV2VzdCwgbm9ydGhFYXN0KTsKCiAgICAgICAgICAgIHZhciBtYXBfOWI4MWMzZmEzMzU3NDU0ODg3ZmJiMGRlZDBmMDc2Y2MgPSBMLm1hcCgnbWFwXzliODFjM2ZhMzM1NzQ1NDg4N2ZiYjBkZWQwZjA3NmNjJywgewogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2VudGVyOlszNC4yODEyMjgwMDAwMDAwMSwtMTE4LjQ4NjQ3Nl0sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB6b29tOiAxMCwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1heEJvdW5kczogYm91bmRzLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbGF5ZXJzOiBbXSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB9KTsKICAgICAgICAgICAgCiAgICAgICAgCiAgICAgICAgCiAgICAgICAgICAgIAogICAgICAgICAgICB2YXIgdGlsZV9sYXllcl8yZTg3ODliYzk5ZDY0NjZlODNkZmExY2VhZTVjNDgzZiA9IEwudGlsZUxheWVyKAogICAgICAgICAgICAgICAgJ2h0dHBzOi8ve3N9LnRpbGUub3BlbnN0cmVldG1hcC5vcmcve3p9L3t4fS97eX0ucG5nJywKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBtYXhab29tOiAxOCwKICAgICAgICAgICAgICAgICAgICBtaW5ab29tOiAxLAogICAgICAgICAgICAgICAgICAgIGF0dHJpYnV0aW9uOiAnRGF0YSBieSA8YSBocmVmPSJodHRwOi8vb3BlbnN0cmVldG1hcC5vcmciPk9wZW5TdHJlZXRNYXA8L2E+LCB1bmRlciA8YSBocmVmPSJodHRwOi8vd3d3Lm9wZW5zdHJlZXRtYXAub3JnL2NvcHlyaWdodCI+T0RiTDwvYT4uJywKICAgICAgICAgICAgICAgICAgICBkZXRlY3RSZXRpbmE6IGZhbHNlCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOWI4MWMzZmEzMzU3NDU0ODg3ZmJiMGRlZDBmMDc2Y2MpOwoKICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCgogICAgICAgICAgICB2YXIgc291dGhXZXN0ID0gTC5sYXRMbmcoLTkwLCAtMTgwKTsKICAgICAgICAgICAgdmFyIG5vcnRoRWFzdCA9IEwubGF0TG5nKDkwLCAxODApOwogICAgICAgICAgICB2YXIgYm91bmRzID0gTC5sYXRMbmdCb3VuZHMoc291dGhXZXN0LCBub3J0aEVhc3QpOwoKICAgICAgICAgICAgdmFyIG1hcF9mYmVkYjMwOGY4Y2U0MGM1OWYxYTk5N2RjYTMyMTJjZCA9IEwubWFwKCdtYXBfZmJlZGIzMDhmOGNlNDBjNTlmMWE5OTdkY2EzMjEyY2QnLCB7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjZW50ZXI6WzM0LjI4MTcxLC0xMTguNDkwNTM1XSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHpvb206IDEwLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbWF4Qm91bmRzOiBib3VuZHMsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsYXllcnM6IFtdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY3JzOiBMLkNSUy5FUFNHMzg1NwogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0pOwogICAgICAgICAgICAKICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyX2NmMWQ1ZDY4MWQ2NjRhYWFhNjYyMDg0MjI2MTkwN2Y5ID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAnaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmcnLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIG1heFpvb206IDE4LAogICAgICAgICAgICAgICAgICAgIG1pblpvb206IDEsCiAgICAgICAgICAgICAgICAgICAgYXR0cmlidXRpb246ICdEYXRhIGJ5IDxhIGhyZWY9Imh0dHA6Ly9vcGVuc3RyZWV0bWFwLm9yZyI+T3BlblN0cmVldE1hcDwvYT4sIHVuZGVyIDxhIGhyZWY9Imh0dHA6Ly93d3cub3BlbnN0cmVldG1hcC5vcmcvY29weXJpZ2h0Ij5PRGJMPC9hPi4nLAogICAgICAgICAgICAgICAgICAgIGRldGVjdFJldGluYTogZmFsc2UKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mYmVkYjMwOGY4Y2U0MGM1OWYxYTk5N2RjYTMyMTJjZCk7CgogICAgICAgIAogICAgICAgIAogICAgICAgICAgICAKCiAgICAgICAgICAgIHZhciBzb3V0aFdlc3QgPSBMLmxhdExuZygtOTAsIC0xODApOwogICAgICAgICAgICB2YXIgbm9ydGhFYXN0ID0gTC5sYXRMbmcoOTAsIDE4MCk7CiAgICAgICAgICAgIHZhciBib3VuZHMgPSBMLmxhdExuZ0JvdW5kcyhzb3V0aFdlc3QsIG5vcnRoRWFzdCk7CgogICAgICAgICAgICB2YXIgbWFwX2Q1MTI1NWRmNjc3OTQ3ZTA5NjQ1Zjg3ZWZlNWZiOTQzID0gTC5tYXAoJ21hcF9kNTEyNTVkZjY3Nzk0N2UwOTY0NWY4N2VmZTVmYjk0MycsIHsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNlbnRlcjpbMzQuMjgxMjg5LC0xMTguNDkwNzg5XSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHpvb206IDEwLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbWF4Qm91bmRzOiBib3VuZHMsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsYXllcnM6IFtdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY3JzOiBMLkNSUy5FUFNHMzg1NwogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0pOwogICAgICAgICAgICAKICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyXzZiNjdmMmE4ZDhlMzQ3NzliNzZiZTE0ZTNlM2YzZWI4ID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAnaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmcnLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIG1heFpvb206IDE4LAogICAgICAgICAgICAgICAgICAgIG1pblpvb206IDEsCiAgICAgICAgICAgICAgICAgICAgYXR0cmlidXRpb246ICdEYXRhIGJ5IDxhIGhyZWY9Imh0dHA6Ly9vcGVuc3RyZWV0bWFwLm9yZyI+T3BlblN0cmVldE1hcDwvYT4sIHVuZGVyIDxhIGhyZWY9Imh0dHA6Ly93d3cub3BlbnN0cmVldG1hcC5vcmcvY29weXJpZ2h0Ij5PRGJMPC9hPi4nLAogICAgICAgICAgICAgICAgICAgIGRldGVjdFJldGluYTogZmFsc2UKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9kNTEyNTVkZjY3Nzk0N2UwOTY0NWY4N2VmZTVmYjk0Myk7CgogICAgICAgIAogICAgICAgIAogICAgICAgICAgICAKCiAgICAgICAgICAgIHZhciBzb3V0aFdlc3QgPSBMLmxhdExuZygtOTAsIC0xODApOwogICAgICAgICAgICB2YXIgbm9ydGhFYXN0ID0gTC5sYXRMbmcoOTAsIDE4MCk7CiAgICAgICAgICAgIHZhciBib3VuZHMgPSBMLmxhdExuZ0JvdW5kcyhzb3V0aFdlc3QsIG5vcnRoRWFzdCk7CgogICAgICAgICAgICB2YXIgbWFwXzA3ZjFlZDBiNzQzNDQ2OGJiMmRiNTM0NGU4NTQyMTMxID0gTC5tYXAoJ21hcF8wN2YxZWQwYjc0MzQ0NjhiYjJkYjUzNDRlODU0MjEzMScsIHsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNlbnRlcjpbMzQuMjgzMjIxOTk5OTk5OTk1LC0xMTguNDg4Njk2XSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHpvb206IDEwLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbWF4Qm91bmRzOiBib3VuZHMsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsYXllcnM6IFtdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY3JzOiBMLkNSUy5FUFNHMzg1NwogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0pOwogICAgICAgICAgICAKICAgICAgICAKICAgICAgICAKICAgICAgICAgICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyXzQ5ZWViOTJkZGIwMDQzMDM4MmU4ZjhkMjM5NjMwOTM1ID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAnaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmcnLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIG1heFpvb206IDE4LAogICAgICAgICAgICAgICAgICAgIG1pblpvb206IDEsCiAgICAgICAgICAgICAgICAgICAgYXR0cmlidXRpb246ICdEYXRhIGJ5IDxhIGhyZWY9Imh0dHA6Ly9vcGVuc3RyZWV0bWFwLm9yZyI+T3BlblN0cmVldE1hcDwvYT4sIHVuZGVyIDxhIGhyZWY9Imh0dHA6Ly93d3cub3BlbnN0cmVldG1hcC5vcmcvY29weXJpZ2h0Ij5PRGJMPC9hPi4nLAogICAgICAgICAgICAgICAgICAgIGRldGVjdFJldGluYTogZmFsc2UKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wN2YxZWQwYjc0MzQ0NjhiYjJkYjUzNDRlODU0MjEzMSk7CgogICAgICAgIAogICAgICAgIAogICAgICAgIAogICAgICAgIDwvc2NyaXB0PgogICAgICAgIA==\" style=\"position:absolute;width:100%;height:100%;left:0;top:0;\"></iframe></div></div>"
      ],
      "text/plain": [
       "<folium.folium.Map at 0x1184cdb38>"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mapit = None\n",
    "mapit = folium.Map( location=[34.280998, -118.489711], zoom_start=6 )\n",
    "for coord in locationlist:\n",
    "    mapit = folium.Map( location=[ coord[0], coord[1]] ).add_to( mapit )\n",
    "mapit"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda root]",
   "language": "python",
   "name": "conda-root-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
