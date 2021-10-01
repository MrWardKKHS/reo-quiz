<script context="module">
	export async function preload(page, session) {
	  const res = await fetch("https://bmvw2i.deta.dev/")
	  const data = await res.json();
	  return data
	}
</script>


<script>
	import Welcome from "./screens/welcome.svelte"
	import Game from "./screens/game.svelte"
	let data
	let state = 'welcome'
	const start = async (e) => {
		data = await preload()
		state = 'playing'
	}

	const load_questions = async () => {
		data = await preload()
	}

</script>

<main>
	{#if state =="welcome"}
		<Welcome on:select={start}/>
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