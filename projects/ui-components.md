---
layout: default
title: Free UI Components Library – CSS, HTML & JS
permalink: /free-ui-components/
description: A curated collection of free UI components built with HTML, CSS, and JavaScript. Instantly usable, customizable, and perfect for modern web design and development.
keywords: free ui components, html css js ui kits, open source components, frontend design blocks, web design elements, reusable components
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.11/clipboard.min.js"></script>
<script type="text/javascript">
  document.addEventListener("DOMContentLoaded", function () {
    var clipboard = new ClipboardJS('article button', {
      text: function (trigger) {
        const article = trigger.closest("article");
        const div = article.querySelector("div");
        const style = article.querySelector("style");

        if (div && style) {
          const loaderId = div.id;
          const html = `<div class="loader"></div>`;
          const css = style.innerHTML.replaceAll('#' + loaderId, '.loader');
          return `<!-- HTML -->\n${html}\n\n/* CSS */\n${css}`;
        }
        return '';
      }
    });

    clipboard.on('success', function (e) {
      e.trigger.textContent = "Copied!";
      setTimeout(() => {
        e.trigger.textContent = "Copy the CSS";
      }, 1800);
      e.clearSelection();
    });
  });
</script>

# 🎨 Free UI Components Gallery

Explore a visually rich collection of **HTML & CSS-based UI components**. Perfect for modern web apps, portfolios, and creative experiments. No dependencies, just clean, animated visuals.
<link rel="stylesheet" href="/projects/free-ui-components/style.css">
<section class="load-container">
<article><div id="l1"></div>
<style>#l1 {
  --s: 25px;

--_d: calc(0.353*var(--s));
width: calc(var(--s) + var(--_d));
aspect-ratio: 1;
clip-path: polygon(var(--_d) 0,100% 0,100% calc(100% - var(--_d)),calc(100% - var(--_d)) 100%,0 100%,0 var(--_d));
background:
conic-gradient(from -90deg at var(--s) var(--_d),
#fff 135deg,#666 0 270deg,#aaa 0);
animation: l1 1s infinite cubic-bezier(0.5,300,0.5,-300);
}
@keyframes l1{
50%,100% {transform:translateY(0.1px)}
}</style>
<button>Copy the CSS</button>
</article>

        <article>
            <div id="l2"></div>
            <style>#l2 {
--s: 25px;

--_d: calc(0.353*var(--s));
width: calc(var(--s) + var(--_d));
aspect-ratio: 1;
display: grid;
filter: drop-shadow(0 0 0 #fff);
animation: l2 0.8s infinite;
}
#l2:before {
content: "";
clip-path: polygon(var(--_d) 0,100% 0,100% calc(100% - var(--_d)),calc(100% - var(--_d)) 100%,0 100%,0 var(--_d));
background:
conic-gradient(from -90deg at var(--s) var(--_d),
#fff 135deg,#666 0 270deg,#aaa 0);
}
@keyframes l2{
50% {filter:drop-shadow(0 0 5px #fff)}
}</style>
<button>Copy the CSS</button>
</article>
<article>
<div id="l3"></div>
<style>#l3 {
--s: 25px;
--_d: calc(0.353*var(--s));

height: calc(var(--s) + var(--_d));
aspect-ratio: 1;
display: grid;
}
#l3:before {
content: "";
height: 100%;
margin: auto 0;
clip-path: polygon(var(--_d) 0,100% 0,100% calc(100% - var(--_d)),calc(100% - var(--_d)) 100%,0 100%,0 var(--_d));
background:
conic-gradient(from -90deg at var(--s) var(--_d),
#fff 135deg,#666 0 270deg,#aaa 0);
animation: l3 .8s infinite alternate;
}
@keyframes l3{
100% {height:40%}
}</style>
<button>Copy the CSS</button>
</article>
<article>
<div id="l4"></div>
<style>#l4 {
--s: 25px;

--_d: calc(0.353*var(--s));
width: calc(var(--s) + var(--_d));
aspect-ratio: 1;
display: grid;
}
#l4:before,
#l4:after {
content:"";
clip-path:polygon(var(--_d) 0,100% 0,100% calc(100% - var(--_d)),calc(100% - var(--_d)) 100%,0 100%,0 var(--_d));
background:
conic-gradient(from -90deg at var(--s) var(--_d),
#fff 135deg,#666 0 270deg,#aaa 0);
animation: l4 1.2s infinite;
}
#l4:before {
z-index: 1;
margin-bottom: calc(var(--_d)/-2 - 1px);
}
#l4:after {
margin-top: calc(var(--_d)/-2 - 1px);
animation-delay: 0.6s
}
@keyframes l4{
0%     {transform: translate(0)}
16.67% {transform: translate(-10px)}
33.33% {transform: translate(10px)}
50%,
100%   {transform: translate(0)}
}</style>
<button>Copy the CSS</button>
</article>
<article>
<div id="l5"></div>
<style>#l5 {
--s: 25px;

