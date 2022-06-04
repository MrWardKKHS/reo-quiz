<script context="module">
	import { make_questions } from "./utils";

	export async function preload() {
		const res = await fetch("placenames.txt")
		const text = await res.text()

		const lines = text.split("\n")
		const kupu = lines.map(line => {
		const [english, maori, breakdown] = line.split("; ")
		return {
			maori,
			english,
			breakdown
		}
		})

		const questions = make_questions(kupu)
		return questions
	}

	const get_kupu = async function () {
		// get the words from file, split in to word-definition pairs
		// clean data and choose 1 correct word and 3 incorect choices per question
		const res = await fetch('kupu.txt')
		const txt = await res.text()
		let lines = txt.split("\n")
		let kupu = []
		for (let line of lines){
			line = line.replace('\r', '')
			let parts = line.split(";")
			kupu.push(parts)
		}
		const questions = make_questions(kupu)
		return questions
	}
</script>


<script>
	import Welcome from "./screens/welcome.svelte"
	import Kotahi from "./screens/kotahi.svelte"
	import Game from "./screens/game.svelte"
	let data
	let state = 'welcome'
	let category 
	const start = async (e) => {
		state = 'loading'
		category = e.detail.category.slug
		if (category === 'placenames'){
			data = await preload()
		} else {
			data = await get_kupu()
		}
		state = 'playing'
	}
</script>

<main>
	{#if state =="welcome"}
		<Welcome on:select={start}/>
	{:else if state =="loading"}
		<div class="loader">
			<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="margin: auto; display: block; shape-rendering: auto;" width="200px" height="200px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
				<circle cx="50" cy="50" r="32" stroke-width="8" stroke="#df1317" stroke-dasharray="50.26548245743669 50.26548245743669" fill="none" stroke-linecap="round">
					<!-- <animateTransform attributeName="transform" type="rotate" repeatCount="indefinite" dur="1s" keyTimes="0;1" values="0 50 50;360 50 50"></animateTransform> -->
				</circle>
			</svg>
		</div>
	{:else if state =='playing' && category === 'placenames'}
		<Game {data} on:restart={() => state = 'welcome'}/>
	{:else if state =='playing'}
		<Kotahi {data} {category} on:restart={() => state = 'welcome'}/>
	{/if}
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 800px;
		height: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		margin: 0 auto;
	}
	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
	.loader {
        position: fixed;
        top: 0;
		left: 0;
		right: 0;
		bottom: 0;
        display: grid;
        place-items: center;
		animation-name: ckw;
		animation-duration: 1s;
		animation-iteration-count: infinite;
    }
@keyframes ckw {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}


</style>