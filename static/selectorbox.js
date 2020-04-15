class SelectorBox extends ElementBox {
	constructor(initialx, initialy, width, height, title, options) {
		super(initialx, initialy, width, height, true, COLOR_GREY);

		/* Create a text box for the title at the top. */
		this.titleBox = new TextBox(initialx, initialy, width, height / (options.length + 1), title, true, COLOR_BLACK);

		/* Decide on some dimensions. */
		let elementHeight = height / (options.length + 1);
		let initialyOptions = initialy + elementHeight;
		let initialxTextBox = initialx + width / 4;
		let widthTextBox = 3 * width / 4;

		/* Create a set of small tick boxes on the left and text boxes on the right. */
		this.tickBoxes = [];
		this.textBoxes = [];
		for (let i = 0; i < options.length; i++) {
			this.tickBoxes.push(new TickBox(initialx, initialyOptions + i * elementHeight, width / 4, elementHeight));
			this.textBoxes.push(new TextBox(initialxTextBox, initialyOptions + i * elementHeight, widthTextBox, elementHeight, options[i], false, COLOR_BLACK));
		}

		/* By default, always select the first option. */
		this.tickBoxes[0].select();
	}

	/* Leaves the selector box as it was created. */
	initialize() {
		for (let tickBox of this.tickBoxes) {
			tickBox.deselect();
		}
		this.tickBoxes[0].select();
	}

	/* Updates the selection. */
	keyPressed(code, mode) {
		let changed = false;
		if (code == UP_ARROW) {
			changed = this.moveSelectionUp();
		}
		else if (code == DOWN_ARROW) {
			changed = this.moveSelectionDown();
		}

		/* If there has been a change and mode is duo, send a message to the server */
		if (changed && mode == MODE_DUO) {
			client.sendMessage('updateSelector', {selection: this.getActiveTickBoxIndex()});
		}
	}

	/* Returns the index of the tick box currently selected. */
	getActiveTickBoxIndex() {
		for (let i = 0; i < this.tickBoxes.length; i++) {
			if (this.tickBoxes[i].isSelected()) {
				return i;
			}
		}

		return undefined;
	}

	setActiveTickBoxIndex(index) {
		this.initialize();
		this.tickBoxes[0].deselect();
		this.tickBoxes[index].select();
	}

	/* Selects the tick box above the one currently selected. */
	moveSelectionUp() {
	 	let activeIndex = this.getActiveTickBoxIndex();
		if (activeIndex == 0) {
			return false;
		}
		else {
			this.tickBoxes[activeIndex].deselect();
			this.tickBoxes[activeIndex - 1].select();
			return true;
		}
	}

	/* Selects the tick box below the one currently selected. */
	moveSelectionDown() {
		let activeIndex = this.getActiveTickBoxIndex();
		if (activeIndex == this.tickBoxes.length - 1) {
			return false;
		}
		else {
			this.tickBoxes[activeIndex].deselect();
			this.tickBoxes[activeIndex + 1].select();
			return true;
		}
	}

	/* Display all the elements in the selector box. */
	display() {
		super.display();
		this.titleBox.display();
		for (let i = 0; i < this.tickBoxes.length; i++) {
			this.tickBoxes[i].display();
			this.textBoxes[i].display();
		}
	}
}