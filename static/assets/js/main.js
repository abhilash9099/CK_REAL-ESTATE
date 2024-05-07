/**
* Template Name: Ninestars
* Template URL: https://bootstrapmade.com/ninestars-free-bootstrap-3-theme-for-creative/
* Updated: Mar 23 2024 with Bootstrap v5.3.3
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

(function() {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  mobileNavToggleBtn.addEventListener('click', mobileNavToogle);

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .has-dropdown i').forEach(navmenu => {
    navmenu.addEventListener('click', function(e) {
      if (document.querySelector('.mobile-nav-active')) {
        e.preventDefault();
        this.parentNode.classList.toggle('active');
        this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
        e.stopImmediatePropagation();
      }
    });
  });

  /**
   * Preloader
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  scrollTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);



  
  // document.querySelectorAll('.isotope-filters li').forEach(navmenu => {
  //   navmenu.addEventListener('click', (e) => {
  //     var selectedVal =e.target.dataset.filter;
      
  //     document.querySelectorAll(".portfolio-item").forEach(item=>{
        
  //       if(selectedVal==""){
  //         item.style.display='block';
  //       }else{
  //         if(item.classList.contains(selectedVal)){
  //           item.style.display='block';
  //         }
  //         else{
  //           item.style.display='none';
  //         }
  //       }
  //     })
  //   });

  // });

  /**
   * Animation on scroll function and init
   */
  // function aosInit() {
  //   AOS.init({
  //     duration: 600,
  //     easing: 'ease-in-out',
  //     once: true,
  //     mirror: false
  //   });
  // }
  // window.addEventListener('load', aosInit);

  /**
   * Initiate glightbox
   */
  // const glightbox = GLightbox({
  //   selector: '.glightbox'
  // });

  /**
   * Init isotope layout and filters
   */
  // document.querySelectorAll('.isotope-layout').forEach(function(isotopeItem) {
  //   let layout = isotopeItem.getAttribute('data-layout') ?? 'masonry';
  //   let filter = isotopeItem.getAttribute('data-default-filter') ?? '*';
  //   let sort = isotopeItem.getAttribute('data-sort') ?? 'original-order';

  //   let initIsotope;
  //   imagesLoaded(isotopeItem.querySelector('.isotope-container'), function() {
  //     initIsotope = new Isotope(isotopeItem.querySelector('.isotope-container'), {
  //       itemSelector: '.isotope-item',
  //       layoutMode: layout,
  //       filter: filter,
  //       sortBy: sort
  //     });
  //   });

  //   isotopeItem.querySelectorAll('.isotope-filters li').forEach(function(filters) {
  //     filters.addEventListener('click', function() {
  //       isotopeItem.querySelector('.isotope-filters .filter-active').classList.remove('filter-active');
  //       this.classList.add('filter-active');
  //       initIsotope.arrange({
  //         filter: this.getAttribute('data-filter')
  //       });
  //       if (typeof aosInit === 'function') {
  //         aosInit();
  //       }
  //     }, false);
  //   });

  // });

  /**
   * Frequently Asked Questions Toggle
   */
  document.querySelectorAll('.faq-item h3, .faq-item .faq-toggle').forEach((faqItem) => {
    faqItem.addEventListener('click', () => {
      faqItem.parentNode.classList.toggle('faq-active');
    });
  });

  /**
   * Init swiper sliders
   */
  // function initSwiper() {
  //   document.querySelectorAll('.swiper').forEach(function(swiper) {
  //     let config = JSON.parse(swiper.querySelector('.swiper-config').innerHTML.trim());
  //     new Swiper(swiper, config);
  //   });
  // }
  // window.addEventListener('load', initSwiper);

  /**
   * Correct scrolling position upon page load for URLs containing hash links.
   */
  window.addEventListener('load', function(e) {
    if (window.location.hash) {
      const section = document.querySelector(window.location.hash);
      if (section) {
        section.scrollIntoView({
          behavior: "smooth",
          block: "start"
        });
      }
    }
  });

  /**
   * Auto-Active Navmenu Links
   */
  let navmenulinks = document.querySelectorAll('.navmenu a');

  function navmenuActive() {
    navmenulinks.forEach(navmenulink => {
      if (!navmenulink.hash) return;
      let section = document.querySelector(navmenulink.hash);
      if (!section) return;
      let position = window.scrollY + 200;
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        document.querySelectorAll('.navmenu a.active').forEach(link => link.classList.remove('active'));
        navmenulink.classList.add('active');
      } else {
        navmenulink.classList.remove('active');
      }
    })
  }
  window.addEventListener('load', navmenuActive);
  document.addEventListener('scroll', navmenuActive);

})();

function searchProperty(){
  var property_type = document.getElementById("property_type").value;
  var from_price = document.getElementById("from_price").value;
  var to_price = document.getElementById("to_price").value;

  from_price = (from_price)?parseFloat(from_price):0;
  to_price = (to_price)?parseFloat(to_price):0;
  
  document.querySelectorAll(".portfolio-item").forEach(item=>{
      

    if(property_type=="" && from_price=="" && to_price ==""){
      item.style.display='block';
    }else{

      itemPrice =parseFloat(item.id.replace(',',''));
      if(property_type=="" && from_price!="" && to_price !=""){
          if(itemPrice >= from_price && itemPrice <= to_price){
            item.style.display='block';
          }else{
            item.style.display='none';
          }
      }
      if(property_type!="" && from_price=="" && to_price ==""){
        if(item.classList.contains(property_type)){
          item.style.display='block';
        }else{
          item.style.display='none';
        }
    }
      else if(property_type!=""  && from_price!="" && to_price !=""){
        if(item.classList.contains(property_type) && itemPrice >= from_price && itemPrice <= to_price){
          item.style.display='block';
        }
        else{
          item.style.display='none';
        }
      }
    }
  })
}