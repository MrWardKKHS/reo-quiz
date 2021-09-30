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

    <p>
        Lorem ipsum dolor sit amet consectetur adipisicing 
    </p>
<p>Placeat, aliquid?</p>

<p>Pick a category to play a game</p>

<div class="categories">
<!-- using categories to make this modular over time -->
    {#each categories as category}
        <button diabled={selected} on:click={() => select(category)}>{category.label}</button>
    {/each}

</div>


<style>
   h1 {
        color: #ff3e00;
        text-transform: uppercase;
        font-size: min(12vw, 4em);
        font-weight: 100;
        margin: 0 0 0.5em 0;
    }
    
    /* .logo {
        display: inline-block;
        background: url(/icons/compare.svg) 50% 50% no-repeat;
        background-size: 100% 100%;
        width: 0.8em;
        top: 0.05em;
        transform: scale(1.4);
        left: 0.02em;
        text-indent: -9999px;
    } */

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

    @media (min-width: 640px) {
        button {
            display: inline;
            margin: 0 0.2em 0.4em 0.2em;
            width: auto;
        }
    }

</style>