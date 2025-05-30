---
layout: iconlayout
title: Free UI Components Library – CSS, HTML & JS
permalink: /free-ui-components/
description: A curated collection of free UI components built with HTML, CSS, and JavaScript. Instantly usable, customizable, and perfect for modern web design and development.
keywords: free ui components, html css js ui kits, open source components, frontend design blocks, web design elements, reusable components
---

<section class="load-container threed">
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


<section class="load-container arcade">
        <article>
          <div id="l1"></div>
          <style>#l1 {
   width: 45px;
   height: 30px;
   animation: l1 2s infinite linear;
}
@keyframes l1{
  0%,
  25%  {background:
          linear-gradient(#e50021 0 0) 50% 0/66% 100% no-repeat}
  25.1%,
  50%  {background:
          linear-gradient(#004ce4 0 0) 0 0/100% 50% no-repeat,
          linear-gradient(#004ce4 0 0) 0 0/33% 100% no-repeat}
  50.1%,
  75%  {background:
          linear-gradient(#00e622 0 0) 100% 0/66% 50% no-repeat,
          linear-gradient(#00e622 0 0) 0 100%/66% 50% no-repeat}
  75.1%,
  100% {background:
          linear-gradient(#9d0be6 0 0) 0 100%/100% 50% no-repeat,
          linear-gradient(#9d0be6 0 0) 50% 0 /33%  50% no-repeat}
}</style>
          <button>Copy the CSS</button>
        </article>
        <article>
          <div id="l2"></div>
          <style>#l2 {
  width: 45px;
  height: 30px;
  background:
    linear-gradient(#004ce4 0 0) 0 100%/100% 50%,
    linear-gradient(#004ce4 0 0) 0 0   /calc(100%/3) 100%;
  background-repeat: no-repeat;
  position: relative;
  clip-path: inset(-100% 0 0 0);
  animation: l2-0 2s infinite steps(4);
}
#l2::before,
#l2::after {
  content: "";
  position: absolute;
  inset:-50% 0 50%;
  background:
    linear-gradient(#00e622 0 0) 0 0      /calc(2*100%/3) 50%,
    linear-gradient(#00e622 0 0) 100% 100%/calc(2*100%/3) 50%;
  background-repeat: no-repeat;
  animation: inherit;
  animation-name: l2-1;
}
#l2::after {
  inset:-100% 0 100%;
  background:
    linear-gradient(#e50021 0 0) 0    0/100%         50%,
    linear-gradient(#e50021 0 0) 100% 0/calc(100%/3) 100%;
  background-repeat: no-repeat; 
  animation-name: l2-2;
}
@keyframes l2-0{
  0%       {transform: translateY(-250%);clip-path: inset(100% 0 0 0)}
  25%,100% {transform: translateY(0);clip-path: inset(-100% 0 0 0)}
}
@keyframes l2-1{
  0% ,25%  {transform: translateY(-250%)}
  50%,100% {transform: translateY(0)}
}
@keyframes l2-2{
  0% ,50%  {transform: translateY(-250%)}
  75%,100% {transform: translateY(0)}
}</style>
          <button>Copy the CSS</button>
        </article>
        <article>
          <div id="l3"></div>
          <style>#l3 {
  width: 80px;
  height: 70px;
  border: 5px solid #000;
  padding: 0 8px;
  box-sizing: border-box;
  background:
    linear-gradient(#fff 0 0) 0    0/8px 20px,
    linear-gradient(#fff 0 0) 100% 0/8px 20px,
    radial-gradient(farthest-side,#fff 90%,#0000) 0 5px/8px 8px content-box,
    #000;
  background-repeat: no-repeat; 
  animation: l3 2s infinite linear;
}
@keyframes l3{
  25% {background-position: 0 0   ,100% 100%,100% calc(100% - 5px)}
  50% {background-position: 0 100%,100% 100%,0    calc(100% - 5px)}
  75% {background-position: 0 100%,100%    0,100% 5px}
}</style>
          <button>Copy the CSS</button>
        </article>
        <article>
          <div id="l4"></div>
          <style>#l4 {
  width: 50px;
  aspect-ratio: 1;
  border-radius: 50%;
  background:
    radial-gradient(farthest-side,#000 98%,#0000) 55% 20%/8px 8px no-repeat,  
    #ffcc00;
  box-shadow: 2px -6px 12px 0px inset rgba(0, 0, 0, 0.7);
  animation: l4 .5s infinite steps(5) alternate;
}
@keyframes l4{ 
    0% {clip-path: polygon(50% 50%,100%   0,100% 0,0 0,0 100%,100% 100%,100% 100%)}
  100% {clip-path: polygon(50% 50%,100% 65%,100% 0,0 0,0 100%,100% 100%,100%  35%)}
}</style>
          <button>Copy the CSS</button>
        </article>
        <article>
          <div id="l5"></div>
          <style>#l5 {
  width: 90px;
  height: 24px;
  padding: 2px 0;
  box-sizing: border-box;
  display: flex;
  animation: l5-0 3s infinite steps(6);
  background:
    linear-gradient(#000 0 0) 0 0/0% 100% no-repeat,
    radial-gradient(circle 3px,#eeee89 90%,#0000) 0 0/20% 100%
    #000;
  overflow: hidden;
}
#l5::before {
  content: "";
  width: 20px;
  transform: translate(-100%);
  border-radius: 50%;
  background: #ffff2d;
  animation: 
    l5-1 .25s .153s infinite steps(5) alternate,
    l5-2  3s        infinite linear;
}
@keyframes l5-1{ 
    0% {clip-path: polygon(50% 50%,100%   0,100% 0,0 0,0 100%,100% 100%,100% 100%)}
  100% {clip-path: polygon(50% 50%,100% 65%,100% 0,0 0,0 100%,100% 100%,100%  35%)}
}
@keyframes l5-2{ 
  100% {transform: translate(90px)}
}
@keyframes l5-0{ 
  100% {background-size:120% 100%,20% 100%}
}</style>
          <button>Copy the CSS</button>
        </article>
        <article>
          <div id="l6"></div>
          <style>#l6 {
  width: 80px;
  height: 60px;
  box-sizing: border-box;
  background:
    linear-gradient(#fff 0 0) left /calc(50% - 15px) 8px no-repeat,
    linear-gradient(#fff 0 0) right/calc(50% - 15px) 8px no-repeat,
    conic-gradient(from 135deg at top,#0000, red 1deg 90deg,#0000 91deg) bottom/14px 8px repeat-x,
    #000;
  border-bottom: 2px solid red;
  position: relative;
  overflow: hidden;
  animation: l6-0 1s infinite linear;
}
#l6::before {
  content: "";
  position: absolute;
  width: 10px;
  height: 14px;
  background: lightblue;
  left: -5px;
  animation:
    l6-1 2s infinite cubic-bezier(0,100,1,100), 
    l6-2 2s infinite linear;
}
@keyframes l6-0{
  50% { background-position: left,right,bottom -2px left -4px}
}
@keyframes l6-1{
  0%,27%   {bottom: calc(50% + 4px)}
  65%,100% {bottom: calc(50% + 4.1px)}
}
@keyframes l6-2{
  100% {left:100%}
}</style>
          <button>Copy the CSS</button>
        </article>
        <article>
          <div id="l7"></div>
          <style>#l7 {
  width: 70px;
  height: 50px;
  box-sizing: border-box;
  background:
    conic-gradient(from 135deg at top,#0000, #fff 1deg 90deg,#0000 91deg) right -20px bottom 8px/18px 9px,
    linear-gradient(#fff 0 0) bottom/100% 8px,
    #000;
  background-repeat: no-repeat;
  border-bottom: 8px solid #000;
  position: relative;
  animation: l7-0 2s infinite linear;
}
#l7::before {
  content: "";
  position: absolute;
  width: 10px;
  height: 14px;
  background: lightblue;
  left: 10px;
  animation: l7-1 2s infinite cubic-bezier(0,200,1,200);
}
@keyframes l7-0{
  100% { background-position: left -20px bottom 8px,bottom}
}
@keyframes l7-1{
  0%,50%   {bottom: 8px}
  90%,100% {bottom: 8.1px}
}</style>
          <button>Copy the CSS</button>
        </article>
        <article>
          <div id="l8"></div>
          <style>#l8 {
  width: fit-content;
  font-size: 17px;
  font-family: monospace;
  line-height: 1.4;
  font-weight: bold;
  --c: no-repeat linear-gradient(#000 0 0); 
  background: var(--c),var(--c),var(--c),var(--c),var(--c),var(--c),var(--c);
  background-size: calc(1ch + 1px) 100%;
  border-bottom: 10px solid #0000; 
  position: relative;
  animation: l8-0 3s infinite linear;
  clip-path: inset(-20px 0);
}
#l8::before {
  content:"Loading";
}
#l8::after {
  content: "";
  position: absolute;
  width: 10px;
  height: 14px;
  background: #25adda;
  left: -10px;
  bottom: 100%;
  animation: l8-1 3s infinite linear;
}
@keyframes l8-0{
   0%,
   12.5% {background-position: calc(0*100%/6) 0   ,calc(1*100%/6)    0,calc(2*100%/6)    0,calc(3*100%/6)    0,calc(4*100%/6)    0,calc(5*100%/6)    0,calc(6*100%/6) 0}
   25%   {background-position: calc(0*100%/6) 40px,calc(1*100%/6)    0,calc(2*100%/6)    0,calc(3*100%/6)    0,calc(4*100%/6)    0,calc(5*100%/6)    0,calc(6*100%/6) 0}
   37.5% {background-position: calc(0*100%/6) 40px,calc(1*100%/6) 40px,calc(2*100%/6)    0,calc(3*100%/6)    0,calc(4*100%/6)    0,calc(5*100%/6)    0,calc(6*100%/6) 0}
   50%   {background-position: calc(0*100%/6) 40px,calc(1*100%/6) 40px,calc(2*100%/6) 40px,calc(3*100%/6)    0,calc(4*100%/6)    0,calc(5*100%/6)    0,calc(6*100%/6) 0}
   62.5% {background-position: calc(0*100%/6) 40px,calc(1*100%/6) 40px,calc(2*100%/6) 40px,calc(3*100%/6) 40px,calc(4*100%/6)    0,calc(5*100%/6)    0,calc(6*100%/6) 0}
   75%   {background-position: calc(0*100%/6) 40px,calc(1*100%/6) 40px,calc(2*100%/6) 40px,calc(3*100%/6) 40px,calc(4*100%/6) 40px,calc(5*100%/6)    0,calc(6*100%/6) 0}
   87.4% {background-position: calc(0*100%/6) 40px,calc(1*100%/6) 40px,calc(2*100%/6) 40px,calc(3*100%/6) 40px,calc(4*100%/6) 40px,calc(5*100%/6) 40px,calc(6*100%/6) 0}
   100%  {background-position: calc(0*100%/6) 40px,calc(1*100%/6) 40px,calc(2*100%/6) 40px,calc(3*100%/6) 40px,calc(4*100%/6) 40px,calc(5*100%/6) 40px,calc(6*100%/6) 40px}
}
@keyframes l8-1{
  100% {left:115%}
}</style>
          <button>Copy the CSS</button>
        </article>
        <article>
          <div id="l9"></div>
          <style>#l9 {
  width: fit-content;
  font-size: 17px;
  font-family: monospace;
  line-height: 1.4;
  font-weight: bold;
  background: 
    linear-gradient(#000 0 0) left ,
    linear-gradient(#000 0 0) right;
  background-repeat: no-repeat; 
  border-right: 5px solid #0000;
  border-left: 5px solid #0000;
  background-origin: border-box;
  position: relative;
  animation: l9-0 2s infinite;
}
#l9::before {
  content:"Loading";
}
#l9::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 0;
  width: 22px;
  height: 60px;
  background: 
   linear-gradient(90deg,#000 4px,#0000 0 calc(100% - 4px),#000 0) bottom            /22px 20px,
   linear-gradient(90deg,red  4px,#0000 0 calc(100% - 4px),red  0) bottom 10px left 0/22px 6px,
   linear-gradient(#000 0 0) bottom 3px left 0  /22px 8px,
   linear-gradient(#000 0 0) bottom 0   left 50%/8px  16px;
 background-repeat: no-repeat;
 animation: l9-1 2s infinite;
}
@keyframes l9-0{
  0%,25%    {background-size: 50% 100%}
  25.1%,75% {background-size: 0 0,50% 100%}
  75.1%,100%{background-size: 0 0,0 0}
}
@keyframes l9-1{
  25%   { background-position:bottom, bottom 54px left 0,bottom 3px left 0,bottom 0 left 50%;left:0}
  25.1% { background-position:bottom, bottom 10px left 0,bottom 3px left 0,bottom 0 left 50%;left:0}
  50%   { background-position:bottom, bottom 10px left 0,bottom 3px left 0,bottom 0 left 50%;left:calc(100% - 22px)}
  75%   { background-position:bottom, bottom 54px left 0,bottom 3px left 0,bottom 0 left 50%;left:calc(100% - 22px)}
  75.1% { background-position:bottom, bottom 10px left 0,bottom 3px left 0,bottom 0 left 50%;left:calc(100% - 22px)}
}</style>
          <button>Copy the CSS</button>
        </article>
        <article>
          <div id="l10"></div>
          <style>#l10 {
  width: fit-content;
  font-size: 17px;
  font-family: monospace;
  line-height: 1.4;
  font-weight: bold;
  padding: 30px 2px 50px;
  background: linear-gradient(#000 0 0) 0 0/100% 100% content-box padding-box no-repeat; 
  position: relative;
  overflow: hidden;
  animation: l10-0 2s infinite cubic-bezier(1,175,.5,175);
}
#l10::before {
  content:"Loading";
  display:inline-block;
  animation: l10-2 2s infinite;
}
#l10::after {
  content:"";
  position: absolute;
  width: 34px;
  height: 28px;
  top: 110%;
  left: calc(50% - 16px);
  background:
    linear-gradient(90deg,#0000 12px,#f92033 0 22px,#0000 0 26px,#fdc98d 0 32px,#0000) bottom 26px left 50%,
    linear-gradient(90deg,#0000 10px,#f92033 0 28px,#fdc98d 0 32px,#0000 0) bottom 24px  left 50%,
    linear-gradient(90deg,#0000 10px,#643700 0 16px,#fdc98d 0 20px,#000 0 22px,#fdc98d 0 24px,#000 0 26px,#f92033 0 32px,#0000 0) bottom 22px left 50%,
    linear-gradient(90deg,#0000 8px,#643700 0 10px,#fdc98d 0 12px,#643700 0 14px,#fdc98d 0 20px,#000 0 22px,#fdc98d 0 28px,#f92033 0 32px,#0000 0) bottom 20px left 50%,
    linear-gradient(90deg,#0000 8px,#643700 0 10px,#fdc98d 0 12px,#643700 0 16px,#fdc98d 0 22px,#000 0 24px,#fdc98d 0 30px,#f92033 0 32px,#0000 0) bottom 18px left 50%,
    linear-gradient(90deg,#0000 8px,#643700 0 12px,#fdc98d 0 20px,#000 0 28px,#f92033 0 30px,#0000 0) bottom 16px left 50%,
    linear-gradient(90deg,#0000 12px,#fdc98d 0 26px,#f92033 0 30px,#0000 0) bottom 14px left 50%,
    linear-gradient(90deg,#fdc98d 6px,#f92033 0 14px,#222a87 0 16px,#f92033 0 22px,#222a87 0 24px,#f92033 0 28px,#0000 0 32px,#643700 0) bottom 12px left 50%,
    linear-gradient(90deg,#fdc98d 6px,#f92033 0 16px,#222a87 0 18px,#f92033 0 24px,#f92033 0 26px,#0000 0 30px,#643700 0) bottom 10px left 50%,
    linear-gradient(90deg,#0000 10px,#f92033 0 16px,#222a87 0 24px,#feee49 0 26px,#222a87 0 30px, #643700 0) bottom 8px left 50%,
    linear-gradient(90deg,#0000 12px,#222a87 0 18px,#feee49 0 20px,#222a87 0 30px,#643700 0) bottom 6px left 50%,
    linear-gradient(90deg,#0000 8px,#643700 0 12px,#222a87 0 30px,#643700 0) bottom 4px left 50%,
    linear-gradient(90deg,#0000 6px,#643700 0 14px,#222a87 0 26px,#0000 0) bottom 2px left 50%,
    linear-gradient(90deg,#0000 6px,#643700 0 10px,#0000 0 ) bottom 0px left 50%;
  background-size: 34px 2px;
  background-repeat: no-repeat;
  animation: inherit;
  animation-name: l10-1;
}
@keyframes l10-0{
  0%,30%   { background-position: 0 0px }
  50%,100% { background-position: 0 -0.1px }
}
@keyframes l10-1{
  50%,100% { top:109.5% };
}
@keyframes l10-2{
  0%,30%   { transform:translateY(0); }
  80%,100% { transform:translateY(-260%); }
}</style>
          <button>Copy the CSS</button>
        </article>
      </section>


<section class="load-container arrow">
        <article>
          <div id="l1"></div>
          <style>#l1 {
  width: 100px;
  height: 30px;
  display: flex;
}
#l1:before {
  content: "";
  background: #000;
  width: 15px;
  clip-path: polygon(0 10px,calc(100% - 15px) 10px,calc(100% - 15px) 0,100% 50%,calc(100% - 15px) 100%,calc(100% - 15px) calc(100% - 10px),0 calc(100% - 10px));
  animation: l1 1.5s infinite linear;
}
@keyframes l1 {
  90%,100%{flex-grow: 1}
}</style>
          <button>Copy the CSS</button>
        </article>
        <article>
          <div id="l2"></div>
          <style>#l2 {
  width: 100px;
  height: 30px;
  display: flex;
  justify-content: center;
}
#l2:before,
#l2:after {
  content: "";
  background: #000;
  width: 15px;
  clip-path: polygon(0 10px,calc(100% - 15px) 10px,calc(100% - 15px) 0,100% 50%,calc(100% - 15px) 100%,calc(100% - 15px) calc(100% - 10px),0 calc(100% - 10px));
  animation: l2 1s infinite linear;
}
#l2:before {
  transform: scaleX(-1);
}
@keyframes l2 {
  90%,100%{flex-grow: .5}
}</style>
          <button>Copy the CSS</button>
        </article>
        <article>
          <div id="l3"></div>
          <style>#l3 {
  width: 100px;
  height: 30px;
  display: flex;
}
#l3:before,
#l3:after {
  content: "";
  flex: 1;
  margin: 0 5px;
  background: #000;
  clip-path: polygon(0 10px,calc(100% - 15px) 10px,calc(100% - 15px) 0,100% 50%,calc(100% - 15px) 100%,calc(100% - 15px) calc(100% - 10px),0 calc(100% - 10px));
  animation: l3 .5s infinite alternate;
}
#l3:after {
  --s:-1;
}
@keyframes l3 {
  0%  {transform: scaleX(var(--s,1)) translate(-4px)}
  100%{transform: scaleX(var(--s,1)) translate( 4px)}
}</style>
          <button>Copy the CSS</button>
        </article>
        <article>
          <div id="l4"></div>
          <style>#l4 {
  width: 40px;
  height: 30px;
  display: grid;
}
#l4:before,
#l4:after {
  content: "";
  grid-area: 1/1;
  background: #000;
  clip-path: polygon(0 10px,calc(100% - 15px) 10px,calc(100% - 15px) 0,100% 50%,calc(100% - 15px) 100%,calc(100% - 15px) calc(100% - 10px),0 calc(100% - 10px));
  animation: l4 .5s infinite alternate;
}
#l4:after {
  --s:-1;
}
@keyframes l4 {
  0%  {transform: scale(var(--s,1)) translate(12px,-6px) translate(4px)}
  100%{transform: scale(var(--s,1)) translate(12px,-6px) translate(-4px)}
}</style>
          <button>Copy the CSS</button>
        </article>
        <article>
          <div id="l5"></div>
          <style>#l5 {
  width: 50px;
  height: 30px;
  display: grid;
  overflow: hidden;
}
#l5:before,
#l5:after {
  content: "";
  grid-area: 1/1;
  background: #000;
  clip-path: polygon(0 10px,calc(100% - 15px) 10px,calc(100% - 15px) 0,100% 50%,calc(100% - 15px) 100%,calc(100% - 15px) calc(100% - 10px),0 calc(100% - 10px));
  animation: l5 1s infinite;
  transform: translate(calc(0% + var(--s,0%)));
}
#l5:after {
  --s:-100%;
}
@keyframes l5 {
  80%,100%{transform: translate(calc(100% + var(--s,0%)))}
}</style>
          <button>Copy the CSS</button>
        </article>
        <article>
          <div id="l6"></div>
          <style>#l6 {
  width: 50px;
  height: 60px;
  color: #000;
  display: grid;
}
#l6:before,
#l6:after {
  content: "";
  background:
    linear-gradient(90deg,currentColor calc(100% - 15px),#0000 0) 0 50%/100% 10px,
    conic-gradient(from -136deg at 15px 50%,#0000 ,currentColor 1deg 90deg,#0000 91deg) 35px 0/100% 100%;
  background-repeat: repeat-x;
  animation: l6 1s infinite;
}
#l6:after {
  transform: scaleX(-1);
}
@keyframes l6 {
  80%,100%{background-position: 50px 50%,85px 0}
}</style>
          <button>Copy the CSS</button>
        </article>
        <article>
          <div id="l7"></div>
          <style>#l7 {
  width: 110px;
  height: 30px;
  color: #000;
  display: flex;
  background: 
    linear-gradient(currentColor 0 0) left /30px 10px,
    linear-gradient(currentColor 0 0) right/30px 10px,
    conic-gradient(from -136deg at             15px  50%,#0000 ,currentColor 1deg 90deg,#0000 91deg) 30px              0/100% 100%,
    conic-gradient(from   44deg at calc(100% - 15px) 50%,#0000 ,currentColor 1deg 90deg,#0000 91deg) calc(100% - 30px) 0/100% 100%;
  background-repeat: no-repeat;
  animation: l7 .5s infinite alternate;
}
#l7:before {
  content: "";
  flex: 1;
  background: inherit;
  transform: rotate(90deg);
}
@keyframes l7 {
  90%,100%{width:93px}
}</style>
          <button>Copy the CSS</button>
        </article>
        <article>
          <div id="l8"></div>
          <style>#l8 {
  width: 30px;
  height: 30px;
  color: #000;
  display: flex;
  background: 
    linear-gradient(currentColor 0 0) center/calc(100% - 30px) 10px,
    conic-gradient(from -136deg at right,#0000 ,currentColor 1deg 90deg,#0000 91deg) right/15px 100%,
    conic-gradient(from   44deg at left ,#0000 ,currentColor 1deg 90deg,#0000 91deg) left /15px 100%;
  background-repeat: no-repeat;
  animation: l8 .5s infinite alternate;
}
#l8:before {
  content: "";
  flex: 1;
  background: inherit;
  transform: rotate(90deg);
}
@keyframes l8 {
  90%,100%{width:80px}
}</style>
          <button>Copy the CSS</button>
        </article>
        <article>
          <div id="l9"></div>
          <style>#l9 {
  width: 60px;
  height: 30px;
  color: #000;
  display: flex;
  background: 
    linear-gradient(currentColor 0 0) center/calc(100% - 30px) 10px,
    conic-gradient(from -136deg at right,#0000 ,currentColor 1deg 90deg,#0000 91deg) right/15px 100%,
    conic-gradient(from   44deg at left ,#0000 ,currentColor 1deg 90deg,#0000 91deg) left /15px 100%;
  background-repeat: no-repeat;
  animation: l9 .5s infinite linear alternate;
}
@keyframes l9 {
  0%   {transform: translate(-30px)}
  100% {transform: translate( 30px)}
}</style>
          <button>Copy the CSS</button>
        </article>
        <article>
          <div id="l10"></div>
          <style>#l10 {
  width: 30px;
  height: 60px;
  padding-top: 60px;
  box-sizing: border-box;
  display: grid;
  background: 
    linear-gradient(currentColor 0 0) bottom/10px calc(100% - 15px),
    conic-gradient(from 134deg at top,#0000 ,currentColor 1deg 90deg,#0000 91deg) top/100% 15px;
  background-origin: content-box;
  background-repeat: no-repeat;
  animation: l10-0 2s infinite;
}
#l10:before,
#l10:after {
  content: "";
  grid-area: 1/1;
  background:inherit;
  background-size: 10px calc(100% - 25px),100% 25px;
  animation: l10-1 2s infinite;
}
#l10:after {
  background-size: 10px calc(100% - 30px),100% 30px;
  animation: l10-2 2s infinite;
}
@keyframes l10-0 {
  25%,100% {padding-top:0px}
}
@keyframes l10-1 {
  0%,25%   {margin:60px -10px 0}
  50%,100% {margin:8px  -10px 0}
}
@keyframes l10-2 {
  0%,50%   {margin:60px -15px 0}
  75%,100% {margin:20px -15px 0}
}</style>
          <button>Copy the CSS</button>
        </article>
      </section>