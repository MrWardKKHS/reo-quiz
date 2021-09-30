<script>
    export let data
    import { pick_random, load_image, sleep } from "../utils";
    import {createEventDispatcher} from 'svelte'
    import {fly, crossfade, scale} from 'svelte/transition'
    import * as eases from "svelte/easing"
    let i = 0
    let done = false
    let ready = true
    let last_result = null
    const results = Array(data.length)
    const dispatch = createEventDispatcher()
    $: score = results.filter(x => x=== 'right').length
    $: options = data[i].all_questions
    $: correct = data[i].correct
    $: headingText = data[i].correct.maori

    const [send, receive] = crossfade({
        easing: eases.cubicOut, 
        duration: 300
    })

    const pick_message =(p) => {
        if (p < 0.5) return pick_random(['Ouch', "that wasn't very good", "Must try harder"]);
        if (p < 0.8) return pick_random(['So close', "Almost there"]);
        else return pick_random(['Ka pai!', "You rock!", "ka wani kē!"]);
    }

    // Edit to match selection 
    const submit = async (choice) => {
        last_result = correct.english === choice
            ? 'right'
            : 'wrong';

        await sleep(3200)

        results[i] = last_result

        console.log({last_result})
        last_result = null

        await sleep(500)
        if (i < data.length - 1) {
            i += 1
            options = options
            correct = correct
            headingText = headingText
        }   else {
            done = true
        }
    }

</script>

<header>
    <p>Tap on the correct translation</p>
    <h2 class="reo">{correct.maori}</h2>
</header>

<div class="game-container">
{#if done}
    <div class="done">
        <strong>{score}/{results.length}</strong>
        <p>{pick_message(score / results.length)}</p>
        <button on:click={() => dispatch('restart')}>Back to welcome screen</button>
    </div>

    {:else if ready}
        <div class="game"
            in:fly={{duration: 200, y:20}}
            out:fly={{duration: 200, y:-20}}
            on:outrostart={() => ready = false}
            on:outroend={() => ready = true}
        >  
            <div class='answer-container'>
                {#each options as option}
                <button class='answer' on:click={() => submit(option.english)}>{option.english}</button>
                {/each}
            </div>
        </div>
{/if}



<div class="breakdown-container">          
    {#if !!last_result}
        <p in:fly={{duration: 200, y:20}}
        out:fly={{duration: 200, y:-20}}>{correct.breakdown}</p>
    {/if}
</div>
<div class="big-icon-container">
{#if last_result}
    <img class='giant-result'
        in:fly={{x:100, duration: 200}}
        out:send={{key: i}}
        alt='{last_result} answer'
        src='/icons/{last_result}.svg'
    >
{/if}
</div>
<div class="results" style="grid-template-columns: repeat({results.length}, 1fr)">
    {#each results as result}
    <span class="result">
        {#if result}
                    <img
                    in:receive={{key: i}}
                    alt='{result} answer'
                    src='/icons/{result}.svg'
                    >
        {/if}
    </span>
    {/each}
</div>
</div>

<style>
    .answer {
        width: 20em;
        padding: 1em;
        box-shadow: lightslategray 5px 5px;
        margin: 10px;
    }
    .breakdown-container {
        height: 3em;
        border: 3px darkslategray solid;
        padding-bottom: 5px;
    }

    /* .game {
        display: grid;
        grid-template-rows: 1fr 2em 1fr;
        grid-gap: 0.5em;
        width: 100%;
        height: 100%;
        margin: 0 auto;
        max-width: min(100%, 40vh);
    } */

    /* .game > div {
        display: flex;
        align-items: center;
    } */

    /* .game-container {
        flex: 1;
    } */

    .giant-result {
        position: fixed;
        width: 50vmin;
        height: 50vmin;
        left: calc(50vw - 25vmin);
        top: calc(50vh - 25vmin);
        opacity: 0.5;
    }

    .results {
    display: grid;
    grid-gap: 0.2em;
    width: 100%;
    max-width: 320px;
    margin: 1em auto 0 auto;
    }

    .result {
    background: rgba(255,255,255,0.1);
    border-radius: 50%;
    padding: 0 0 100% 0;
    transition: background 0.2s;
    transition-delay: 0.2s;
    }
    /* .result img {
    position: absolute;
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
    } */
    .done {
        position: absolute;
        width: 100%;
        height: 100%;
        left: 0;
        top: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .done strong {
        font-size: 6em;
        font-weight: 700;
    } 
    @media (min-width: 640px) {
        .game {
            max-width: 100%;
            grid-template-rows: none;
            grid-template-columns: 1fr 8em 1fr;
            max-height: calc(100vh -6em);
        }

    }
</style>