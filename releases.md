---
title: Releases
layout: default
---

<table  class="table-striped">
<colgroup>
<col width="15%" />
<col width="15%" />
<col width="70%" />
</colgroup>
<thead >
<tr class="header">
<th>Date</th>
<th>Package</th>
<th>Summary</th>
<th>Source</th>
</tr>
</thead>
<tbody>
{% for release in site.data.releases %}
  <tr>
     <td>{{ release.date }}</td>
     <td>{{ release.name }}</td>
     <td>{{ release.summary }}</td>
     <td><a href="{{ release.download }}">Download</a></td>
  </tr>
{% endfor %}
</tbody>
</table>

