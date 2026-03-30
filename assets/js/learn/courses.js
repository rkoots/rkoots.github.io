/* RKoots Learning Platform — Courses Loader
   Combines courses-p1.js and courses-p2.js into window.LEARN_COURSES
   Scripts must be loaded in order: courses-p1.js, courses-p2.js, courses.js
*/
(function () {
  'use strict';
  var p1 = window.COURSES_P1 || [];
  var p2 = window.COURSES_P2 || [];
  window.LEARN_COURSES = p1.concat(p2);
})();
