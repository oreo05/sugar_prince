let  lastScroll = 0;
const defaultoffset = 100;
const header = document.querySelector('.header');
const menu = document.querySelector('.header__nav');

const scrollPosition = () => window.pageYOffset || document.documentElement.scrollTop;
const containHide = () => header.classList.contains('hide');

window.addEventListener('scroll', () => {

	if(scrollPosition() > lastScroll && !containHide() && scrollPosition() > defaultoffset) {
		// scroll down
		header.classList.add('hide');
		menu.classList.remove('header__nav_active');
	}
	else if(scrollPosition() < lastScroll && containHide()){
		// scroll up
		menu.classList.remove('header__nav_active');
		header.classList.remove('hide');
	}
	else if(scrollPosition() < lastScroll){
		// scroll up
		menu.classList.remove('header__nav_active');
	}

	lastScroll = scrollPosition();
});

// Burger handler

(function () {
	const burgerItem = document.querySelector('.burger');
	const menu = document.querySelector('.header__nav');
	const menuCloseItem = document.querySelector('.header__nav-close');
	const menuCloseItemMain = document.querySelector('.main');
	burgerItem.addEventListener('click', () => {
		menu.classList.add('header__nav_active');
	});
	menuCloseItem.addEventListener('click', () => {
		menu.classList.remove('header__nav_active');
	});
	menuCloseItemMain.addEventListener('click', () => {
		menu.classList.remove('header__nav_active');
	});
}());

