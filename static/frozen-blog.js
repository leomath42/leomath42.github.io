class Page {
	// maxPage = 3;
	actualPage = 1;

	constructor(pages, items){
		this.pages = pages;
		this.items = items;
		this.maxPage = items.length - 2 ;

		items.forEach((item, index) => {
			console.log(index);
			if(index == 0 ){
				item.addEventListener('click', (event) =>{
					this.previousPage();
				});
			}
			else if(index + 1 == items.length ){
				item.addEventListener('click', (event) =>{
					this.nextPage();
				});
			}
			else {
				item.addEventListener('click', (event) =>{
					this.toPage(index);
				});
			}
		});
	}
	toPage(number){
		this.#changePage(number);
		console.log(number);
	};

	previousPage(){
		if(this.actualPage > 1){
			this.#changePage(this.actualPage - 1);
		}

	};
	nextPage() {
		if(this.actualPage < this.maxPage){
			this.#changePage(this.actualPage + 1);
		}

	};

	#changePage(number) {
		this.pages[this.actualPage - 1].style['display'] = 'none';
		this.items[this.actualPage].classList.remove('active');

		this.pages[number - 1].style['display'] = 'block';
		this.items[number].classList.add('active');

		this.actualPage = number;

		if(1 < this.actualPage && this.actualPage <  this.maxPage){
			this.items[0].classList.remove('disabled');
			this.items[this.maxPage + 1].classList.remove('disabled');
		}
		else if(1 == this.actualPage){
			this.items[0].classList.add('disabled');
			this.items[this.maxPage + 1].classList.remove('disabled');
		}
		else if(this.maxPage == this.actualPage){
			this.items[this.maxPage + 1].classList.add('disabled');
			this.items[0].classList.remove('disabled');
		}
	};
};
