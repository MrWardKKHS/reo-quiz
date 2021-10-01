<script>
    import { createEventDispatcher } from 'svelte'
    const categories = [
        { slug: "placenames", label: "Place Names"}
    ]

    const dispatch = createEventDispatcher()

    let selected = false

    const select = (category => {
        selected = true
        dispatch('select', { category })
    })
    
</script>
<h1>Te Reo Place Names</h1>

<p>How well do you know your own backyard?</p>
<p>Take the quiz to find out</p>
<br>
<!-- <p>Pick a category to play a game</p> -->

<div class="categories">
<!-- using categories to make this modular over time -->
    {#each categories as category}
        <button diabled={selected} on:click={() => select(category)}>{category.label}</button>
    {/each}

</div>
<br>
<br>
<footer>
   <p>translations from <a href="https://nzhistory.govt.nz/culture/maori-language-week/1000-maori-place-names">NZ History</a></p>
   <p>Made by <a href="https://www.youtube.com/channel/UCHm5sxfqw5Oq2mbiYH1kgzw">Mr Ward</a></p>
</footer>

<style>
   h1 {
        color: #ff3e00;
        text-transform: uppercase;
        font-size: min(12vw, 4em);
        font-weight: 100;
        margin: 0 0 0.5em 0;
    }

    p {
        max-width: 24em;
        margin: 0 auto 1em auto;
    }

    .categories {
        width: 100%;
        max-width: 26em;
        margin: 0 auto;
    }

    button {
        padding: 1em;
        display: block;
        margin: 0 0 0.2em 0;
        width: 100%;
    }

    footer {
        margin: 0 auto;
        color:dimgray;
        opacity: 80%;
    }

    @media (min-width: 640px) {
        button {
            display: inline;
            margin: 0 0.2em 0.4em 0.2em;
            width: auto;
        }
    }

</style>