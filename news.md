---
title: News
layout: default
permalink: /news
---

<table  class="table-striped">
<colgroup>
<col width="25%" />
<col width="75%" />
</colgroup>
<thead >
<tr class="header">
<th>Date</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
{% for item in site.data.news %}
  <tr>
    <td>{{ item.date }}</td>
    <td>{{ item.summary }}</td>
  </tr>
{% endfor %}
</tbody>
</table>

