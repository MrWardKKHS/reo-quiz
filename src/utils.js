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

export function make_questions(wordList, length=10){
	let questions = []
		for (let i = 0; i < length; i++) {
			let question = {
				all: [],
				correct: []
			}
			let choice = pick_random(wordList)
			question.correct = choice
			question.all.push(choice)
			for (let i = 0; i < 3; i++){
				let incorrect = pick_random(wordList)
				while (question.all.includes(incorrect)) {
					incorrect = pick_random(wordList)
				}
				question.all.push(incorrect)
			}
			question.all = shuffle(question.all)
			questions.push(question)
		}
		return questions
}