/* Class that represents a simple text box that can be displayed. */
class MessageBoard {
    constructor(initialx, initialy, width, height) {
		/* Store values. */
        this.initialx = initialx;
        this.initialy = initialy;
        this.width = width;
        this.height = height;

        /* Calculate coordinates for the center of the board. */
        this.centerx = this.initialx + this.width / 2;
        this.centery = this.initialy + this.height / 2;

        /* A message board has a message that it can display. */
        this.message = 'Hello';
    }

    /* Replaces the old message with a new one. */
    changeMessage(message) {
        this.message = message;
    }

    /* Displays the message board to the screen. */
    display() {
        fill(255);
		noStroke();
		textAlign(CENTER);
        text(this.message, this.centerx, this.centery);
    }
}