--_d: calc(0.353*var(--s));
width: calc(var(--s) + var(--_d));
aspect-ratio: 1;
display: flex;
}
#l5:before,
#l5:after {
content: "";
flex: 1;
clip-path: polygon(var(--_d) 0,100% 0,100% calc(100% - var(--_d)),calc(100% - var(--_d)) 100%,0 100%,0 var(--_d));
background:
conic-gradient(from -90deg at calc(100% - var(--_d)) var(--_d),
#fff 135deg,#666 0 270deg,#aaa 0);
animation: l5 1.2s infinite;
}
#l5:before {
margin-right: calc(var(--_d)/-2 - 1px);
}
#l5:after {
margin-left: calc(var(--_d)/-2 - 1px);
animation-delay: 0.6s
}
@keyframes l5{
0%     {transform: translateY(0)}
16.67% {transform: translateY(-10px)}
33.33% {transform: translateY(10px)}
50%,
100%   {transform: translateY(0)}
}</style>
<button>Copy the CSS</button>
</article>
<article>
<div id="l6"></div>
<style>#l6 {
--s: 20px;

--_d: calc(0.353*var(--s));
width: calc(var(--s) + var(--_d));
aspect-ratio: 1;
display: grid;
}
#l6:before,
#l6:after {
content: "";
grid-area: 1/1;
clip-path: polygon(var(--_d) 0,100% 0,100% calc(100% - var(--_d)),calc(100% - var(--_d)) 100%,0 100%,0 var(--_d));
background:
conic-gradient(from -90deg at calc(100% - var(--_d)) var(--_d),
#fff 135deg,#666 0 270deg,#aaa 0);
animation: l6 2s infinite;
}
#l6:after {
animation-delay:-1s;
}
@keyframes l6{
0%  {transform:translate(0,0)}
25% {transform:translate(30px,0)}
50% {transform:translate(30px,30px)}
75% {transform:translate(0,30px)}
100%{transform:translate(0,0)}
}</style>
<button>Copy the CSS</button>
</article>
<article>
<div id="l7"></div>
<style>#l7 {
--s: 25px;
--g: 5px;

