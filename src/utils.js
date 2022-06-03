export function pick_random(array) {
	const index = Math.floor(array.length * Math.random());
	return array[index];
}

export function sleep(ms) {
	return new Promise(fulfil => {
		setTimeout(fulfil, ms)
	})
}

export function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
	return array
}

export function load_image(src){
	return new Promise((fulfil, reject) => {
		const img = new Image();
		img.onload = () => fulfil(img);
		img.onerror = reject
		img.src = src
	})
}