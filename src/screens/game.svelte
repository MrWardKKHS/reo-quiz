<script>
    export let data
    import { pick_random, load_image, sleep } from "../utils";
    import {createEventDispatcher} from 'svelte'
    import {fly, crossfade, scale} from 'svelte/transition'
    import * as eases from "svelte/easing"
    console.log(data)
    let i = 0
    let done = false
    let ready = true
    const results = Array(data.length)
    const dispatch = createEventDispatcher()
    $: score = results.filter(x => x=== 'right').length

    const [send, recieve] = crossfade({
        easing: eases.cubicOut, 
        duration: 300
    })

    const pick_message =(p) => {
        if (p < 0.5) return pick_random(['Ouch', "that wasn't very good", "Must try harder"]);
        if (p < 0.8) return pick_random(['So close', "Almost there"]);
        else return pick_random(['Ka pai!', "You rock!", "ka wani kē!"]);
    }

    // Edit to match selection 
    const submit = async (correct, chose) => {
        last_result = correct === sign
            ? 'right'
            : 'wrong';

        await sleep(1500)

        results[i] = last_result

        last_result = null

        await sleep(500)

        console.log({last_result})

        if (i < selection.length - 1) {
            i += 1
        }   else {
            done = true
        }
    }

    const get_button_text = function(button_num) {
        return data.data[i].all_questions[button_num].english
    }

</script>

<header>
    <p>Tap on the correct translation</p>
    <h2 class="reo">{data.data[i].correct.maori}</h2>
</header>

{#if done}
    <div class="done">
        <strong>{score}/{results.length}</strong>
        <p>{pick_message(score / results.length)}</p>
        <button on:click={() => dispatch('restart')}>Back to welcome screen</button>
    </div>

    {:else if ready}
        {#await data then [a, b]}
            <div class="game"
                in:fly={{duration: 200, y:20}}
                out:fly={{duration: 200, y:-20}}
                on:outrostart={() => ready = false}
                on:outroend={() => ready = true}
            >
                <div class='answer-container'>
                    {#each [0, 1, 2, 3] as num}
                    <button class='answer' on:click={() => submit(get_button_text(num))}>{get_button_text(num)}</button>
                    {/each}
                </div>
            </div>
        {:catch}
            <p class="error">Opps! Failed to load data</p>
        {/await}
{/if}