height: calc(1.353*var(--s) + var(--g));
aspect-ratio: 3;
background:
linear-gradient(#ff1818 0 0) left/33% 100% no-repeat,
conic-gradient(from -90deg at var(--s) calc(0.353*var(--s)),
#fff 135deg,#666 0 270deg,#aaa 0);
background-blend-mode: multiply;
--_m:
linear-gradient(to bottom right,
#0000 calc(0.25*var(--s)),#000 0 calc(100% - calc(0.25*var(--s)) - 1.414*var(--g)),#0000 0),
conic-gradient(from -90deg at right var(--g) bottom var(--g),#000 90deg,#0000 0);
-webkit-mask: var(--_m);
mask: var(--_m);
background-size:   calc(100%/3) 100%;
-webkit-mask-size: calc(100%/3) 100%;
mask-size: calc(100%/3) 100%;
-webkit-mask-composite: source-in;
mask-composite: intersect;
animation: l7 steps(3) 1.5s infinite;
}
@keyframes l7 {
to {background-position: 150% 0%}
}</style>
<button>Copy the CSS</button>
</article>
<article>
<div id="l8"></div>
<style>#l8 {
--s: 25px;
--g: 5px;

height: calc(1.353*var(--s) + var(--g));
aspect-ratio: 3;
display: grid;
justify-items: end;
overflow: hidden;
--_m: linear-gradient(90deg,#0000,#000 15px calc(100% - 15px),#0000);
-webkit-mask: var(--_m);
mask: var(--_m);
}
#l8:before {
content: "";
width: calc(4*100%/3);
background:
conic-gradient(from -90deg at var(--s) calc(0.353*var(--s)),
#fff 135deg,#666 0 270deg,#aaa 0);
--_m:
linear-gradient(to bottom right,
#0000 calc(0.25*var(--s)),#000 0 calc(100% - calc(0.25*var(--s)) - 1.414*var(--g)),#0000 0),
conic-gradient(from -90deg at right var(--g) bottom var(--g),#000 90deg,#0000 0);
-webkit-mask: var(--_m);
mask: var(--_m);
background-size:   calc(100%/4) 100%;
-webkit-mask-size: calc(100%/4) 100%;
mask-size: calc(100%/4) 100%;
-webkit-mask-composite: source-in;
mask-composite: intersect;
animation: l8 1s infinite linear;
}
@keyframes l8 {
to {transform:translate(calc(100%/4))}
}</style>
<button>Copy the CSS</button>
</article>
<article>
<div id="l9"></div>
<style>#l9 {
--s: 25px;
--g :5px;

width: calc(2*(1.353*var(--s) + var(--g)));
aspect-ratio: 1;
background:
linear-gradient(#ff1818 0 0) left/50% 100% no-repeat,
conic-gradient(from -90deg at var(--s) calc(0.353*var(--s)),
#fff 135deg,#666 0 270deg,#aaa 0);
background-blend-mode: multiply;
--_m:
linear-gradient(to bottom right,
#0000 calc(0.25*var(--s)),#000 0 calc(100% - calc(0.25*var(--s)) - 1.414*var(--g)),#0000 0),
conic-gradient(from -90deg at right var(--g) bottom var(--g),#000 90deg,#0000 0);
-webkit-mask: var(--_m);
mask: var(--_m);
background-size:   50% 50%;
-webkit-mask-size: 50% 50%;
mask-size: 50% 50%;
-webkit-mask-composite: source-in;
mask-composite: intersect;
animation: l9 1.5s infinite;
}
@keyframes l9 {
0%,12.5%    {background-position:0% 0%,0 0}
12.6%,37.5% {background-position:100% 0%,0 0}
37.6%,62.5% {background-position:100% 100%,0 0}
62.6%,87.5% {background-position:0% 100%,0 0}
87.6%,100%  {background-position:0% 0%,0 0}
}</style>
<button>Copy the CSS</button>
</article>
<article>
<div id="l10"></div>
<style>#l10 {
--s: 25px;
--g :5px;

width: calc(3*(1.353*var(--s) + var(--g)));
display: grid;
justify-items: end;
aspect-ratio: 3;
overflow: hidden;
--_m: linear-gradient(90deg,#0000,#000 15px calc(100% - 15px),#0000);
-webkit-mask: var(--_m);
mask: var(--_m);
}
#l10:before {
content: "";
width: 200%;
background:
linear-gradient(90deg,#ff1818 50%,#0000 0),
conic-gradient(from -90deg at var(--s) calc(0.353*var(--s)),
#fff 135deg,#666 0 270deg,#aaa 0);
background-blend-mode: multiply;
--_m:
linear-gradient(to bottom right,
#0000 calc(0.25*var(--s)),#000 0 calc(100% - calc(0.25*var(--s)) - 1.414*var(--g)),#0000 0),
conic-gradient(from -90deg at right var(--g) bottom var(--g),#000 90deg,#0000 0);
-webkit-mask: var(--_m);
mask: var(--_m);
background-size:   calc(100%/3) 100%, calc(100%/6) 100%;
-webkit-mask-size: calc(100%/6) 100%;
mask-size: calc(100%/6) 100%;
-webkit-mask-composite: source-in;
mask-composite: intersect;
animation: l10 1s infinite linear;
}
@keyframes l10 {
to {transform:translate(calc(100%/3))}
}</style>
<button>Copy the CSS</button>
</article>
<article>
<div id="l11"></div>
<style>#l11 {
--s: 40px;
--g: 5px;

height: calc(var(--s) + var(--g));
aspect-ratio: 3;
background:
radial-gradient(calc(var(--s)/sqrt(2)) at calc(50% - .1*var(--s)) calc(50% - .2*var(--s)),#0000 5%,60%,#111 98%),
linear-gradient(#FE4365 0 0) no-repeat #fff;
background-size: calc(100%/3) 100%;
mask: radial-gradient(calc(var(--s)/2),#000 calc(100% - 1px),#0000) 0/calc(100%/3) 100%;
animation: l11 steps(3) 1.5s infinite;
}
@keyframes l11 {
to {background-position:0 ,150%}
}</style>
<button>Copy the CSS</button>
</article>
<article>
<div id="l12"></div>
<style>#l12 {
--s: 40px;
--g: 5px;

height: calc(2*(var(--s) + var(--g)));
aspect-ratio: 1;
background:
radial-gradient(calc(var(--s)/sqrt(2)) at calc(50% - .1*var(--s)) calc(50% - .2*var(--s)),#0000 5%,60%,#111 98%),
linear-gradient(#FE4365 0 0) no-repeat #fff;
background-size: 50% 50%;
mask: radial-gradient(calc(var(--s)/2),#000 calc(100% - 1px),#0000) 0 0/50% 50%;
animation: l12 steps(3) 1.5s infinite;
}
@keyframes l12 {
0%,12.5%    {background-position:0 0}
12.6%,37.5% {background-position:0 0,100% 0}
37.6%,62.5% {background-position:0 0,100% 100%}
62.6%,87.5% {background-position:0 0,0 100%}
87.6%,100%  {background-position:0 0}
}</style>
<button>Copy the CSS</button>
</article>
</section>
