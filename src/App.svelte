



<script>
	import Welcome from "./screens/welcome.svelte"
	import Game from "./screens/game.svelte"
	import Loader from "./screens/loader.svelte"
	import { make_questions } from "./utils";

	export async function preload(filename, prompt_language='maori') {
		const res = await fetch(filename);
		const text = await res.text();
		const swap_prompt = prompt_language === 'english';
		const lines = text.split("\n");
		const kupu = lines.map(line => {
			const [maori, english, breakdown] = line.split("; ")
				return {
					prompt: swap_prompt? english : maori,
					answer: swap_prompt? maori : english,
					breakdown
				}
			})
	
		return make_questions(kupu)
	}

	let state = 'welcome'
	let data
	const start = async (e) => {
		state = 'loading'
		data = await preload(e.detail.category.filename, e.detail.category.prompt_language)
		console.log(data)
		state = 'playing'
	}
</script>

<main>
	{#if state =="welcome"}
		<Welcome on:select={start}/>
	{:else if state =="loading"}
		<Loader/>
	{:else if state =='playing'}
		<Game {data} on:restart={() => state = 'welcome'}/>
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


</style>