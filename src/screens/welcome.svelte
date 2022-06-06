<script>
    import { createEventDispatcher } from 'svelte'
    const categories = [
        { slug: "maori", label: "Maori", filename: "kupu.txt", prompt_language: 'maori'},
        { slug: "english", label: "English", filename: "kupu.txt", prompt_language: 'english'},
        { slug: "placenames", label: "Place Names", filename: "placenames.txt", prompt_language: 'maori'},
    ]
    const dispatch = createEventDispatcher()
    let selected = false
    const select = (category => {
        selected = true
        dispatch('select', { category })
    })
</script>

<h1>Kotahi Mano Kupu</h1>

<p>A Thousand Words</p>
<p>Practice the thousand most common words in Te Reo</p>
<br>

<div class="categories">
<!-- using categories to make this modular over time -->
    {#each categories as category}
        <button diabled={selected} on:click={() => select(category)}>{category.label}</button>
    {/each}

</div>
<br>
<br>
<footer>
    <p>translations from <a href="https://nzhistory.govt.nz/culture/maori-language-week/1000-maori-place-names">NZ History</a> and <a href="https://tereomaori.tki.org.nz/Teacher-tools/Te-Whakaipurangi-Rauemi/High-frequency-word-lists">TKI</a></p>
   <p>Made by <a href="https://www.youtube.com/channel/UCHm5sxfqw5Oq2mbiYH1kgzw">Mr Ward</a></p>
</footer>

<style>
   h1 {
        color: #ff3e00;
        text-transform: uppercase;
        font-size: min(12vw, 4em);
        font-weight: 200;
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
        margin: 0 0 0.5em 0;
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