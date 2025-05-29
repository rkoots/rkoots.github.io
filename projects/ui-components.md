---
layout: default
title: Free UI Components
permalink: /free-ui-components/
description: FREE

components:
- name: Button
  description: A simple button component
  preview: asd
- name: Card
  description: A card layout component
  preview: asd
---

<h1>Free Open-Source UI Library with Live Previews — Buttons, Cards, Modals & More</h1>

<div class="components-grid">
  {% for component in page.components %}
    <div class="tool-card">
      <h3>{{ component.name }}</h3>
      <p>{{ component.description }}</p>
      <div>{{ component.preview }}</div>
    </div>
  {% endfor %}
</div>
